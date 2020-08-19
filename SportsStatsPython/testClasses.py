from nba_api.stats.static import players, teams
from nba_api.stats.endpoints import playergamelog
from nba_api.stats.library.parameters import SeasonAll
from nba_api.stats.endpoints import teamgamelog
from nba_api.stats.endpoints import teamgamelogs
from nba_api.stats.endpoints import leaguegamefinder
import time



import nba_py


team_dict = teams.get_teams()
player_dict = players.get_players()

#this time we convert it to a dataframe in the same line of code
GSW = [x for x in team_dict if x['full_name'] == 'Golden State Warriors'][0]
GSW_id = GSW['id']

GSW_games_2018 = teamgamelog.TeamGameLog(GSW_id,season='2018')
gamelog_bron = playergamelog.PlayerGameLog(player_id='2544', season='2018')

# Converts gamelog object into a dictionary
dict_bron_games_2018 = gamelog_bron.get_dict()

class Team:  # very similar to player class
    def __init__(self, playerName=None):
        while type(playerName) is not str:
            playerName = str(input('Please input the name of a current or past NBA player: '))
        if ' ' in playerName:  # name is a full name
            for player in player_dict:
                if player['full_name'].lower() == playerName.lower():  # avoid case issues by converting all to lower
                    self.id = player['id']
                    self.name = player['full_name']
                    self.isActive = player['is_active']

        else:  # check for player first or last name
            for player in player_dict:
                if player['first_name'].lower() == playerName.lower() or player[
                    'last_name'].lower() == playerName.lower():
                    checkPlayer = ''
                    # confirm since we don't have the full name
                    while checkPlayer not in ['yes', 'Yes', 'YES', 'YEs', 'Y', 'y', 'no', 'No', 'NO', 'n', 'N']:
                        checkPlayer = input('Did you mean ' + player['full_name'] + '?')
                    if checkPlayer in ['yes', 'Yes', 'YES', 'YEs', 'Y', 'y']:  # only input player if the answer is yes
                        self.id = player['id']
                        self.name = player['full_name']
                        self.isActive = player['is_active']

        if hasattr(self, 'id') is False:  # player was not found
            raise Exception(str(playerName) + " could not be found. You may want to check your spelling.")

        # get career stats
        self.seasons = self.getStats()
        self.careerGames = self.getGames()
        self.PTS = self.getPTS()
        self.PPG = self.getPPG()
        self.REB = self.getREB()
        self.RPG = self.getRPG()
        self.AST = self.getAST()
        self.APG = self.getAPG()
        self.activeSeasons = self.getActiveSeasons()

    def addSeason(self, season):
        if type(season) is Season:
            self.seasons.append(season)
        elif type(season) is list:
            for current in season:
                if type(current) is Season:
                    self.seasons.append(current)
                else:
                    raise TypeError('Only seasons can be added to a career')
        elif season is not None:
            raise TypeError('Only seasons can be added to a career')

        self.updateStats()

    def getGames(self, team=None):
        totalGames = 0
        if team is None:
            for year in self.seasons:
                totalGames += len(year.games)
        else:
            team = getTeamAbbreviation(team)
            for year in self.seasons:
                totalGames += year.getNumberOfGames(team)
        return totalGames

    def getPTS(self, team=None):
        totalPoints = 0
        if team is None:
            for year in self.seasons:
                totalPoints += year.PTS
        else:
            team = getTeamAbbreviation(team)
            for year in self.seasons:
                totalPoints += year.getSeasonPTS(team)
        return totalPoints

    def getPPG(self, team=None):
        if team is None:
            return round(self.PTS / self.careerGames, 2)
        else:
            team = getTeamAbbreviation(team)
            return round(self.getPTS(team) / self.getGames(team), 2)

    def getREB(self, team=None):
        totalREB = 0
        if team is None:
            for year in self.seasons:
                totalREB += year.REB
        else:
            team = getTeamAbbreviation(team)
            for year in self.seasons:
                totalREB += year.getSeasonREB(team)
        return totalREB

    def getRPG(self, team=None):
        if team is None:
            return round(self.REB / self.careerGames, 2)
        else:
            team = getTeamAbbreviation(team)
            return round(self.getREB(team) / self.getGames(team), 2)

    def getAST(self, team=None):
        totalAST = 0
        if team is None:
            for year in self.seasons:
                totalAST += year.AST
        else:
            team = getTeamAbbreviation(team)
            for year in self.seasons:
                totalAST += year.getSeasonAST(team)
        return totalAST

    def getAPG(self, team=None):
        if team is None:
            return round(self.AST / self.careerGames, 2)
        else:
            team = getTeamAbbreviation(team)
            return round(self.getAST(team) / self.getGames(team), 2)

    def getActiveSeasons(self):
        activeSeasons = []
        for year in self.seasons:
            activeSeasons.append(int(str(year.games[0][0])[-4:]))
        return activeSeasons

    def updateStats(self):
        self.careerGames = self.getGames()
        self.PTS = self.getPTS()
        self.PPG = self.getPPG()
        self.REB = self.getREB()
        self.RPG = self.getRPG()
        self.AST = self.getAST()
        self.APG = self.getAPG()
        self.activeSeasons = self.getActiveSeasons()

    def getSeason(self, season):
        if season not in self.activeSeasons:
            raise ValueError('Not a valid season')
        return self.seasons[self.activeSeasons.index(season)]

    def getStats(self, season=None):
        if season is not None:  # updating a season, not the whole career
            while len(str(season)) != 4:
                season = int(input('Please enter the season you want to update as a 4 digit year'))
            gamelog = playergamelog.PlayerGameLog(player_id=self.id, season=season)
            gamestats = gamelog.get_dict()
            return Season(str(season), gamestats['resultSets'][0]['rowSet'])  # gets season and dictionary of stats

        else:
            # gets career dataframes from nba_api module
            gamelog = playergamelog.PlayerGameLog(player_id=self.id, season=SeasonAll.all)
            careerStats = gamelog.get_data_frames()

            # makes a list of all years the player has played in the nba
            activeYears = []
            for year in careerStats[0]['SEASON_ID']:
                if str(year)[-4:] not in activeYears:
                    activeYears.append(str(year)[-4:])

            # makes season stats 1 year at a time
            career = []
            for year in activeYears:
                career.append(self.getStats(year))
            # after making each year as an individual season, return as a
            return career

    def __str__(self):
        return 'PPG: ' + str(self.PPG) + ' RPG: ' + str(self.RPG) + ' APG: ' + str(self.APG)


class Player:  # import player information from dictionaries
    def __init__(self, playerName, season=None):
        while type(playerName) is not str:
            playerName = str(input('Please input the name of a current or past NBA player: '))
        if ' ' in playerName:  # name is a full name
            for player in player_dict:
                if player['full_name'].lower() == playerName.lower():  # avoid case issues by converting all to lower
                    self.id = player['id']
                    self.name = player['full_name']
                    self.isActive = player['is_active']

        else:  # check for player first or last name
            for player in player_dict:
                if player['first_name'].lower() == playerName.lower() or player['last_name'].lower() == playerName.lower():
                    checkPlayer = ''
                    # confirm since we don't have the full name
                    while checkPlayer not in ['yes', 'Yes', 'YES', 'YEs', 'Y', 'y', 'no', 'No', 'NO', 'n', 'N']:
                        checkPlayer = input('Did you mean ' + player['full_name'] + '?')
                    if checkPlayer in ['yes', 'Yes', 'YES', 'YEs', 'Y', 'y']:  # only input player if the answer is yes
                        self.id = player['id']
                        self.name = player['full_name']
                        self.isActive = player['is_active']

        if hasattr(self, 'id') is False:  # player was not found
            raise Exception(str(playerName) + " could not be found. You may want to check your spelling.")

        # get career stats
        self.seasons = self.getStats(season)
        self.careerGames = self.getGames()
        self.PTS = self.getPTS()
        self.PPG = self.getPPG()
        self.REB = self.getREB()
        self.RPG = self.getRPG()
        self.AST = self.getAST()
        self.APG = self.getAPG()
        self.activeSeasons = self.getActiveSeasons()

    def addSeason(self, season):
        if type(season) is Season:
            self.seasons.append(season)
        elif type(season) is list:
            for current in season:
                if type(current) is Season:
                    self.seasons.append(current)
                else:
                    raise TypeError('Only seasons can be added to a career')
        elif season is not None:
            raise TypeError('Only seasons can be added to a career')

        self.updateStats()

    def getGames(self, team=None,season=None):
        totalGames = 0
        if season == None:
            seasons = self.seasons
        else:
            if int(season) in self.activeSeasons:
                seasons = self.seasons[self.activeSeasons.index(season)]
        if team is None:
            for year in seasons:
                totalGames += len(year.games)
        else:
            team = getTeamAbbreviation(team)
            for year in seasons:
                totalGames += year.getNumberOfGames(team)
        return totalGames

    def getPTS(self, team=None):
        totalPoints = 0
        if team is None:
            for year in self.seasons:
                totalPoints += year.PTS
        else:
            team = getTeamAbbreviation(team)
            for year in self.seasons:
                totalPoints += year.getSeasonPTS(team)
        return totalPoints

    def getPPG(self, team=None):
        if team is None:
            return round(self.PTS / self.careerGames, 2)
        else:
            team = getTeamAbbreviation(team)
            return round(self.getPTS(team) / self.getGames(team), 2)

    def getREB(self, team=None):
        totalREB = 0
        if team is None:
            for year in self.seasons:
                totalREB += year.REB
        else:
            team = getTeamAbbreviation(team)
            for year in self.seasons:
                totalREB += year.getSeasonREB(team)
        return totalREB

    def getRPG(self, team=None):
        if team is None:
            return round(self.REB / self.careerGames, 2)
        else:
            team = getTeamAbbreviation(team)
            return round(self.getREB(team) / self.getGames(team), 2)

    def getAST(self, team=None):
        totalAST = 0
        if team is None:
            for year in self.seasons:
                totalAST += year.AST
        else:
            team = getTeamAbbreviation(team)
            for year in self.seasons:
                totalAST += year.getSeasonAST(team)
        return totalAST

    def getAPG(self, team=None):
        if team is None:
            return round(self.AST / self.careerGames, 2)
        else:
            team = getTeamAbbreviation(team)
            return round(self.getAST(team) / self.getGames(team), 2)

    def getActiveSeasons(self):
        activeSeasons = []
        for year in self.seasons:
            activeSeasons.append(int(str(year.games[0][0])[-4:]))
        return activeSeasons

    def updateStats(self):
        self.numberOfGames = self.getGames()
        self.PTS = self.getPTS()
        self.PPG = self.getPPG()
        self.REB = self.getREB()
        self.RPG = self.getRPG()
        self.AST = self.getAST()
        self.APG = self.getAPG()
        self.seasons = self.getActiveSeasons()
        
    def getSeason(self, season):
        if season not in self.activeSeasons:
            raise ValueError('Not a valid season')
        return self.seasons[self.activeSeasons.index(season)]

    def getStats(self, season=None):
        if season is not None:  # updating a season, not the whole career
            while len(str(season)) != 4:
                season = int(input('Please enter the season you want to update as a 4 digit year'))
            gamelog = playergamelog.PlayerGameLog(player_id=self.id, season=season)
            gamestats = gamelog.get_dict()
            return [Season(str(season), gamestats['resultSets'][0]['rowSet'])]  # return as list for loops expected

        else:
            # gets career dataframes from nba_api module
            gamelog = playergamelog.PlayerGameLog(player_id=self.id, season=SeasonAll.all)
            careerStats = gamelog.get_data_frames()

            # makes a list of all years the player has played in the nba
            activeYears = []
            for year in careerStats[0]['SEASON_ID']:
                if str(year)[-4:] not in activeYears:
                    activeYears.append(str(year)[-4:])

            # makes season stats 1 year at a time
            career = []
            for year in activeYears:
                career.append(self.getStats(year))
            # after making each year as an individual season, return as a list
            return career

    def __str__(self):
        return 'PPG: ' + str(self.PPG) + ' RPG: ' + str(self.RPG) + ' APG: ' + str(self.APG)


class Season:
    def __init__(self, season, games=None):
        self.season = str(season)
        self.games = []

        if games is not None:
            self.addGame(games)

        # update all stats
        if len(self.games) > 0:
            self.PTS = self.getSeasonPTS()
            self.PPG = self.getPPG()
            self.REB = self.getSeasonREB()
            self.RPG = self.getRPG()
            self.AST = self.getSeasonAST()
            self.APG = self.getAPG()

    def addGame(self, game):
        if type(game) is dict:
            self.games.append(game)
            return
        elif type(game) is list:
            for x in game:
                if type(x) is list:
                    self.games.append(x)
                else:
                    raise TypeError('Games stats must be a list')

    def getNumberOfGames(self, team=None):
        if team is None:
            return len(self.games)
        else:
            team = getTeamAbbreviation(team)
            number = 0
            for game in self.games:
                if team in game[4]:
                    number += 1
            return number

    def getSeasonPTS(self, team=None):
        totalPoints = 0
        if team is None:
            for game in self.games:
                totalPoints += game[24]
        else:
            team = getTeamAbbreviation(team)
            for game in self.games:
                if team in game[4]:
                    totalPoints += game[24]

        return totalPoints

    def getPPG(self, team=None):
        if team is None:
            return round(self.PTS / len(self.games), 2)
        else:
            team = getTeamAbbreviation(team)
            return round(self.getSeasonPTS(team) / self.getNumberOfGames(team), 2)

    def getSeasonREB(self, team=None):
        totalREB = 0
        if team is None:
            for game in self.games:
                if game[18] is not None:
                    totalREB += game[18]
        else:
            team = getTeamAbbreviation(team)
            for game in self.games:
                if team in game[4]:
                    totalREB += game[18]

        return totalREB

    def getRPG(self, team=None):
        if team is None:
            return round(self.REB / len(self.games), 2)
        else:
            team = getTeamAbbreviation(team)
            return round(self.getSeasonREB(team) / self.getNumberOfGames(team), 2)

    def getSeasonAST(self, team=None):
        totalAST = 0
        if team is None:
            for game in self.games:
                totalAST += game[19]
        else:
            team = getTeamAbbreviation(team)
            for game in self.games:
                if team in game[4]:
                    totalAST += game[19]
        return totalAST

    def getAPG(self, team=None):
        if team is None:
            return round(self.AST/len(self.games), 2)
        else:
            team = getTeamAbbreviation(team)
            return round(self.getSeasonAST(team) / self.getNumberOfGames(team), 2)

    def updateStats(self):
        self.PTS = self.getSeasonPTS()
        self.PPG = self.getPPG()
        self.REB = self.getSeasonREB()
        self.RPG = self.getRPG()
        self.AST = self.getSeasonAST()
        self.APG = self.getAPG()

    def __str__(self):
        return self.season + ': ' + str(self.PPG) + '/' + str(self.RPG) + '/' + str(self.APG) + ', ' + str(len(self.games)) + ' games played'


def getTeamAbbreviation(teamName):
    teamName = str(teamName).lower()
    for team in team_dict:
        if teamName in list(team['full_name'].lower().split(' ')) or team['abbreviation'].lower() == teamName:
            return team['abbreviation'].upper()
    raise Exception('Matchup not found')


def getTime(name,season=None):
    start = time.time()
    player = Player(name,season)
    print(time.time() - start)
    return player


dame = getTime('Damian Lillard',2019)

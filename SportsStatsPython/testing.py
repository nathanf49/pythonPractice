from nba_api.stats.static import players, teams
from nba_api.stats.endpoints import playergamelog
from nba_api.stats.library.parameters import SeasonAll
from nba_api.stats.endpoints import leaguegamefinder

'''
#this time we convert it to a dataframe in the same line of code
GSW = [x for x in teams if x['full_name'] == 'Golden State Warriors'][0]
GSW_id = GSW['id']
GSW_games = leaguegamefinder.LeagueGameFinder(team_id_nullable=GSW_id).get_data_frames()[0]
'''
team_dict = teams.get_teams()
player_dict = players.get_players()

gamelog_bron = playergamelog.PlayerGameLog(player_id='2544', season='2018')

# Converts gamelog object into a pandas dataframe
# can also convert to JSON or dictionary
df_bron_games_2018 = gamelog_bron.get_data_frames()

class Player:  # import player information from dictionaries
    def __init__(self, playerName=None):
        while type(playerName) is not str:
            playerName = str(input('Please input the name of a current or past NBA player: '))
        if ' ' in playerName:  # name is a full name
            for player in player_dict:
                if player['full_name'].lower() == playerName.lower():  # avoid case issues by converting all to lower
                    self.id = player['id']
                    self.name = player['full_name']
                    self.isActive = player['is_active']
                    self.seasons = self.getStats()

        else: # check for player first or last name
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
                        self.seasons = self.getStats()

        if hasattr(self, 'id') is False:  # player was not found
            raise Exception(str(playerName) + " could not be found. You may want to check your spelling.")

        # get career stats
        self.careerGames = self.getCareerGames()
        self.PTS = self.getCareerPTS()
        self.PPG = self.getCareerPPG()
        self.REB = self.getCareerREB()
        self.RPG = self.getCareerRPG()
        self.AST = self.getCareerAST()
        self.APG = self.getCareerAPG()
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

    def getCareerGames(self, team=None):
        totalGames = 0
        if team is None:
            for year in self.seasons:
                totalGames += len(year.games)
        else:
            team = getTeamAbbreviation(team)
            for year in self.seasons:
                 totalGames += year.getNumberOfGames(team)
        return totalGames

    def getCareerPTS(self, team=None):
        totalPoints = 0
        if team is None:
            for year in self.seasons:
                totalPoints += year.PTS
        else:
            team = getTeamAbbreviation(team)
            for year in self.seasons:
                totalPoints += year.getSeasonPTS(team)
        return totalPoints

    def getCareerPPG(self, team=None):
        if team is None:
            return round(self.PTS / self.careerGames, 2)
        else:
            team = getTeamAbbreviation(team)
            return round(self.getCareerPTS(team) / self.getCareerGames(team), 2)

    def getCareerREB(self, team=None):
        totalREB = 0
        if team is None:
            for year in self.seasons:
                totalREB += year.REB
        else:
            team = getTeamAbbreviation(team)
            for year in self.seasons:
                totalREB += year.getSeasonREB(team)
        return totalREB

    def getCareerRPG(self, team=None):
        if team is None:
            return round(self.REB / self.careerGames, 2)
        else:
            team = getTeamAbbreviation(team)
            return round(self.getCareerREB(team) / self.getCareerGames(team), 2)

    def getCareerAST(self, team=None):
        totalAST = 0
        if team is None:
            for year in self.seasons:
                totalAST += year.AST
        else:
            team = getTeamAbbreviation(team)
            for year in self.seasons:
                totalAST += year.getSeasonAST(team)
        return totalAST

    def getCareerAPG(self, team=None):
        if team is None:
            return round(self.getCareerAST() / self.careerGames, 2)
        else:
            team = getTeamAbbreviation(team)
            return round(self.getCareerAST(team) / self.getCareerGames(team), 2)

    def getActiveSeasons(self):
        activeSeasons = []
        for year in self.seasons:
            activeSeasons.append(int(str(year.games[0].seasonID)[-4:]))
        return activeSeasons

    def updateStats(self):
        self.careerGames = self.getCareerGames()
        self.PTS = self.getCareerPTS()
        self.PPG = self.getCareerPPG()
        self.REB = self.getCareerREB()
        self.RPG = self.getCareerRPG()
        self.AST = self.getCareerAST()
        self.APG = self.getCareerAPG()
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
            'need to finish updates after importing career stats'
            seasonGames = []
            for game in gamestats['resultSets'][0]['rowSet']:  # saves all player stats from individual games
                seasonGames.append(
                    GameStats(game[24], game[18], game[19], game[0], self.id, game[2],
                              game[3], game[4], game[5], game[6], game[7],
                              game[8], game[9], game[10], game[11], game[12],
                              game[13], game[14], game[15], game[16], game[17], game[20],
                              game[21], game[22], game[23], game[25]))
            return Season(str(season),seasonGames)

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
            # after making each year as an individual season, cast as a Career
            return career

    def __str__(self):
        return 'PPG: ' + str(self.PPG) + ' RPG: ' + str(self.RPG) + ' APG: ' + str(self.APG)


class GameStats:
    def __init__(self, PTS=None, REB=None, AST=None, seasonID=None, playerID=None, gameID=None, date=None, matchup=None,
                 WL=None, MIN=None, FGM=None, FGA=None, FG_PCT=None, FG3M=None, FG3A=None, FG3_PCT=None, FTM=None,
                 FTA=None, FT_PCT=None, OREB=None, DREB=None, STL=None, BLK=None, TO=None, PF=None, PLUS_MINUS=None):
        # checking against none to cast in proper format
        if PTS is not None:
            self.PTS = PTS
        else:
            self.PTS = None
        if REB is not None:
            self.REB = REB
        else:
            self.REB = None
        if AST is not None:
            self.AST = AST
        else:
            self.AST = None
        if seasonID is not None:
            self.seasonID = str(seasonID)
        else:
            self.seasonID = None
        if playerID is not None:
            self.playerID = str(playerID)
        else:
            self.playerID = None
        if gameID is not None:
            self.gameID = str(gameID)
        else:
            self.playerID = None
        if date is not None:
            self.date = str(date)
        else:
            self.playerID = None
        if matchup is not None:
            self.matchup = str(matchup)
        else:
            self.matchup = None
        if WL is not None:
            if str(WL) == 'W':
                self.result = 'Win'
            else:
                self.result = 'Loss'
        else:
            self.result = None
        if MIN is not None:
            self.minutes = int(MIN)
        else:
            self.minutes = None
        if FGM is not None:
            self.FGM = int(FGM)
        else:
            self.FMG = None
        if FGA is not None:
            self.FGA = int(FGA)
        else:
            self.FGA = None
        if FG_PCT is not None:
            self.FG_PCT = float(FG_PCT)
        else:  # calculate FG% if not input
            if self.FGM is not None and self.FGA is not None:
                try:
                    self.FG_PCT = self.FGM / self.FGA
                except ZeroDivisionError:
                    self.FG_PCT = 0
            else:
                self.FG_PCT = None
        if FG3M is not None:
            self.FG3M = int(FG3M)
        else:
            self.FG3M = None
        if FG3A is not None:
            self.FG3A = int(FG3A)
        else:
            self.FG3A = None
        if FG3_PCT is not None:
            self.FG3_PCT = float(FG3_PCT)
        else:  # calculate FG3% if not input
            if self.FG3M is not None and self.FG3A is not None:
                try:
                    self.FG3_PCT = self.FG3M / self.FG3A
                except ZeroDivisionError:
                    self.FG3_PCT = 0
            else:
                self.FG3_PCT = None
        if FTM is not None:
            self.FTM = int(FTM)
        else:
            self.FTM = None
        if FTA is not None:
            self.FTA = int(FTA)
        else:
            self.FTA = None
        if FT_PCT is not None:
            self.FT_PCT = float(FT_PCT)
        else:  # calculate FT% if not input
            if self.FTM is not None and self.FTA is not None:
                try:
                    self.FT_PCT = self.FTM / self.FTA
                except ZeroDivisionError:
                    self.FT_PCT = 0
            else:
                self.FT_PCT = None
        if OREB is not None:
            self.OREB = int(OREB)
        else:
            self.OREB = None
        if DREB is not None:
            self.DREB = int(DREB)
        else:
            self.DREB = None
        if self.OREB is None:
            if self.REB is not None and self.DREB is not None:
                self.OREB = self.REB - self.DREB
        if self.DREB is None:
            if self.REB is not None and self.OREB is not None:
                self.DREB = self.REB - self.OREB
        if self.REB is None:
            if self.OREB is not None and self.DREB is not None:
                self.REB = self.DREB + self.OREB
        if STL is not None:
            self.STL = int(STL)
        else:
            self.STL = None
        if BLK is not None:
            self.BLK = int(BLK)
        else:
            self.BLK = None
        if TO is not None:
            self.TO = int(TO)
        else:
            self.TO = None
        if PF is not None:
            self.PF = int(PF)
        else:
            self.PF = None
        if PLUS_MINUS is not None:
            self.PLUS_MINUS = int(PLUS_MINUS)

    def __str__(self):
        return str(self.matchup) + ', ' + self.date + ' - ' + str(self.PTS) + '/' + str(self.REB) + '/' + str(self.AST)


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
        if type(game) is GameStats:
            self.games.append(game)
            return
        elif type(game) is list:
            for x in game:
                if type(x) is GameStats:
                    self.games.append(x)
                else:
                    raise TypeError('Games must be type GameStats')

        self.updateStats()

    def getNumberOfGames(self, team):
        team = getTeamAbbreviation(team)
        number = 0
        for game in self.games:
            if team in game.matchup:
                number += 1
        if number == 0:
            raise Exception('This teams did not play')
        return number

    def getSeasonPTS(self, team=None):
        totalPoints = 0
        if team is None:
            for game in self.games:
                totalPoints += game.PTS
        else:
            team = getTeamAbbreviation(team)
            for game in self.games:
                if team in game.matchup:
                    totalPoints += game.PTS

        return totalPoints

    def getPPG(self, team=None):
        if team is None:
            return self.PTS / len(self.games)
        else:
            team = getTeamAbbreviation(team)
            return round(self.getSeasonPTS(team) / self.getNumberOfGames(team), 2)

    def getSeasonREB(self, team=None):
        totalREB = 0
        if team is None:
            for game in self.games:
                totalREB += game.REB
        else:
            team = getTeamAbbreviation(team)
            for game in self.games:
                if team in game.matchup:
                    totalREB += 1

        return totalREB

    def getRPG(self, team=None):
        if team is None:
            return self.REB/len(self.games)
        else:
            team = getTeamAbbreviation(team)
            return round(self.getSeasonREB(team) / self.getNumberOfGames(team), 2)

    def getSeasonAST(self, team=None):
        totalAST = 0
        if team is None:
            for game in self.games:
                totalAST += game.AST
        else:
            team = getTeamAbbreviation(team)
            for game in self.games:
                if team in game.matchup:
                    totalAST += 1
        return totalAST

    def getAPG(self, team=None):
        if team is None:
            return self.AST/len(self.games)
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
    raise Exception('Team not found')



jordan = Player('Michael Jordan')

'''
yourPlayers = []

def addPlayer(playerName: str):
    for player in player_dict:
        if player['full_name'].lower() == playerName.lower():
            yourPlayers.append(player)
            print(player['full_name'] + ' added.')
            return
'''
'''
class Team:
    def __init__(self, teamName: str, roster=None):
        self.teamName = teamName
        
    def addPlayer(self, player):
        if 
'''

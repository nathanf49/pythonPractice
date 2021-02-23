"""
These are the best WORKING Player classes currently, with cython testing added
"""
from nba_api.stats.static import players, teams
from nba_api.stats.endpoints import playergamelog
from nba_api.stats.library.parameters import SeasonAll
import time
from nba_api.stats.endpoints import leaguegamefinder

# TODO switch everything to c++ funtions


team_dict = teams.get_teams()
player_dict = players.get_players()


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
                        self.seasons = self.getStats()

        if hasattr(self, 'id') is False:  # player was not found
            raise Exception(str(playerName) + " could not be found. You may want to check your spelling.")

        # get career stats
        self.gamesPlayed = self.getGames()
        self.PTS = self.getPTS()
        self.PPG = self.getPPG()
        self.REB = self.getREB()
        self.RPG = self.getRPG()
        self.AST = self.getAST()
        self.APG = self.getAPG()
        self.activeSeasons = self.getActiveSeasons()

    def getGames(self, season=None, team=None):  # gets number of games played
        # allows user to get games from a specific season
        validSeasons = self.seasonInputChecker(season)

        # allows user to get games against a specific team or just total games
        totalGames = 0
        if team is None:
            for year in validSeasons:
                totalGames += len(year.games)
        else:
            team = getTeamAbbreviation(team)
            for year in validSeasons:
                totalGames += year.getNumberOfGames(team)
        return totalGames

    def getPTS(self, season=None, team=None):  # get points scored
        # allows user to get games from a specific season
        validSeasons = self.seasonInputChecker(season)

        totalPoints = 0
        if team is None:
            for year in validSeasons:
                totalPoints += year.PTS
        else:  # go season by season to get stats against a specific team
            team = getTeamAbbreviation(team)
            for year in validSeasons:
                totalPoints += year.getSeasonPTS(team)
        return totalPoints

    def getPPG(self, season=None, team=None):  # get average points scored per game
        # getPTS and getGames only gets season and team inputs that aren't None, so any mix will arrive correctly
        if team is not None:
            team = getTeamAbbreviation(team)
        return round(self.getPTS(season=season, team=team) / self.getGames(season=season, team=team), 2)

    def getREB(self, season=None, team=None):  # get total rebounds
        # allows user to get games from a specific season
        validSeasons = self.seasonInputChecker(season)

        totalREB = 0
        if team is None:
            for year in validSeasons:
                totalREB += year.REB
        else:  # goes season by season to find stats against a specific team
            team = getTeamAbbreviation(team)
            for year in validSeasons:
                totalREB += year.getSeasonREB(team)
        return totalREB

    def getRPG(self, season=None, team=None):  # get average rebounds per game
        if team is not None:
            team = getTeamAbbreviation(team)
        return round(self.getREB(season=season, team=team) / self.getGames(season=season, team=team), 2)

    def getAST(self, season=None, team=None):  # get total assists
        # allows user to get games from a specific season
        validSeasons = self.seasonInputChecker(season)

        totalAST = 0
        if team is None:
            for year in validSeasons:
                totalAST += year.AST
        else:  # goes season by season to find stats against a specific team
            team = getTeamAbbreviation(team)
            for year in validSeasons:
                totalAST += year.getSeasonAST(team)
        return totalAST

    def getAPG(self, season=None, team=None):  # get average assists per game
        if team is not None:
            team = getTeamAbbreviation(team)
        return round(self.getAST(season=season, team=team) / self.getGames(season=season, team=team), 2)

    def getActiveSeasons(self):
        activeSeasons = []
        for year in self.seasons:
            activeSeasons.append(int(str(year.games[0].seasonID)[-4:]))
        return activeSeasons

    def getStats(self, season=None):
        if season is not None:  # updating a season, not the whole career
            while len(str(season)) != 4:
                season = int(input('Please enter the season you want to update as a 4 digit year'))
            gamestats = playergamelog.PlayerGameLog(player_id=self.id, season=season).get_dict()
            'need to finish updates after importing career stats'
            seasonGames = []
            for game in gamestats['resultSets'][0]['rowSet']:  # saves all player stats from individual games
                seasonGames.append(
                    GameStats(PTS=game[24], REB=game[18], AST=game[19], seasonID=game[0], playerID=self.id,
                              gameID=game[2],
                              date=game[3], matchup=game[4], WL=game[5], MIN=game[6], FGM=game[7],
                              FGA=game[8], FG_PCT=game[9], FG3M=game[10], FG3A=game[11], FG3_PCT=game[12],
                              FTM=game[13], FTA=game[14], FT_PCT=game[15], OREB=game[16], DREB=game[17], STL=game[20],
                              BLK=game[21], TO=game[22], PF=game[23], PLUS_MINUS=game[25]))
            return Season(str(season), seasonGames)

        else:
            # gets career dataframes from nba_api module
            careerStats = playergamelog.PlayerGameLog(player_id=self.id, season=SeasonAll.all).get_data_frames()

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

    def seasonInputChecker(self, season):  # only return season inputs are years that player was active
        if season is None:  # if the year is not input all seasons are valid
            validSeasons = self.seasons
        elif type(season) is int:
            if season not in self.activeSeasons:
                raise ValueError('Player was not active during this season')
            else:
                validSeasons = [self.getStats(season)]
        elif type(season) is list:
            validSeasons = []
            for year in season:
                if year not in self.activeSeasons:
                    raise ValueError('Player was not active during this season')
                else:
                    validSeasons.append(self.getStats(year))
        else:
            raise TypeError('Seasons must be input as an integer or a list of integers')
        return validSeasons

    '''
    These functions are for a Player and are not really used anymore but could be helpful in the future

    def addSeason(self, season):  # allows a season to be added to a players career
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

    def updateStats(self):
        self.gamesPlayed = self.getGames()
        self.PTS = self.getPTS()
        self.PPG = self.getPPG()
        self.REB = self.getREB()
        self.RPG = self.getRPG()
        self.AST = self.getAST()
        self.APG = self.getAPG()
        self.activeSeasons = self.getActiveSeasons()
    '''

    def __str__(self):
        return 'PPG: ' + str(self.PPG) + ' RPG: ' + str(self.RPG) + ' APG: ' + str(self.APG)


class GameStats:
    def __init__(self, PTS=None, REB=None, AST=None, seasonID=None, playerID=None, gameID=None, date=None, matchup=None,
                 WL=None, MIN=None, FGM=None, FGA=None, FG_PCT=None, FG3M=None, FG3A=None, FG3_PCT=None, FTM=None,
                 FTA=None, FT_PCT=None, OREB=None, DREB=None, STL=None, BLK=None, TO=None, PF=None, PLUS_MINUS=None):
        self.PTS = PTS
        self.REB = REB
        self.AST = AST
        self.seasonID = str(seasonID)
        self.playerID = str(playerID)
        self.gameID = str(gameID)
        self.date = str(date)
        self.matchup = str(matchup)
        self.result = str(WL)
        self.minutes = MIN
        self.FGM = FGM
        self.FGA = FGA
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
        self.FG3M = FG3M  # 3s didn't always exist so they can be None
        self.FG3A = FG3A
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
        self.FTM = FTM
        self.FTA = FTA
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
        elif DREB is not None and self.REB is not None:  # self.REB has been set above, but self.DREB is set below
            self.OREB = self.REB - self.DREB
        else:
            self.OREB = None
        if DREB is not None:
            self.DREB = int(DREB)
        elif self.OREB is not None and self.REB is not None:
            self.DREB = self.REB - self.OREB
        else:
            self.DREB = None
        self.STL = STL
        self.BLK = BLK
        self.TO = TO
        self.PF = PF
        self.PLUS_MINUS = PLUS_MINUS

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

    def getNumberOfGames(self, team):
        team = getTeamAbbreviation(team)
        number = 0
        for game in self.games:
            if team in game.matchup:
                number += 1
        return number

    def getSeasonPTS(self, team=None):
        totalPoints = 0
        if team is None:
            for game in self.games:
                if game.PTS is not None:
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
                if game.REB is not None:
                    totalREB += game.REB
        else:
            team = getTeamAbbreviation(team)
            for game in self.games:
                if team in game.matchup:
                    totalREB += game.REB

        return totalREB

    def getRPG(self, team=None):
        if team is None:
            return self.REB / len(self.games)
        else:
            team = getTeamAbbreviation(team)
            return round(self.getSeasonREB(team) / self.getNumberOfGames(team), 2)

    def getSeasonAST(self, team=None):
        totalAST = 0
        if team is None:
            for game in self.games:
                if game.AST is not None:
                    totalAST += game.AST
        else:
            team = getTeamAbbreviation(team)
            for game in self.games:
                if team in game.matchup:
                    totalAST += game.AST
        return totalAST

    def getAPG(self, team=None):
        if team is None:
            return self.AST / len(self.games)
        else:
            team = getTeamAbbreviation(team)
            return round(self.getSeasonAST(team) / self.getNumberOfGames(team), 2)

    def __str__(self):
        return self.season + ': ' + str(self.PPG) + '/' + str(self.RPG) + '/' + str(self.APG) + ', ' + str(
            len(self.games)) + ' games played'


def getTeamAbbreviation(teamName):
    teamName = str(teamName).lower()
    for team in team_dict:
        if teamName in list(team['full_name'].lower().split(' ')) or team['abbreviation'].lower() == teamName:
            return team['abbreviation'].upper()
    raise Exception('Team not found')


def getTime(name):
    start = time.time()
    player = Player(name)
    print(time.time() - start)
    return player


# dame = getTime('Damian Lillard')
# jordan = Player('Michael Jordan')
# wilt = Player('Wilt Chamberlain') # TODO fix stats for old players


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
#this time we convert it to a dataframe in the same line of code
GSW = [x for x in teams if x['full_name'] == 'Golden State Warriors'][0]
GSW_id = GSW['id']
GSW_games = leaguegamefinder.LeagueGameFinder(team_id_nullable=GSW_id).get_data_frames()[0]

class Team:
    def __init__(self, teamName: str, roster=None):
        self.teamName = teamName

    def addPlayer(self, player):
        if 
'''


### How to run cython file ###

# setup file
"""
from distutils.core import setup
from Cython.Build import cythonize

setup(ext_modules = cythonize('cTestClasses.pyx'))
"""

# run 'python3 setup.py build_ext --inplace' in terminal in this folder to compile


# run python3 from command prompt and import cTestClasses to run
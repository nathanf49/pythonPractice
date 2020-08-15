from nba_api.stats.static import players, teams
from nba_api.stats.endpoints import playergamelog
from nba_api.stats.library.parameters import SeasonAll
"""

Need to work on importing stats to finish getting player data

"""
player_dict = players.get_players()
team_dict = teams.get_teams()
import pandas as pd

# Call the API endpoint passing in lebron's ID & which season
gamelog_bron18 = playergamelog.PlayerGameLog(player_id='2544', season='2018')
gamelog_bron19 = playergamelog.PlayerGameLog(player_id='2544', season='2019')
gamelog_bron20 = playergamelog.PlayerGameLog(player_id='2544', season='2020')
# Converts gamelog object into a pandas dataframe
# can also convert to JSON or dictionary
df_bron_games_2018 = gamelog_bron18.get_data_frames()
df_bron_games_2019 = gamelog_bron19.get_data_frames()
df_bron_games_2020 = gamelog_bron20.get_data_frames()

# If you want all seasons, you must import the SeasonAll parameter


gamelog_bron_all = playergamelog.PlayerGameLog(player_id='2544', season=SeasonAll.all)

df_bron_games_all = gamelog_bron_all.get_data_frames()


class Player:  # import player information from dictionaries
    def __init__(self, playerName: str):
        if ' ' in playerName:  # name is a full name
            for player in player_dict:
                if player['full_name'].lower() == playerName.lower():  # avoid case issues by converting all to lower
                    self.id = player['id']
                    self.name = player['full_name']
                    self.isActive = player['is_active']
                    # get stats

        else:
            for player in player_dict:  # check for player first or last name
                if player['first_name'].lower() == playerName.lower() or player['last_name'].lower() == playerName.lower():
                    checkPlayer = ''
                    # confirm since we don't have the full name
                    while checkPlayer not in ['yes', 'Yes', 'YES', 'YEs', 'Y', 'y', 'no', 'No', 'NO', 'n', 'N']:
                        checkPlayer = input('Did you mean ' + player['full_name'] + '?')
                    if checkPlayer in ['yes', 'Yes', 'YES', 'YEs', 'Y', 'y']:  # only input player if the answer is yes
                        self.id = player['id']
                        self.name = player['full_name']
                        self.isActive = player['is_active']
                        # get stats
                        break

        if hasattr(Player, 'self.id') is False:  # player was not found
            raise Exception(str(playerName) + " could not be found. You may want to check your spelling.")

        # player found, can now input stats with the player ID

    def updateAllStats(self, season=None):
        if season is not None:  # updating a season, not the whole career
            while len(str(season)) != 4:
                season = int(input('Please enter the season you want to update as a 4 digit year'))
            gamelog = playergamelog.PlayerGameLog(player_id=self.id, season=season)
            gamestats = gamelog.get_data_frames()
            'need to finish updates after importing career stats'
            seasonGames = []
            for game in gamestats[0]: # saves all player stats from individual games
                seasonGames.append(
                    GameStats_Player(game['PTS'], game['REB'], game['AST'], game['SEASON_ID'], self.id, game['GAME_ID'],
                                     game['GAME_DATE'], game['MATCHUP'], game['WL'], game['MIN'], game['FGM'],
                                     game['FGA'], game['FG_PCT'], game['FG3M'], game['FG3A'], game['FG3_PCT'],
                                     game['FTM'], game['FTA'], game['FT_PCT'], game['OREB'], game['DREB'], game['STL'],
                                     game['BLK'], game['TOV'], game['PF'], game['PLUS_MINUS']))

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
            seasonalStats = []
            for year in activeYears:
                seasonalStats.append(self.updateAllStats(year))


""" Need to work on importing stats to finish getting player data """
""" Might need to add a season class. Not sure yet """

class GameStats_Player:
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
                self.FG_PCT = self.FGM / self.FGA
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
                self.FG3_PCT = self.FG3M / self.FG3A
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
                self.FT_PCT = self.FTM / self.FTA
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
            self.BLk = None
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

from nba_api.stats.static import players, teams
from nba_api.stats.endpoints import playergamelog
from nba_api.stats.library.parameters import SeasonAll

player_dict = players.get_players()
team_dict = teams.get_teams()
import pandas as pd

#Call the API endpoint passing in lebron's ID & which season
gamelog_bron18 = playergamelog.PlayerGameLog(player_id='2544', season = '2018')
gamelog_bron19 = playergamelog.PlayerGameLog(player_id='2544', season = '2019')
gamelog_bron20 = playergamelog.PlayerGameLog(player_id='2544', season = '2020')
#Converts gamelog object into a pandas dataframe
#can also convert to JSON or dictionary
df_bron_games_2018 = gamelog_bron18.get_data_frames()
df_bron_games_2019 = gamelog_bron19.get_data_frames()
df_bron_games_2020 = gamelog_bron20.get_data_frames()

# If you want all seasons, you must import the SeasonAll parameter


gamelog_bron_all = playergamelog.PlayerGameLog(player_id='2544', season = SeasonAll.all)

df_bron_games_all = gamelog_bron_all.get_data_frames()


class Player: # import player information from dictionaries
    def __init__(self, playerName: str):
        if ' ' in playerName: # name is a full name
            for player in player_dict:
                if player['full_name'].lower() == playerName.lower(): # avoid case issues by converting all to lower
                    self.id = player['id']
                    self.name = player['full_name']
                    self.isActive = player['is_active']

        else:
            for player in player_dict: # check for player first or last name
                if player['first_name'].lower() == playerName.lower() or player['last_name'].lower() == playerName.lower():
                    checkPlayer = ''
                    # confirm since we don't have the full name
                    while checkPlayer not in ['yes','Yes','YES','YEs','Y','y','no','No','NO','n','N']:
                        checkPlayer = input('Did you mean ' + player['full_name'] + '?')
                    if checkPlayer in ['yes','Yes','YES','YEs','Y','y']: # only input player if the answer is yes
                        self.id = player['id']
                        self.name = player['full_name']
                        self.isActive = player['is_active']

        if hasattr(Player, 'self.id') == False: # player was not found
            Exception(str(playerName) + " could not be found. You may want to check your spelling.")

        # player found, can now input stats with the player ID

    def updateAllStats(self, season=None):
        if season is not None: # updating a season, not the whole career
            while len(str(season)) != 4:
                season = int(input('Please enter the season you want to update as a 4 digit year'))
            gamelog = playergamelog.PlayerGameLog(player_id=self.id, season=season)
            gamestats = gamelog.get_data_frames()
            'need to finish updates after importing career stats'

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
            for year in activeYears:
                self.seasonStats.append(updateAllStats(year))

class GameStats_Player:
    def __init__(self,seasonID=None,playerID=None,gameID=None,date=None,matchup=None,WL=None,MIN=None,FGM=None,FGA=None,FG_PCT=None,FG3M=None,FG3A=None,FG3_PCT=None,FTM=None,FTA=None,FT_PCT=None,OREB=None,DREB=None,REB=None,AST=None,STL=None,TO=None,PF=None,PLUS_MINUS=None):
        if seasonID is not None:
            self.seasonID = str(seasonID)
        if playerID is not None:
            self.playerID = str(playerID)
        if gameID is not None:
            self.gameID = str(gameID)
        if date is not None:
            self.date = str(date)
        if matchup is not None:
            self.matchup = str(matchup)



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
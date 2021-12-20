from nba_api.stats.static import players, teams
from nba_api.stats.endpoints import playergamelog
from nba_api.stats.library.parameters import SeasonAll
import time

# import pandas as pd
# from nba_api.stats.endpoints import leaguegamefinder

# TODO currently working on adding advanced stats

team_dict = teams.get_teams()
player_dict = players.get_players()


class Player:  # import player information from dictionaries
    def __init__(self, playerName=None, season=None):
        while type(playerName) is not str:
            playerName = str(input('Please input the name of a current or past NBA player: '))
        if ' ' in playerName:  # name is a full name
            playersOut = players.find_players_by_full_name(playerName)
            if len(playersOut) == 0:  # return error if player is not found
                Exception('Player not found.')
            elif len(playersOut) > 1:  # make user select proper player if there is more than 1 option
                for player in playersOut:
                    checkPlayer = input('Did you mean ' + player['full_name'] + '?')  # confirm player
                    if checkPlayer in ['yes', 'Yes', 'YES', 'YEs', 'Y', 'y']:  # only input player if the answer is yes
                        self.id = player['id']
                        self.name = player['full_name']
                        self.isActive = player['is_active']
                        self.careerStats, self.seasons = self.getStats(season)
                        break

            else:  # only one option for player, assume it's right
                player = playersOut[0]  # using this instead of editing lines below to keep data input the same
                self.id = player['id']
                self.name = player['full_name']
                self.isActive = player['is_active']
                self.careerStats, self.seasons = self.getStats(season)

        else:  # check for player first or last name
            playersOut = players.find_players_by_first_name(playerName)
            for player in players.find_players_by_last_name(playerName):
                playersOut.append(player)
            for player in playersOut:
                checkPlayer = ''
                # confirm since we don't have the full name
                while checkPlayer.lower() not in ['yes', 'y', 'no', 'n']:  # answer must be yes or no
                    checkPlayer = input('Did you mean ' + player['full_name'] + '?')
                if checkPlayer.lower() in ['yes', 'y']:  # only input player if the answer is yes
                    self.id = player['id']
                    self.name = player['full_name']
                    self.isActive = player['is_active']
                    self.careerStats, self.seasons = self.getStats(season)
                    break

        if hasattr(self, 'id') is False:  # player was not found
            raise Exception(str(playerName) + " could not be found. You may want to check your spelling.")

    def getStats(self, season=None):
        if season is not None:  # getting a season, not the whole career
            while len(str(season)) != 4 or type(season) != int:
                season = int(input('Please enter the season you want to update as a 4 digit year'))
            stats = Season(playergamelog.PlayerGameLog(player_id=self.id, season=season).get_data_frames()[0])
            seasons = {season: len(stats.gameData)}

        else:
            # gets career dataframes from nba_api module, returns the dataframe of the career and each season
            stats = [Season(playergamelog.PlayerGameLog(player_id=self.id, season=SeasonAll.all).get_data_frames()[0])]
            seasons = {}
            for year in stats[0].gameData['SEASON_ID']:  # gets the number of games in each season
                if year[-4:] not in seasons:
                    seasons[year[-4:]] = 1
                else:
                    seasons[year[-4:]] += 1

            totalGames = 0
            for year in seasons:  # appends data frame of each season to careerStats
                stats.append(Season(stats[0].gameData[totalGames:totalGames + seasons[year]]))  # splits seasons up
                totalGames += seasons[year]

        return stats, seasons

    def __str__(self):
        return self.name


class Season:
    def __init__(self, season):
        self.season = str(min(season['SEASON_ID'])[-4:])  # all the same but indexing isn't consistent so we use min
        if max(season['SEASON_ID'])[-4:] != min(season['SEASON_ID'])[-4:]:
            self.season = 'Career: ' + str(min(season['SEASON_ID'])[-4:]) + '-' + str(max(season['SEASON_ID'])[-4:])
        self.gameData = season

        # update all stats
        if len(self.gameData) > 0:
            self.PTS = self.getPTS()
            self.PPG = round(self.getPPG(), 2)
            self.REB = self.getREB()
            self.RPG = round(self.getRPG(), 2)
            self.AST = self.getAST()
            self.APG = round(self.getAPG(), 2)

    def getNumberOfGames(self, team):
        team = getTeamAbbreviation(team)
        number = 0
        for game in self.gameData['MATCHUP']:
            if team in game:
                number += 1
        return number

    def getPTS(self, team=None):
        if team is None:
            totalPoints = sum(self.gameData['PTS'])
        else:
            team = getTeamAbbreviation(team)
            totalPoints = 0
            for game in self.gameData.iterrows():
                if team in game[1]['MATCHUP']:
                    totalPoints += game[1]['PTS']
        return totalPoints

    def getPPG(self, team=None):
        if team is None:
            return self.PTS / len(self.gameData)
        else:
            team = getTeamAbbreviation(team)
            return self.getPTS(team) / self.getNumberOfGames(team)

    def getREB(self, team=None):
        if team is None:
            totalREB = sum(self.gameData['REB'])
        else:
            team = getTeamAbbreviation(team)
            totalREB = 0
            for game in self.gameData.iterrows():
                if team in game[1]['MATCHUP']:
                    totalREB += game[1]['REB']

        return totalREB

    def getRPG(self, team=None):
        if team is None:
            return self.REB / len(self.gameData)
        else:
            team = getTeamAbbreviation(team)
            return round(self.getREB(team) / self.getNumberOfGames(team), 2)

    def getAST(self, team=None):
        if team is None:
            totalAST = sum(self.gameData['AST'])
        else:
            team = getTeamAbbreviation(team)
            totalAST = 0
            for game in self.gameData.iterrows():
                if team in game[1]['MATCHUP']:
                    totalAST += game[1]['AST']
        return totalAST

    def getAPG(self, team=None):
        if team is None:
            return self.AST / len(self.gameData)
        else:
            team = getTeamAbbreviation(team)
            return round(self.getAST(team) / self.getNumberOfGames(team), 2)

    def __str__(self):
        return self.season + ': ' + str(self.PPG) + '/' + str(self.RPG) + '/' + str(self.APG) + ', ' + \
               str(len(self.gameData)) + ' games played'


def getTeamAbbreviation(teamName):
    teamName = str(teamName).lower()
    for team in team_dict:
        if teamName in list(team['full_name'].lower().split(' ')) or team['abbreviation'].lower() == teamName or team[
            'city'].lower() == teamName or team['nickname'].lower() == teamName:
            return team['abbreviation'].upper()  # checks every element of full name, team abbreviation, mascot and city
    raise Exception('Team not found')


def getTime(name):
    start = time.time()
    player = Player(name)
    print(time.time() - start)
    return player


dame = getTime('Damian Lillard')
# jordan = Player('Michael Jordan')
# wilt = Player('Wilt Chamberlain')


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

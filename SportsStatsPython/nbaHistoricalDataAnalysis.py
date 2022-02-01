from nba_api.stats.static import players, teams
import nbaClasses
import timeit

team_dict = teams.get_teams()
player_dict = players.get_players()

players = []

for player in player_dict:  # times out. not getting any data rn
    stats = nbaClasses.Player(player['full_name'])
    players.append(stats)
pass
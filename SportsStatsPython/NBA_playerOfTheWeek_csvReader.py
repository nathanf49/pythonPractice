import csv


def percentage(players):
    """
    Calculates and prints the average win percentage and overall wins of each player, team, conference, and position
    """
    playerCount = {}
    teamCount = {}
    conferenceCount = {}
    positionCount = {}

    for p in players:
        if p['Player'] in playerCount:  # individual players
            playerCount[p['Player']] += 1
        else:
            playerCount[p['Player']] = 1

        if p['Team'] in teamCount:
            teamCount[p['Team']] += 1
        else:
            teamCount[p['Team']] = 1

        if p['Conference'] in conferenceCount:
            teamCount[p['Conference']] += 1
        else:
            conferenceCount[p['Conference']] = 1

        if p['Position'] in positionCount:
            positionCount[p['Team']] += 1
        else:
            positionCount[p['Team']] = 1

    for player in playerCount:
        if playerCount[player] != 0:
            print(str(player) + ': ' + str(playerCount[player]) + str(playerCount[player]/sum(playerCount.values())))

    for team in teamCount:
        if teamCount[team] != 0:
            print(str(team) + ': ' + str(teamCount[team]) + str(teamCount[team] / sum(teamCount.values())))

    for conference in conferenceCount:
        print(str(conference) + ': ' + str(conferenceCount[conference]) + str(conferenceCount[conference] / sum(conferenceCount.values())))

    for position in positionCount:
        print(str(position) + ': ' + str(positionCount[position]) + str(positionCount[position] / sum(positionCount.values())))



if __name__ == '__main__':
    file = 'NBA_player_of_the_week.csv'
    with open(file) as f:
        data = csv.DictReader(f)
        playerOfTheWeek = []
        for row in data:
            playerOfTheWeek += row
            
    percentage(playerOfTheWeek)


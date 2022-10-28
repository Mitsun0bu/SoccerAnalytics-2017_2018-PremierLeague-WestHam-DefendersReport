from statistics import mean

def getLeagueDefenderInterceptPerGame(events, defenderList):
    interceptTag         = 1401
    leagueDefenderInterceptPerGameList = []

    for defenderId in defenderList:
        interceptCount  = 0
        gamesPlayedList = []

        for event in events:
            if event['playerId'] == defenderId:
                if event['matchId'] not in gamesPlayedList: 
                    gamesPlayedList.append(event['matchId'])
                for tag in event['tags']:
                    if tag['id'] == interceptTag:
                        interceptCount = interceptCount + 1

        if len(gamesPlayedList):
            interceptPerGame = round((interceptCount / len(gamesPlayedList)), 1)

        leagueDefenderInterceptPerGameList.append(interceptPerGame)
    
    averageLeagueDefenderInterceptPerGame = round(mean(leagueDefenderInterceptPerGameList), 1)
    
    return averageLeagueDefenderInterceptPerGame
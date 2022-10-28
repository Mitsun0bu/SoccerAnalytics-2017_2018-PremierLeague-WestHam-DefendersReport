def getPlayerInterceptPerGame(events, defenderId):
    interceptTag    = 1401
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
    return interceptPerGame
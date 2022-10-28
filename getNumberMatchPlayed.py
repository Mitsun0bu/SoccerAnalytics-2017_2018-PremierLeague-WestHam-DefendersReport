def getNumberMatchPlayed(events, playerId):
    gamesPlayedList = []

    for event in events:
        if event['playerId'] == playerId:
            if event['matchId'] not in gamesPlayedList: 
                gamesPlayedList.append(event['matchId'])
    return (len(gamesPlayedList))
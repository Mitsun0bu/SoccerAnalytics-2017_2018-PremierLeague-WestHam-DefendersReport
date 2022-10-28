def getPlayerDefendingDuelSuccessRate(events, playerId):
    
    wonTag             = 703
    wonCount           = 0
    totalCount         = 0

    for event in events:
        if event['subEventName'] == "Ground defending duel" and event['playerId'] == playerId:
            totalCount = totalCount + 1
            for tag in event['tags']:
                if tag['id'] == wonTag:
                    wonCount = wonCount + 1
           
    defendingDuelSuccessRate = round(((wonCount / totalCount)  * 100), 1)

    return defendingDuelSuccessRate
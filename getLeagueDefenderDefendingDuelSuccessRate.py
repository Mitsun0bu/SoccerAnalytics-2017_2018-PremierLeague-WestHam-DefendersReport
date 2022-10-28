def getLeagueDefenderDefendingDuelSuccessRate(events, defenderList):
    
    wonTag                   = 703

    for defenderId in defenderList:
        wonCount           = 0
        totalCount         = 0
    
        for event in events:
            if event['playerId'] == defenderId:
                if event['subEventName'] == "Ground defending duel":
                    totalCount = totalCount + 1
                    for tag in event['tags']:
                        if tag['id'] == wonTag:
                            wonCount = wonCount + 1
    
    defendingDuelSuccessRate = round(((wonCount / totalCount)  * 100), 1)
    
    return defendingDuelSuccessRate
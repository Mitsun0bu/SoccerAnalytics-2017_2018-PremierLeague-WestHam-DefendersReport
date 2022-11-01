from statistics import mean

def getLeagueDefenderDefendingDuelSuccessRate(events, defenderList):
    
    wonTag                   = 703
    successRateList          = []

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
        if totalCount == 0:
            defendingDuelSuccessRate = 0
        else:
            defendingDuelSuccessRate = round(((wonCount / totalCount)  * 100), 1)
        successRateList.append(defendingDuelSuccessRate)
   
    averageSuccessRate = mean(successRateList)
    averageSuccessRate = round(averageSuccessRate, 1)

    return averageSuccessRate
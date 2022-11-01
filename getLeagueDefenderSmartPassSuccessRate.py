from statistics import mean

def getLeagueDefenderSmartPassSuccessRate(events, defenderList):
    accurateTag     = 1801
    successRateList = []

    for defenderId in defenderList:
        accurateCount  = 0
        totalCount     = 0

        for event in events:
            if event['playerId'] == defenderId:
                if event['subEventName'] == "Smart pass":
                     totalCount = totalCount + 1
                     for tag in event['tags']:
                         if tag['id'] == accurateTag:
                             accurateCount = accurateCount + 1

        if totalCount == 0:
            smartPassSuccessRate = 0
        else:
            smartPassSuccessRate = round(((accurateCount / totalCount)  * 100), 1)
        successRateList.append(smartPassSuccessRate)
    
    averageSuccessRate = mean(successRateList)
    averageSuccessRate = round(averageSuccessRate, 1)

    return averageSuccessRate
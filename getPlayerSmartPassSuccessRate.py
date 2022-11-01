def getPlayerSmartPassSuccessRate(events, playerId):
    
    accurateTag     = 1801
    accurateCount  = 0
    totalCount     = 0

    for event in events:
        if event['subEventName'] == "Smart pass" and event['playerId'] == playerId:
            totalCount = totalCount + 1
            for tag in event['tags']:
                if tag['id'] == accurateTag:
                    accurateCount = accurateCount + 1

    if totalCount == 0:
        smartPassSuccessRate = 0
    else:
        smartPassSuccessRate = round(((accurateCount / totalCount)  * 100), 1)

    return smartPassSuccessRate
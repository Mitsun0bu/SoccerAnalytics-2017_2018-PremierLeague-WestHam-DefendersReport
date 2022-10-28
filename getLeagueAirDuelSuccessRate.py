def getLeagueAirDuelSuccessRate(events):
    wonTag             = 703
    wonCount           = 0
    totalCount         = 0
    airDuelSuccessRate = 0

    for event in events:
        if event['subEventName'] == "Air duel":
            totalCount = totalCount + 1
            for tag in event['tags']:
                if tag['id'] == wonTag:
                    wonCount = wonCount + 1
    airDuelSuccessRate = round(((wonCount / totalCount)  * 100), 1)
    return airDuelSuccessRate
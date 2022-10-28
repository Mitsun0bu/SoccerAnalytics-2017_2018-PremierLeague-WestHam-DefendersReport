def getPlayerRedCardsNumber(events, playerId):
    redCardTag   = 1701
    redCardCount = 0

    for event in events:
        if event['subEventName'] == "Foul" and event['playerId'] == playerId:
            for tag in event['tags']:
                if tag['id'] == redCardTag:
                    redCardCount = redCardCount + 1

    return redCardCount
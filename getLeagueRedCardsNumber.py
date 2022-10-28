def getLeagueRedCardsNumber(events):
    redCardTag   = 1701
    redCardCount = 0

    for event in events:
        if event['subEventName'] == "Foul":
            for tag in event['tags']:
                if tag['id'] == redCardTag:
                    redCardCount = redCardCount + 1

    return redCardCount
def getConcededGoalCoordinate(matchIdList, events, teamId):
    concededGoalTotal    = 0
    concededOwnGoal      = 0
    shotXList            = []
    shotYList            = []

    # For each match playe by a team
    for matchId in matchIdList:
        # For each event in the data set
        for event in events:
            # If the event corresponds to a match played by the team 
            if event['matchId'] == matchId :
                eventType = event['eventName']
                if event['tags']:
                    tag = event['tags'][0].get('id')
                eventTeamId = event['teamId']
                # If the event is a 'Shot' / 'Free Kick' by an opposing team leading to a goal
                if (eventType == 'Shot' or eventType == 'Free Kick') and \
                   tag == 101                                        and \
                   eventTeamId != teamId:
                    concededGoalTotal = concededGoalTotal + 1
                    shotX = event['positions'][0].get('x')
                    shotY = event['positions'][0].get('y')
                    shotXList.append(shotX)
                    shotYList.append(shotY)
                # Else if the event is an own goal
                elif tag == 102 and eventTeamId == teamId:
                    concededOwnGoal = concededOwnGoal + 1
                    concededGoalTotal = concededGoalTotal + 1
                    shotX = event['positions'][0].get('x')
                    shotY = event['positions'][0].get('y')
                    shotXList.append(shotX)
                    shotYList.append(shotY)

    return shotXList, shotYList, concededGoalTotal
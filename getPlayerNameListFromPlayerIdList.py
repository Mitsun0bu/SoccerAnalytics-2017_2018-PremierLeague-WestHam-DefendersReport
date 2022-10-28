def getPlayerNameListFromPlayerIdList(players, playerIdList):
    playerNameList = []
    for playerId in playerIdList:    
        for player in players:
            if player['wyId'] == playerId:
                playerNameList.append(player['shortName'])
    return playerNameList
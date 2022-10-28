def getLeaguePlayerIdList(players, leagueTeamIdList):
    '''
    Parameters :
        players          : list
        leagueTeamIdList : list

    Returns    :
        A list of IDs for the players playing in a given league
    '''
    playerIdList = []
    for player in players:
        if player['currentTeamId'] in leagueTeamIdList:
            playerIdList.append(player['wyId'])
    return playerIdList
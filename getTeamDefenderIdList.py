def getTeamDefenderIdList(players, teamId):
    '''
    Parameters :
        players  : list
        teamId   : int

    Returns    :
        A list of IDs for the defenders playing in a given team
    '''
    defenderIdList = []
    for player in players:
        if (player['currentTeamId'] == teamId and
            player['role']['name'] == 'Defender'):
                defenderIdList.append(player['wyId'])
    return defenderIdList
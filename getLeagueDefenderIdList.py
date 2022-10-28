def getLeagueDefenderIdList(players, leagueTeamIdList):
    '''
    Parameters :
        players          : list
        leagueTeamIdList : list

    Returns    :
        A list of IDs for the defenders playing in a given league
    '''
    defenderIdList = []
    for player in players:
        if player['currentTeamId'] in leagueTeamIdList and player['role']['name'] == 'Defender':
            defenderIdList.append(player['wyId'])
    return defenderIdList
def getMatchIdList(matches, teamId):
    '''
    Parameters :
        matches  : list
        teamId   : int

    Returns    :
        A list of IDs for the games played by a team during a given competition
    '''
    matchIdList = []
    for match in matches:
        teamsData = list(match['teamsData'].keys())
        if int(teamsData[0]) == teamId or int(teamsData[1]) == teamId:
            matchIdList.append(match['wyId'])
    return matchIdList
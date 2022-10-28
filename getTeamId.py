def getTeamId(teams, teamName):
    '''
    Parameters :
        teams    : list
        teamName : string

    Returns    :
        The ID of a given team
    '''
    for team in teams:
        if team['name'] == teamName :
            return team['wyId']
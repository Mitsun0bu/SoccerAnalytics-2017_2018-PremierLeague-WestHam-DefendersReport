def getLeagueTeamIdList(teams, country):
    '''
    Parameters :
        teams    : list
        country  : string

    Returns    :
        The ID of all teams from a given country
    '''
    teamIdList = []
    for team in teams:
        if team['area']['name'] == country:
            teamIdList.append(team['wyId'])
    return teamIdList
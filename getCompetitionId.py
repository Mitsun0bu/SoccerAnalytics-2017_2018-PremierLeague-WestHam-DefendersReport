def getCompetitionId(competitions, competitionName):
    '''
    Parameters :
        competitions   : list
        competitonName : string

    Returns    :
        The ID of a given competition
    '''
    for competition in competitions:
        if competition['name'] == competitionName :
            return competition['wyId']
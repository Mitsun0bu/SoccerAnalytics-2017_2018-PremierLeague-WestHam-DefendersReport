def getSeasonMatches(matches, seasonId):
    '''
    Parameters :
        matches  : list
        seasonId : int

    Returns    :
        List of matches played in a given competition, during a given season
    '''
    for i in range(len(matches)):
        if matches[i]['seasonId'] != seasonId:
            del matches[i]
            break
def getSeasonId(matches, seasonYear):
    '''
    Parameters :
        matches : list

    Returns    :
        The ID of a given season
    '''
    for match in matches:
        if match['dateutc'].startswith(seasonYear + "-10"):
            return match['seasonId']
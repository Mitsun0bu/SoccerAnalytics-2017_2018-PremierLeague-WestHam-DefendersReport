import json

import pandas                                    as pd

from   getCompetitionId                          import getCompetitionId
from   getSeasonId                               import getSeasonId
from   getLeagueTeamIdList                       import getLeagueTeamIdList
from   getTeamId                                 import getTeamId
from   getMatchIdList                            import getMatchIdList
from   getSeasonMatches                          import getSeasonMatches

from getConcededGoalCoordinate                   import getConcededGoalCoordinate
from drawDividedPitch                            import drawDividedPitch

from fillPitchDivisionGoalConceded               import fillPitchDivisionGoalConceded

from getGoalMap                                  import getGoalMap


# *************************************************************************** #
#                                                                             #
#                         ~~~ OPEN JSONs FILES ~~~                            #
#                                                                             #
# *************************************************************************** #


wyscoutFolderPath = "../wyscout_data/"

with open(wyscoutFolderPath + "competitions.json") as competitionsFile:
    competitions = json.load(competitionsFile)

with open(wyscoutFolderPath + "teams.json") as teamsFile:
    teams = json.load(teamsFile)

with open(wyscoutFolderPath + "players.json") as playerFile:
    players = json.load(playerFile)

with open(wyscoutFolderPath + "matches/matches_England.json") as matchesFile:
    matches = json.load(matchesFile)
    
with open(wyscoutFolderPath + "events/events_England.json") as eventsFile:
    events = json.load(eventsFile)

# *************************************************************************** #
#                                                                             #
#                         ~~~ GET IDs OF INTEREST ~~~                         #
#                                                                             #
# *************************************************************************** #


country                 = "England"
competitionName         = "English first division"
seasonYear              = "2017"

# Get ID of the 2017-2018 Season
seasonId                = getSeasonId(matches, seasonYear)

# Get ID of the Premier League
competitionId           = getCompetitionId(competitions, competitionName)

nameManCity             = "Manchester City"
nameManUtd              = "Manchester United"
nameTottenham           = "Tottenham Hotspur"
nameChelsea             = "Chelsea"
nameLiverpool           = "Liverpool"

idManCity               = getTeamId(teams, nameManCity)
idManUtd                = getTeamId(teams, nameManUtd)
idTottenham             = getTeamId(teams, nameTottenham)
idChelsea               = getTeamId(teams, nameChelsea)
idLiverpool             = getTeamId(teams, nameLiverpool)

matchIdListManCity      = getMatchIdList(matches, idManCity)
matchIdListManUtd       = getMatchIdList(matches, idManUtd)
matchIdListTottenham    = getMatchIdList(matches, idTottenham)
matchIdListChelsea      = getMatchIdList(matches, idChelsea)
matchIdListLiverpool    = getMatchIdList(matches, idLiverpool)


# *************************************************************************** #
#                                                                             #
#                         ~~~ GET SEASON DATA ~~~                             #
#                                                                             #
# *************************************************************************** #


getSeasonMatches(matches, seasonId)

    
# *************************************************************************** #
#                                                                             #
#                         ~~~ GET MAN CITY MAP ~~~                            #
#                                                                             #
# *************************************************************************** #


shotXList, shotYList, nConcededGoal = getConcededGoalCoordinate(matchIdListManCity, events, idManCity)
dfGoalCoord                         = pd.DataFrame({"x": shotXList, "y": shotYList})
figGoalMap, axGoalMap               = getGoalMap()

drawDividedPitch(axGoalMap, grids = True)

fillPitchDivisionGoalConceded(nConcededGoal, axGoalMap, dfGoalCoord)


# *************************************************************************** #
#                                                                             #
#                         ~~~ GET MAN UTD MAP ~~~                             #
#                                                                             #
# *************************************************************************** #


shotXList, shotYList, nConcededGoal = getConcededGoalCoordinate(matchIdListManUtd, events, idManUtd)
dfGoalCoord                         = pd.DataFrame({"x": shotXList, "y": shotYList})
figGoalMap, axGoalMap               = getGoalMap()

drawDividedPitch(axGoalMap, grids = True)

fillPitchDivisionGoalConceded(nConcededGoal, axGoalMap, dfGoalCoord)

# *************************************************************************** #
#                                                                             #
#                         ~~~ GET TOTTENHAM MAP ~~~                           #
#                                                                             #
# *************************************************************************** #


shotXList, shotYList, nConcededGoal = getConcededGoalCoordinate(matchIdListTottenham, events, idTottenham)
dfGoalCoord                         = pd.DataFrame({"x": shotXList, "y": shotYList})
figGoalMap, axGoalMap               = getGoalMap()

drawDividedPitch(axGoalMap, grids = True)

fillPitchDivisionGoalConceded(nConcededGoal, axGoalMap, dfGoalCoord)


# *************************************************************************** #
#                                                                             #
#                         ~~~ GET CHELSEA MAP ~~~                             #
#                                                                             #
# *************************************************************************** #


shotXList, shotYList, nConcededGoal = getConcededGoalCoordinate(matchIdListChelsea, events, idChelsea)
dfGoalCoord                         = pd.DataFrame({"x": shotXList, "y": shotYList})
figGoalMap, axGoalMap               = getGoalMap()

drawDividedPitch(axGoalMap, grids = True)

fillPitchDivisionGoalConceded(nConcededGoal, axGoalMap, dfGoalCoord)


# *************************************************************************** #
#                                                                             #
#                         ~~~ GET LIVERPOOL MAP ~~~                           #
#                                                                             #
# *************************************************************************** #


shotXList, shotYList, nConcededGoal = getConcededGoalCoordinate(matchIdListLiverpool, events, idLiverpool)
dfGoalCoord                         = pd.DataFrame({"x": shotXList, "y": shotYList})
figGoalMap, axGoalMap               = getGoalMap()

drawDividedPitch(axGoalMap, grids = True)

fillPitchDivisionGoalConceded(nConcededGoal, axGoalMap, dfGoalCoord)





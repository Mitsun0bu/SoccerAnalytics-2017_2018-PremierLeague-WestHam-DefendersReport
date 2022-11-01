import json

import pandas                                    as pd

from   getCompetitionId                          import getCompetitionId
from   getSeasonId                               import getSeasonId
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

fillPitchDivisionGoalConceded(25, axGoalMap, dfGoalCoord, "#5CBEEB")

figGoalMap.set_size_inches(10, 10)
savePath = "./output/ManCityGoalMap.png"
figGoalMap.savefig(savePath, dpi = 800, transparent=True)

# *************************************************************************** #
#                                                                             #
#                         ~~~ GET MAN UTD MAP ~~~                             #
#                                                                             #
# *************************************************************************** #


shotXList, shotYList, nConcededGoal = getConcededGoalCoordinate(matchIdListManUtd, events, idManUtd)
dfGoalCoord                         = pd.DataFrame({"x": shotXList, "y": shotYList})
figGoalMap, axGoalMap               = getGoalMap()

drawDividedPitch(axGoalMap, grids = True)

fillPitchDivisionGoalConceded(26, axGoalMap, dfGoalCoord, "#E30606")

figGoalMap.set_size_inches(10, 10)
savePath = "./output/ManUtdGoalMap.png"
figGoalMap.savefig(savePath, dpi = 800, transparent=True)

# *************************************************************************** #
#                                                                             #
#                         ~~~ GET TOTTENHAM MAP ~~~                           #
#                                                                             #
# *************************************************************************** #


shotXList, shotYList, nConcededGoal = getConcededGoalCoordinate(matchIdListTottenham, events, idTottenham)
dfGoalCoord                         = pd.DataFrame({"x": shotXList, "y": shotYList})
figGoalMap, axGoalMap               = getGoalMap()

drawDividedPitch(axGoalMap, grids = True)

fillPitchDivisionGoalConceded(35, axGoalMap, dfGoalCoord, "#001C57")

figGoalMap.set_size_inches(10, 10)
savePath = "./output/TottenhamGoalMap.png"
figGoalMap.savefig(savePath, dpi = 800, transparent=True)

# *************************************************************************** #
#                                                                             #
#                         ~~~ GET CHELSEA MAP ~~~                             #
#                                                                             #
# *************************************************************************** #


shotXList, shotYList, nConcededGoal = getConcededGoalCoordinate(matchIdListChelsea, events, idChelsea)
dfGoalCoord                         = pd.DataFrame({"x": shotXList, "y": shotYList})
figGoalMap, axGoalMap               = getGoalMap()

drawDividedPitch(axGoalMap, grids = True)

fillPitchDivisionGoalConceded(35, axGoalMap, dfGoalCoord, "#001A4D")

figGoalMap.set_size_inches(10, 10)
savePath = "./output/ChelseaGoalMap.png"
figGoalMap.savefig(savePath, dpi = 800, transparent=True)


# *************************************************************************** #
#                                                                             #
#                         ~~~ GET LIVERPOOL MAP ~~~                           #
#                                                                             #
# *************************************************************************** #


shotXList, shotYList, nConcededGoal = getConcededGoalCoordinate(matchIdListLiverpool, events, idLiverpool)
dfGoalCoord                         = pd.DataFrame({"x": shotXList, "y": shotYList})
figGoalMap, axGoalMap               = getGoalMap()

drawDividedPitch(axGoalMap, grids = True)

fillPitchDivisionGoalConceded(38, axGoalMap, dfGoalCoord, "#D00027")

figGoalMap.set_size_inches(10, 10)
savePath = "./output/LiverpoolGoalMap.png"
figGoalMap.savefig(savePath, dpi = 800, transparent=True)





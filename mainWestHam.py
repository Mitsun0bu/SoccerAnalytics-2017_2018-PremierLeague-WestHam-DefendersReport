import json

import pandas                                    as pd

from   getCompetitionId                          import getCompetitionId
from   getSeasonId                               import getSeasonId
from   getTeamId                                 import getTeamId

from   getSeasonMatches                          import getSeasonMatches

from   getLeagueTeamIdList                       import getLeagueTeamIdList
from   getMatchIdList                            import getMatchIdList

from   getLeaguePlayerIdList                     import getLeaguePlayerIdList
from   getLeagueDefenderIdList                   import getLeagueDefenderIdList
from   getTeamDefenderIdList                     import getTeamDefenderIdList

from   getPlayerNameListFromPlayerIdList         import getPlayerNameListFromPlayerIdList

from   getLeagueAirDuelSuccessRate               import getLeagueAirDuelSuccessRate
from   getPlayerAirDuelSuccessRate               import getPlayerAirDuelSuccessRate

from   getPlayerInterceptPerGame                 import getPlayerInterceptPerGame
from   getLeagueDefenderInterceptPerGame         import getLeagueDefenderInterceptPerGame

from   getNumberMatchPlayed                      import getNumberMatchPlayed

from   getLeagueDefenderSmartPassSuccessRate     import getLeagueDefenderSmartPassSuccessRate
from   getPlayerSmartPassSuccessRate             import getPlayerSmartPassSuccessRate


from   getPlayerRedCardsNumber                   import getPlayerRedCardsNumber
from   getLeagueRedCardsNumber                   import getLeagueRedCardsNumber

from   getLeagueDefenderDefendingDuelSuccessRate import getLeagueDefenderDefendingDuelSuccessRate
from   getPlayerDefendingDuelSuccessRate         import getPlayerDefendingDuelSuccessRate

from makeComparisonRadar                         import makeComparisonRadar

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


competitionName = "English first division"
seasonYear      = "2017"
teamName        = "West Ham United"

# Get ID of the Premier League
competitionId = getCompetitionId(competitions, competitionName)

# Get ID of the 2017-2018 Season
seasonId      = getSeasonId(matches, seasonYear)

# Get ID of the West Ham team
teamId        = getTeamId(teams, teamName)


# *************************************************************************** #
#                                                                             #
#                         ~~~ GET SEASON DATA ~~~                             #
#                                                                             #
# *************************************************************************** #


getSeasonMatches(matches, seasonId)


# *************************************************************************** #
#                                                                             #
#                         ~~~ GET PREMIER LEAGUE DEFENDERS DATA ~~~           #
#                                                                             #
# *************************************************************************** #


country                     = "England"
premierLeagueTeamIdList     = getLeagueTeamIdList(teams, country)
premierLeaguePlayerIdList   = getLeaguePlayerIdList(players, premierLeagueTeamIdList)
premierLeagueDefenderIdList = getLeagueDefenderIdList(players, premierLeagueTeamIdList)


# *************************************************************************** #
#                                                                             #
#                         ~~~ GET WEST HAM DEFENDERS DATA ~                   #
#                                                                             #
# *************************************************************************** #


westHamMatchIdList      = getMatchIdList(matches, teamId)
westHamDefenderIdList   = getTeamDefenderIdList(players, teamId)
westHamDefenderNameList = getPlayerNameListFromPlayerIdList(players, westHamDefenderIdList) 


# *************************************************************************** #
#                                                                             #
#                         ~~~ NUMBER OF MATCH PLAYED ~~~                      #
#                                                                             #
# *************************************************************************** #


westHamNumberMatchPlayed = []
for defenderId in westHamDefenderIdList:
    westHamNumberMatchPlayed.append(getNumberMatchPlayed(events, defenderId))
    

# *************************************************************************** #
#                                                                             #
#                         ~~~ DEFENDING DUEL DATA ~~~                         #
#                                                                             #
# *************************************************************************** #


# Comparison between defenders only

leagueDefendingDuelSuccessRate = getLeagueDefenderDefendingDuelSuccessRate(events, premierLeagueDefenderIdList)

westHamDefendingDuelSuccessRate = []
for defenderId in westHamDefenderIdList:
    westHamDefendingDuelSuccessRate.append(getPlayerDefendingDuelSuccessRate(events, defenderId)) 
    

# *************************************************************************** #
#                                                                             #
#                         ~~~ AIR DUEL DATA ~~~                               #
#                                                                             #
# *************************************************************************** #

# Comparison between all players

leagueAirDuelSuccessRate  = getLeagueAirDuelSuccessRate(events)

westHamAirDuelSuccessRate = []
for defenderId in westHamDefenderIdList:
    westHamAirDuelSuccessRate.append(getPlayerAirDuelSuccessRate(events, defenderId)) 


# *************************************************************************** #
#                                                                             #
#                         ~~~ INTERCEPTION DATA ~~~                           #
#                                                                             #
# *************************************************************************** #


# Comparison between defenders only

leagueInterceptPerGame = getLeagueDefenderInterceptPerGame(events, premierLeagueDefenderIdList)

westHamIntercept = []
for defenderId in westHamDefenderIdList:
    westHamIntercept.append(getPlayerInterceptPerGame(events, defenderId))
    

# *************************************************************************** #
#                                                                             #
#                         ~~~ SMART PASS DATA ~~~                             #
#                                                                             #
# *************************************************************************** #


# Comparison between defenders only

leagueSmartPassSuccessRate = getLeagueDefenderSmartPassSuccessRate(events, premierLeagueDefenderIdList)

westHamSmartPassSuccessRate = []
for defenderId in westHamDefenderIdList:
    westHamSmartPassSuccessRate.append(getPlayerSmartPassSuccessRate(events, defenderId))


# *************************************************************************** #
#                                                                             #
#                         ~~~ NUMBER OF RED CARDS ~~~                         #
#                                                                             #
# *************************************************************************** #


# Comparison between all players

leagueRedCardsNumber = getLeagueRedCardsNumber(events)

redCardPerGame       = round((leagueRedCardsNumber / len(matches)), 2) 

westHamRedCardsPerGame = []

for (defenderId, matchPlayed) in zip(westHamDefenderIdList, westHamNumberMatchPlayed):
    nRedCard = getPlayerRedCardsNumber(events, defenderId)
    westHamRedCardsPerGame.append(nRedCard / matchPlayed)


# *************************************************************************** #
#                                                                             #
#                         ~~~ FORMAT RADAR DATA ~~~                           #
#                                                                             #
# *************************************************************************** #


dataLeague    = [
                    leagueDefendingDuelSuccessRate,
                    leagueAirDuelSuccessRate,
                    leagueInterceptPerGame,
                    leagueSmartPassSuccessRate,
                    redCardPerGame
                ]

dataOgbonna   = [
                    westHamDefendingDuelSuccessRate[0],
                    westHamAirDuelSuccessRate[0],
                    westHamIntercept[0],
                    westHamSmartPassSuccessRate[0],
                    westHamRedCardsPerGame[0]
                ]

dataZabaleta  = [
                    westHamDefendingDuelSuccessRate[1],
                    westHamAirDuelSuccessRate[1],
                    westHamIntercept[1],
                    westHamSmartPassSuccessRate[1],
                    westHamRedCardsPerGame[1]
                ]

dataReid      = [
                    westHamDefendingDuelSuccessRate[2],
                    westHamAirDuelSuccessRate[2],
                    westHamIntercept[2],
                    westHamSmartPassSuccessRate[2],
                    westHamRedCardsPerGame[2]
                ]

dataCresswell = [
                    westHamDefendingDuelSuccessRate[3],
                    westHamAirDuelSuccessRate[3],
                    westHamIntercept[3],
                    westHamSmartPassSuccessRate[3],
                    westHamRedCardsPerGame[3]
                ]

dataMasuaku   = [
                    westHamDefendingDuelSuccessRate[4],
                    westHamAirDuelSuccessRate[4],
                    westHamIntercept[4],
                    westHamSmartPassSuccessRate[4],
                    westHamRedCardsPerGame[4]
                ]

dataRice      = [
                    westHamDefendingDuelSuccessRate[5],
                    westHamAirDuelSuccessRate[5],
                    westHamIntercept[5],
                    westHamSmartPassSuccessRate[5],
                    westHamRedCardsPerGame[5]
                ]


# *************************************************************************** #
#                                                                             #
#                         ~~~ GENERATE RADARS ~~~                             #
#                                                                             #
# *************************************************************************** #


clubColors = ["#7C2C3B", "#2DAFE5", "#FAD351"]
makeComparisonRadar(clubColors, "Ogbonna", dataOgbonna, dataLeague)
makeComparisonRadar(clubColors, "Zabaleta", dataZabaleta, dataLeague)
makeComparisonRadar(clubColors, "Reid", dataReid, dataLeague)
makeComparisonRadar(clubColors, "Cresswell", dataCresswell, dataLeague)
makeComparisonRadar(clubColors, "Masuaku", dataMasuaku, dataLeague)
makeComparisonRadar(clubColors, "Rice", dataRice, dataLeague)


# *************************************************************************** #
#                                                                             #
#                         ~~~ GET CONCEDED GOAL COORDINATE ~~~                #
#                                                                             #
# *************************************************************************** #


shotXList, shotYList, nConcededGoal = getConcededGoalCoordinate(westHamMatchIdList, events, teamId)

dfGoalCoord = pd.DataFrame({"x": shotXList, "y": shotYList})


# *************************************************************************** #
#                                                                             #
#                         ~~~ GENERATE DIVIDED PITCH ~~~                      #
#                                                                             #
# *************************************************************************** #


# Generate the figure

figGoalMap, axGoalMap = getGoalMap()

# Draw the actual pitch with divisons on the figure

drawDividedPitch(axGoalMap, grids = True)


# *************************************************************************** #
#                                                                             #
#                         ~~~ FILL PITCH DIVISONS ~~~                         #
#                                                                             #
# *************************************************************************** #

fillPitchDivisionGoalConceded(66, axGoalMap, dfGoalCoord, "#56061F")

# *************************************************************************** #
#                                                                             #
#                         ~~~ SAVE GOAL MAP FIGURE ~~~                        #
#                                                                             #
# *************************************************************************** #

figGoalMap.set_size_inches(10, 10)
savePath = "./output/WestHamGoalMap.png"
figGoalMap.savefig(savePath, dpi = 800, transparent=True)
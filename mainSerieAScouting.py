import json

from   getSeasonMatches                          import getSeasonMatches

from   getCompetitionId                          import getCompetitionId
from   getSeasonId                               import getSeasonId
from   getTeamId                                 import getTeamId
from   getPlayerNameListFromPlayerIdList         import getPlayerNameListFromPlayerIdList
from   getLeagueTeamIdList                       import getLeagueTeamIdList
from   getLeaguePlayerIdList                     import getLeaguePlayerIdList
from   getLeagueDefenderIdList                   import getLeagueDefenderIdList
from   getLeagueDefenderDefendingDuelSuccessRate import getLeagueDefenderDefendingDuelSuccessRate
from   getPlayerDefendingDuelSuccessRate         import getPlayerDefendingDuelSuccessRate
from   getNumberMatchPlayed                      import getNumberMatchPlayed
from   getLeagueAirDuelSuccessRate               import getLeagueAirDuelSuccessRate
from   getPlayerAirDuelSuccessRate               import getPlayerAirDuelSuccessRate
from   getPlayerInterceptPerGame                 import getPlayerInterceptPerGame
from   getLeagueDefenderInterceptPerGame         import getLeagueDefenderInterceptPerGame
from   getLeagueDefenderSmartPassSuccessRate     import getLeagueDefenderSmartPassSuccessRate
from   getPlayerSmartPassSuccessRate             import getPlayerSmartPassSuccessRate
from   getPlayerRedCardsNumber                   import getPlayerRedCardsNumber
from   getLeagueRedCardsNumber                   import getLeagueRedCardsNumber
from   makeComparisonRadar                       import makeComparisonRadar


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

with open(wyscoutFolderPath + "matches/matches_Italy.json") as matchesFile:
    matches = json.load(matchesFile)
    
with open(wyscoutFolderPath + "events/events_Italy.json") as eventsFile:
    events = json.load(eventsFile)
    

# *************************************************************************** #
#                                                                             #
#                         ~~~ GET IDs OF INTEREST ~~~                         #
#                                                                             #
# *************************************************************************** #


competitionName = "Italian first division"
seasonYear      = "2017"
teamName        = "Fiorentina"

# Get ID of the Serie A
competitionId = getCompetitionId(competitions, competitionName)

# Get ID of the 2017-2018 Season
seasonId      = getSeasonId(matches, seasonYear)

# Get ID of the Fiorentina team
teamId        = getTeamId(teams, teamName)


# *************************************************************************** #
#                                                                             #
#                         ~~~ GET SEASON DATA ~~~                             #
#                                                                             #
# *************************************************************************** #


getSeasonMatches(matches, seasonId)


# *************************************************************************** #
#                                                                             #
#                         ~~~ GET SERIE A DEFENDERS DATA ~~~                  #
#                                                                             #
# *************************************************************************** #


country              = "Italy"
serieATeamIdList     = getLeagueTeamIdList(teams, country)
serieAPlayerIdList   = getLeaguePlayerIdList(players, serieATeamIdList)
serieADefenderIdList = getLeagueDefenderIdList(players, serieATeamIdList)


# *************************************************************************** #
#                                                                             #
#                         ~~~ TOP 10 DEFENDING DUEL DATA ~~~                  #
#                                                                             #
# *************************************************************************** #


# Comparison between defenders only
 
leagueDefendingDuelSuccessRate = getLeagueDefenderDefendingDuelSuccessRate(events, serieADefenderIdList)

serieADefendingDuelSuccessRate  = []
top10IdDefendingDuelSuccessRate = []

for defenderId in serieADefenderIdList:
    newValue = getPlayerDefendingDuelSuccessRate(events, defenderId)
    if newValue == 0:
        continue
    if len(serieADefendingDuelSuccessRate) < 10:
        serieADefendingDuelSuccessRate.append(newValue)
        top10IdDefendingDuelSuccessRate.append(defenderId)
    else:
        minimum = min(serieADefendingDuelSuccessRate)
        if newValue > minimum:
            iMin = serieADefendingDuelSuccessRate.index(minimum)
            serieADefendingDuelSuccessRate[iMin]  = newValue
            top10IdDefendingDuelSuccessRate[iMin] = defenderId

namesTop10 = getPlayerNameListFromPlayerIdList(players,  top10IdDefendingDuelSuccessRate)


# *************************************************************************** #
#                                                                             #
#                         ~~~ NUMBER OF MATCH PLAYED ~~~                      #
#                                                                             #
# *************************************************************************** #


top10NumberMatchPlayed = []
for defenderId in top10IdDefendingDuelSuccessRate:
    top10NumberMatchPlayed.append(getNumberMatchPlayed(events, defenderId))


# *************************************************************************** #
#                                                                             #
#                         ~~~ DEFENDING DUEL DATA ~~~                         #
#                                                                             #
# *************************************************************************** #


# Comparison between defenders only

leagueDefendingDuelSuccessRate = getLeagueDefenderDefendingDuelSuccessRate(events, serieADefenderIdList)

top10DefendingDuelSuccessRate = []
for defenderId in top10IdDefendingDuelSuccessRate:
    top10DefendingDuelSuccessRate.append(getPlayerDefendingDuelSuccessRate(events, defenderId)) 
    

# *************************************************************************** #
#                                                                             #
#                         ~~~ AIR DUEL DATA ~~~                               #
#                                                                             #
# *************************************************************************** #

# Comparison between all players

leagueAirDuelSuccessRate  = getLeagueAirDuelSuccessRate(events)

top10AirDuelSuccessRate = []
for defenderId in top10IdDefendingDuelSuccessRate:
    top10AirDuelSuccessRate.append(getPlayerAirDuelSuccessRate(events, defenderId))


# *************************************************************************** #
#                                                                             #
#                         ~~~ INTERCEPTION DATA ~~~                           #
#                                                                             #
# *************************************************************************** #


# Comparison between defenders only

leagueInterceptPerGame = getLeagueDefenderInterceptPerGame(events, serieADefenderIdList)

top10Intercept = []
for defenderId in top10IdDefendingDuelSuccessRate:
    top10Intercept.append(getPlayerInterceptPerGame(events, defenderId))

    
# *************************************************************************** #
#                                                                             #
#                         ~~~ SMART PASS DATA ~~~                             #
#                                                                             #
# *************************************************************************** #


# Comparison between defenders only

leagueSmartPassSuccessRate = getLeagueDefenderSmartPassSuccessRate(events, serieADefenderIdList)

top10SmartPassSuccessRate = []
for defenderId in top10IdDefendingDuelSuccessRate:
    top10SmartPassSuccessRate.append(getPlayerSmartPassSuccessRate(events, defenderId))


# *************************************************************************** #
#                                                                             #
#                         ~~~ NUMBER OF RED CARDS ~~~                         #
#                                                                             #
# *************************************************************************** #


# Comparison between all players

leagueRedCardsNumber = getLeagueRedCardsNumber(events)

redCardPerGame       = round((leagueRedCardsNumber / len(matches)), 2) 

top10RedCardsPerGame = []

for (defenderId, matchPlayed) in zip(top10IdDefendingDuelSuccessRate, top10NumberMatchPlayed):
    nRedCard = getPlayerRedCardsNumber(events, defenderId)
    top10RedCardsPerGame.append(nRedCard / matchPlayed)


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

dataDeSciglio = [
                    top10DefendingDuelSuccessRate[5],
                    top10AirDuelSuccessRate[5],
                    top10Intercept[5],
                    top10SmartPassSuccessRate[5],
                    top10RedCardsPerGame[5]
                ]

dataVitorHugo = [
                    top10DefendingDuelSuccessRate[6],
                    top10AirDuelSuccessRate[6],
                    top10Intercept[6],
                    top10SmartPassSuccessRate[6],
                    top10RedCardsPerGame[6]
                ]


# *************************************************************************** #
#                                                                             #
#                         ~~~ GENERATE RADARS ~~~                             #
#                                                                             #
# *************************************************************************** #


clubColors = ["black", "white", "white"]
makeComparisonRadar(clubColors, "De Sciglio", dataDeSciglio, dataLeague)

clubColors = ["#5A2E8B", "#E12114", "white"]
makeComparisonRadar(clubColors, "Vitor Hugo", dataVitorHugo, dataLeague)


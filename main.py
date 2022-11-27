from functions import getTeamInfo,convertWebpageToSoup,getAllPlayersBoxScore,createExcel
from datetime import datetime 

start_time = datetime.now() 

gameId = 2110419
competitionId = 34106
#user = 597    osäker på om den behövs


summary = f"https://hosted.dcd.shared.geniussports.com/SBF/en/competition/{competitionId}/match/{gameId}/summary"
#playByPlay = f"https://hosted.dcd.shared.geniussports.com/SBF/en/competition/{competitionId}/match/{gameId}/playbyplay"
boxScore = f"https://hosted.dcd.shared.geniussports.com/SBF/en/competition/{competitionId}/match/{gameId}/boxscore"

summarySoup = convertWebpageToSoup(summary)
homeTeamName,homeTeamScore,awayTeamName,awayTeamScore  = getTeamInfo(summarySoup)
#playByPlaySoup = convertWebpageToSoup(playByPlay)

boxScoreSoup = convertWebpageToSoup(boxScore)

homeTeamPlayerList, awayTeamPlayerList = getAllPlayersBoxScore(boxScoreSoup)
print(f"{homeTeamName}: {homeTeamScore} - {awayTeamName}: {awayTeamScore} ")
print(f"Spelare nummer:{homeTeamPlayerList[4].number}, {homeTeamPlayerList[4].name}, har just nu {homeTeamPlayerList[4].assists}st assists och har spelat {homeTeamPlayerList[0].minutes} minuter. ")

time_elapsed = datetime.now() - start_time 
print(f"Programmets körtid: {time_elapsed}")

createExcel(homeTeamName,homeTeamScore,awayTeamName,awayTeamScore,homeTeamPlayerList, awayTeamPlayerList, gameId, competitionId)

from functions import getHomeTeamInfo, getAwayTeamInfo, convertWebpageToSoup

gameId = 2110419
otherId = 34106
#user = 597    osäker på om den behövs


website = f"https://hosted.dcd.shared.geniussports.com/SBF/en/competition/{otherId}/match/{gameId}/summary"

soup = convertWebpageToSoup(website)
homeTeamName,homeTeamScore = getHomeTeamInfo(soup)
awayTeamName,awayTeamScore = getAwayTeamInfo(soup)

print(f"{homeTeamName}: {homeTeamScore} - {awayTeamName}: {awayTeamScore} ")

import requests
from bs4 import BeautifulSoup
import xlsxwriter

def convertWebpageToSoup(website):
    result = requests.get(website)
    content = result.text
    soup = BeautifulSoup(content, "lxml")
    return soup

def getTeamInfo(soup):
    tag = soup.body
    homeTeamInfo = tag.find(class_="home-wrapper team-box")
    homeTeamName = homeTeamInfo.find(class_="name")
    homeTeamName = homeTeamName.text
    homeTeamName = homeTeamName.strip()
    homeTeamScore = homeTeamInfo.find(class_="score")
    homeTeamScore = homeTeamScore.text
    homeTeamScore = homeTeamScore.strip()
    awayTeamInfo = tag.find(class_="away-wrapper team-box")
    awayTeamName = awayTeamInfo.find(class_="name")
    awayTeamName = awayTeamName.text
    awayTeamName = awayTeamName.strip()
    awayTeamScore = awayTeamInfo.find(class_="score")
    awayTeamScore = awayTeamScore.text
    awayTeamScore = awayTeamScore.strip()
    return homeTeamName, homeTeamScore, awayTeamName, awayTeamScore

def getAllPlayersBoxScore(soup):
    homePlayerStats = []
    awayPlayerStats = []
    class Player:
        def __init__(self, position, number, name, minutes, points, twoPointsMade,twoPointsAttempted,
        twoPointsPercentage,threePointsMade,threePointsAttempted, threePointsPercentage,freeThrowsMade,
        freeThrowsAttempted,freeThrowsPercentage,offensiveRebounds,devensiveRebounds,totalRebounds,
        assists,turnovers,steals,blocks,blocksReceived,personalFouls,foulsOn,plusMinus):
            self.position = position
            self.number = number
            self.name = name
            self.minutes = minutes
            self.points = points
            self.twoPointsMade = twoPointsMade
            self.twoPointsAttempted = twoPointsAttempted
            self.twoPointsPercentage = twoPointsPercentage
            self.threePointsMade = threePointsMade
            self.threePointsAttempted = threePointsAttempted
            self.threePointsPercentage = threePointsPercentage
            self.freeThrowsMade = freeThrowsMade
            self.freeThrowsAttempted = freeThrowsAttempted
            self.freeThrowsPercentage = freeThrowsPercentage
            self.offensiveRebounds = offensiveRebounds
            self.devensiveRebounds = devensiveRebounds
            self.totalRebounds = totalRebounds
            self.assists = assists
            self.turnovers = turnovers
            self.steals = steals
            self.blocks = blocks
            self.blocksReceived = blocksReceived
            self.personalFouls = personalFouls
            self.foulsOn = foulsOn
            self.plusMinus = plusMinus

    boxInfo = soup.find(class_="boxscore smallstats")
    boxInfo = boxInfo.find_all(class_="table-wrap")
    
    boxInfoHome = boxInfo[0]
    boxInfoHome = boxInfoHome.find_all("tr")
    boxInfoHome = boxInfoHome[1:-1]
    for hPlayer in boxInfoHome:
        hplayerStats = hPlayer.text
        hplayerStats = hplayerStats.replace(" ","")
        hplayerStats = hplayerStats.replace("\n\n\n","\n")
        hplayerStats = hplayerStats.replace("\n",";")
        hplayerStats = hplayerStats[:-1]
        hstatsList = list(hplayerStats.split(";"))
        homePlayer = Player("Player",hstatsList[1],hstatsList[2],hstatsList[3],hstatsList[4],hstatsList[5],hstatsList[6],hstatsList[7],hstatsList[8],hstatsList[9],hstatsList[10],hstatsList[11],hstatsList[12],hstatsList[13],hstatsList[14],hstatsList[15],hstatsList[16],hstatsList[17],hstatsList[18],hstatsList[19],hstatsList[20],hstatsList[21],hstatsList[22],hstatsList[23],hstatsList[24])
        homePlayerStats.append(homePlayer)

    boxInfoAway = boxInfo[1]
    boxInfoAway = boxInfoAway.find_all("tr")
    boxInfoAway = boxInfoAway[1:-1]
    for aPlayer in boxInfoAway:
        playerStats = aPlayer.text
        playerStats = playerStats.replace(" ","")
        playerStats = playerStats.replace("\n\n\n","\n")
        playerStats = playerStats.replace("\n",";")
        playerStats = playerStats[:-1]
        statsList = list(playerStats.split(";"))
        awayPlayer = Player("Player",statsList[1],statsList[2],statsList[3],statsList[4],statsList[5],statsList[6],statsList[7],statsList[8],statsList[9],statsList[10],statsList[11],statsList[12],statsList[13],statsList[14],statsList[15],statsList[16],statsList[17],statsList[18],statsList[19],statsList[20],statsList[21],statsList[22],statsList[23],statsList[24])
        awayPlayerStats.append(awayPlayer)



    return homePlayerStats, awayPlayerStats

def createExcel(homeTeamName,homeTeamScore,awayTeamName,awayTeamScore,homeTeamPlayerList, awayTeamPlayerList, gameId, competitionId):
    homePlayersStats =[]
    awayPlayersStats =[]

    for player in homeTeamPlayerList:
        homePlayersStats.append([player.position,player.number,player.name,player.minutes,player.points,player.twoPointsMade,player.twoPointsAttempted,player.twoPointsPercentage,player.threePointsMade,player.threePointsAttempted,
        player.threePointsPercentage,player.freeThrowsMade,player.freeThrowsAttempted,player.freeThrowsPercentage,player.offensiveRebounds,player.devensiveRebounds,player.totalRebounds,player.assists,player.turnovers,
        player.steals,player.blocks,player.blocksReceived,player.personalFouls,player.foulsOn,player.plusMinus])

    for player in awayTeamPlayerList:
        awayPlayersStats.append([player.position,player.number,player.name,player.minutes,player.points,player.twoPointsMade,player.twoPointsAttempted,player.twoPointsPercentage,player.threePointsMade,player.threePointsAttempted,
        player.threePointsPercentage,player.freeThrowsMade,player.freeThrowsAttempted,player.freeThrowsPercentage,player.offensiveRebounds,player.devensiveRebounds,player.totalRebounds,player.assists,player.turnovers,
        player.steals,player.blocks,player.blocksReceived,player.personalFouls,player.foulsOn,player.plusMinus])

    listToExcel = []
    first = [f"Game ID:",f"{gameId}","Competition ID:", f"{competitionId}"],[f"Home Team:",f"{homeTeamName}",f"Away Team:",f"{awayTeamName}"],["Home Team Score",f"{homeTeamScore}","Away Team Score",f"{awayTeamScore}"],
    ["Home Team Player Stats"],["Position","Jersey#","Name","Minutes","Points", "2p made","2p attempted","2p %","3p made","3p attempted","3p %","Freetrows Made",
    "Freethrows attempted","Freethrows %","Offensive Rebounds","Defensive Rebounds","Total Rebounds","Assists","Turnovers","Steals","Blocks",
    "Blocks Received","Personal Fouls","Fouls on","+/-"]
    for item in first:
        listToExcel.append(item)
    for pL in homePlayersStats:
        listToExcel.append(pL)
    second = ["Away Team Player Stats"],["Position","Jersey#","Name","Minutes","Points", "2p made","2p attempted","2p %","3p made","3p attempted","3p %","Freetrows Made","Freethrows attempted","Freethrows %","Offensive Rebounds","Defensive Rebounds","Total Rebounds","Assists","Turnovers","Steals","Blocks","Blocks Received","Personal Fouls","Fouls on","+/-"]
    for items in second:
        listToExcel.append(items)
    for pLa in awayPlayersStats:
        listToExcel.append(pLa)

    with xlsxwriter.Workbook('Stats.xlsx') as workbook:
        worksheet = workbook.add_worksheet()

        for row_num, data in enumerate(listToExcel):
            worksheet.write_row(row_num, 0, data)

def readTextfileWithGameInfo(fileToRead):
    with open(fileToRead) as f:
        lines = f.readlines()
    return lines

gameinfo = readTextfileWithGameInfo('gameinfo.txt')
gameId = int(gameinfo[0])
competitionId = int(gameinfo[1])
summary = f"https://hosted.dcd.shared.geniussports.com/SBF/en/competition/{competitionId}/match/{gameId}/summary"
boxScore = f"https://hosted.dcd.shared.geniussports.com/SBF/en/competition/{competitionId}/match/{gameId}/boxscore"

summarySoup = convertWebpageToSoup(summary)
homeTeamName,homeTeamScore,awayTeamName,awayTeamScore  = getTeamInfo(summarySoup)

boxScoreSoup = convertWebpageToSoup(boxScore)

homeTeamPlayerList, awayTeamPlayerList = getAllPlayersBoxScore(boxScoreSoup)

createExcel(homeTeamName,homeTeamScore,awayTeamName,awayTeamScore,homeTeamPlayerList, awayTeamPlayerList, gameId, competitionId)

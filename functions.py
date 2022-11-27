import requests
from bs4 import BeautifulSoup

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
    boxInfoHome, boxInfoAway = boxInfo.find_all(class_="table-wrap")

    boxInfoHome = boxInfoHome.find("tbody")
    boxInfoHome = boxInfoHome.find_all("tr")
    for player in boxInfoHome:
        playerStats = player.text
        playerStats = playerStats.replace(" ","")
        playerStats = playerStats.replace("\n\n\n","\n")
        playerStats = playerStats.replace("\n",";")
        playerStats = playerStats[:-1]
        statsList = list(playerStats.split(";"))
        homePlayer = Player
        homePlayer.position = "C"
        homePlayer.number = statsList[1]
        homePlayer.name = statsList[2]
        homePlayer.minutes = statsList[3]
        homePlayer.points = statsList[4]
        homePlayer.twoPointsMade = statsList[5]
        homePlayer.twoPointsAttempted = statsList[6]
        homePlayer.twoPointsPercentage = statsList[7]
        homePlayer.threePointsMade = statsList[8]
        homePlayer.threePointsAttempted = statsList[9]
        homePlayer.threePointsPercentage = statsList[10]
        homePlayer.freeThrowsMade = statsList[11]
        homePlayer.freeThrowsAttempted = statsList[12]
        homePlayer.freeThrowsPercentage = statsList[13]
        homePlayer.offensiveRebounds = statsList[14]
        homePlayer.devensiveRebounds = statsList[15]
        homePlayer.totalRebounds = statsList[16]
        homePlayer.assists = statsList[17]
        homePlayer.turnovers = statsList[18]
        homePlayer.steals = statsList[19]
        homePlayer.blocks = statsList[20]
        homePlayer.blocksReceived = statsList[21]
        homePlayer.personalFouls = statsList[22]
        homePlayer.foulsOn = statsList[23]
        homePlayer.plusMinus = statsList[24]
        homePlayerStats.append(homePlayer)

    boxInfoAway = boxInfoAway.find("tbody")
    boxInfoAway = boxInfoAway.find_all("tr")
    for player in boxInfoAway:
        playerStats = player.text
        playerStats = playerStats.replace(" ","")
        playerStats = playerStats.replace("\n\n\n","\n")
        playerStats = playerStats.replace("\n",";")
        playerStats = playerStats[:-1]
        statsList = list(playerStats.split(";"))
        awayPlayer = Player
        awayPlayer.position = "C"
        awayPlayer.number = statsList[1]
        awayPlayer.name = statsList[2]
        awayPlayer.minutes = statsList[3]
        awayPlayer.points = statsList[4]
        awayPlayer.twoPointsMade = statsList[5]
        awayPlayer.twoPointsAttempted = statsList[6]
        awayPlayer.twoPointsPercentage = statsList[7]
        awayPlayer.threePointsMade = statsList[8]
        awayPlayer.threePointsAttempted = statsList[9]
        awayPlayer.threePointsPercentage = statsList[10]
        awayPlayer.freeThrowsMade = statsList[11]
        awayPlayer.freeThrowsAttempted = statsList[12]
        awayPlayer.freeThrowsPercentage = statsList[13]
        awayPlayer.offensiveRebounds = statsList[14]
        awayPlayer.devensiveRebounds = statsList[15]
        awayPlayer.totalRebounds = statsList[16]
        awayPlayer.assists = statsList[17]
        awayPlayer.turnovers = statsList[18]
        awayPlayer.steals = statsList[19]
        awayPlayer.blocks = statsList[20]
        awayPlayer.blocksReceived = statsList[21]
        awayPlayer.personalFouls = statsList[22]
        awayPlayer.foulsOn = statsList[23]
        awayPlayer.plusMinus = statsList[24]
        awayPlayerStats.append(awayPlayer)



    return homePlayerStats, awayPlayerStats










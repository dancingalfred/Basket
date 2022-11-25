import requests
from bs4 import BeautifulSoup

def convertWebpageToSoup(website):
    result = requests.get(website)
    content = result.text
    soup = BeautifulSoup(content, "lxml")
    return soup

def getHomeTeamInfo(soup):
    tag = soup.body
    homeTeamInfo = tag.find(class_="home-wrapper team-box")
    homeTeamName = homeTeamInfo.find(class_="name")
    homeTeamName = homeTeamName.text
    homeTeamName = homeTeamName.strip()
    homeTeamScore = homeTeamInfo.find(class_="score")
    homeTeamScore = homeTeamScore.text
    homeTeamScore = homeTeamScore.strip()
    return homeTeamName, homeTeamScore

def getAwayTeamInfo(soup):
    tag = soup.body
    awayTeamInfo = tag.find(class_="away-wrapper team-box")
    awayTeamName = awayTeamInfo.find(class_="name")
    awayTeamName = awayTeamName.text
    awayTeamName = awayTeamName.strip()
    awayTeamScore = awayTeamInfo.find(class_="score")
    awayTeamScore = awayTeamScore.text
    awayTeamScore = awayTeamScore.strip()
    return awayTeamName, awayTeamScore









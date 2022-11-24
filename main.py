import requests
from bs4 import BeautifulSoup

gameId = 2110419
otherId = 34106
user = 597


website = f"https://hosted.dcd.shared.geniussports.com/SBF/en/competition/{otherId}/match/{gameId}/summary"

result = requests.get(website)

content = result.text

soup = BeautifulSoup(content, "lxml")
print(soup.prettify())

body = soup.find("body", dir="ltr", class_=f"_user_{user} _comp_{otherId} ltr  summary")
body = body.find("div", class_="hs-page hs-container xs-hs-container")
body = body.find("div", class_="hs-container noresize main-container")
body = body.find("div", class_="hs-page hs-container xs-hs-container")
body = body.find("div", class_="hs-row")
body = body.find("div", class_="hs-col-full")
body = body.find("div", class_=f"extfix_{gameId}")
body = body.find("div", class_="match-page page")





matchDetails = body.find("div", class_="BLOCK_MATCH_HEADER")

homeInfo = matchDetails.find("div", class_="home-wrapper team-box")
homeTeamScore = homeInfo.find("div", class_="score").get_text()

awayInfo = matchDetails.find("div", class_="home-wrapper team-box")
awayTeamScore = awayInfo.find("div", class_="score").get_text()

print(f"Hemmalag: {homeTeamScore} - Bortalag: {awayTeamScore} ")

from bs4 import BeautifulSoup
import urllib
import requests
import re

def scrape(site): # basic scrape, takes URL as an argument
    if site[0:4] == 'http':
        r = requests.get(site).text
    else:
        r = urllib.urlopen(site).read()
    return BeautifulSoup(r, "html.parser")

def get_raw_data(): # get raw player data to parse for player_id's
    raw_data = scrape('http://www.golfstrat.com').find_all('option')
    raw_data = raw_data[1:(len(raw_data)/2)]
    return raw_data

def get_names_and_power_ranking(raw_data): # use raw player data to put player_id's in an array
    players = []

    for datum in raw_data:
        player = {}
        power_ranking_raw = str(datum).strip().split('"')
        power_ranking = power_ranking_raw[1]
        full_name = datum.get_text().encode('UTF8')
        first_name = str(full_name).strip().split(',')[1]
        last_name = str(full_name).strip().split(',')[0]
        player["First Name"] = first_name.strip()
        player["Last Name"] = last_name.strip()
        player["Power Ranking"] = power_ranking.strip()
        players.append(player)

    return players

def write_to_file(players):
    root = 'http://www.golfstrat.com/golfstrat-fantasy-edge-player-comparison/'
    for player in players:
        print("Downloading information for %s %s" % (player["First Name"], player["Last Name"]))
        ranking = player["Power Ranking"]
        print(ranking)
        ranking_low = len(players)
        file = open(player["Power Ranking"] + player["First Name"] + player["Last Name"] + ".txt", "w")
        if int(ranking) < ranking_low:
            x = str(scrape(root + '?compare=%s,%d' % (ranking, ranking_low)))
        else:
            print("Ranking == ranking_low" + ranking + " " + str(ranking_low))
            x = str(scrape(root + '?compare=%s,%d' % (ranking_low, 1)))
        file.write(x)
        file.close()
        print("Done!\n")

def get_stat(players):
    numbers = re.compile('\d+(?:\.\d+)?')
    for player in players:
        x = scrape(player["Power Ranking"] + player["First Name"] + player["Last Name"] + ".txt").findAll('tbody')
        x = x[4].find_all('center')
        holding = []
        for i in x:
            i = numbers.findall(str(i))
            holding.append(i)
        try:
            player["Recent Performance"] = holding[0][0]
        except:
            player["Recent Performance"] = "NR"
        try:
            player["Course History"] = holding[2][0]
        except:
            player["Course History"] = "NR"
        try:
            player["Course Fit"] = holding[4][0]
        except:
            player["Course Fit"] = "NR"
        try:
            player["Similar Course"] = holding[6][0]
        except:
            player["Similar Course"] = "NR"

    return players[0:len(players)]

players = get_names_and_power_ranking(get_raw_data())

# write_to_file(players)

print(get_stat(players))
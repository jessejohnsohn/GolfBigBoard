from bs4 import BeautifulSoup
import requests

def scrape(site): # basic scrape, takes URL as an argument
    r = requests.get(site).text
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
        player["First Name"] = first_name
        player["Last Name"] = last_name
        player["Power Ranking"] = power_ranking
        players.append(player)

    return players

def write_to_file(players):
    root = 'http://www.golfstrat.com/golfstrat-fantasy-edge-player-comparison/'
    for player in players:
        print("Downloading information for %s %s" % (player["First Name"], player["Last Name"]))
        ranking = player["Power Ranking"]
        ranking_low = len(players)
        file = open("scrapedata%s.txt" % ranking, "w")
        if ranking < ranking_low:
            x = str(scrape(root + '?compare=%s,%d' % (ranking, ranking_low)))
        else:
            x = str(scrape(root + '?compare=%s,%d' % (ranking_low, 1)))
        file.write(x)
        file.close()
        print("Done!\n")

players = get_names_and_power_ranking(get_raw_data())

write_to_file(players)
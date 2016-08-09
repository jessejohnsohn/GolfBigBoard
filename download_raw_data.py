from bs4 import BeautifulSoup
import urllib

def split_and_strip(code,point):
    code1 = []
    for word in code:
        code1.append(word.strip().split(point))
    return code1

def get_player_data(): # get raw player data to parse for player_id's
    r = urllib.urlopen('http://www.golfstrat.com').read()
    raw_data = BeautifulSoup(r, "html.parser").find_all('option')
    raw_data = raw_data[1:(len(raw_data)/2)]
    return raw_data

def get_golfstrat_id(data): # use raw player data to put player_id's in an array
    for i in range(0,len(data)):
        data[i] = str(data[i]).strip().split('"')
    id_data = []
    for i in range(0,len(data)):
        id_data.append(data[i][1])
    return id_data

def scrape(site): # basic scrape, takes URL as an argument
    r = urllib.urlopen(site).read()
    return BeautifulSoup(r, "html.parser")

def write_to_file(): # takes raw data from get_course_fit_info() and spitsout an array of course_fits
    for i in golfstrat_id:  # scrapes all player data from GolfStrat.com
        file = open("scrapedata%s.txt" % i, "w")
        x = str(scrape('http://www.golfstrat.com/golfstrat-fantasy-edge-player-comparison/?compare=%s,161' % i))
        file.write(x)
        file.close()

player_data = get_player_data() # gets raw data for use in parsing for player_id's
golfstrat_id = get_golfstrat_id(player_data) #gets player_id's -- important for iterating URL

write_to_file()
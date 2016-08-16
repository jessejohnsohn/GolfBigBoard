from bs4 import BeautifulSoup
import urllib
import sqlite3

conn = sqlite3.connect('golfbigboardTEST.db')
conn.text_factory = str
c = conn.cursor()

def get_first_names(full_names):  # Gives first names its own array
    holding_array = []
    for i in range(0, len(full_names)):
        holding_array.append(str(full_names[i][1]).strip())
    return holding_array


def get_last_names(full_names):  # Gives last names its own array
    holding_array = []
    for i in range(0, len(full_names)):
        holding_array.append(full_names[i][0])
    return holding_array


def get_full_names(data):  # Takes the text of the raw data and creates an array of arrays with first and last names
    golfer_name = []
    for datum in data:
        x = datum.get_text()
        golfer_name.append(x.encode('UTF8'))
    golfer_name = split_and_strip(golfer_name, ',')
    return golfer_name


def split_and_strip(code, point):  # takes strings and splits and strips it at a point
    code1 = []
    for word in code:
        code1.append(word.strip().split(point))
    return code1


def get_player_data():  # get raw player data to parse for player_id's
    r = urllib.urlopen('http://www.golfstrat.com').read()
    raw_data = BeautifulSoup(r, "html.parser").find_all('option')
    raw_data = raw_data[1:(len(raw_data) / 2)]
    return raw_data


def get_golfstrat_id(data):  # use raw player data to put player_id's into an array
    for i in range(0, len(data)):
        data[i] = str(data[i]).strip().split('"')  # not sure why split_and_strip() doesn't work on this
    id_data = []
    for i in range(0, len(data)):
        id_data.append(int(data[i][1]))
    return id_data


def scrape(site):  # basic scrape, takes URL as an argument, returns code
    r = urllib.urlopen(site).read()
    return BeautifulSoup(r, "html.parser")


def get_stat(indice):
    holding3 = []
    if indice == 0:
        print 'Getting Recent Performance...'
    elif indice == 2:
        print 'Getting Course History...'
    elif indice == 4:
        print 'Getting Course Fit...'
    elif indice == 6:
        print 'Getting Similar Course...'

    for k in golfstrat_id:
       try:
            holding1 = []
            holding2 = []
            x = scrape('scrapedata%s.txt' % k).findAll('tbody')
            x = x[4].find_all('center')
            for i in x:
                holding1.append(str(i).strip('<center> '))
            for j in holding1:
                z = str(j).strip(' </')
                if z == '':
                    z = 150
                holding2.append(z)
            #print holding2
            holding3.append(int(holding2[indice]))
       except IndexError:
           del k

    return holding3

player_data = get_player_data()  # gets raw data for use in parsing for player_id's
for i in player_data:
    print i

complete_names = get_full_names(player_data)

golfstrat_id = get_golfstrat_id(player_data)  # gets player_id's -- important for iterating URL

first_names = get_first_names(complete_names)
last_names = get_last_names(complete_names)

recent_performance = get_stat(0)
tournament_history = get_stat(2)
course_fit = get_stat(4)
similar_course = get_stat(6)

print first_names
print last_names
print recent_performance
print tournament_history
print course_fit
print similar_course
print golfstrat_id

def createGolferTable():
   c.execute('DROP TABLE IF EXISTS golfstratgolfer')
   c.execute('CREATE TABLE IF NOT EXISTS golfstratgolfer (full_name TEXT, first_name TEXT, last_name TEXT, golfstrat_id INTEGER, course_fit INTEGER, similar_course INTEGER, tournament_history INTEGER, recent_performance INTEGER, total INTEGER)')

def addGolfer(full_name,first_name,last_name,golfstrat_id,course_fit,similar_course,tournament_history,recent_performance,total):
   c.execute('INSERT INTO golfstratgolfer (full_name,first_name,last_name,golfstrat_id,course_fit,similar_course,tournament_history,recent_performance,total) VALUES (?,?,?,?,?,?,?,?,?)',
             (full_name,first_name,last_name,golfstrat_id,course_fit,similar_course,tournament_history,recent_performance,total))

createGolferTable()

z = len(golfstrat_id)

for i in range(0,z):
    try:
        addGolfer((first_names[i]+' '+last_names[i]),first_names[i],last_names[i],golfstrat_id[i],course_fit[i],similar_course[i],tournament_history[i],recent_performance[i],(golfstrat_id[i]+course_fit[i]+similar_course[i]+tournament_history[i]+recent_performance[i]))
    except IndexError:
        print i
        del i
conn.commit()

# saved formula for getting totals array
# for i in range(0,len(golfstrat_id)):
#     totals.append(recent_performance[i]+tournament_history[i]+course_fit[i]+similar_course[i]+golfstrat_id[i])

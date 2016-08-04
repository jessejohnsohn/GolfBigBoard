import sqlite3


conn = sqlite3.connect('golfbigboardTEST.db')
conn.text_factory = str
c = conn.cursor()

first_names = ['Thomas', 'Tyler', 'Robert', 'Abraham', 'Miguel', 'Aaron', 'Blayne', 'Ricky', 'Daniel', 'Zac', 'Jonas', 'Steven', 'Keegan', 'Scott', 'Bronson', 'Angel', 'Chad', 'Paul', 'Bud', 'Alex', 'Greg', 'Kevin', 'Chad', 'Erik', 'Ben', 'Jon', 'Brendon', 'Bryson', 'Luke', 'Jamie', 'Ken', 'Ernie', 'Derek', 'Derek', 'Tony', 'Jim', 'Robert', 'Brian', 'Lucas', 'Andres', 'Retief', 'Jason', 'Branden', 'Chesson', 'Adam', 'James', 'Brian', 'Padraig', 'Russell', 'J.J.', 'Charley', 'Morgan', 'Tom', 'J.B.', 'John', 'Billy', 'Hiroshi', 'Freddie', 'Zach', 'Matt', 'Sung', 'Smylie', 'Jerry', 'Michael', 'Patton', 'Soren', 'Colt', 'Russell', 'Brooks', 'Jason', 'Kelly', 'Matt', 'Martin', 'Andrew', 'D.H.', 'Marc', 'Justin', 'Spencer', 'Luke', 'Andrew', 'Jamie', 'Shane', 'Will', 'Hunter', 'Peter', 'Steve', 'Ben', 'Lee', 'George', 'Troy', 'Bryce', 'Francesco', 'Ryan', 'Jordan', 'Seung-Yul', 'Henrik', 'Sean', 'Geoff', 'Louis', 'Rob', 'Carlos', 'Greg', 'Rod', 'Tim', 'Martin', 'Scott', 'Jr.', 'Dicky', 'Jon', 'Adam', 'Chez', 'Patrick', 'Kyle', 'Wes', 'Patrick', 'Rory', 'Sam', 'John', 'Robby', 'Webb', 'Vijay', 'Heath', 'Cameron', 'Scott', 'Kyle', 'Brendan', 'Shawn', 'Darron', 'Kevin', 'Chris', 'Brian', 'Daniel', 'Hudson', 'Nick', 'Vaughn', 'Justin', 'Michael', 'Brendon', 'David', 'Tyrone', 'Dawie', 'Camilo', 'Johnson', 'Bubba', 'Boo', 'Steve', 'Meen', 'Tim', 'Mark', 'Si', 'Gary']
last_names = ['Aiken', 'Aldridge', 'Allenby', 'Ancer', 'Angel Carballo', 'Baddeley', 'Barber', 'Barnes', 'Berger', 'Blair', 'Blixt', 'Bowditch', 'Bradley', 'Brown', 'Burgoon', 'Cabrera', 'Campbell', 'Casey', 'Cauley', 'Cejka', 'Chalmers', 'Chappell', 'Collins', 'Compton', 'Crane', 'Curran', 'de Jonge', 'Dechambeau', 'Donald', 'Donaldson', 'Duke', 'Els', 'Ernst', 'Fathauer', 'Finau', 'Furyk', 'Garrigus', 'Gay', 'Glover', 'Gonzales', 'Goosen', 'Gore', 'Grace', 'Hadley', 'Hadwin', 'Hahn', 'Harman', 'Harrington', 'Henley', 'Henry', 'Hoffman', 'Hoffmann', 'Hoge', 'Holmes', 'Huh', 'Hurley III', 'Iwata', 'Jacobson', 'Johnson', 'Jones', 'Kang', 'Kaufman', 'Kelly', 'Kim', 'Kizzire', 'Kjeldsen', 'Knost', 'Knox', 'Koepka', 'Kokrak', 'Kraft', 'Kuchar', 'Laird', 'Landry', 'Lee', 'Leishman', 'Leonard', 'Levin', 'List', 'Loupe', 'Lovemark', 'Lowry', 'MacKenzie', 'Mahan', 'Malnati', 'Marino', 'Martin', 'Mccoy', 'McNeill', 'Merritt', 'Molder', 'Molinari', 'Moore', 'Niebrugge', 'Noh', 'Norlander', 'O\xe2\x80\x99Hair', 'Ogilvy', 'Oosthuizen', 'Oppenheim', 'Ortiz', 'Owen', 'Pampling', 'Petrovic', 'Piller', 'Pinckney', 'Potter', 'Pride', 'Rahm', 'Rainaud', 'Reavie', 'Reed', 'Reifers', 'Roach', 'Rodgers', 'Sabbatini', 'Saunders', 'Senden', 'Shelton', 'Simpson', 'Singh', 'Slocum', 'Smith', 'Stallings', 'Stanley', 'Steele', 'Stefani', 'Stiles', 'Streelman', 'Stroud', 'Stuard', 'Summerhays', 'Swafford', 'Taylor', 'Taylor', 'Thomas', 'Thompson', 'Todd', 'Toms', 'Van Aswegen', 'Van Der Walt', 'Villegas', 'Wagner', 'Watson', 'Weekley', 'Wheatcroft', 'Whee Kim', 'Wilkinson', 'Wilson', 'Woo Kim', 'Woodland']
full_names = ['Bubba Watson', 'Branden Grace', 'Brooks Koepka', 'Patrick Reed', 'Matt Kuchar', 'Zach Johnson', 'Webb Simpson', 'Paul Casey', 'Jon Rahm', 'J.B. Holmes', 'Daniel Berger', 'Jim Furyk', 'Louis Oosthuizen', 'Gary Woodland', 'Francesco Molinari', 'Russell Knox', 'Brendan Steele', 'Kevin Chappell', 'Tony Finau', 'Marc Leishman', 'Charley Hoffman', 'Martin Laird', 'Shane Lowry', 'Ryan Moore', 'Justin Thomas', 'Brian Harman', 'Soren Kjeldsen', 'Tyrrell Hatton', 'Keegan Bradley', 'Daniel Summerhays', 'Kyle Reifers', 'Kevin Streelman', 'Padraig Harrington', 'Luke Donald', 'Boo Weekley', 'Bryson DeChambeau', 'Colt Knost', 'Retief Goosen', 'Hudson Swafford', 'Aaron Baddeley', 'Patton Kizzire', 'Fredrik Jacobson', 'John Senden', 'Ricky Barnes', 'Steve Wheatcroft', 'Robert Garrigus', 'Jon Curran', 'Jason Kokrak', 'Russell Henley', 'Ken Duke', 'Smylie Kaufman', 'Chris Stroud', 'Jamie Lovemark', 'Bryce Molder', 'Chesson Hadley', 'Michael Thompson', 'Chez Reavie', 'Robby Shelton', 'Adam Hadwin', 'Chad Campbell', 'Seung-Yul Noh', 'Troy Merritt', 'Derek Fathauer', 'James Hahn', 'Mark Wilson', 'Lucas Glover', 'Thomas Aiken', 'Jerry Kelly', 'Brendon De Jonge', 'Ben Crane', 'Patrick Rodgers', 'Geoff Ogilvy', 'Jamie Donaldson', 'Billy Hurley', 'Bud Cauley', 'Tom Hoge', 'Wes Roach', 'Angel Cabrera', 'Spencer Levin', 'Luke List', 'Vaughn Taylor', 'Chad Collins', 'Sam Saunders', 'David Toms', 'Justin Leonard', 'Ben Martin', 'Scott Pinckney', 'Miguel Angel Carballo', 'Rory Sabbatini', 'Si Woo Kim', 'J.J. Henry', 'Alex Cejka', 'Tyler Aldridge', 'Rob Oppenheim', 'Camilo Villegas', 'Morgan Hoffmann', 'Shawn Stefani', 'Martin Piller', 'Sung Kang', 'Hunter Mahan', 'Greg Owen', 'George McNeill', 'Blayne Barber', "Sean O'Hair", 'Ernie Els', 'Nick Taylor', 'Carlos Ortiz', 'Jordan Niebrugge', 'Johnson Wagner', 'Michael Kim', 'Scott Brown', 'Greg Chalmers', 'Brendon Todd', 'Andres Gonzales', 'Vijay Singh', 'Kyle Stanley', 'Kelly Kraft', 'Matt Jones', 'Whee Kim', 'Jason Gore', 'Jonas Blixt', 'Cameron Smith', 'Peter Malnati', 'Will MacKenzie', 'Lee McCoy', 'Ted Potter', 'Scott Stallings', 'Brian Gay', 'Tim Wilkinson', 'Robert Allenby', 'Tim Petrovic', 'Steve Marino', 'John Huh', 'Henrik Norlander', 'Dicky Pride', 'Derek Ernst', 'Zac Blair', 'Brian Stuard', 'Bronson Burgoon', 'Erik Compton', 'Tyrone Van Aswegen', 'Andrew Landry', 'Steven Bowditch', 'Dong-Hwan Lee', 'Abraham Ancer', 'Adam Rainaud', 'Dawie Van der Walt', 'Andrew Loupe', 'Hiroshi Iwata', 'Heath Slocum', 'Darron Stiles']

recent_performance = [82, 88, 100, 100, 100, 14, 56, 35, 37, 100, 100, 100, 44, 98, 100, 110, 15, 31, 66, 50, 100, 58, 73, 100, 31, 52, 47, 63, 67, 100, 54, 70, 100, 26, 85, 55, 27, 100, 62, 100, 12, 134, 10, 71, 29, 106, 8, 4, 36, 100, 107, 78, 120, 33, 75, 9, 100, 68, 1, 51, 100, 60, 96, 21, 99, 7, 92, 16, 2, 43, 100, 23, 6, 100, 100, 109, 100, 79, 53, 100, 100, 115, 77, 100, 100, 100, 46, 100, 100, 74, 94, 3, 84, 100, 100, 103, 38, 30, 25, 100, 100, 100, 100, 100, 100, 100, 100, 100, 17, 100, 39, 5, 28, 100, 93, 100, 22, 48, 100, 13, 69, 100, 100, 100, 119, 72, 95, 100, 41, 80, 90, 23, 19, 100, 49, 61, 34, 100, 59, 122, 100, 111, 65, 40, 20, 18, 81, 100, 64, 45, 11]
tournament_history = [80, 80, 80, 80, 80, 26, 80, 42, 80, 80, 80, 80, 18, 80, 80, 25, 34, 2, 37, 80, 80, 79, 61, 80, 80, 21, 34, 80, 8, 80, 15, 80, 80, 80, 24, 80, 51, 80, 64, 80, 14, 17, 80, 80, 80, 80, 13, 40, 80, 80, 6, 22, 80, 47, 80, 69, 80, 9, 16, 67, 80, 80, 48, 80, 80, 80, 68, 49, 80, 78, 80, 4, 20, 80, 80, 11, 80, 58, 80, 80, 80, 80, 57, 80, 80, 80, 80, 80, 80, 80, 43, 27, 3, 80, 80, 80, 80, 80, 59, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 19, 44, 80, 80, 62, 80, 80, 80, 80, 12, 36, 80, 80, 80, 56, 10, 80, 80, 32, 7, 63, 80, 44, 80, 30, 54, 71, 80, 5, 39, 80, 65, 60, 1, 49, 80, 80, 80, 44, 80, 53]
course_fit = [44, 78, 37, 37, 37, 149, 57, 53, 17, 37, 37, 37, 15, 69, 37, 99, 12, 13, 45, 24, 37, 11, 98, 37, 117, 95, 56, 104, 41, 37, 23, 101, 37, 143, 67, 2, 21, 37, 3, 37, 124, 6, 136, 73, 85, 64, 86, 115, 81, 37, 63, 139, 22, 68, 38, 54, 37, 88, 8, 126, 37, 40, 36, 138, 96, 104, 72, 4, 27, 62, 37, 31, 119, 37, 37, 55, 37, 28, 141, 37, 37, 80, 60, 37, 37, 37, 39, 37, 37, 61, 76, 50, 20, 37, 37, 18, 122, 140, 35, 37, 37, 37, 37, 37, 37, 37, 37, 37, 104, 37, 1, 84, 74, 37, 97, 37, 75, 77, 37, 5, 58, 37, 37, 37, 10, 51, 59, 37, 19, 79, 30, 127, 34, 37, 9, 16, 93, 37, 32, 26, 37, 52, 82, 14, 33, 146, 104, 37, 83, 104, 43]
similar_course = [136, 139, 137, 137, 137, 43, 100, 74, 44, 137, 137, 137, 13, 35, 137, 67, 31, 3, 6, 76, 137, 19, 95, 137, 90, 51, 56, 115, 5, 137, 81, 96, 137, 109, 10, 1, 102, 137, 82, 137, 75, 70, 7, 134, 79, 86, 26, 135, 40, 137, 9, 59, 71, 60, 80, 65, 137, 17, 16, 62, 137, 115, 22, 115, 115, 151, 39, 23, 14, 47, 137, 4, 30, 137, 137, 8, 137, 58, 98, 137, 137, 129, 103, 137, 137, 137, 57, 137, 137, 78, 52, 18, 11, 137, 137, 141, 68, 144, 41, 137, 137, 137, 137, 137, 137, 137, 137, 137, 115, 137, 53, 37, 88, 137, 42, 137, 87, 49, 137, 21, 55, 137, 137, 137, 64, 29, 25, 137, 32, 33, 105, 34, 61, 137, 48, 12, 94, 137, 15, 66, 137, 50, 45, 2, 91, 104, 107, 137, 89, 115, 20]
golfstrat_id = [90, 101, 148, 135, 134, 40, 75, 45, 18, 111, 113, 125, 22, 84, 110, 100, 15, 9, 52, 54, 118, 20, 88, 127, 67, 36, 61, 94, 28, 131, 50, 96, 140, 71, 48, 12, 43, 123, 47, 108, 25, 95, 3, 92, 53, 72, 14, 38, 34, 128, 39, 78, 91, 23, 93, 29, 136, 33, 2, 64, 133, 74, 66, 62, 85, 49, 65, 6, 4, 46, 126, 5, 19, 116, 137, 35, 121, 60, 86, 145, 114, 97, 80, 130, 149, 103, 55, 143, 112, 70, 69, 8, 27, 129, 104, 98, 68, 87, 17, 138, 141, 106, 122, 150, 151, 120, 139, 147, 11, 152, 30, 10, 42, 105, 76, 119, 57, 51, 115, 7, 56, 146, 117, 124, 89, 41, 79, 142, 37, 44, 73, 16, 21, 109, 32, 26, 63, 132, 31, 82, 144, 83, 59, 1, 24, 58, 99, 107, 81, 77, 13]
dk_price = [6900, 5000, 6200, 5000, 5700, 5400, 5100, 5000, 5900, 6000, 5800, 5900, 5600, 7300, 11500, 8500, 6000, 5400, 5300, 7700, 5100, 5100, 11200, 6300, 7200, 12300, 5900, 5300, 5700, 5500, 6200, 5800, 8100, 6300, 6200, 6300, 7100, 9600, 7600, 5000, 5800, 5000, 5200, 6100, 5200, 5000, 5100, 5500, 8900, 6800, 9100, 6000, 5600, 5400, 5600, 5000, 5200, 5000, 6900, 5600, 9700, 5700, 6100, 5900, 6300, 5300, 6400, 6000, 9400, 5200, 6700, 5500, 6500, 9800, 5300, 5500, 5800, 7800, 7600, 5400, 6400, 8400, 7500, 7500, 5400, 5300, 9300, 6100, 7300, 5800, 8200, 6100, 8000, 5600, 5400, 10600, 5500, 6200, 5700, 5600, 5500, 7400, 10900, 6000, 6800, 9900, 5300, 7000, 6700, 5700, 6200, 5200, 6500, 5700, 6400, 8600, 7800, 5800, 5500, 5800, 5300, 5600, 6100, 7900, 5600, 5700, 6400, 7700, 5900, 5200, 6500, 5000, 5600, 5300, 6000, 5200, 5300, 5900, 8300, 6100, 5700, 5100, 7700, 5800, 5400, 10000, 5900, 5400, 5300, 5100, 10200]

totals = [432, 486, 502, 489, 488, 272, 368, 249, 196, 465, 467, 479, 112, 366, 464, 401, 107, 58, 206, 284, 472, 187, 415, 481, 385, 255, 254, 456, 149, 485, 223, 443, 494, 429, 234, 150, 244, 477, 258, 462, 250, 322, 236, 450, 326, 408, 147, 332, 271, 482, 224, 376, 384, 231, 366, 226, 490, 215, 43, 370, 487, 369, 268, 416, 475, 391, 336, 98, 127, 276, 480, 67, 194, 470, 491, 218, 475, 283, 458, 499, 468, 501, 377, 484, 503, 457, 277, 497, 466, 363, 334, 106, 145, 483, 458, 440, 376, 481, 177, 492, 495, 460, 476, 504, 505, 474, 493, 501, 327, 506, 142, 180, 312, 459, 370, 473, 321, 305, 469, 58, 274, 500, 471, 478, 338, 203, 338, 496, 161, 243, 361, 280, 179, 463, 168, 169, 355, 486, 142, 335, 498, 361, 311, 58, 217, 406, 471, 461, 361, 421, 140]

print len(first_names)

fake_array = []

for j in range(0,len(dk_price)):
    holding_array = []
    for i in range(1,len(dk_price)):
        if totals[j] < totals[i] and dk_price[j] < dk_price[i]:
            holding_array.append(last_names[j])
    if len(holding_array) == len(dk_price):
        fake_array.append(holding_array[0])

print fake_array

# for i in range(0,47):
#     for j in range(0,47):
#         if (dk_price[i] < dk_price[j+1]) and (totals[i] < totals[j+1]):
#             del dk_price[j+1]
#             del recent_performance[j+1]
#             del tournament_history[j+1]
#             del course_fit[j+1]
#             del similar_course[j+1]
#             del first_names[j+1]
#             del last_names[j+1]
#             del totals[j+1]
#             del golfstrat_id[j+1]
#             del full_names[j+1]
#
# print len(first_names)
#
# print full_names
# print totals

def createAlgorithmTable():
    c.execute('DROP TABLE IF EXISTS algorithm')
    c.execute('CREATE TABLE IF NOT EXISTS algorithm (full_name TEXT, salary INTEGER)')

def addGolfer(full_name,salary):
    c.execute('INSERT INTO algorithm (full_name,salary) VALUES (?,?)',(full_name,salary))

createAlgorithmTable()

for k in range(0,len(full_names)):
    addGolfer(full_names[k],dk_price[i])

conn.commit()

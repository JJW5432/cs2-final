#!/usr/bin/python
print "Content-Type: text/html\n"
print ""
print "<!DOCTYPE html>"

import datetime

from about_lib import *


print '''
<html>
    <head>
        <link href="./vendor/font.woff" rel='stylesheet' type='text/css'>
        <link rel="stylesheet" type="text/css" href="./frontend/about.css">
    </head>
    <body>
        <h1>About Tic-Tac-Toe</h1>
        <p>This page is a study of machine learning, using the model game of Tic-Tac-Toe. Each time the user plays a game, data about the success of chosen moves is added to the computer's memory. The computer then uses this memory to choose future moves, becoming more intelligent about the game as it plays more often. Data below displays statistics about the computer's gameplay for both its entire memory, and the current date. Note that wins are considered successful, ties are considered half as successful, and losses are not considered successful.</p>
        
=======
'''

# current date and time information

print '''
        <h2>Current Statistics</h2>
'''

print current()

print '''
        <br>
        <h2>Today's Statistics</h2>
'''

# print today's date
print str(datetime.datetime.now().date())

print find(str(datetime.datetime.now().date()))

print '''
</table>
        <br>
        <h2>Search a Date</h2>
        <table>
            <tr>
            <form name="input" method="GET" action="find_about.py">
                <td>
                    Year:
'''

print options(yearOptions(),"year",str(datetime.datetime.now().date())[:4])

print '''
                </td>
                <td>
                    Month:
'''

print options(["01","02","03","04","05","06","07","08","09","10","11","12"],"month",str(datetime.datetime.now().date())[5:7])

print '''
                </td>
                <td>
                    Day:
'''

print options(["01","02","03","04","05","06","07","08","09","10","11","12",'13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'],"day",str(datetime.datetime.now().date())[8:10])

print '''
                </td>
                <td>
                    <input type="submit" value="Find!">
                </td>
                </form>
            </tr>
        </table>
'''

print '''
        <br>
        <h2>Show All Data</h2>
        <br>
        <form method="GET" action="about.py">
            <input type="submit" value="Show" 
                name="show" id="show" />
        </form>
'''

import os
if os.environ["QUERY_STRING"] == 'show=Show':
    print show_all()

print '''
<br>
        <h2>created by</h2> <h3>Jake Waksbaum</h3> <h2>and</h2> <h3>Ariel Levy</h3>
        <br><br>
        <a href="index.html">Return</a>
    </body>
</html>
'''

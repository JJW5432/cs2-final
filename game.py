#!/usr/bin/python
print "Content-Type: text/html\n"
print ""
print "<!DOCTYPE html>"

import cgi
import cgitb
cgitb.enable()
fs = cgi.FieldStorage()
piece = fs['piece'].value
#piece = 'X'

from play_lib import *

print """
<html>
    <head>
        <link href="./vendor/font.woff" rel='stylesheet' type='text/css'>
        <link rel="stylesheet" type="text/css" href="./frontend/main.css">
        <script src="./vendor/jquery-1.11.1.min.js"></script>
    </head>
    <body>
        <table id="board">
            <tr>
                <td id="1" state="0"></td>
                <td id="2" state="0" class="v"></td>
                <td id="3" state="0"></td>
            </tr>
            <tr>
                <td id="4" state="0" class="h"> </td>
                <td id="5" state="0" class="v h"></td>
                <td id="6" state="0" class="h"></td>
            </tr>
            <tr>
                <td id="7" state="0"> </td>
                <td id="8" state="0" class="v"> </td>
                <td id="9" state="0"> </td>
            </tr>
        </table>
       <!-- <svg width="300" height="300">
            <circle cx="50" cy="50" r="40" stroke="green" stroke-width="4" fill="yellow" />
            <rect x="100" y="100" width="100" height="100" stroke="white" stroke-width="10" fill="none" />
        </svg>-->
        <div id="overlay" >
            <p></p>
            <a href='.'>Play Again?</a>
        </div>
        <p id="piece_storage" display="none">
"""
print piece
if piece == 'O':
    print "</p><p id='move_storage'>"
    moves = readMem(Board())
    move = chooseMove(moves)
    print move.num
print """
       </p>
           <script src="./frontend/game.js"></script>
    </body>
</html>
"""

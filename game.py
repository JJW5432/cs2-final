#!/usr/bin/python
print ""
print "Content-Type:text/html\n\n"

import cgi
fs = cgi.FieldStorag()
piece = fs['piece'].value


print """
<html>
    <head>
        <link href="./vendor/font.woff" rel='stylesheet' type='text/css'>
        <link rel="stylesheet" type="text/css" href="./frontend/main.css">
        <script src="./vendor/jquery-1.11.1.min.js"></script>
	<script src="./frontend/main.js"></script>
    </head>
    <body>
        <div class="square">
        <div class="inner">
        <table id="board">
            <tr>
                <td id="1" state="0">&nbsp;</td>
                <td id="2" state="0" class="v">&nbsp;</td>
                <td id="3" state="0">&nbsp;</td>
            </tr>
            <tr>
                <td id="4" state="0" class="h"> &nbsp;</td>
                <td id="5" state="0" class="v h">&nbsp;</td>
                <td id="6" state="0" class="h">&nbsp;</td>
            </tr>
            <tr>
                <td id="7" state="0"> &nbsp;</td>
                <td id="8" state="0" class="v"> &nbsp;</td>
                <td id="9" state="0"> &nbsp;</td>
            </tr>
        </table>
        </div>
        </div>
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
print value
print"""
       </p>
    </body>
</html>
"""

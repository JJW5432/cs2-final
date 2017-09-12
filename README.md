# **Final Project Proposal** -- Coding Butterflies
Introduction to Computer Science, Term 2  
Brown Mykolyk  
Spring 2014  
Jake Waksbaum and Ariel Levy  

* * *


## Overview
Our project will be an effort to implement very basic machine learning to teach our script to play Tic-Tac-Toe. The script will start out by deciding moves randomly, but it will keep track of all the moves and outcomes of every game. If it recognizes the situation, it will base its move on the outcome of different moves it has seen played in that situation. In this way the more it plays, the better it will get.

## User Experience
The user will be able to play the computer in a game of Tic-Tac-Toe. First the user can select what stage of learning he or she wishes to play. The default mode would use the live database of all past games. However, the user could also choose an old version to play against. Novice mode would use an empty game database, beginner mode would use a database of 10 games, and so on. Expert mode uses a different algorithm that always chooses the optimal move. There will be data displayed about the computer’s win/loss record in the live mode, and each special mode on a separate data page.

## Major Components
The user needs to be able successfully play a game of Tic-Tac-Toe against the computer. The computer needs to store the game in a CSV database of some sort so it can use it as a reference later on.

## Incorporation of IntroCS2 Topics
We will store its “memory” in a csv file which we will read and update each move. We will also analyze the same database for trends and stats on the program’s improvements as time passes. We will also pass the state of the game board via url parameters to the Python script, and the script will return its desired move.
## Specific Features of Note
We will offer a feature where the user can input a game board, and we will return both the actual optimal move and what the learning algorithm would do.
## Stretch Goals
One way to grow the project would be to incorporate meta analysis of how the computer is learning. We could analyze how many games it takes for a computer to learn the best response to a given board, how the win versus loss record changes over time, and in how many moves the computer wins or loses. Based on analysis of how the computer learns, we can project what its win percentage will be after a given number of games. For every move of every game, in addition to keeping track of what actually occurred, we will keep track of what the optimal move should have been, so we can measure how often both the user and the learning algorithm choose the optimal move.In addition, we could have the computer customize learning to each unique player. Users can choose to start playing with a novice computer, and teach the computer solely based on the user’s individual play. That way the computer’s learned strategy would be unique to the user. 

## Anticipated Hurdles
The algorithm for the computer to take into account previous experiences will be complicated, as well as finding a good way of storing game histories.On the frontend side, we need to find a good way of displaying the board and allowing the user to make a move and updating the board without too much page reload and long urls.

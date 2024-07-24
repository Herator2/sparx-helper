# Sparx Maths Bookwork Code Logger
The goal of this program is to be able to complete your sparx maths homework faster and more efficiently.
It does this by automatically guessing your bookwork code and saving the answer to a folder. 
You are then able to type in a bookwork code to return the answer when there is a check

## Features
 - Automatically guesses next bookwork code to save you from having to type it in.
 - Saves inputted answers to be returned to later incase of a bookwork check. (Discaimer: You must manually type the answer into sparx **and** into this program)
 - Designed to be quick to use without unnessesary menus.
 - Very few dependencies

## Dependencies
These should be in the Python Standard Library
 - os python module

## Installation
1. Download the newest release from [releases](https://github.com/Herator2/Sparx-Maths-Bookwork-Code-Logger/releases)
2. Create a folder on your computer for the program
3. Move the program into the folder
4. Run the main.py file with python (You may have to install python)
5. The program will automatically create a data folder to store codes

## How to use
To save a code, simpily enter an answer into the input and hit enter. The script will store this code and immediately roll over to the next code
`>>> [PUT ANSWER TO CURRENT CODE HERE]`
To move on to the next section of codes (The number infront) type n or next in the input
`>>> n`
To manually override the bookwork code, type c followed by the new code
`>>> c 1A`
To view a stored answer, type o followed by the code.
`>>> o 1A`

## Disclaimer
This program has been tested on only windows and linux. The script **should** work on mac, but there will be no support if it fails (Blame apple's pricing).

Basketball Team Stats Tool

In this project you will be writing a program that reads from the "constants" data (PLAYERS and TEAMS) in constants.py. This data will need to be translated into a new collection of your choosing and the fields need to be changed to something that makes more sense for Python to do its comparisons.

Project Requirements
Meets Expectations
Create a new file seperate from constants.py called app.py or application.py.
Import and use the data from constants.py in your program, but do not change the data in constants.
Catch exceptions and errors
Function calls, print statements, or any calculated execution logic should be wrapped inside a Dunder Main statement for your script.
Clean the data from constants.py when adding it to the new data structure: player experience should be boolean True or False instead of a string; player height should be an int; guardians should be split into a list of strings
Assign players to each team so the teams are evenly balanced by total players. The same player cannot be assigned to multiple teams.
Create a clear and readable menu for the user
The team stats should display the team's name, the total number of players, and the player names as a comma-separated string (not a list object)
Exceeds Expectations
Clean the guardians string so that it becomes a List of strings. Remove the and between the names and storing each guardian in a List together for that player.
Also balance players in a way that also ensures teams have equal numbers of experienced vs inexperienced players.
The user should be re-prompted with the main menu until they decide to "Quit the program".
The stats should also display the number of experienced vs inexperienced players, average height, and all of the guardians as a comma-separated list.

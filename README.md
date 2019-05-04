# Basketball Team Stats Tool
---

You will apply your knowledge of built-in Python data types and combine these types to create structures to store and organize a team of Basketball players into distributed teams. This tool will not only balance the teams by the total number of players but also let you generate some statistics for a given team.

# Project Requirements
---

## Meets Expectations

* Create a file name app.py or application.py which contains the entry point to start your program logic.
* Import and use the data from constants.py in your program
* The script should not crash due to uncaught exceptions. Raised exceptions should be handled appropriately so the program can continue or exit without a crash.
* Function calls, print statements, or any calculated execution logic should be wrapped inside a Dunder Main statement for your script.
NOTE: This does not mean everything written has to be contained within Dunder Main. You can extract code out to functions, which can be outside dunder main.
* The player data imported from constants.py needs to be cleaned up and stored in new data types in a structure that makes sense.
* Convert the following data: 
  * The height string should be an integer
  * The experienced string should become a boolean of: True if YES or False if NO.
* Assign players to each team so the teams are evenly balanced by total players.
  * The order in which you assign the players do not matter but should be balanced when team assignment is finished.
  * The same player cannot be assigned to multiple teams.
* Do not modify or mutate the imported data from constants.py in any way. HINT: You will want to iterate over this data and create a new data structure to hold your cleaned data.
* As a user, I should be able to respond to a menu with each of the following options:
  * Display a given teams stats
  * Quit the program
  * Actual names of the displayed options are up to you but must make sense.
* Team stats should display:
  * Team's name
  * Total number of players on that team
  * The player names of that team (joined together as a comma-separated string not displayed as a List object.)
  * The formatting you use to display is up to you, though should be readable using spacing.

## Exceeds Expectations

* Additionally clean:
  * the guardians string so that it becomes a List of strings. Remove the and between the names and storing each guardian in a List   together for that player.
* Also balance players in a way that also ensures teams have equal numbers of experienced vs inexperienced players
  * Teams still must be balanced with the same number of players.
  * Each team should have the same number of experienced vs. experienced players.
* The user should be re-prompted with the main menu until they decide to "Quit the program".
* Team stats should additionally display:
  * Total number of inexperienced players
  * Total number of experienced players
  * Average height of the team
  * The guardian names of all the players on the team (joined together as a comma-separated string not displayed as a List object).
  * Math formula for average height: (sum of all the heights) / (total players)
  
  
  

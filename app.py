import constants

if __name__ == "__main__":

    print("BASKETBALL TEAM STATS TOOL\n")
    print("----MENU----\n")
        
    
    experienced = []
    inexperienced = []
    
    players_in_list = constants.PLAYERS
    
    for player in players_in_list:
        if player['experience'] == 'YES':
            player['experience'] = True
            player['height'] = player['height'].split(" ")
            player['height'][0] = int(player['height'][0])
            player['guardians'] = player['guardians'].replace("and", ",")
            experienced.append(player)
        if player['experience'] == 'NO':
            player['experience'] = False
            player['height'] = player['height'].split(" ")
            player['height'][0] = int(player['height'][0])
            player['guardians'] = player['guardians'].replace("and", ",")
            inexperienced.append(player)
    
            
    panthers = []
    bandits = []
    warriors = []
    
    for player in experienced:
        if len(panthers) < 3:
            panthers.append(player)
            experienced.pop(0)
    
    for player in experienced:
        if len(bandits) < 3:
            bandits.append(player)
            experienced.pop(0)
            
    for player in experienced:
            warriors.append(player)
    
    for player in inexperienced:
        if len(panthers) < 6:
            panthers.append(player)
            inexperienced.pop(0)
    
    for player in inexperienced:
        if len(bandits) < 6:
            bandits.append(player)
            inexperienced.pop(0)
            
    for player in inexperienced:
            warriors.append(player) 
    
        
        
def stats(team):
    player_list = []
    experienced_list = []
    inexperienced_list = []
    guardians_list = []
    height_numbers = []
    
    print("Total players {}".format(len(team)))
    
    for players in team:
        height_numbers.append(players['height'][0])
    
    print("Average height of team {}: ".format((sum(height_numbers)) / (len(height_numbers))))
    
    for players in team:
        if players['experience'] == True:
            experienced_list.append(players['experience'])
        elif players['experience'] == False:
            inexperienced_list.append(players['experience'])
            
    print("Total Experienced players {}".format(len(experienced_list)))
    print("Total Inexperienced players {}\n".format(len(inexperienced_list)))   
    
    print("Players on Team:") 
    for players in team:
        player_list.append(players['name'])
    print(", ".join(player_list))
    
    print("")
    
    print("Guardians on Team:")
    for players in team:
        guardians_list.append(players['guardians'])
    print(", ".join(guardians_list))


if __name__ == "__main__":
    
    start = True
    
    
    while start:
        try:
            print("")
            print("Here are your choices:")
            print("1) Display Team Stats")
            print("2) Quit\n")
            first_option = input("Enter an option > ")
            first_option = int(first_option)
            if first_option == 2:
                print("See you next time, Goodbye!")
                break
            elif first_option > 2 or first_option < 1:
                print("")
                print("Invalid number! please try again")
                continue
            
            while first_option == 1:
                teams_in_list = constants.TEAMS
                print("")
                for number, team in enumerate(teams_in_list, 1):
                    print("{}) {}".format(number, team))
                print("")
                second_option = input("Enter an option > ")
                second_option = int(second_option)
                print("")
                
                if second_option == 1:
                    print("Team: {} Stats".format(teams_in_list[0]))
                    print("--------------------")
                    stats(panthers)
                elif second_option == 2:
                    print("Team: {} Stats".format(teams_in_list[1]))
                    print("--------------------")
                    stats(bandits)
                elif second_option == 3:
                    print("Team: {} Stats".format(teams_in_list[2]))
                    print("--------------------")
                    stats(warriors)
                else:
                    print("Invalid entry! Please try again")
                    
                print("")
                third_option = input("Press any key to continue...")
                break 
        except ValueError:
            print("")
            print("Please enter numbers only")
            continue

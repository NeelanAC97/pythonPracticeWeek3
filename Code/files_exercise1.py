
teams_file = open("teams.txt", "w")

teams_file.write("Chelsea \n")
teams_file.write("Manchester United \n")
teams_file.write("Liverpool \n")
teams_file.write("Arsenal \n")
teams_file.write("Manchester City \n")

teams_file.close()

teams_file = open("teams.txt", "r")

for i in range(1,6):
    lines = teams_file.readline()
    if i == 1 or i == 4:
        print(lines)
        
teams_file.close()
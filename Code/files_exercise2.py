
teams_file = open("teams.txt", "r")


line1 = teams_file.readline()
line2 = teams_file.readline()
line3 = teams_file.readline()
line4 = teams_file.readline()
line5 = teams_file.readline()

line1 = "This is a new line \n"

teams_file.close()

teams_file = open("teams.txt", "w")

teams_file.write(line1 + line2 + line3 + line4 + line5)

teams_file.close()

teams_file = open("teams.txt", "r")

for i in range (5):
    print(teams_file.readline())

teams_file.close()



#teams_file = open("teams.txt", "r")

#outfile = ""

#for i in range(5):
    
    #line = []
    
    #line[i] = teams_file.readline()

    #if line[i] == line[1]:
    #    line[i] = "This is a new line \n"

    #outfile += line[i]

#teams_file.close()

#teams_file = open("teams.txt", "w")

#teams_file.write(outline)

#for i in range (5):
    #print(teams_file.readline())

#teams_file.close()

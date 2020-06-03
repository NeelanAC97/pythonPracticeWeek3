
#example_file = open("example_file.txt", "r")

#print(example_file.readline())
#example_file.readline()
#print(example_file.readline())
#example_file.seek(0)
#print(example_file.readline())

#example_file.read()
#example_file.seek(0)

#lines = example_file.readlines()
#print(lines)


#example_file = open("example_file.txt", "w")

#for n in range(1,11):
#    newline = "This is CHANGED line" + str(n) + "\n"
#    example_file.write(newline)


example_file = open("example_file.txt", "r")
lines = example_file.readline()
example_file.close()

example_file = open("example_file.txt", "w")
example_file.write(lines)
example_file.close()
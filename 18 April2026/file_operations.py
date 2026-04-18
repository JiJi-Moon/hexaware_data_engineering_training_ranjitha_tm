#print line by line from text file
with open("data.txt","r") as f:
    for line in f:
        print(line.strip())

#find total number of lines
with open("data.txt","r") as f:
    students= f.readlines()
print("Total Students:",len(students))



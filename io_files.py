import csv

with open("names.txt", "w") as file:
    for i in range(10):
        file.write(f"name_{i}\n")

#readLines
with open("names.txt", "r") as file:
    lines = file.readlines() # returns all lines as list
    print(lines)

#loop through rows; rstrip
with open("names.txt", "r") as file:
    for line in file:
        print(line.rstrip()) # strip off the end of the line

# csv reader (no header)
with open("names.txt", "w") as file:
    for i in range(10):
        file.write(f"{i},name_{i}\n") # uses , as separator (csv)

with open("names.txt", "r") as file:
    reader = csv.reader(file)
    for line in reader:
        print(line) # returns list of strings

# csv DistReader (with header)
with open("names.txt", "w") as file:
    file.write("number,name\n")
    for i in range(10):
        file.write(f"{i},name_{i}\n") # uses , as separator (csv)

with open("names.txt", "r") as file:
    reader = csv.DictReader(file)
    d=dict()
    for line in reader:
        d[line["name"]]=line["number"] # cretes new item for the dictionary
    print(d)

# read and write with csv







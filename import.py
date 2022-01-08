from cs50 import SQL
from csv import reader
from sys import argv

# opens database in a variable
db = SQL("sqlite:///students.db")


if len(argv) < 2:
    print("error, import.py characters.csv")
    exit()

# opens the comma separated values file containing the students information and stores into an array
with open(argv[1], newline='') as charactersFile:
    characters = reader(charactersFile)
    for character in characters:
        if character[0] == 'name':
            continue

        # splits the full name into first, last and middle name if available
        fullName = character[0].split()
        # inserts the names and other information into database
        if len(fullName) < 3:
            db.execute("INSERT INTO students(first, middle, last, house, birth) VALUES(?, ?, ?, ?, ?)",
                       fullName[0], None, fullName[1], character[1], character[2])

        else:
            db.execute("INSERT INTO students(first, middle, last, house, birth) VALUES(?, ?, ?, ?, ?)",
                       fullName[0], fullName[1], fullName[2], character[1], character[2])
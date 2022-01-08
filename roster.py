from cs50 import SQL
from sys import argv


if len(argv) < 2:
    print("usage error, roster.py houseName")
    exit()

# open the database and lists all the people from a specific house, sorted by alphabetic order
db = SQL("sqlite:///students.db")
students = db.execute("SELECT * FROM students WHERE house = (?) ORDER BY last", argv[1])

# prints each person along with their personal information
for student in students:
    if student['middle'] != None:
        print(f"{student['first']} {student['middle']} {student['last']}, born {student['birth']}")
    else:
        print(f"{student['first']} {student['last']}, born {student['birth']}")

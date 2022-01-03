"""
@gole : print Pattern Of Squere
@date : 3-1-2022
"""

Row = int(input("Enter The Number Of Rows =>"))
Column = int(input("Enter The Number Of Column =>"))

for x in range(Row):
    for x in range(Column):
        print(" * ", end = ' ')
    print()

print("Thanks")
input()

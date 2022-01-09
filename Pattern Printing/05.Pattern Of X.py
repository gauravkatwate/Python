"""
@gole : Pattern Of X
@date : 3-1-2022
"""

Row = int(input("Enter Count Of Rows =>"))
Column = int(input("Enter Count Of Column =>"))

for i in range(1, Row + 1):
    for j in range(1, Column + 1):
        if i == j or i + j == Row + 1:
            print(" * ",end = ' ')
        else:
            print("   ",end = ' ')
    print()

print("Thanks")
input()

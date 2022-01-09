"""
@gole : Check Given Number 5 Or Not
@date : 10-1-2022
"""

def Check(ino):
    if ino % 5 == 0:
        return True
    else:
        return False

ino = int(input("Enter Any Number =>"))

if Check(ino):
    print("Divisible By 5")
else:
    print("Not Divisible By 5")

input()

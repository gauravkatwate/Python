"""
@gole : inputted no. is divisible by both 5 & 7 or only by 5 or only by 7 or not by both 5 & 7.
@date : 1-1-2022
"""

ino = int(input("Enter Any Numbe =>"))

if ino % 5 == 0 and ino % 7 == 0:
    print("Given Number Divisible Both 5 & 7.")
elif ino % 5 == 0:
    print("Given Number Divisible By 5.")
elif ino % 7 == 0:
    print("Given Number Divisible By 7.")
else:
    print("Given Number Not Divisible Both 5 & 7")

print("Thanks...")
input()

"""
@gole : Sum Of Digits Inputed Number.
@date : 1-1-2022
"""

ino = int(input("Enter Any Number =>"))

sum = 0;

while ino != 0:
    digit = ino % 10
    sum = sum + digit
    ino = ino // 10

print("Given Number Digit Sum Is =>",sum)

print("Thanks")
input()

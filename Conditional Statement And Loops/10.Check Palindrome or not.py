"""
@gole : Check Given Number Palindrome Or Not
@date : 3-1-2022
"""

ino = int(input("Enter Any Number =>"))
temp = ino
no = 0

while ino != 0:
    digit = ino % 10
    no = (no * 10) + digit
    ino = ino // 10

if no == temp:
    print("Given Number Is Palindrome")
else:
    print("Given Number Is Not Palindrome")

print("Thanks")
input()

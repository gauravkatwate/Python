"""
@gole : Accept Number From User And Display Reverse.
@date : 1-1-2022
"""

ino = int(input("Enter Any Number =>"))
rev = 0

while ino != 0:
    digit = ino % 10
    rev = (rev * 10) + digit  
    ino = ino // 10

print("Reverse Number =>",rev)

print("Thanks")
input()

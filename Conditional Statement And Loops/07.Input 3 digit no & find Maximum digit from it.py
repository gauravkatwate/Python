"""
@gole : input Any Number And Find Maximum Digit From It.
@date : 1-1-2022
"""

ino = int(input("Enter Any Number =>"))
max = 0

while ino != 0:
    digit = ino % 10
    if max < digit:
        max = digit
    ino = ino // 10

print("Maximum Digit Is =>",max)

print("Thanks")
input()

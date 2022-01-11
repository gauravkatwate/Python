"""
@gole : Accept Two Numbers From User And Display First Number In Second Number Of Times
@date : 11-1-2022
"""

def Display(no1,no2):
    x = 0
    for x in range(no2):
        print(no1)

ino1 = int(input("Enter First Number =>"))
ino2 = int(input("Enter Second Number =>"))

Display(ino1,ino2)

input()
print("Thanks")

"""
@gole : Find Maximum Number Of Given Two Numbers
@date : 18-2-2021
"""

ino1 = input("Enter First Number =>")
ino1 = int(ino1)

ino2 = input("Enter Second Number =>")
ino2 = int(ino2)

if ino1 > ino2:
    print(ino1,"Is Greter Than",ino2)

elif ino1 < ino2:
    print(ino2,"Is Greter Than",ino1)

else:
    print("Given Numbers Are Equal")

print("...Thanks...")

"""
@gole : Find Maximum Of Given Three Numbers
@date : 1-1-2022
"""

ino1 = int(input("Enter First Number =>"))
ino2 = int(input("Enter Second Number =>"))
ino3 = int(input("Enter Third Number =>"))

if ino1 > ino2:
    print(ino1 ,"IS Maximum Number")
elif ino2 > ino3:
    print(ino2 ,"Is Maximum Number")
elif ino3 > ino1:
    print(ino3 ,"Is Maximum Number")
else:
    print("Given Numbers Are Equal")

print("Thanks...")
input()
    

"""
@gole : Swapping Two Numbers.
@Date : 1-1-2022
"""

ino1 = int(input("Enter First Number =>"))
ino2 = int(input("Enter Second Number =>"))

print("\n")

print("Before Swapping First Number =>",ino1)
print("Before Swapping Second Number =>",ino2, "\n")

ino1 = ino1 + ino2
ino2 = ino1 - ino2
ino1 = ino1 - ino2

print("After Swapping First Number =>",ino1)
print("After Swapping Second Number =>",ino2 , "\n")


print("Thanks...")
input()

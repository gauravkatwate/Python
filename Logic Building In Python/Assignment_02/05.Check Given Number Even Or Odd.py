"""
@gole : Accept Number And Check Even Or Odd
@date : 11-1-2022
"""

def Check(no):
    if no % 2 == 0:
        return True
    else:
        return False
    
if Check(int(input("Enter Any Number =>"))):
    print("Given Number Is Even")
else:
    print("Given Number Is Odd")

input()
print("Thanks")

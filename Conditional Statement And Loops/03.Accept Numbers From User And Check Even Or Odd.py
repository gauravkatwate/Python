"""
@gole : Check Given Number Even Or Odd
@date : 18-12-2021
"""

no = input("Enter Any Number =>")
no = int(no)

if no == 0:
    print("Given Number Is Nutral")
    
elif no % 2 == 0:
    print("Given Number",no,"Is Even")

else :
    print("Given Number",no,"Is Odd")

print("Thanks")
    

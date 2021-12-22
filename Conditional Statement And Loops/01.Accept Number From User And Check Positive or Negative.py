"""
@gole : Check Given Number Positive Or Negative.
@date : 18-12-2021
"""

no = input("Enter Any Number =>")
no = int(no)

if 0 < no:
    print("Given Number",no,"Is Positive")

elif 0 > no:
    print("Given Number",no,"Is Negative")

else:
    print("Given Number Is Zero")

print("...Thanks...")



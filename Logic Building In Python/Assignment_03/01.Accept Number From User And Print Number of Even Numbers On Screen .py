"""
@gole : Accept Number From User And Print That Number Of Even Numbers
@date : 12-1-2022
"""

def Display(no):
    i = 2
    if no <= 0:
        return 0
    while no > 0:
        print(i)
        i = i + 2
        no = no - 1
        
Display(int(input("Enter Any Number =>")))

input()

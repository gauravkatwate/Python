"""
@gole : Accept Number From User And Print Even Factors Of That Number
@date : 13-1-2022
"""

def Display(no):
    if no <= 0:
        return 0 
    temp = no // 2
    for i in range(1,temp + 1):
        if no % i == 0:
            if i % 2 == 0:
                print(i)
    
    
Display(int(input("Enter Any Number =>")))

input()

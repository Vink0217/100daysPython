'''
x=int(input("Enter Number: "))
if x%2==0:
    print(f"{x} is even")
else:
    print(f"{x} is odd")    
'''
def Ticket_system():
    price=0
    age=int(input("Enter your age: "))
    height=int(input("Enter Height(in cm): "))
    if age>=18 and age<45:
        if height>=120:
            print("You have to pay 18 dollars")
            price=price+18
        else:
            print("You are short to enter the ride :(")
    elif age<=55 and age>=45:
        print("Your ticket price is free")
        price=0
    elif age>55:
        print('You are too old for this ride')
    elif age>12:
        if height>=120:
            print("You have to pay 10 dollars")
            price=price+10
        else:
            print("You are short to enter this ride :(")   
    else:
        print("You are too young to enter this ride")       
    if price!=0 or price==0:
        photos=input("Do you want photos for your ride?(Y/N): ")
        if photos=='Y':
            price=price+3
            print(f"Your total bill is {price} dollars")
        else:
            print(f'Your total bill is {price} dollars')

Ticket_system()
       

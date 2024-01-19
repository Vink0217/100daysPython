import random
num=int(input("What do you wanna choose? '0' for rock, '1' for papers and '2' for scissors: "))
x=random.randint(0,2)
print(f"computer chose {x}")
if num==x:
    print("Its a tie")
    print(x)
elif num==0 and x==1:
    print("Computer Wins")
    print(x)
elif num==0 and x==2:
    print("Player Wins")
    print(x)
elif num==1 and x==0:
    print("Player Wins")
    print(x)
elif num==1 and x==2:
    print("Computer Wins")
    print(x)
elif num==2 and x==0:
    print("Computer Wins")
    print(x)
elif num==2 and x==1:
    print("Player Wins") 
    print(x)         
else:
    print("Wrong Number")                  
    
def love_calc():
    t=0
    r=0
    u=0
    e=0
    l=0
    o=0
    v=0
    name1=input("Enter First Name: ")
    name2=input("Enter Second Name: ")
    name1=name1.lower()
    name2=name2.lower()
    for i in name1:
        if i=='t':
            t=t+1
        elif i=='r':
            r=r+1
        elif i=='u':
            u=u+1        
        elif i=='e':
            e=e+1
        elif i=='l':
            l=l+1
        elif i=='o':
            o=o+1
        elif i=='v':
            v=v+1
    for i in name2:
        if i=='t':
            t=t+1
        elif i=='r':
            r=r+1
        elif i=='u':
            u=u+1        
        elif i=='e':
            e=e+1
        elif i=='l':
            l=l+1
        elif i=='o':
            o=o+1
        elif i=='v':
            v=v+1  
    print("The Love compatibility is: ")
    a=t+r+u+e
    b=l+o+v+e
    print(f'{a}{b}%')  
love_calc()                                
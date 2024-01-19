def leap_year():
    year=int(input("Enter Year: "))
    if year%4==0:
        if year%100==0:
            if year%400==0:
                print("Leap year")
            else:
                print("Not leap Year")
        else:
            print("Leap")
    else:
        print("Not leap")             
leap_year()        
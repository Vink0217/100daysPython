print("Welcome to the tip calculator")
def tipcalc(Total_bill):
    tip=int(input("how much tip you want to give: "))
    tip=(tip/100)*Total_bill
    Total_bill=Total_bill+tip
    return Total_bill
Total_bill=float(input("What is the total bill?: \n"))    
Total_bill=tipcalc(Total_bill)
Num_of_people=int(input("How many people to split bill with?: \n"))
Individual_bill=round(Total_bill/Num_of_people,2)
print(f"Each person would pay: {Individual_bill}")
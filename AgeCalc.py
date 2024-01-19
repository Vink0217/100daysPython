'''
x=input("Enter Number: ")
a=x[0]
b=x[1]
c=int(a)+int(b)
print(c)
weight=float(input("Enter Weight: "))
height=float(input("Enter Height(in m): "))
BMI=weight/height**2
print(BMI)
a=0
b=2.1
c=True
print(f'the winning is {a},score is {b},and chance is {c}')
'''
age=int(input("What is your age?: "))
Months_left=(90-age)*12
Weeks_left=(90-age)*52
days_left=(90-age)*365
print(f"The number of days left={days_left},the number of weeks left={Weeks_left},the number of months left={Months_left}")
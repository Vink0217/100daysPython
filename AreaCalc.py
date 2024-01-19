from math import ceil
test_h=float(input("Enter the height of the wall: "))
test_w=float(input("Enter the width of the wall: "))
coverage=5
Cans_needed=(test_h*test_w)/coverage
Cans_needed=ceil(Cans_needed)
print(Cans_needed)
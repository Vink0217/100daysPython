import random
n=''
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','@','#','$','%','^','&','*','(',')','_','-','+','=','<','>']
alp=int(input("Enter the amount of alphabet you want: "))
num=int(input("Enter the amount of numbers you want: "))
sym=int(input("Enter the amount of Symbols you want: "))
password=[]
for i in range(0,alp):
    random_char=random.choice(alphabet)
    password.append(random_char)
for i in range(0,num):
    random_char=random.choice(numbers)
    password.append(random_char)
for i in range(0,sym):
    random_char=random.choice(symbols)
    password.append(random_char)
random.shuffle(password)
for i in password:
    n=n+i
print(n)    
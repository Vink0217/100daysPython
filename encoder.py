def encode(String_input,shift_number):
    symbols=['!','@','#','$','%','^','&','<','>',',','.','"',"'",'?','/','-','_','+']
    for i in String_input:
        if i==' ':
            print(" ",end='')
            continue
        elif i in symbols:
            print(i,end='')
            continue
        else:
            i=ord(i)+shift_number
            print(chr(i), end='')
String_input=input('Enter String: ').lower()
shift_number=int(input("Entert the shift number: "))
encode(String_input,shift_number)        
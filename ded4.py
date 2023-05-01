c=input("введите число")
a=0
b=0

for i in c:
    if int(i) % 2 == 0:
        a+=1
    else:
        b+=1
print(f'четных чисел = {a} а нечетных {b}')
        
    

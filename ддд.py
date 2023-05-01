n=int(input ("Введите положительное число"))
m=[]
for i in range(1,n+1):
    if n % i == 0:
        m.append(i)
print(m)

shop=[]
while True:
    u=input("Что вы хотите добавить в список? Если закончили напишите-выход")
    if u.lower()=='выход':
        break
    else:
        shop.append(u)

    print(f'Текущий список покупок содержит{", ".join(shop)}')
        

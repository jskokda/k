print("Выберите направление: направо или налево")
print("Или напишите выход для завершения программы")
a=input("Текущее положение персонажа:['_', '*', '_']")
b="направо"
c="налево"
field = ['_', '*', '_']
ind_pl = 1
d="Текущее положение персонажа:['*', '_', '_']"
e="Текущее положение персонажа:['_', '_', '*']"
while True:
    if a==b:
        field[ind_pl] = '_'
        field[ind_pl + 1] = '*'
        ind_pl += 1
    else:
        field[ind_pl] = '_'
        field[ind_pl - 1] = '*'
        ind_pl -= 1
    a=input(f"Текущее положение персонажа:{field}/ Введите направление")
            
    
        
    


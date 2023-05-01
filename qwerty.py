qwerty=[['_','_','_'],
        ['_','_','_'],        
        ['_','_','_'] ]
for i in range(9):
    guess = input(f'''Введите через пробел номер строки и номер столбика.
        0    1    2
    0   {' |  '.join(qwerty[0])}
    1   {' |  '.join(qwerty[1])}        
    2   {' |  '.join(qwerty[2])}''')
    newguess=guess.split()
    one = int(newguess[0])
    two = int(newguess[1])
    
    if i % 2==0:
        qwerty[one][two] = 'x'
    else:
        qwerty[one][two] = 'o'
    
    print(qwerty)


'''Введите через пробел номер строки и номер столбика.
      0 1 2
    0 _|_|_
    1 _|_|_        
    2 _|_|_'''
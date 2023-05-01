def find_uniq(l):
    evens=[]
    odd=[]
    for i in l:
        if not i % 2:
            evens.append(i)
        else:
            odd.append(i)
    if len (evens)>len(odd):
        return odd[0]
    return evens(0)
print(find_uniq([2, 4, 0, 100, 4, 11, 36])) # 11

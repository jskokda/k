def popa(a):
    return a[-1:-(len(a)+1):-1]
a='hello'
print(popa(a))

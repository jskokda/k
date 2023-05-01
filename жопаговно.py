def calc_banq(m):
    res={}
    if m % 1000:
        res["тысяча"]=m//1000
        m-=m//1000*1000
    if m % 500:
        res["пятьсот"]=m//500
        m-=m//500*500
    if m % 100:
        res["сто"]=m//100
        m-=m//100*100
    if m % 50:
        res["пятьдесят"]=m//50
        m-=m//50*50
    if m % 10:
        res["десять"]=m//10
        m-=m//10*10
    if m % 5:
        res["пять"]=m//5
        m-=m//5*5
    if m:
        res["рубль"]=m
    return res    
print(calc_banq(456))
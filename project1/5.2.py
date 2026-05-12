def fun(n):
    s=0
    for i in range(1,n):
        if i%3==0 and i%7==0:
            s+=i
    return s**0.5
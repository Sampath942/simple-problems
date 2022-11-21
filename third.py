n=int(input())
def fun(n):
    s=''
    while n>0:
        if n%7==0:
            s+='0'
        if n%7==1:
            s+='1'
        if n%7==2:
            s+='2'
        if n%7==3:
            s+='5'
        if n%7==4:
            s+='6'
        if n%7==5:
            s+='8'
        if n%7==6:
            s+='9'
        n//=7
    return s[::-1]
print(fun(n))
n=int(input())
s=''
while n != 0:
    s = str(n%3) + s
    n = n//3
print(s)
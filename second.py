s1=input()
s2=input()
ch=s2[-1]
count=0
for x in s1:
    if x==ch:
        count+=1
print(count)
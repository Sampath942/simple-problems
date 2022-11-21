import sys
left=sys.maxsize
right=-sys.maxsize
top=sys.maxsize
bottom=-sys.maxsize

matrix=[list(map(int,input().split())) for x in range(256)]
for x in range(256):
    for y in range(256):
        if matrix[x][y]==0:
            if y<left:
                left=y
            elif y>right:
                right=y
            if x<top:
                top=x
            elif x>bottom:
                bottom=x
c1=(top,left)
c2=(top,right)
c3=(bottom,left)
c4=(bottom,right)
print(c1,c2,c3,c4)
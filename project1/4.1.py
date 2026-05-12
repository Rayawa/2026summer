x=int(input())
n=0
y=x
while x:
    n+=1
    x//=10
print('{}是{}位数'.format(y,n))
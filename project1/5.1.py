def fun(x,y):
    return (x**2+y**2)**0.5

leg1,leg2=eval(input('输入两条直角边，以逗号分隔：'))
print('斜边的长度为：{:.2f}'.format(fun(leg1,leg2)))
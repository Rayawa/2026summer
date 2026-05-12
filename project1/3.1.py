score=float(input())
if score<0 or score>100:
    print('无效')
elif score>=90:
    print('优秀')
elif score>=80:
    print('良好')
elif score>=70:
    print('中等')
elif score>=60:
    print('及格')
else:
    print('不及格')
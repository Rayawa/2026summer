ch=input()
if ch.isdigit():
    print('这是一个数字字符')
elif ch.isupper():
    print('这是一个大写英文字符')
elif ch.islower():
    print('这是一个小写英文字符')
else:
    print('这是其他字符')
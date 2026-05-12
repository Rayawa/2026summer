s=0
for i in range(1,11):
    s+=__import__('math').factorial(i)
print(s)
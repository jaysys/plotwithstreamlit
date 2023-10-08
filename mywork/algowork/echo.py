
def fnc1():
    import pandas as pd

    v = pd.read_excel('ex.xls')
    #print(v)

    v = v.reset_index()
    print(v)
    for index, row in v.iterrows():
        res = row['Age']*10
        print(index, row['First Name'], res)
fnc1()

def fnc2():
    ans = 45
    print(ans)
    print(ans:=43)
    print(ans*2)
#fnc2()

def fnc3_avg(*nums):
    avg = sum(nums)/len(nums)
    print(avg)
#fnc3_avg(2,2,2,2,2,2,2,2,2,2,2,2,2,2,2)

def fnc4():
    my_list=['a','b','d','e','f','g','c']
    my_list.insert(2,my_list.pop(6))
    print(my_list)
#fnc4()

def fnc5():
    import random
    lower = 'abcdefghijklmnoperswuvwxyz'
    upper = lower.upper()
    symbols = '!@#$%^&*()+[]:;<>,.?'
    numbers = '1234567890'
    all = lower+upper+symbols+numbers

    length=10
    password=''

    for _ in range(length):
        password = ''.join([password, random.choice(all)])

    print(password)
#fnc5()

def fnc6():
    num1 = 1_000_000
    num2 = 2_000

    ans = num1*num2
    print(f'{ans:,}')
#fnc6()

def fnc7():
    a = [1,2,3,4,5,6,7]
    b = a[::-2]
    print(b)
    b = a[::2]
    print(b)

    c = 'abcdefg'
    d = c[::-1]
    print(d)
    d = c[::-2]
    print(d)
#fnc7() 

def fnc8():
    num = 17429.2371
    rnum= str(round(num, -3))
    print(rnum)
#fnc8()

def fnc9():
    x = [.1, .1, .1, .1, .1, .1, .1, .1, .1, .1]
    print(sum(x))

    import math
    print(math.fsum(x))

    x = math.frexp(16)
    print(x)
    y = x[0]*(2**x[1])
    print(y)
#fnc9()

def fnc10():
    def func(x):
        return x[::-1].title()
    x = 'Oediv eht ekil esaelp'
    print(func(x))
#fnc10()


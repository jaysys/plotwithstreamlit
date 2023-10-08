

def fnc1():
    inv = {
        'aaa':1,
        'bbb':3
    }

    loot = {
        'aaa':2,
        'bbb':200,
        'ccc':1
    }

    # inv.update(loot)
    # print(inv)

    print( set(inv|loot) )
    new_inv = { k: (inv.get(k,0)+loot.get(k,0)) for k in set(inv | loot) }
#fnc1()

def fnc2():
    inv = [ 
        'aaa',
        'bbb',
        'ccc',
        'ddd dddd'
    ]

    indx = inv.index('aaa')
    item = inv.pop(indx)
    inv.append(item)
    print(inv)
#fnc2()


def fnc3():
    x = [1,2,1,3,4,1,2,4,1]

    most = max(x)
    print(most)

    most = max(x, key=x.count)
    print(most)
#fnc3()

def fnc4():
    myTuple = ([1,2], [3])
    myTuple[1].append(4)
    print(myTuple)
#fnc4()


def fnc5():
    import time
    from itertools import cycle
    lights = [
        ('green', 2),
        ('yello', 0.5),
        ('red', 2)
    ]

    colors = cycle(lights)
    du = 0
    while True:
        c,s = next(colors)
        print(c,s)
        du = du + s
        if du > 10:
            break
        time.sleep(s)
#fnc5()


def fnc6():
    links = [
        "www.abc.io",
        "www.bbc.com",
        "www.google.com",
        "www.wiki.org"
    ]

    for link in links:
        print(link.lstrip("www.")) # == "w."

    for link in links:
        print(link.removeprefix("www."))
#fnc6()

import time
def my_decorator(func):
    def wrapper():
        print(f"start ~> {func.__name__}")
        func()
        time.sleep(1)
        print(f"completed ~> {func.__name__}")

    return wrapper

@my_decorator
def do_this():
    print(" doing this")

@my_decorator
def do_that():
    print(" doing that")

#do_this()
#do_that()

from threading import Thread
t1 = Thread(target=do_this)
t2 = Thread(target=do_that)
t1.start()
t2.start()


# from functools import lru_cache
# @lru_cache
def incr(num):
    print("running ...")
    return (num+1)

# print(incr(1))
# print(incr(2))
# print(incr(3))
# print(incr(1))


x = [1,20,3,2,1]
x.remove(20) # 실제값을 리무브한다
print(x)


while 1:
    exit()
    match input('which fnc?'):
        case '1':
            fnc1()
        case '2':
            fnc2()
        case '3':
            fnc3()
        case _:
            exit()



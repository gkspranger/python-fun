def myfunc(name):
    return f"hello {name}"

names = ["greg", "bob", "frank"]

for i in map(myfunc, names):
    print(i)


def gethigh(num):
    return num >= 10

nums = [0,5,10,15]

for i in filter(gethigh,nums):
    print(i)

for i in map(lambda name: f"hello {name}", names):
    print(i)

for i in filter(lambda num: num >= 10, nums):
    print(i)

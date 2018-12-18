name = "frank"

for i in name:
    print(i)

# basically turn an iterable object (string) into a generator/yield
name_iter = iter(name)

print(next(name_iter))

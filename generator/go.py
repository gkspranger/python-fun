# def create_cubes(n):
#     result = []
#     for i in range(n):
#         result.append(i**3)
#     return result

# CAN BE much more memory efficient
def create_cubes(n):
    for i in range(n):
        yield i**3
        # you can continue to do work AFTER the yield that will
        # be stored/remembered

for i in create_cubes(10):
    print(i)

# can't do this cuz it doesn't return complete list
# total = create_cubes(10)
# print(total)

total = list(create_cubes(10))
print(total)

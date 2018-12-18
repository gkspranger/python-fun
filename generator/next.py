def simp_gen():
    for x in range(3):
        yield x

for num in simp_gen():
    print(num)

result = simp_gen()

print(result)

# next will get the next result
# your way of manually iterating a generator
# step by step
print(next(result))

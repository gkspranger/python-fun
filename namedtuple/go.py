t = (1,2,3)

print(t[1])

from collections import namedtuple

Dog = namedtuple("Dog", "age breed name")

sam = Dog(age=2, name="sam", breed="fox")

print(sam)

# might be good for a simple data struct
# if you expect no setters and only getters
# quick way to create a "class"

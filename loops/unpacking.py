mydict = {
    "hello": "world"
}

for key,value in mydict.items():
    print(key)
    print(value)


word = "hello world"

for index,value in enumerate(word):
    print(f"{index} = {value}")


ml1 = [1,2,3]
ml2 = ["a","b","c"]

for key,value in zip(ml1,ml2):
    print(f"{key} = {value}")

age = input("what is your age:")
print(age)
print(type(age))

mystr = "hello"
mylist = [f"this is {letter}" for letter in mystr]
print(mylist)

mylist = [letter for letter in mystr if letter == "l"]
print(mylist)

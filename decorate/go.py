# returning funcs inside other funcs

def myfunc():
    print("myfunc has ran")

    def innerfunc():
        return "hello"

    print(innerfunc())

    return innerfunc

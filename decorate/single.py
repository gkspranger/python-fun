def hello():
    return 'hi greg'

def other(some_func):
    print("other code")
    print(some_func())

other(hello)


def new_dec(orig_func):
    def wrap_func():
        print("some extra code before")
        orig_func()
        print("some extra code after")
    return wrap_func

# def func_needs_dec():
#     print("i want to be decorated")
#
# all_func = new_dec(func_needs_dec)
#
# all_func()

@new_dec
def func_needs_dec():
    print("i want to be decorated")

func_needs_dec()

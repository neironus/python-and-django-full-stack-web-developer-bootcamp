def dec(func):
    def wrap():
        print("Hello")
        return func
    # print("************")


    return wrap()

@dec
def func():
    print("world")

func()
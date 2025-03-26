# funkcja wewnętrzna zagnieżdzona

def fun1():
    print("to jest fun1")

    def fun2():
        print("To jest fun2")

    return fun2


fun2_reference = fun1()
fun2_reference()

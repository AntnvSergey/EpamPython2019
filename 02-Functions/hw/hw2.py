def func1(a):
    return a + 1


def func2(b):
    return b + 2


def atom(a=None):
    variable = a

    def set_value(z):
        nonlocal variable
        variable = z
        return variable

    def get_value():
        return variable

    def process_value(*f):
        nonlocal variable
        for func in f:
            variable = func(variable)
        return variable

    def delete_value():
        nonlocal variable
        variable = None

    return get_value, set_value, process_value, delete_value


# Test function
vget, vset, veval, vdel = atom(3)
print(vget())
print(vset(0))
print(veval(*[func1, func2]))
vdel()
print(vget())
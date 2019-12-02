counter_name = 0


def sort(element: str):
    return sorted(element)


def make_it_count(func):
    def new_func(var):
        global counter_name
        counter_name += 1
        return func(var)
    return new_func


# Test function
result = make_it_count(sort)
string = [5, 6, 1, 2, 4, 3, 7, 9, 8]
for i in range(5):
    print(result(string), counter_name)
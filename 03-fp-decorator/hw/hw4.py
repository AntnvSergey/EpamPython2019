def applydecorator(func):
    def wrap1(original):
        def wrap2(*args, **kwargs):
            return func(original, *args, **kwargs)
        return wrap2
    return wrap1


@applydecorator
def saymyname(f, *args, **kwargs):
  print('Name is', f.__name__)
  return f(*args, **kwargs)

# saymyname is now a decorator
@saymyname
def foo(*whatever):
    return whatever

print(*(foo(40, 2)))
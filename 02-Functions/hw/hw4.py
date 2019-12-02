import inspect


def function(*args, **kwargs):
    print(args, kwargs)


def modified_func(func, *fixated_args, **fixated_kwargs):

    def new_func(*fixed_args, **fixed_kwargs):
        """
        A func implementation of {name}
        with pre-applied arguments being:
        {fixated_args}, {fixated_kwargs}
        source_code:
        {source}
        """
        if not fixed_args and not fixed_kwargs:
            return function(*fixated_args, **fixated_kwargs)
        else:
            fixed_kwargs.update(fixated_kwargs)
            fixed_args += fixated_args
            return func(*fixed_args, **fixed_kwargs)
        
    source = inspect.getsource(new_func)
    doc = new_func.__doc__
    doc = doc.replace('{source}', source)
    func_name = func.__name__
    doc = doc.replace('{name}', func_name)
    doc = doc.replace('{fixated_args}', str(fixated_args))
    doc = doc.replace('{fixated_kwargs}', str(fixated_kwargs))
    new_func.__doc__ = inspect.cleandoc(doc)
    return new_func


# Test function
result = modified_func(function, *[1, 2], **{'a': 1})
result()
result(*[9, 8, 7], **{'c': 2, 'b': 3})
print(result.__doc__)

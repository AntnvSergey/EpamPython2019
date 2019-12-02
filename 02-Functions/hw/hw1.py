def letters_range(start='a', stop=None, step=1, **kwargs):
    abc = 'abcdefghijklmnopqrstuvwxyz'
    abc = [x for x in abc]
    for i in kwargs:
        letter = abc.index(i)
        abc[letter] = kwargs[i]
    if not stop:
        stop = abc.index(start)
        start = 0
    else:
        start = abc.index(start)
        stop = abc.index(stop)
    return abc[start:stop:step]


# Test function
print(letters_range('b', 'w', 2))
print(letters_range('g'))
print(letters_range('g', 'p'))
print(letters_range('g', 'p', **{'l': 7, 'o': 0}))
print(letters_range('p', 'g', -2))
print(letters_range('a'))
from functools import reduce

# Problem 9 : "Special Pythagorean triplet"
proble9 = [a * b * c for a in range(1, 334) for b in range(a, 500)
           for c in range(b, 501) if a + b + c == 1000 and a ** 2 + b ** 2 == c ** 2][0]

# Problem 6 : "Sum square difference"
problem6 = sum([x for x in range(1, 101)]) ** 2 - sum([x ** 2 for x in range(1, 101)])

# Problem 48 : "Self powers"
problem48 = (sum([k ** k for k in range(1000)])-1) % 10 ** 10

# Problem 40 : "Champernowne's constant"
i = [int(''.join(str(c) for c in range(10 ** 6))[10 ** k]) for k in range(7)]
problem40 = reduce(lambda x, y: x * y, i)

print(proble9)
print(problem6)
print(problem48)
print(problem40)
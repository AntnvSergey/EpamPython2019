def collatz_steps(n):
    if n == 1:
        return 0
    elif n % 2 == 0:
        return collatz_steps(n / 2) + 1
    else:
        return collatz_steps(3 * n + 1) + 1


assert collatz_steps(16) == 4
assert collatz_steps(12) == 9
assert collatz_steps(1000000) == 152
def is_armstrong(number):
    result = sum(map(lambda x: int(x) ** len(str(number)), str(number)))
    if result == number:
        return True
    else:
        return False


assert is_armstrong(153) == True, 'Число Армстронга'
assert is_armstrong(10) == False, 'Не число Армстронга'
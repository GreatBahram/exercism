def is_armstrong(number):
    power = len(str(number))
    return sum([int(digit) ** power for digit in str(number)]) == number

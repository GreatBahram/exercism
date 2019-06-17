class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num.replace(' ', '')

    def __repr__(self):
        return f'{type(self).__name__}({repr(self.card_num)})'

    def is_valid(self):
        if not self.card_num.isdigit() or len(self.card_num) < 2:
            return False

        card_num = list(map(int, self.card_num))

        points = (
            value if index % 2 == 0 else self.double(value)
            for index, value in enumerate(reversed(card_num))
        )
        return sum(points) % 10 == 0

    def double(self, number):
        number = number * 2
        if number > 9:
            number -= 9
        return number

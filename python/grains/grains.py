def validation(func):
    """a decorator for validating integer_number"""
    def wrap(*args, **kwargs):
        integer_number = args[0]
        if integer_number <= 0 or 65 <= integer_number:
            raise ValueError('Integer number should in range(0, 64)')
        return func(*args, **kwargs)
    return wrap

@validation
def on_square(integer_number):
    return pow(2, integer_number - 1)


@validation
def total_after(integer_number):
    return pow(2, integer_number) - 1

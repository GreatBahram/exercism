def is_equilateral(sides):
    has_three_same_sides = len(set(sides)) == 1
    if  has_three_same_sides and is_triangle(sides):
        return True
    return False


def is_isosceles(sides):
    has_two_equal_sides = len(set(sides)) <= 2 # at least
    if has_two_equal_sides and is_triangle(sides):
        return True
    return False


def is_scalene(sides):
    has_three_different_sides = len(set(sides)) == 3
    if has_three_different_sides and is_triangle(sides):
        return True
    return False


def is_triangle(sides):
    """Return True if everything is fine."""
    smallest, medium, larget = sorted(sides)
    return smallest + medium >= larget and all(side > 0 for side in sides)

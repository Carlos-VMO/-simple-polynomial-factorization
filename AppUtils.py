import cmath, json


def find_dividers(num_):
    dividers = []
    for_range = [-num_, num_] if num_ > 0 else [num_, -num_]
    for possible_divider in range(for_range[0], for_range[1] + 1):
        if possible_divider != 0 and num_ % possible_divider == 0:
            dividers.append(possible_divider)
    return dividers


def get_zeros_from_quadratic_equation(a, b, c):
    return [(-b + cmath.sqrt((b * b) - (4 * a * c))) / (2 * a), (-b - cmath.sqrt((b * b) - (4 * a * c))) / (2 * a)]


def greather_or_equal_than_zero(item):
    return item >= 0


def substract(item, num):
    return item - num


def print_object(obj_):
    print(json.dumps(obj_.__dict__))

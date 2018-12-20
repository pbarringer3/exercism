from math import sqrt, floor


def prime_factors(natural_number):
    if natural_number == 1:
        return []

    for i in range(2, floor(sqrt(natural_number)) + 1):
        if natural_number % i == 0:
            return [i] + prime_factors(natural_number / i)

    return [natural_number]

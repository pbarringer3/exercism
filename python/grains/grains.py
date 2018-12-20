def on_square(n):
    if n < 1 or n > 64:
        raise ValueError("The input is out of bounds [1,64]")
    return 2 ** (n - 1)


def total_after(n):
    if n < 1 or n > 64:
        raise ValueError("The input is out of bounds [1,64]")
    return 2 ** n - 1

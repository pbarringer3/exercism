def is_armstrong(number):
    sum = 0
    length = len(str(number))
    for i in range(length):
        sum += ((number // 10 ** i) % 10) ** length

    return sum == number

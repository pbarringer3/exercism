def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("The two strings must be the same length")

    total = 0
    for i in range(len(strand_a)):
        if strand_a[i] != strand_b[i]:
            total += 1

    return total

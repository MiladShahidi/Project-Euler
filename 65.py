def f(c, fraction):
    return [fraction[1], c * fraction[1] + fraction[0]]


if __name__ == '__main__':
    K = 99
    a_seq = []
    for i in range(1, 35):
        a_seq.extend([1, 2 * i, 1])

    a_seq = a_seq[:K]

    # I use a list with 2 elements to represent the fraction as frac[0] / frac[1]
    frac = f(c=a_seq[-2], fraction=[1, a_seq[-1]])

    for a in a_seq[:-2][::-1]:
        frac = f(c=a, fraction=frac)

    numerator = 2 * frac[1] + frac[0]
    print(sum([int(x) for x in str(numerator)]))

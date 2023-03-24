from itertools import product


def has_3_digit_divisor_pair(x):
    for i in range(100, 1000):
        if (x % i == 0) and (100 <= (x / i) <= 999):
            return i, x // i

    return None


if __name__ == '__main__':
    revese_digits = list(range(10))[::-1]
    # This is equivalent to 3 nested for loops where d3 is the innermost counter
    for d1, d2, d3 in product(revese_digits, revese_digits, revese_digits):
        x = int(f'{d1}{d2}{d3}{d3}{d2}{d1}')
        if x >= 100000:
            divisors = has_3_digit_divisor_pair(x)
            if divisors is not None:
                print(f'{x} = {divisors[0]} * {divisors[1]}')
                print('Answer:', x)
                exit()

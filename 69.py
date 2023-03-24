def divisors(x):
    res = []
    for i in range(2, x//2 + 1):
        if x % i == 0:
            res.append(i)

    res += [x]
    return set(res)


def are_rel_prime(x, y):
    return len(divisors(x).intersection(divisors(y))) == 0


def rel_prime_count(x):
    res = []
    for i in range(1, x):
        print(i)
        if are_rel_prime(i, x):
            res.append(i)
    return len(res)


def totient(x):
    return x / rel_prime_count(x)


def primes_up_to(max_n):
    def is_prime(n):
        for i in range(2, n):
            if (n % i) == 0:
                return False
        return True

    res = []
    for i in range(2, max_n + 1):
        if is_prime(i):
            res.append(i)

    return res


if __name__ == '__main__':
    # I had a hunch that the more prime factors a number has the higher its
    # n / phi(n). And the smaller these primes are the better. For example:
    # 2 * 3 * 5 has a higher n/phi(n) than 2 * 3 * 7. Because 5 eliminates
    # more numbers from phi(n) than 7.
    # So, I just multiply primes as long as the result is < 1000000 to get
    # the largest such number.
    # And turns out my hunch is correct!

    primes = primes_up_to(100)
    x = 1
    for p in primes:
        if x * p < 1000000:
            x *= p
        else:
            break

    # print(f'n/phi(n) for {x}: {totient(x)}')
    print('Answer:', x)

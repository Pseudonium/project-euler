import itertools
import math

# Problem 1

answer_1 = sum(num for num in range(1000) if (num % 3 == 0 or num % 5 == 0))

# Problem 2


def fibonacci_2(n):
    if n == 0 or n == 1:
        return 1
    previous, current = 0, 1
    for count in range(n):
        previous, current = current, current + previous
    return current


flag_2 = False
if flag_2:
    n_2 = 0
    f_2 = fibonacci_2(n_2)
    acc_2 = 0
    while f_2 < 4000000:
        if f_2 % 2 == 0:
            acc_2 += f_2
        n_2 += 1
        f_2 = fibonacci_2(n_2)
    answer_2 = acc_2

# Problem 3


def primes_less_than(n):
    primes = [2]
    for num in range(3, n):
        if all(num % p != 0 for p in primes):
            primes.append(num)
    return primes


def iter_primes_less_than(n):
    primes = []
    for num in range(2, n):
        if all(num % p != 0 for p in primes):
            primes.append(num)
            yield num


def factor(n):
    current = n
    factors = []
    primes = iter_primes_less_than(math.ceil(math.sqrt(n)))
    for p in primes:
        while current % p == 0:
            factors.append(p)
            current = current // p
        if current == 1:
            break
    if current > 1:
        factors.append(current)
    if not factors:
        return [n]
    return factors


flag_3 = False
if flag_3:
    answer_3 = factor(600851475143)[-1]

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

# Problem 4


def is_palindrome(number):
    """Check whether or not the number is a palindrome."""
    digits = str(number)
    return digits == "".join(reversed(digits))


flag_4 = False
if flag_4:
    products_4 = [
        x*y
        for x in range(100, 1000)
        for y in range(100, 1000)
        if is_palindrome(x*y)
    ]
    answer_4 = max(products_4)
    print(answer_4)


# Problem 5

def greatest_common_divisor(a, b):
    """Return the gcd of the two numbers."""
    while a != b and b > 1:
        # This uses the Euclidean algorithm for finding gcd(a,b)
        c = max(a, b)
        d = min(a, b)
        a, b = d, c % d
        # This should ensure b is always the smaller of the two numbers.
        if b == 0:
            # This implies d evenly divides c,
            # meaning d is the greatest_common_divisor
            return d
    return b


def lowest_common_multiple(*numbers):
    current = 1
    for num in numbers:
        # The idea is to compute the lcm of current and num
        current *= num // greatest_common_divisor(current, num)
    return current


flag_5 = False
if flag_5:
    answer_5 = lowest_common_multiple(*range(1, 21))
    print(answer_5)

# Problem 6

flag_6 = False
if flag_6:
    answer_6 = sum(range(101))**2 - sum(x**2 for x in range(101))
    print(answer_6)

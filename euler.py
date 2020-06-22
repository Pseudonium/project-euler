import itertools
import functools
import math
import operator

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
    """Return a list of primes less than the number n."""
    primes = [2]
    max_index = 0
    max_testing = 2**2
    # Max_index indicates the index of the maximum prime we need to test up to
    # Max_testing indicates the maximum n before we need to increase The
    # maximum prime we need to test up to
    for num in range(3, n):
        if num >= max_testing:
            max_index += 1
            max_testing = primes[max_index]**2
            # The reason for the squared is that, to test if a number is
            # prime, you only need to check divisibility by primes up to
            # the square root of the number - conversely, knowing all the
            # primes up to p allows you to test all numbers up to p^2
        if all(num % p != 0 for p in primes[:max_index]):
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
    primes = primes_less_than(math.ceil(math.sqrt(n)))
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

# Problem 7


def n_primes(n):
    """Get a list of n primes"""
    primes = []
    current = 2
    while len(primes) < n:
        if all(current % p != 0 for p in primes):
            primes.append(current)
        current += 1
    return primes


flag_7 = False
if flag_7:
    answer_7 = n_primes(10001)[-1]
    print(answer_7)

# Problem 8

NUMBER_8 = int("""73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450""".replace("\n", ""))


def string_product(digits):
    """Return the product of the digits in digits."""
    current = 1
    for d in digits:
        current *= int(d)
    return current


flag_8 = False
if flag_8:
    num = str(NUMBER_8)
    max_found = 1
    for current in range(len(num)):
        slice = num[current:current + 13]
        max_found = max(max_found, string_product(slice))
    answer_8 = max_found
    print(answer_8)


# Problem 9

# Solved using maths, by hand. See zk for solution.

flag_9 = False
if flag_9:
    answer_9 = 31_875_000
    print(answer_9)


# Problem 10

flag_10 = False
if flag_10:
    answer_10 = sum(primes_less_than(2_000_000))
    print(answer_10)

# Problem 11

GRID_11 = """08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48"""

GRID_11a = [line.split(" ") for line in GRID_11.split("\n")]

for line in GRID_11a:
    for i, item in enumerate(line):
        line[i] = int(item)


def ELEVEN_max_horizontal(grid):
    """Get the max product of 4 adjacent numbers in the same row in grid."""
    current = 1
    for line in grid:
        for i in range(len(line)):
            current = max(
                current, functools.reduce(operator.mul, line[i:i+4])
            )
    return current


def ELEVEN_max_vertical(grid):
    """Get the max product of 4 adjacent numbers in same column in grid."""
    transposed_grid = list(zip(*grid))
    return ELEVEN_max_horizontal(transposed_grid)


def ELEVEN_max_parallel(grid):
    """
    Get the max product of 4 adjacent numbers parallel to gridlines.

    I.e. all in either the same column or row in grid.
    """
    return max(ELEVEN_max_horizontal(grid), ELEVEN_max_vertical(grid))


def ELEVEN_max_diagonal(grid):
    """Get the max product of 4 diagonally adjacent numbers."""
    # For ones going right then down
    shifted_grid_1 = [
        line[i:] + line[:i]
        for i, line in enumerate(grid)
    ][:len(grid)-4]
    # For ones going left then down
    reversed_grid = [
        list(reversed(line))
        for line in grid
    ]
    shifted_grid_2 = [
        line[i:] + line[:i]
        for i, line in enumerate(reversed_grid)
    ][:len(grid)-4]
    return max(
        ELEVEN_max_vertical(shifted_grid_1), ELEVEN_max_vertical(shifted_grid_2)
    )


def ELEVEN_max(grid):
    """Get the max product of 4 adjacent numbers in grid."""
    return max(ELEVEN_max_parallel(grid), ELEVEN_max_diagonal(grid))


flag_11 = False
if flag_11:
    answer_11 = ELEVEN_max(GRID_11a)
    print(answer_11)


# Problem 12

def prime_factorisation(n):
    """Get the prime factorisation of n.

    Returns a list of tuples, where the first element is the prime,
    and the second element is the power to which the prime is raised.
    """
    factors = factor(n)
    current_prime = factors[0]
    current_exponent = 0
    factorisation = []
    for num in factors:
        if num != current_prime:
            factorisation.append((current_prime, current_exponent))
            current_prime, current_exponent = num, 0
        current_exponent += 1
    factorisation.append((current_prime, current_exponent))
    return factorisation


def number_of_divisors(n):
    """Return the number of divisors of n, including 1 and n."""
    divisors = 1
    for prime, power in prime_factorisation(n):
        # For any factor, can choose any number from 0 to power for what
        # power of prime you should use.
        # E.g. if it was 2^2, can choose either 2^0, 2^1 or 2^2
        # So, the number of choices is power + 1
        divisors *= power + 1
    return divisors


def factorise_product(a, b):
    """Factorise n = ab, with a, b integers."""
    a_dict = {prime: power for prime, power in prime_factorisation(a)}
    b_dict = {prime: power for prime, power in prime_factorisation(b)}
    n_dict = {}
    for prime, power in a_dict.items():
        n_dict[prime] = power
    for prime, power in b_dict.items():
        if prime in n_dict:
            n_dict[prime] += power
        else:
            n_dict[prime] = power
    return sorted(n_dict.items())


print(factorise_product(1500, 3001))


flag_12 = False
if flag_12:
    start = 1
    while number_of_divisors(start*(start+1)//2) <= 500:
        print(start, start*(start+1)//2)
        start += 1
    answer_12 = start*(start+1)//2
    print(answer_12)

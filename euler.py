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

import itertools
import functools
import math
import operator
import collections

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


def number_of_divisors_from_factorisation(factorisation):
    """Return number of divisors of number with the given factorisation."""
    divisors = 1
    for prime, power in factorisation:
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


flag_12 = False
if flag_12:
    current = 1
    k = 1
    while k <= 500:
        current += 1
        if current % 2 == 0:
            a, b = current // 2, current + 1
        else:
            a, b = (current + 1)//2, current
        k = number_of_divisors_from_factorisation(factorise_product(a, b))
    answer_12 = current*(current+1)//2
    print(answer_12)


# Problem 13

NUMBERS_13 = """37107287533902102798797998220837590246510135740250
46376937677490009712648124896970078050417018260538
74324986199524741059474233309513058123726617309629
91942213363574161572522430563301811072406154908250
23067588207539346171171980310421047513778063246676
89261670696623633820136378418383684178734361726757
28112879812849979408065481931592621691275889832738
44274228917432520321923589422876796487670272189318
47451445736001306439091167216856844588711603153276
70386486105843025439939619828917593665686757934951
62176457141856560629502157223196586755079324193331
64906352462741904929101432445813822663347944758178
92575867718337217661963751590579239728245598838407
58203565325359399008402633568948830189458628227828
80181199384826282014278194139940567587151170094390
35398664372827112653829987240784473053190104293586
86515506006295864861532075273371959191420517255829
71693888707715466499115593487603532921714970056938
54370070576826684624621495650076471787294438377604
53282654108756828443191190634694037855217779295145
36123272525000296071075082563815656710885258350721
45876576172410976447339110607218265236877223636045
17423706905851860660448207621209813287860733969412
81142660418086830619328460811191061556940512689692
51934325451728388641918047049293215058642563049483
62467221648435076201727918039944693004732956340691
15732444386908125794514089057706229429197107928209
55037687525678773091862540744969844508330393682126
18336384825330154686196124348767681297534375946515
80386287592878490201521685554828717201219257766954
78182833757993103614740356856449095527097864797581
16726320100436897842553539920931837441497806860984
48403098129077791799088218795327364475675590848030
87086987551392711854517078544161852424320693150332
59959406895756536782107074926966537676326235447210
69793950679652694742597709739166693763042633987085
41052684708299085211399427365734116182760315001271
65378607361501080857009149939512557028198746004375
35829035317434717326932123578154982629742552737307
94953759765105305946966067683156574377167401875275
88902802571733229619176668713819931811048770190271
25267680276078003013678680992525463401061632866526
36270218540497705585629946580636237993140746255962
24074486908231174977792365466257246923322810917141
91430288197103288597806669760892938638285025333403
34413065578016127815921815005561868836468420090470
23053081172816430487623791969842487255036638784583
11487696932154902810424020138335124462181441773470
63783299490636259666498587618221225225512486764533
67720186971698544312419572409913959008952310058822
95548255300263520781532296796249481641953868218774
76085327132285723110424803456124867697064507995236
37774242535411291684276865538926205024910326572967
23701913275725675285653248258265463092207058596522
29798860272258331913126375147341994889534765745501
18495701454879288984856827726077713721403798879715
38298203783031473527721580348144513491373226651381
34829543829199918180278916522431027392251122869539
40957953066405232632538044100059654939159879593635
29746152185502371307642255121183693803580388584903
41698116222072977186158236678424689157993532961922
62467957194401269043877107275048102390895523597457
23189706772547915061505504953922979530901129967519
86188088225875314529584099251203829009407770775672
11306739708304724483816533873502340845647058077308
82959174767140363198008187129011875491310547126581
97623331044818386269515456334926366572897563400500
42846280183517070527831839425882145521227251250327
55121603546981200581762165212827652751691296897789
32238195734329339946437501907836945765883352399886
75506164965184775180738168837861091527357929701337
62177842752192623401942399639168044983993173312731
32924185707147349566916674687634660915035914677504
99518671430235219628894890102423325116913619626622
73267460800591547471830798392868535206946944540724
76841822524674417161514036427982273348055556214818
97142617910342598647204516893989422179826088076852
87783646182799346313767754307809363333018982642090
10848802521674670883215120185883543223812876952786
71329612474782464538636993009049310363619763878039
62184073572399794223406235393808339651327408011116
66627891981488087797941876876144230030984490851411
60661826293682836764744779239180335110989069790714
85786944089552990653640447425576083659976645795096
66024396409905389607120198219976047599490197230297
64913982680032973156037120041377903785566085089252
16730939319872750275468906903707539413042652315011
94809377245048795150954100921645863754710598436791
78639167021187492431995700641917969777599028300699
15368713711936614952811305876380278410754449733078
40789923115535562561142322423255033685442488917353
44889911501440648020369068063960672322193204149535
41503128880339536053299340368006977710650566631954
81234880673210146739058568557934581403627822703280
82616570773948327592232845941706525094512325230608
22918802058777319719839450180888072429661980811197
77158542502016545090413245809786882778948721859617
72107838435069186155435662884062257473692284509516
20849603980134001723930671666823555245252804609722
53503534226472524250874054075591789781264330331690""".split("\n")

NUMBERS_13 = [int(x) for x in NUMBERS_13]
flag_13 = False
if flag_13:
    answer_13 = str(sum(NUMBERS_13))[:10]
    print(answer_13)

# Problem 14


def collatz_chain_length(n, cache={1: 1}):
    """Get the length of the collatz chain starting from n."""
    if n == 1:
        return 1
    original = n
    result = 0
    while n not in cache:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3*n + 1
        result += 1
    cache[original] = result + cache[n]
    return cache[original]


flag_14 = False
if flag_14:
    answer_14 = max(
        (collatz_chain_length(i), i)
        for i in range(1, 1_000_000)
    )[1]
    print(answer_14)

# Problem 15
# See zk for full solution

flag_15 = False
if flag_15:
    answer_15 = math.comb(40, 20)
    print(answer_15)


# Problem 16

flag_16 = False
if flag_16:
    answer_16 = sum(int(d) for d in str(2**1_000))
    print(answer_16)


# Problem 17

UNITS_17 = [
    "zero", "one", "two",
    "three", "four", "five",
    "six", "seven", "eight", "nine"
]

TENS_17 = [
    "ten", "twenty", "thirty", "forty",
    "fifty", "sixty", "seventy", "eighty", "ninety"
]

TEENS_17 = [
    "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
    "seventeen", "eighteen", "nineteen"
]


def number_to_words(n):
    """Converts n to a word representation. 1 <= n <= 999"""
    result = ""
    hundreds = n // 100
    n -= 100*hundreds
    tens = n // 10
    n -= 10*tens
    units = n
    if hundreds > 0:
        result += UNITS_17[hundreds] + "hundred"
        if tens == 0 and units == 0:
            return result
        result += "and"
    num = 10*tens + units
    if num < 10:
        result += UNITS_17[units]
        return result
    elif 11 <= num <= 19:
        result += TEENS_17[num-11]
        return result
    else:
        result += TENS_17[tens-1]
        if units != 0:
            result += UNITS_17[units]
        return result


flag_17 = False
if flag_17:
    answer_17 = sum(len(number_to_words(i)) for i in range(1, 1000))
    answer_17 += len("onethousand")
    print(answer_17)


# Problem 18

TRIANGLE_18 = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23""".split("\n")

TRIANGLE_18 = [row.split(" ") for row in list(TRIANGLE_18)]
for i, row in enumerate(TRIANGLE_18):
    TRIANGLE_18[i] = tuple([int(num) for num in list(row)])
TRIANGLE_18 = tuple(TRIANGLE_18)


@functools.lru_cache(maxsize=None)
def triangle_cell_max_value(row_i, column_i, triangle):
    """
    Return the maximum accumulated value of a route through this cell.

    More specifically, among all possible routes from the top of the triangle
    to this cell, this function returns the maximum accumulated value up to
    this point in the route.
    """
    if row_i < 0 or row_i >= len(triangle):
        return 0
    row = triangle[row_i]
    if column_i < 0 or column_i >= len(row):
        return 0
    cell_value = row[column_i]
    # The way the triangle is set up, you can reach (row_i, column_i) from
    # the previous row by either (row_i - 1, column_i - 1) (going right)
    # or (row_i - 1, column_i) (going left)
    # So, the maximum value is the maximum of either of those two higher
    # values, plus the value of this cell
    return max(
        triangle_cell_max_value(row_i - 1, column_i - 1, triangle),
        triangle_cell_max_value(row_i - 1, column_i, triangle)
    ) + cell_value


def triangle_max_route_value(triangle):
    """Use above function to determine maximum achievable value.

    From top to bottom.
    """
    final_row, final_row_i = triangle[-1], len(triangle) - 1
    return max(
        triangle_cell_max_value(final_row_i, col_i, triangle)
        for col_i in range(len(final_row))
    )


flag_18 = False
if flag_18:
    answer_18 = triangle_max_route_value(TRIANGLE_18)
    print(answer_18)


# Problem 19

def is_leap_year(n):
    """Determine whether year n is a leap year."""
    if n % 4 != 0:
        return False
    if n % 100 == 0:
        return n % 400 == 0
    else:
        return True


def month_length(month, year):
    """Determine the length of month n in year.

    0 is January, 11 is December.
    """
    THIRTY = [3, 5, 8, 10]
    if month in THIRTY:
        return 30
    elif month == 1:
        # February
        return 28 + is_leap_year(year)
    else:
        return 31


flag_19 = False
if flag_19:
    DAY = 1  # Tuesday
    MONTH = 0  # January
    YEAR = 1901  # 1 January 1901
    count = 0
    while YEAR < 2001:
        DAY += month_length(MONTH, YEAR)
        DAY = DAY % 7
        if DAY == 6:
            # So 1st day of month is Sunday
            count += 1
        MONTH += 1
        if MONTH == 12:
            # New year
            MONTH = 0
            YEAR += 1
    answer_19 = count
    print(answer_19)


# Problem 20

flag_20 = False
if flag_20:
    answer_20 = sum(int(d) for d in str(math.factorial(100)))
    print(answer_20)

# Problem 21


def powerset(iterable):
    """Return the powerset of iterable."""
    s = list(iterable)
    return itertools.chain.from_iterable(
        itertools.combinations(s, r) for r in range(len(s)+1)
    )


def divisors(n):
    """Return a list of all divisors of n, sorted."""
    return sorted({math.prod(subset) for subset in powerset(factor(n))})


def proper_divisors(n):
    """Return a sorted list of all proper divisors of n."""
    divisors_list = divisors(n)
    divisors_list.pop()
    return divisors_list


def is_amicable(n, yes_cache=set(), no_cache=set()):
    """Determine whether n is amicable."""
    other = sum(proper_divisors(n))
    if n in yes_cache:
        return True
    elif n in no_cache:
        return False
    elif sum(proper_divisors(other)) == n and other != n:
        yes_cache.add(n)
        yes_cache.add(other)
        return True
    else:
        no_cache.add(n)
        no_cache.add(other)
        return False


flag_21 = False
if flag_21:
    answer_21 = sum(i for i in range(2, 10000) if is_amicable(i))
    print(answer_21)


# Problem 22

ALPHABET = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
    "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
]


def name_value(name):
    """Return alphabetical value of name."""
    return sum(ALPHABET.index(char) for char in name.upper()) + len(name)


flag_22 = False
if flag_22:
    with open("p022_names.txt") as f:
        names = f.read()
    names = names.split(",")
    for i, item in enumerate(names):
        names[i] = item.replace('"', '')
    names.sort()
    answer_22 = sum((i+1)*name_value(name) for i, name in enumerate(names))
    print(answer_22)


# Problem 23

def is_abundant(n):
    """Determine whether n is an abundant number."""
    return sum(proper_divisors(n)) > n


flag_23 = False
if flag_23:
    abundants = [n for n in range(2, 28124) if is_abundant(n)]
    i = 0
    j = 0
    possible_sum = 0
    possible_sums = set()
    while 2*abundants[i] <= 28123:
        possible_sum = abundants[i] + abundants[j]
        if possible_sum <= 28123:
            possible_sums.add(possible_sum)
            j += 1
        else:
            i += 1
            j = i
    answer_23 = sum(i for i in range(28124) if i not in possible_sums)
    print(answer_23)


# Problem 24

def consume(iterator, n=None):
    """Advance the iterator n-steps ahead. If n is None, consume entirely."""
    # Use functions that consume iterators at C speed.
    if n is None:
        # feed the entire iterator into a zero-length deque
        collections.deque(iterator, maxlen=0)
    else:
        # advance to the empty slice starting at position n
        next(itertools.islice(iterator, n, n), None)


flag_24 = False
if flag_24:
    combs = itertools.permutations(range(10), 10)
    consume(combs, n=999_999)
    answer_24 = next(combs)
    print(answer_24)

# Problem 25


def fibonacci_25(n, cache=dict()):
    """Return the nth fibonacci number."""
    if n == 0 or n == 1:
        return n
    elif n in cache:
        return cache[n]
    else:
        result = fibonacci_25(n - 1) + fibonacci_25(n - 2)
        cache[n] = result
        return result


flag_25 = False
if flag_25:
    index = 0
    while len(str(fibonacci_25(index))) < 1000:
        index += 1
    answer_25 = index
    print(answer_25)


# Problem 26

def reciprocal_to_decimal_repr(n):
    """Return 1/n as a repeating decimal (string output)."""
    digits = []
    remainders = []
    remainder = 1
    digit = 0
    while remainder not in remainders:
        digits.append(digit)
        remainders.append(remainder)
        digit, remainder = remainder*10 // n, remainder*10 % n
        #print(digit, remainder)
    digits.append(digit)
    remainders.append(remainder)
    #remainders.insert(0, 1)
    return [digits, remainders]


def reciprocal_repeat_length(n):
    """Return length of repeating block of n."""
    representation = reciprocal_to_decimal_repr(n)
    remainders = representation[1]
    last_remainder = remainders[-1]
    duplicate_index = remainders.index(last_remainder)
    return len(remainders) - duplicate_index - 1


flag_26 = False
if flag_26:
    answer_26 = max(
        (reciprocal_repeat_length(i), i) for i in range(1, 1000)
    )[1]
    print(answer_26)

# Problem 27


def is_prime(n):
    """Check if n is prime."""
    return all(n % p != 0 for p in primes_less_than(math.ceil(math.sqrt(n))))


flag_27 = False
if flag_27:
    primes_27 = primes_less_than(1000)
    max_count = 0
    max_ab = 0
    for b in primes_27:
        for a in range(math.ceil(-2*math.sqrt(b)), 1000):
            n = 0
            while is_prime(n**2 + a*n + b):
                n += 1
            max_count = max(max_count, n)
            if max_count == n:
                max_ab = a * b
    answer_27 = max_ab
    print(answer_27)


# Problem 28

def sum_spiral_28(n):
    """Return sum of diagnals clockwise 2n - 1 spiral."""
    if n == 1:
        return 1
    result = 0
    result += sum_spiral_28(n - 1)
    num = (2*n - 3)**2
    for i in range(4):
        num += 2*(n-1)
        result += num
    return result


flag_28 = False
if flag_28:
    answer_28 = sum_spiral_28(501)
    print(answer_28)


# Problem 29

flag_29 = False
if flag_29:
    numbers = set()
    for a in range(2, 101):
        for b in range(2, 101):
            numbers.add(a**b)
    answer_29 = len(numbers)
    print(answer_29)

# TODO: Define table_volume variable
TABLE_TOP_LENGTH = 63.0
TABLE_TOP_WIDTH = 23.6
TABLE_TOP_HEIGHT = 1.5

TABLE_LEG_BASE_RADIUS = 0.8
TABLE_LEG_HEIGHT = 29.5

from math import pi
# TODO: Define box_vol, cylinder_vol, table_vol functions
def cylinder_vol(base_radius, height):
    return pi * base_radius * base_radius * height

def box_vol(length, width, height):
    return length * width * height

def table_vol(tt_length, tt_width, tt_height, leg_base_rad, leg_height):
    return box_vol(tt_length, tt_width, tt_height) + 4 * cylinder_vol(leg_base_rad, leg_height)

table_volume = table_vol(TABLE_TOP_LENGTH, TABLE_TOP_WIDTH, TABLE_TOP_HEIGHT, TABLE_LEG_BASE_RADIUS, TABLE_LEG_HEIGHT)

########################################################################################################################

# TODO: Define pond_1, pond_2, pond_3, pond_4, pond_5, total_population variables
# TODO: Define variables
INIT_POP_POND_1 = 10
INIT_POP_POND_2 = 25
INIT_POP_POND_3 = 12
INIT_POP_POND_4 = 30
INIT_POP_POND_5 = 4

YEARLY_GROWTH_POND_1 = 2.0
YEARLY_GROWTH_POND_2 = 1.5
YEARLY_GROWTH_POND_3 = 1.8
YEARLY_GROWTH_POND_4 = 2.2
YEARLY_GROWTH_POND_5 = 1.5

YEARS = 3

# TODO: Define pop_after_n_years function
def pop_after_n_years(init_pop, yearly_growth, years):
    return init_pop * (yearly_growth ** years)

pond_1 = pop_after_n_years(INIT_POP_POND_1, YEARLY_GROWTH_POND_1, YEARS)
pond_2 = pop_after_n_years(INIT_POP_POND_2, YEARLY_GROWTH_POND_2, YEARS)
pond_3 = pop_after_n_years(INIT_POP_POND_3, YEARLY_GROWTH_POND_3, YEARS)
pond_4 = pop_after_n_years(INIT_POP_POND_4, YEARLY_GROWTH_POND_4, YEARS)
pond_5 = pop_after_n_years(INIT_POP_POND_5, YEARLY_GROWTH_POND_5, YEARS)

total_population = pond_1 + pond_2 + pond_3 + pond_4 + pond_5

########################################################################################################################

# TODO: Define variables
INITIAL_PRINCIPAL = 10000.0
YEARS = 5
ACCOUNT_RATE_1 = 0.027
ACCOUNT_RATE_2 = 0.0268
ACCOUNT_RATE_3 = 0.0266
ACCOUNT_CMP_FREQ_1 = 1
ACCOUNT_CMP_FREQ_2 = 12
ACCOUNT_CMP_FREQ_3 = 365

# TODO: Define amount_after_n_years function
def amount_after_n_years(init_principal, acc_rate, acc_cmp_freq, years):
    return init_principal * (1 + (acc_rate / acc_cmp_freq)) ** (years * acc_cmp_freq)


c1 = 10000.0 * (1 + 0.027) ** 5
c2 = 10000.0 * (1 + 0.0268 / 12) ** (5 * 12)
c3 = 10000.0 * (1 + 0.0266 / 365) ** (5 * 365)

# TODO: Define amount_1, amount_2, amount_3 variables
amount_1 = amount_after_n_years(INITIAL_PRINCIPAL, ACCOUNT_RATE_1, ACCOUNT_CMP_FREQ_1, YEARS)
amount_2 = amount_after_n_years(INITIAL_PRINCIPAL, ACCOUNT_RATE_2, ACCOUNT_CMP_FREQ_2, YEARS)
amount_3 = amount_after_n_years(INITIAL_PRINCIPAL, ACCOUNT_RATE_3, ACCOUNT_CMP_FREQ_3, YEARS)

# These print states will give more insight into the final values of your account holdings.
# print(c1, c2, c3)
# print(max(c1, c2, c3))
print(f"Account option 1 will hold ${amount_1:,.2f}.")
print(f"Account option 2 will hold ${amount_2:,.2f}.")
print(f"Account option 3 will hold ${amount_3:,.2f}.")
print(f"The maximum amount that can be reached is "
        f"${max(amount_1, amount_2, amount_3):,.2f}.")

########################################################################################################################

def fib(n):
    """
    The function returns the number in Fibonacci sequence that is at the
    position provided by the argument. If the argument is a negative integer or
    some other type the function returns None.
    Examples:
    0 -> 0
    1 -> 1
    2 -> 1  (0 + 1)
    3 -> 2  (1 + 1)
    4 -> 3  (1 + 2)
    5 -> 5  (2 + 3)
    6 -> 8  (3 + 5)
    https://en.wikipedia.org/wiki/Fibonacci_number
    :param n: integer
    :return: integer
    """
    # Check if the input is less than 0 or not an integer.
    # Return None if any of the above is True.
    if n < 0 or type(n) != int:
        return None
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    v1, v2, v3 = 1, 1, 0
    for rec in bin(n)[3:]:
        calc = v2*v2
        v1, v2, v3 = v1 * v1 +calc, (v1 + v3) * v2, calc + v3 * v3
        if rec == '1':
            v1, v2, v3 = v1 + v2, v1, v2
    return v2

def test_fib():
    """
    This is a suite of tests for the fib function.
    :return:
    """
    assert fib(1) == 1
    # TODO 1: PLACE YOUR CODE HERE
    assert fib(2) == 1
    assert fib(3) == 2
    assert fib(4) == 3
    assert fib(5) == 5
    assert fib(6) == 8

########################################################################################################################

def is_prime(n):
    """
    The function returns True if the provided argument is an integer that is
    a prime number. It returns False otherwise.
    https://en.wikipedia.org/wiki/Prime_number
    :param n: integer
    :return: boolean
    """
    # If a given integer is greater than 1
    if n > 1 and type(n) == int:
        # Iterate from 2 to n / 2
        for i in range(2, int(n/2) + 1):
            # If num is divisible by any number between
            # 2 and n / 2, it is not prime.
            if n % i == 0:
                return False
        return True
    return False

def test_is_prime():
    """
    This is a suite of tests for the is_prime function.
    :return:
    """
    assert is_prime(3) == True
    # TODO 2: PLACE YOUR CODE HERE
    assert is_prime(4) == False
    assert is_prime(5) == True
    assert is_prime(6) == False
    assert is_prime(7) == True
    assert is_prime(8) == False

########################################################################################################################

def merge_sort_in_place(lst):
    """
    The function sorts the list in place using the merge sort algorithm.
    https://en.wikipedia.org/wiki/In-place_algorithm
    https://en.wikipedia.org/wiki/Merge_sort
    :param lst: list
    :return: None
    """
    if len(lst) > 1:
        # Finding the mid of the list
        mid = len(lst) // 2
        # Left half
        left = lst[:mid]
        # Right half
        right = lst[mid:]
        # Recursive call to sort the left half
        merge_sort_in_place(left)
        # Recursive call to sort the right half
        merge_sort_in_place(right)
        # Two iterators for traversing the two halves
        i = 0
        j = 0
        # Iterator for the main list
        k = 0
        # Copy data to temp lists left and right
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                # The value from the left half has been used
                lst[k] = left[i]
                # Move the iterator forward
                i += 1
            else:
                lst[k] = right[j]
                j += 1
            # Move to the next slot
            k += 1
        # Checking if any element was left
        while i < len(left):
            lst[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            lst[k] = right[j]
            j += 1
            k += 1


# Lists to use for binarySearch() and mergeSort() tests
lst1 = [1, 5, 2, 6, 2]
lst2 = [9, 8, 7, 6.5]
lst3 = [5, -3, 7, -3]
lst4 = [1]
lst5 = []
lst6 = ['hello', 'a', 'the']

def test_merge_sort_in_place():
    """
    This is a suite of tests for the merge_sort_in_place function.
    :return:
    """
    # The below lines apply the `merge_sort_in_place` function to the `lst_*`
    # lists. After the application the lists should be sorted.
    merge_sort_in_place(lst1)
    merge_sort_in_place(lst2)
    merge_sort_in_place(lst3)
    merge_sort_in_place(lst4)
    merge_sort_in_place(lst5)
    merge_sort_in_place(lst6)
    
    assert lst1 == [1, 2, 2, 5, 6]
    # Below, please, write tests based on `lst2` - `lst6`. A sample test for
    # `lst1 is provided above.`
    # TODO 3: PLACE YOUR CODE HERE
    assert lst2 == [6.5, 7, 8, 9]
    assert lst3 == [-3, -3, 5, 7]
    assert lst4 == [1]
    assert lst5 == []
    assert lst6 == ['a', 'hello', 'the']

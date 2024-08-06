def time_color(time):
    if time > 10:
        return "black"
    elif time > 5:
        return "orange"
    else:
        return "red"

# Assert statements to check validity of code
# assert time_color(25) == 'black'
# assert time_color(10) == 'orange'
# assert time_color(6) == 'orange'
# assert time_color(5) == 'red'
# assert time_color(3) == 'red'
# assert time_color(-100) == 'red'

########################################################################################################################

COLORS = ["red", "orange", "blue", "green", "yellow", "pink", "black", "gray",
          "purple"]

def is_correct(bg_color, text_color, text, input_color, mode):
    if mode == 'Background Color':
        return input_color == bg_color
    elif mode == 'Text Color':
        return input_color == text_color
    elif mode == 'Text':
        return input_color == text
    else:
        return input_color in COLORS and input_color not in [bg_color, text_color, text]

# Assert statements to check validity of your code
# assert is_correct('black', 'red', 'blue', 'blue', 'Background Color') == False
# assert is_correct('black', 'red', 'blue', 'black', 'Background Color') == True
# assert is_correct('black', 'red', 'blue', 'red', 'Text Color') == True
# assert is_correct('black', 'red', 'blue', 'blue', 'Text Color') == False
# assert is_correct('black', 'red', 'blue', 'pink', 'Text') == False
# assert is_correct('black', 'red', 'blue', 'red', 'Text') == False
# assert is_correct('black', 'red', 'blue', 'red', 'Neither') == False
# assert is_correct('black', 'red', 'blue', 'pink', 'Neither') == True

########################################################################################################################
########################################################################################################################

def pretty_print_int(number):
    ans = f"{number:,}"
    return ans

########################################################################################################################

# TODO 2: Place your code for `pretty_print_dollars` here
def pretty_print_dollars(number):
    number = float(f"{number:.2f}")
    negative = number < 0
    if negative:
        number -= (number * 2)
    number = float(f"{number:.2f}")
    return ("-" if negative else "") + "$" + pretty_print_int(number) + ("0" if check_if_two_digits(number) else "")
# TODO 1: Place your code for `pretty_print_int` here
def pretty_print_int(number):
    ans = f"{number:,}"
    return ans

def check_if_two_digits(number):
    number = str(number)
    return number[-2] == "."

########################################################################################################################

# TODO 3: Place your code for `make_field` here
def make_field(content, length):
    content = str(content)
    if len(content) < length - 2:
        return "|" + content.rjust(length - 1) + " |"
    if len(content) == length - 2:
        return "| " + content + " |"
    else:
        return "| " + content[0:length - 2] + " |"
        
########################################################################################################################

# TODO 4: Place your code for `make_line` here
def make_line(length):
    return "+" + ("-" * length) + "+"

########################################################################################################################
# TODO 5: Place your code for `simulate_infection` here
import math

def simulate_infection(population, initial_infected, r_number):
    infected = initial_infected
    deceased = 0
    day = 1
    while deceased < population:
        print(str(day) + " " + str(population - deceased))
        deceased += infected
        infected *= r_number
        infected = math.ceil(infected)
        day += 1

########################################################################################################################
import math

def compound_interest(init_principal, acc_rate, acc_cmp_freq, years):
    if acc_cmp_freq == 0:
        return init_principal * math.e ** (acc_rate * years)
    else:
        return init_principal * (1 + (acc_rate / acc_cmp_freq)) ** (acc_cmp_freq * years)

########################################################################################################################

def simulate_account_balance(init_principal, acc_rate, acc_cmp_freq, setup_fee, years):
    init_principal -= setup_fee
    for i in range(years):
        new_balance = compound_interest(init_principal, acc_rate, acc_cmp_freq, i + 1)
        if i % 2 == 1:
            print(str(i + 1) + " " + str(new_balance))

########################################################################################################################

import math

def pretty_print_dollars(number):
    number = float(f"{number:.2f}")
    negative = number < 0
    if negative:
        number -= (number * 2)
    number = float(f"{number:.2f}")
    return pretty_print_int(number)
# TODO 1: Place your code for `pretty_print_int` here
def pretty_print_int(number):
    ans = f"{number}"
    return ans

def check_if_two_digits(number):
    number = str(number)
    return number[-2] == "."

def compound_interest(init_principal, acc_rate, acc_cmp_freq, years):
    if acc_cmp_freq == 0:
        return init_principal * math.e ** (acc_rate * years)
    else:
        return init_principal * (1 + (acc_rate / acc_cmp_freq)) ** (acc_cmp_freq * years)

# TODO 7: Place your code for `simulate_account_balance` here
def simulate_account_balance(init_principal, acc_rate, acc_cmp_freq, setup_fee, years):
    init_principal -= setup_fee
    for i in range(years):
        new_balance = compound_interest(init_principal, acc_rate, acc_cmp_freq, i + 1)
        if i % 2 == 1:
            print(str(i + 1) + " " + pretty_print_dollars(new_balance))

########################################################################################################################

# TODO 8: Place your code for `simulate_infection_pp` here
# TODO 5: Place your code for `simulate_infection` here
import math

def pretty_print_int(number):
    ans = f"{number:,}"
    return ans

# TODO 3: Place your code for `make_field` here
def make_field(content, length):
    content = str(content)
    if len(content) < length - 2:
        return "|" + content.rjust(length - 1) + " |"
    if len(content) == length - 2:
        return "| " + content + " |"
    else:
        return "| " + content[0:length - 2] + " |"

# TODO 4: Place your code for `make_line` here
def make_line(length):
    return "+" + ("-" * length) + "+"

def simulate_infection(population, initial_infected, r_number):
    res = ""
    infected = initial_infected
    deceased = 0
    day = 1
    while deceased < population:
        res += make_field(day, 5) + make_field(pretty_print_int(population - deceased), 12) + "\n"
        deceased += infected
        infected *= r_number
        infected = math.ceil(infected)
        day += 1
    res += make_field(day, 5) + make_field(pretty_print_int(0), 12) + "\n"
    return res

def simulate_infection_pp(population, initial_infected, r_number):
    res = make_line(5) + make_line(12) + "\n" + make_field("Day", 5) + make_field("Population", 12) + "\n" + make_line(5) + make_line(12) + "\n" + simulate_infection(population, initial_infected, r_number) + make_line(5) + make_line(12)
    print(res)

### 
# TODO 9: Place your code for `simulate_account_balance_pp` here
def pretty_print_int(number):
    ans = f"{number:,}"
    return ans

# TODO 2: Place your code for `pretty_print_dollars` here
def pretty_print_dollars(number):
    number = float(f"{number:.2f}")
    negative = number < 0
    if negative:
        number -= (number * 2)
    number = float(f"{number:.2f}")
    return ("-" if negative else "") + "$" + pretty_print_int(number) + ("0" if check_if_two_digits(number) else "")
# TODO 1: Place your code for `pretty_print_int` here
def pretty_print_int(number):
    ans = f"{number:,}"
    return ans

def check_if_two_digits(number):
    number = str(number)
    return number[-2] == "."

def make_field(content, length):
    content = str(content)
    if len(content) < length - 2:
        return "|" + content.rjust(length - 1) + " |"
    if len(content) == length - 2:
        return "| " + content + " |"
    else:
        return "| " + content[0:length - 2] + " |"

# TODO 4: Place your code for `make_line` here
def make_line(length):
    return "+" + ("-" * length) + "+"

import math

def compound_interest(init_principal, acc_rate, acc_cmp_freq, years):
    if acc_cmp_freq == 0:
        return init_principal * math.e ** (acc_rate * years)
    else:
        return init_principal * (1 + (acc_rate / acc_cmp_freq)) ** (acc_cmp_freq * years)

def simulate_account_balance(init_principal, acc_rate, acc_cmp_freq, setup_fee, years):
    res_list = []
    init_principal -= setup_fee
    for i in range(years):
        new_balance = compound_interest(init_principal, acc_rate, acc_cmp_freq, i + 1)
        if i % 2 == 1:
            res_list.append(str(i + 1))
            res_list.append(pretty_print_dollars(new_balance))
    return res_list

def simulate_account_balance_pp(init_principal, acc_rate, acc_cmp_freq, setup_fee, years):
    interest_list = simulate_account_balance(init_principal, acc_rate, acc_cmp_freq, setup_fee, years)
    str1 = interest_list[-1]
    str2 = "Balance"
    longest_length = max(len(str1), len(str2)) + 2
    res = make_line(6) + make_line(longest_length) + "\n" + make_field("Year", 6) + make_field("Balance", longest_length) + "\n" + make_line(6) + make_line(longest_length) + "\n"
    for i in range(years // 2):
        res += make_field(interest_list[i * 2], 6) + make_field(interest_list[i * 2 + 1], longest_length) + "\n"
    res += make_line(6) + make_line(longest_length)
    print(res)

########################################################################################################################

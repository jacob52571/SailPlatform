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
    return ("-" if negative else "") + "$" + pretty_print_int(number)
# TODO 1: Place your code for `pretty_print_int` here
def pretty_print_int(number):
    ans = f"{number:,}"
    return ans

########################################################################################################################


import sys

def combination_theorem(row_num):
    answers = []
    for i in range(0, row_num):
        top = factorial(row_num - 1)
        bottom = factorial(i) * factorial(row_num - 1 - i)
        answers.append(int(top/bottom))
    return answers

def factorial(num):
    if num == 0:
        return 1
    elif num == 1:
        return 1
    else:
        return num * factorial(num - 1)

def format_row(row):
    row = [str(x) for x in row]
    return " ".join(row)
    
if __name__ == "__main__":
    rows = []
    row = input("Select a height: ")
    try:
        row = int(row)
    except:
        print("Value is not a number.")
        sys.exit(1)
    if row < 1:
        print("Enter value of 1 or more.")
        sys.exit(1)
    if row >= 1:
        rows.append([1])
    if row >= 2:
        rows.append([1, 1])
    for i in range(3, row + 1):
        rows.append(combination_theorem(i))
    max_length = len(format_row(rows[-1]))
    
    for i in range(0, len(rows)):
        print(format_row(rows[i]).center(max_length))
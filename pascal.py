def combination_theorem(row_num):
    answers = []
    # row 4 -> 3c0, 3c1, 3c2, 3c3
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
    row = int(input("Select a height: "))
    if row >= 1:
        rows.append([1])
    if row >= 2:
        rows.append([1, 1])
    # this is for row 7
    for i in range(3, row + 1):
        rows.append(combination_theorem(i))
    max_length = len(format_row(rows[-1]))
    
    for i in range(0, len(rows)):
        print(format_row(rows[i]).center(max_length))
def get_pascal_row(row_number):
    if row_number == 1:
        return "1"
    if row_number == 2:
        return "1 1"
    
    """
    2 5
    row_number = 3; 1 2 1
    row_number = 4; 1 3 3 1'
    """

    numbers = [1, 1]
    new_numbers = [1, 1]
    if (len(numbers) < row_number):
        for i in range(0, row_number - 3):
            sum = numbers[i] + numbers[i + 1]
            numbers_left = new_numbers[0:i + 1]
            numbers_right = new_numbers[i + 1:]
            new_numbers = numbers_left + [sum] + numbers_right
    return numbers
    
if __name__ == "__main__":
    print(get_pascal_row(4))
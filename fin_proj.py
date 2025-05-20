import sys
import csv

def get_input_description():
    file_name = input("What file do you want to open? ")
    try:
        return open(file_name, "r", newline='')
    except FileNotFoundError:
        print("File not found. Please try again.")
        return get_input_description()

def get_data_list(file_object, column_number):
    column_names = ["Date", "Open", "High", "Low", "Close", "Volume", "Adj Close"]
    res = []
    csv_dict_reader = csv.DictReader(file_object)
    for row in csv_dict_reader:
        data = (row["Date"], float(row[column_names[column_number]]))
        res.append(data)
    return res

def average_data(list_of_tuples):
    res = []
    # create a dictionary with the key as the month:year and the value as a list of all the tuples in that month
    data = {}
    for t in list_of_tuples:
        time_data = t[0].split("/")
        month = time_data[0] + "-" + time_data[2]
        if month not in data:
            data[month] = []
        data.setdefault(month, []).append(t[1])
    for key in data.keys():
        average = sum(data[key]) / len(data[key])
        avg = (average, key)
        res.append(avg)
    return res

def main():
    file = get_input_description()
    column = input("Which column do you want to average? ")
    try:
        column = int(column)
    except:
        print("Not a number.")
        sys.exit(1)
    else:
        data = get_data_list(file, column)
        averages = average_data(data)
        # averages = (average, month:year)
        averages.sort()
        # averages now in order from lowest to highest
        print(f"Lowest 6 for column {column}")
        for i in range(6):
            print(f"{averages[i][1]}: {averages[i][0]:.2f}")
        print(f"Highest 6 for column {column}")
        for i in range(6):
            print(f"{averages[-i-1][1]}: {averages[-i-1][0]:.2f}")
        file.close()

if __name__ == "__main__":
    main()

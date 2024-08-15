import os
import random
from datetime import datetime


def create_dev_set(full_data_dir, dev_data_dir, ratio=10):
    os.makedirs(dev_data_dir, exist_ok=True)
    for file_name in sorted(os.listdir(full_data_dir)):
        with open(f'{full_data_dir}/{file_name}') as file_full, \
                open(f'{dev_data_dir}/{file_name}', 'w') as file_dev:
            for line in file_full:
                rand_num = random.randint(0, 100)
                if rand_num < ratio:
                    file_dev.write(line)


# TODO 1: Place your code here.
def load_phone_calls_dict(data_dir):
    phone_calls_dict = {}
    for x in os.listdir(data_dir):
        with open(data_dir + "/" + x, "r") as f:
            for i in f.readlines():
                timestamp = i[0:19]
                phone_number = i[21:-1]
                area_code = phone_number[3:6]
                date_time_obj = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
                if 0 <= date_time_obj.hour < 6:
                    if not (area_code in phone_calls_dict.keys()):
                        phone_calls_dict[area_code] = {}
                    if not (phone_number in phone_calls_dict[area_code].keys()):
                        phone_calls_dict[area_code][phone_number] = []
                    phone_calls_dict[area_code][phone_number].append(date_time_obj)
    return phone_calls_dict


# TODO 2: Place your code here.
def generate_phone_call_counts(phone_calls_dict):
    call_counts = {}
    for x in phone_calls_dict.keys():
        for y in phone_calls_dict[x].keys():
            call_counts[y] = len(phone_calls_dict[x][y])
    return call_counts

# TODO 3: Place your code here.
def most_frequently_called(phone_call_counts, top_n):
    call_counts_list = []
    for x in phone_call_counts.keys():
        call_counts_list.append((x, phone_call_counts[x]))
    return sorted(insertion_sort(call_counts_list)[::-1], key = lambda x: x[0])[:top_n]



def insertion_sort(x):
    for i in range(len(x)):
        for j in range(len(x) - 1):
            if (x[j][1] > x[j + 1][1]):
                temp = x[j + 1]
                x[j + 1] = x[j]
                x[j] = temp
    return x



# TODO 4: Place your code here.
def export_phone_call_counts(most_frequent_list, out_file_path):
    with open(out_file_path, "w") as f:
        for i in most_frequent_list:
            f.write(str(i[0]) + ": " + str(i[1]))

# TODO 5: Place your code here.

# testing
if __name__ == "__main__":
    print(generate_phone_call_counts(load_phone_calls_dict("./toy_data")))
    print(most_frequently_called(generate_phone_call_counts(load_phone_calls_dict("./toy_data")), 2))

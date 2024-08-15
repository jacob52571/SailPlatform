# TODO: Place your code here.
from datetime import datetime


def filter_phone_calls(area_code, start_hour, end_hour, input_path, output_path):
    with open(input_path, "r") as f, open(output_path, mode='w') as f2:
        out = f.readlines()
        for i in out:
            x, y = i.split("(")
            a, b = i.split("+")
            time = datetime.strptime(a[:-2], "%Y-%m-%d %H:%M:%S")
            if y[0:3] == str(area_code) and start_hour <= time.hour < end_hour:
                f2.write(i)


if __name__ == "__main__":
    filter_phone_calls(
        area_code=412,  # not used at this point
        start_hour=-1,  # not used at this point
        end_hour=-1,  # not used at this point
        input_path='data/phone_calls.txt',
        output_path='data/phone_calls_filtered.txt'  # not at this point
    )

# convert csv values to 2d list to copy paste into my_obj.py

import csv

def main():
    # https://stackoverflow.com/questions/24662571/python-import-csv-to-list
    try:
        with open('PyreEmblem\map_file.csv', newline='') as f:
            reader = csv.reader(f)
            data = list(reader)
        print('[', end='')
        for i in range(len(data)):
            if i == len(data)-1:
                print(data[i], end='')
                print(']')
            else:
                print(data[i], end='')
                print(',')
    except IOError:
        print("Error: could not open map_file")

if __name__ == "__main__":
    main()
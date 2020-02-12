import csv


def read_csv(filepath, encoding_type="utf-8", mode_type="r"):
    with open(filepath, encoding=encoding_type, mode=mode_type) as file_input:
        reader = csv.reader(file_input)
        headers = next(reader)
        print(headers)
        for line in reader:
            print(line)


def read_csv_dirct(file_path):
    with open(file_path, encoding="utf-8", newline="") as file_input:
        csv.excel
        reader = csv.DictReader(file_input)
        result = []
        for row in reader:
            result_in = {}
            for x, y in row.items():
                result_in[x] = y
            result.append(result_in)
        print(result)
import csv


def write_csv(file_path, lines, mode_type="w", encoding_type="utf-8"):
    with open(file_path, mode=mode_type, encoding=encoding_type, newline="") as file_output:
        writer = csv.writer(file_output)
        writer.writerows(lines)


def write_csv_dict(file_path, lines, mode_type="w", encoding_type="utf-8"):
    with open(file_path, mode=mode_type, encoding=encoding_type, newline="") as file_output:
        writer = csv.DictWriter(file_output, lines[0].keys())
        writer.writerows(lines)

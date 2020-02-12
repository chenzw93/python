def read_file(file_path):
    with open(file_path, encoding="utf-8", mode="r") as file_input:
        lines = file_input.readlines()
        for line in lines:
            print(line, end="")

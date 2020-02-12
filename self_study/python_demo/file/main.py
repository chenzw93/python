from file import read_normal
from file import write_normla
from file import read_csv
from file import write_csv

if __name__ == "__main__":
    """
        normal file
    """
    # lines = ["this is first line\n", "this is second line\n", "this is third line\n"]
    # file_path = "a.txt";
    # write_normla.write_file("a.txt", lines, mode_type="a")
    # read_normal.read_file(file_path)

    """
        csv file
    """
    # lines = [("id", "name", "age"), (1, "xiaohua", 10), (2, "xiaohei", 15), (3, "xiaohui", 20)]
    # write_csv.write_csv("b.csv", lines)
    read_csv.read_csv('b.csv')
    lines = [{"id":4,"name":"xiaohua","age":10},{"id":5,"name":"xiaohua","age":15},{"id":6,"name":"xiaohua","age":20}]
    write_csv.write_csv_dict('c.csv', lines,mode_type='a')
    read_csv.read_csv_dirct('b.csv')

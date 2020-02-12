import os
import shutil
import sys
import zipfile
import re
from datetime import *
from enum import Enum, unique


def get_files_listdir(file_path):
    # os.listdir 查询当前目录下所有目录，文件，不包含子目录
    for x in os.listdir(file_path):
        # os.path.join 目录拼接
        file = os.path.join(file_path, x)
        # os.path.isfile 判断是文件还是文件夹
        if os.path.isfile(file):
            print(file)
        else:
            get_files_listdir(file)


def get_files_walk(file_path):
    for root, dirs, files in os.walk(file_path):
        print(root)
        print(dirs)
        print(files)


def get_files_shutil():
    shutil.copy2("demo.py", "demo1.py")
    shutil.move("demo1.py", "demo2.py")


def get_arvgs(param):
    print(param)
    print(sys.path)


def get_time():
    print(datetime.now())
    print(datetime.today())
    print(datetime.timestamp(datetime.now()))
    print(date.year, date.month, date.day)


def zip_file(src, dist):
    with zipfile.ZipFile(dist, 'w') as zip_io:
        for root, dirs, files in os.walk(src):
            for file in files:
                zip_io.write(os.path.join(root, file))


def regex_match(reg, str):
    pattern = re.compile(reg)
    return pattern.match(str)


@unique
class WEEK(Enum):
    SUN = 0
    MON = 1
    THU = 2
    FRI = 3

if __name__ == '__main__':
    # current_dir = os.getcwd()
    # get_files_shutil()
    # get_files_listdir(current_dir)
    # get_arvgs(sys.argv)
    # get_time()
    # zip_file("./", "./demo1.zip")
    print(WEEK.MON, WEEK.MON.value)
    print(WEEK(3))
    Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
    for name, member in Month.__members__.items():
        print(name, '=>', member, ',', member.value)

    # input_line = "this is a line"
    # input_re = re.compile(r"^[a-zA-Z\s]+$")
    # if input_re.match(input_line):
    #     print("input is ok")
    # else:
    #     print("input is error")

    # m = re.match(r'^(\d{3})--(\d{3,8})$', '010--12345')
    # print(m)
    # print(m.groups())
    # print(m.group(0))
    # print(m.group(1))
    # print(m.group(2))
    pass

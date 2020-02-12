from random import randrange, randint, sample


def display(balls):
    """
    输出列表中的双色球号码
    """
    for index, ball in enumerate(balls):
        if index == len(balls) - 1:
            print('|', end=' ')
        print('%02d' % ball, end=' ')
    print()


def random_select():
    """
    随机选择一组号码
    """
    red_balls = [x for x in range(1, 34)]
    selected_balls = []
    selected_balls = sample(red_balls, 6)
    selected_balls.sort()
    selected_balls.append(randint(1, 16))
    return selected_balls


def main():
    n = int(input('机选几注: '))
    for _ in range(n):
        display(random_select())

def read_file(file):
    try:
        f = open(file, "r")
        print(f.readlines())
    except Exception as e:
        print("读取文件失败", e)
    finally:
        if f:
            print("close file")
            f.close()

if __name__ == '__main__':
    read_file("H:/python/self_study/python_demo/variable_type/__init__.py")
    # pass
    # main()

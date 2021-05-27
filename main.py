# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pathlib
import re
keyword = "apple"

# 获取索引文件路径
current_path = pathlib.PurePath(__file__).parent
dbfile = current_path.joinpath("search.db")

# 在索引文件中搜索关键字
with open(dbfile, encoding='utf-8') as f:
    for line in f.readlines():
        if re.search(keyword, line):
            print(line.rstrip())


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

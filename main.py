# coding=utf-8
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import xlwt


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print("Hi, {0}".format(name))  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    workbook=xlwt.Workbook(encoding="utf-8")
    workSheet = workbook.add_sheet("sheet2")
    for i in range(1):
        for j in range(0, 3):
            workSheet.write(i,j, "你好上海")
    workbook.save("student.xls")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

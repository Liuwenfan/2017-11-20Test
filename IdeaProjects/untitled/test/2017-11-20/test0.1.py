#!/usr/bin/env python
# 书上练习 书名:python核心编程第二版


# 获取输入的两个数字的乘积
def test5_2_1():
    number_a = input(">input one number: ")
    number_a = int(number_a)
    number_b = input(">input the other number:")
    number_b = int(number_b)
    print("the result:", number_a * number_b)


# 获取输入分数的等级
def test5_3(grade):
    grade = int(grade)
    if grade < 60:
        print("F")
    elif grade < 70:
        print("D")
    elif grade < 80:
        print("C")
    elif grade < 90:
        print("B")
    else:
        print("A")


# 判断输入年份是不是闰年
def test5_4(year):
    year = int(year)
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print(year, " is run year")
    else:
        print(year, "is not run year")


# 分解金额为人民币面值
def test5_5(doller):
    dos = (1000, 500, 200, 100, 50, 10, 5, 1)
    for do in dos:
        if int(doller) % int(do) == 0:
            print("需要", float(do) / 10, "元", int(int(doller) / int(do)), "张")
            break
        elif int(int(doller) / int(do)) > 0:
            print("需要", float(do) / 10, "元", int(int(doller) / int(do)), "张")
            doller = doller % do


if __name__ == '__main__':
    test5_5(int(float(input(">enter you money")) * 10))

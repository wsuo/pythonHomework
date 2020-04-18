"""
@author: shoo Wang
@contact: wangsuoo@foxmail.com
@file: demo01.py
@time: 2020/4/16 0016
"""
import turtle
import random

'''
雪花位置随机
雪花个数随机[2,10]之间
雪花大小随机
'''


# 递归的画科赫曲线
def koch(size, n):
    if n == 0:
        turtle.fd(size)
    else:
        for angle in [0, 60, -120, 60]:
            turtle.left(angle)
            koch(size / 3, n - 1)


# 控制雪花的 个数、位置; 此函数为核心函数!
def control_num(n):
    pen_attr()
    # 一个随机函数控制随机位置和大小,参数为雪花的个数
    for i in range(n):
        # 隐藏画笔
        turtle.hideturtle()
        # 开始填充背景颜色
        turtle.begin_fill()
        turtle.color('white')
        # 生成随机数,控制 x 轴 与 y 轴
        num1 = random.randint(-100, 100)
        num2 = random.randint(-100, 100)
        num3 = random.randint(20, 80)
        # 控制位置随机
        control_locate(num1 * 3, num2 * 3)
        # 控制大小
        control_size(num3, 3)
        turtle.end_fill()


# 设置画笔的属性
def pen_attr():
    # 设置背景颜色
    turtle.bgcolor('blue')
    # 设置画笔的颜色和速度等属性, (吐槽一下速度真的慢,最快就是10了
    turtle.pen({'pensize': 1, 'shown': True, 'resizemode': 'auto', 'outline': 1,
                'pencolor': 'white', 'pendown': False, 'fillcolor': 'white',
                'speed': 10})


# 控制每一阶的 大小、转向
def control_size(size, level, angle=120):
    # 画第一部分
    koch(size, level)
    turtle.right(angle)
    # 画第二部分
    koch(size, level)
    turtle.right(angle)
    # 画第三部分
    koch(size, level)


# 控制位置随机
def control_locate(resetX, resetY):
    # turtle.setup(startX, startY)
    turtle.penup()
    turtle.goto(resetX, resetY)
    turtle.pendown()


# 主函数
def main():
    """
    总体控制画布的位置,入口函数,调用其他函数
    """
    # 控制个数, 这里是随机,[2,10]
    num = random.randint(2, 10)
    control_num(num)
    turtle.done()


# 函数调用,启动!!!
main()

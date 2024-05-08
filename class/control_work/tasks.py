from tkinter import *


class Shape:
    def square(self):
        pass


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def square(self):
        return 3.14 * (self.r ^ 2)


class Rect(Shape):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def square(self):
        return self.x * self.y


def circle():
    r = int(input("Введите радиус: "))
    print(F"Площадь круга равна: {Circle(r).square()}\n")


def rect():
    x = int(input("Введите первую сторону: "))
    y = int(input("Введите вторую сторону: "))
    print(F"Площадь круга прямоугольника: {Rect(x, y).square()}\n")


def out():
    r1 = int(input("Введите радиус первого круга: "))
    r2 = int(input("Введите радиус второго круга: "))

    window = Tk()
    window.title('Работа с canvas')

    canvas = Canvas(window, width=r1 * r2 // 2, height=r1 * r2 // 2, bg="white")
    canvas.create_oval([r1 * 1.5, r1 * 1.5], [r1 * 1.5 + r1, r1 * 1.5 + r1], fill="grey")
    canvas.create_oval([r2 * 2.5, r2 * 2.5], [r2 * 2.5 + r2, r2 * 2.5 + r2], fill="grey")

    canvas.pack()
    window.mainloop()


while True:
    print("\nКакую фигуру вы хотите?\n"
          "1 - площадь круга\n"
          "2 - площадь прямоугольника\n"
          "3 - выввод двух кругов")
    choi = int(input("Вводите: "))
    choice = {1: circle, 2: rect, 3: out}
    choice[choi]()

import math
import tkinter as tk
from tkinter.constants import END


class Button(tk.Button):
    def __init__(self, master, **kw):
        tk.Button.__init__(self, master=master, **kw)
        self.defaultBackground = self["background"]
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        self['background'] = self['activebackground']

    def on_leave(self, e):
        self['background'] = self.defaultBackground


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.attributes('-topmost', True)

        self.photo = tk.PhotoImage(file="res/icon.png")
        self.root.iconphoto(False, self.photo)

        self.flag = 0
        self.stat = ''
        self.num = ''

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Input", width=5, borderwidth=3).grid(row=0, column=4, pady=8, columnspan=2)

        self.e = tk.Entry(self.root, font=("default, 11"), insertontime=0, bd=5, width=21, borderwidth=10,
                          foreground="#ff0000", highlightthickness=5, highlightcolor="#f5d0d0", highlightbackground="#f5d0d0")
        self.e.grid(row=0, rowspan=2, column=0, columnspan=4, padx=5, pady=5)
        self.e.bind("<Key>", lambda e: "break")

        tk.Label(self.root, borderwidth=3, relief="sunken", text="Calculations here", width=34, bg="#f5d0d0",
                 fg="#000000").grid(row=2, column=0, columnspan=5, pady=5)

        self.create_buttons()

    def create_buttons(self):
        Button(self.root, activebackground='#73f5d7', bg="#f5f0f0", text="7", padx=20, pady=15,
               command=lambda: self.insert("7")).grid(row=4, column=0)
        Button(self.root, activebackground='#73f5d7', bg="#f5f0f0", text="8", padx=20, pady=15,
               command=lambda: self.insert("8")).grid(row=4, column=1)
        Button(self.root, activebackground='#73f5d7', bg="#f5f0f0", text="9", padx=20, pady=15,
               command=lambda: self.insert("9")).grid(row=4, column=2)
        Button(self.root, activebackground='#73f5d7', bg="#d0c6f5", text="/", padx=20, pady=15,
               command=self.divide).grid(row=3, column=3)

        Button(self.root, activebackground='#73f5d7', bg="#f5f0f0", text="4", padx=20, pady=15,
               command=lambda: self.insert("4")).grid(row=5, column=0)
        Button(self.root, activebackground='#73f5d7', bg="#f5f0f0", text="5", padx=20, pady=15,
               command=lambda: self.insert("5")).grid(row=5, column=1)
        Button(self.root, activebackground='#73f5d7', bg="#f5f0f0", text="6", padx=20, pady=15,
               command=lambda: self.insert("6")).grid(row=5, column=2)
        Button(self.root, activebackground='#73f5d7', bg="#d0c6f5", text="x", padx=20, pady=15,
               command=self.multiply).grid(row=4, column=3)

        Button(self.root, activebackground='#73f5d7', bg="#f5f0f0", text="1", padx=20, pady=15,
               command=lambda: self.insert("1")).grid(row=6, column=0)
        Button(self.root, activebackground='#73f5d7', bg="#f5f0f0", text="2", padx=20, pady=15,
               command=lambda: self.insert("2")).grid(row=6, column=1)
        Button(self.root, activebackground='#73f5d7', bg="#f5f0f0", text="3", padx=20, pady=15,
               command=lambda: self.insert("3")).grid(row=6, column=2)
        Button(self.root, activebackground='#73f5d7', bg="#d0c6f5", text="-", padx=20, pady=15,
               command=self.subtract).grid(row=5, column=3)

        Button(self.root, activebackground='#73f5d7', bg="#f5f0f0", text="0", padx=50, pady=15,
               command=lambda: self.insert("0")).grid(row=7, column=0, columnspan=2)
        Button(self.root, activebackground='#73f5d7', bg="#f5f0f0", text=".", padx=20, pady=15,
               command=lambda: self.insert(".")).grid(row=7, column=2)
        Button(self.root, activebackground='#73f5d7', bg="#d0c6f5", text="+", padx=20, pady=32,
               command=self.add).grid(row=6, column=3, rowspan=2)

        Button(self.root, activebackground='#73f5d7', bg="#c6f5ea", text="=", padx=18, pady=115,
               command=self.calculate).grid(row=3, column=4, rowspan=5)
        Button(self.root, activebackground='#73f5d7', bg="#6699ff", text="cls", padx=20, pady=15,
               command=self.clear).grid(row=3, column=0)

        Button(self.root, activebackground='#73f5d7', bg="#d0c6f5", text="\u221A", padx=20, pady=15,
               command=self.root_func).grid(row=3, column=1)
        Button(self.root, activebackground='#73f5d7', bg="#d0c6f5", text="pow", padx=20, pady=15,
               command=self.power_func).grid(row=3, column=2)

    def insert(self, value):
        if self.flag:
            self.e.delete(0, END)
            self.update_view("Calculations here")
            self.flag = 0
        current = self.e.get()
        self.e.delete(0, END)
        self.e.insert(0, current + value)

    def set_operation(self, operation):
        self.update_label(operation)
        self.stat = operation
        self.num = self.e.get()
        self.e.delete(0, END)

    def add(self):
        self.set_operation("+")

    def subtract(self):
        self.set_operation("-")

    def multiply(self):
        self.set_operation("x")

    def divide(self):
        self.set_operation("/")

    def root_func(self):
        self.set_operation("root")

    def power_func(self):
        self.set_operation("pow")

    def calculate(self):
        num2 = self.e.get()
        expression = ''
        ans = ''
        if self.stat == "+":
            ans = float(self.num) + float(num2)
            expression = f"{self.num} + {num2} = {ans}"
        elif self.stat == "-":
            ans = float(self.num) - float(num2)
            expression = f"{self.num} - {num2} = {ans}"
        elif self.stat == "x":
            ans = float(self.num) * float(num2)
            expression = f"{self.num} * {num2} = {ans}"
        elif self.stat == "/":
            ans = "{:.3f}".format(float(self.num) / float(num2))
            expression = f"{self.num} / {num2} = {ans}"
        elif self.stat == "root":
            ans = "{:.2f}".format(math.pow(float(num2), 1 / 2))
            expression = f"root {num2} = {ans}"
        elif self.stat == "pow":
            ans = "{:.2f}".format(math.pow(float(self.num), int(num2)))
            expression = f"{self.num} pow {num2} = {ans}"

        self.e.delete(0, END)
        self.e.insert(0, ans)
        self.update_view(expression)
        self.flag = 1

    def clear(self):
        self.update_label("")
        self.update_view("Calculations here")
        self.flag = 1
        self.e.delete(0, END)

    def update_label(self, text):
        tk.Label(self.root, text=text, width=5, borderwidth=3).grid(row=0, column=4, pady=8, columnspan=2)

    def update_view(self, text):
        tk.Label(self.root, borderwidth=3, relief="sunken", text=text, width=34, bg="#f5d0d0", fg="#000000")\
            .grid(row=2, column=0, columnspan=5, pady=5)


if __name__ == "__main__":
    ui = tk.Tk()
    Calculator(ui)
    ui.resizable(False, False)
    ui.mainloop()

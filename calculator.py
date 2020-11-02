from tkinter import *

# ---Calculator Class----
class Calculator:

    # ---Button Functions---
    def buttonClick(self, number):
        current = self.e.get()
        self.e.delete(0, END)
        self.e.insert(0, str(current) + str(number))

    def buttonClear(self):
        self.e.delete(0, END)

    def buttonAdd(self):
        global value
        global math
        math = "addition"
        value = self.e.get()
        self.e.delete(0, END)

    def buttonDivide(self):
        global value
        global math
        math = "division"
        value = self.e.get()
        self.e.delete(0, END)

    def buttonMultiply(self):
        global value
        global math
        math = "multiplication"
        value = self.e.get()
        self.e.delete(0, END)

    def buttonSubtract(self):
        global value
        global math
        math = "subtraction"
        value = self.e.get()
        self.e.delete(0, END)

    def buttonEqual(self):

        if math == "addition":
            current = self.e.get()
            self.e.delete(0, END)
            self.e.insert(0, float(value) + float(current))

        if math == "division":
            current = self.e.get()
            self.e.delete(0, END)
            self.e.insert(0, float(value) / float(current))

        if math == "multiplication":
            current = self.e.get()
            self.e.delete(0, END)
            self.e.insert(0, float(value) * float(current))

        if math == "subtraction":
            current = self.e.get()
            self.e.delete(0, END)
            self.e.insert(0, float(value) - float(current))

    # ----Constructor----
    def __init__(self, root):
        root.title("Calculator")


        # --Defining & Asserting Entry---
        self.e = Entry(root, width=65, bd=5)
        self.e.grid(row=0, column=0, columnspan=4)

        # --Defining & Asserting Buttons---
        self.btn7 = Button(root, text=7, padx=38, pady=18, command=lambda: self.buttonClick(7)).grid(row=1, column=0)
        self.btn8 = Button(root, text=8, padx=38, pady=18, command=lambda: self.buttonClick(8)).grid(row=1, column=1)
        self.btn9 = Button(root, text=9, padx=38, pady=18, command=lambda: self.buttonClick(9)).grid(row=1, column=2)
        self.btnDivide = Button(root, text="/", padx=38, pady=18, command=self.buttonDivide).grid(row=1, column=3)
        self.btn4 = Button(root, text=4, padx=38, pady=18, command=lambda: self.buttonClick(4)).grid(row=2, column=0)
        self.btn5 = Button(root, text=5, padx=38, pady=18, command=lambda: self.buttonClick(5)).grid(row=2, column=1)
        self.btn6 = Button(root, text=6, padx=38, pady=18, command=lambda: self.buttonClick(6)).grid(row=2, column=2)
        self.btnMultiply = Button(root, text="x", padx=38, pady=18, command=self.buttonMultiply).grid(row=2, column=3)
        self.btn1 = Button(root, text=1, padx=38, pady=18, command=lambda: self.buttonClick(1)).grid(row=3, column=0)
        self.btn2 = Button(root, text=2, padx=38, pady=18, command=lambda: self.buttonClick(2)).grid(row=3, column=1)
        self.btn3 = Button(root, text=3, padx=38, pady=18, command=lambda: self.buttonClick(3)).grid(row=3, column=2)
        self.btnAdd = Button(root, text="+", padx=36.5, pady=18, command=self.buttonAdd).grid(row=3, column=3)
        self.btnClear = Button(root, text="Clear", padx=28, pady=18, command=self.buttonClear).grid(row=4, column=0)
        self.btn0 = Button(root, text=0, padx=38, pady=18, command=lambda: self.buttonClick(0)).grid(row=4, column=1)
        self.btnEqual = Button(root, text="=", padx=37, pady=18, command=self.buttonEqual).grid(row=4, column=2)
        self.btnSubtract = Button(root, text="-", padx=38, pady=18, command=self.buttonSubtract).grid(row=4, column=3)



root = Tk()
c = Calculator(root)

root.mainloop()
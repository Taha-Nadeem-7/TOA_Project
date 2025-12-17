#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tkinter as tk
class MooreCalculator:
    def __init__(self):
        self.reset()

    def reset(self):
        self.state = "q0"
        self.num1 = ""
        self.num2 = ""
        self.operator = ""

    def transition(self, symbol):

        # q0: initial state
        if self.state == "q0":
            if symbol.isdigit():
                self.num1 += symbol
                self.state = "q1"
            else:
                self.state = "qt"

        # q1: Reading first number
        elif self.state == "q1":
            if symbol.isdigit():
                self.num1 += symbol
            elif symbol in "+-*/":
                self.operator = symbol
                self.state = "q2"
            else:
                self.state = "qt"

        # q2: Operator received and expecting second number
        elif self.state == "q2":
            if symbol.isdigit():
                self.num2 += symbol
                self.state = "q3"
            else:
                self.state = "qt"

        # q3: Reading second number
        elif self.state == "q3":
            if symbol.isdigit():
                self.num2 += symbol
            elif symbol == "=":
                self.state = "qf"
            elif symbol in "+-*/":
                #two-operand rule
                self.state = "qt"
            else:
                self.state = "qt"

        # qf: Output state
        elif self.state == "qf":
            if symbol in "+-*/":
                self.operator = symbol
                self.num2 = ""
                self.state = "q2"
            else:
                self.state = "qt"

    def output(self):
        if self.state == "qf":
            a = int(self.num1)
            b = int(self.num2)

            if self.operator == "+":
                result = a + b
            elif self.operator == "-":
                result = a - b
            elif self.operator == "*":
                result = a * b
            elif self.operator == "/":
                if b == 0:
                    self.state = "qt"
                    return "Invalid Expression"
                result = a / b
            else:
                self.state = "qt"
                return "Invalid Expression"

            # We store the result for next computation
            self.num1 = str(int(result))
            self.num2 = ""
            self.operator = ""

            return result

        # Error
        elif self.state == "qt":
            return "Invalid Expression"

        return None


#GUI 
calc = MooreCalculator()

def press(btn):
    if btn == "C":
        calc.reset()
        display.set("")
        state_label.set("Current State: q0")
        return

    calc.transition(btn)         
    result = calc.output()        

    # Update display
    if result is not None:
        display.set(result)
    else:
        display.set(display.get() + btn)

    #state update
    state_label.set(f"Current State: {calc.state}")


# Window
root = tk.Tk()
root.title("Moore Machine Calculator")
root.configure(bg="#1e1e1e")

# display
display = tk.StringVar()
tk.Entry(
    root,
    textvariable=display,
    font=("Arial", 20),
    justify="right",
    width=20,
    bg="#2d2d2d",
    fg="white",
    insertbackground="white"
).grid(row=0, column=0, columnspan=4, pady=5)

# State Label
state_label = tk.StringVar()
state_label.set("Current State: q0")

tk.Label(
    root,
    textvariable=state_label,
    font=("Arial", 12),
    fg="#00ffcc",
    bg="#1e1e1e"
).grid(row=1, column=0, columnspan=4)

#buttons
buttons = [
    "7","8","9","+",
    "4","5","6","-",
    "1","2","3","*",
    "0","=","/","C"
]

r = 2
c = 0
for b in buttons:
    tk.Button(
        root,
        text=b,                                                                                
        width=5,
        height=2,
        font=("Arial", 14),
        bg="#3c3f41",
        fg="white",
        activebackground="#555555",
        command=lambda x=b: press(x)
    ).grid(row=r, column=c, padx=2, pady=2)

    c += 1
    if c == 4:
        c = 0
        r += 1

root.mainloop()



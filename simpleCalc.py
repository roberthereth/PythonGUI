# Simple Calculator by Robert Hereth

from tkinter import *

# Makes window for calculator
from tkinter import messagebox

wn = Tk()
wn.title("Simple Calculator")
wn.geometry("570x600")
wn.resizable(False, False)
wn.configure(bg="#062625")

userMath = ""

labResult = Label(wn, width=25, height=2, text="", font=("georgia", 30))
labResult.pack()


def show(val):  # Used for most keys, adds given symbol to user's equation
    global userMath
    userMath += val
    labResult.config(text=userMath)


def clear():  # Used for C key, clears user's equation
    global userMath
    userMath = ""
    labResult.config(text=userMath)


def solve():  # Used for = key, solves user's equation and rewrites user's equation to result
    global userMath
    result = ""
    if userMath != "":
        try:
            result = eval(userMath)
            userMath = str(result)
        except:
            result = "err"
            userMath = ""
            messagebox.showerror(title="FATAL ERROR", message="Simple Calculator has encountered\nthe following error(s):"
                                                              "\n\nBad Math")
    labResult.configure(text=result)


# Creates buttons for calculator
butClear = Button(wn, text="C", width=5, height=1, font=("georgia", 30, "bold"), bd=1, fg="#fff", bg="#3697f5")
butMod = Button(wn, text="%", width=5, height=1, font=("georgia", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36")
butDivide = Button(wn, text="/", width=5, height=1, font=("georgia", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36")
butMult = Button(wn, text="*", width=5, height=1, font=("georgia", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36")

but7 = Button(wn, text="7", width=5, height=1, font=("georgia", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36")
but8 = Button(wn, text="8", width=5, height=1, font=("georgia", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36")
but9 = Button(wn, text="9", width=5, height=1, font=("georgia", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36")
butSub = Button(wn, text="-", width=5, height=1, font=("georgia", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36")

but4 = Button(wn, text="4", width=5, height=1, font=("georgia", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36")
but5 = Button(wn, text="5", width=5, height=1, font=("georgia", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36")
but6 = Button(wn, text="6", width=5, height=1, font=("georgia", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36")
butAdd = Button(wn, text="+", width=5, height=1, font=("georgia", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36")

but1 = Button(wn, text="1", width=5, height=1, font=("georgia", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36")
but2 = Button(wn, text="2", width=5, height=1, font=("georgia", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36")
but3 = Button(wn, text="3", width=5, height=1, font=("georgia", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36")
butDecimal = Button(wn, text=".", width=5, height=1, font=("georgia", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36")

but0 = Button(wn, text="0", width=10, height=1, font=("georgia", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36")
butEquals = Button(wn, text="=", width=10, height=1, font=("georgia", 30, "bold"), bd=1, fg="#fff", bg="#ffaa00")


def placeButtons():  # adds buttons to specified locations
    butClear.place(x=10, y=100)
    butMod.place(x=150, y=100)
    butDivide.place(x=290, y=100)
    butMult.place(x=430, y=100)
    but7.place(x=10, y=200)
    but8.place(x=150, y=200)
    but9.place(x=290, y=200)
    butSub.place(x=430, y=200)
    but4.place(x=10, y=300)
    but5.place(x=150, y=300)
    but6.place(x=290, y=300)
    butAdd.place(x=430, y=300)
    but1.place(x=10, y=400)
    but2.place(x=150, y=400)
    but3.place(x=290, y=400)
    butDecimal.place(x=430, y=400)
    but0.place(x=10, y=500)
    butEquals.place(x=290, y=500)


def addButtonFeatures():  # adds functions to buttons
    butClear.configure(command=lambda: clear())
    butMod.configure(command=lambda: show("%"))
    butDivide.configure(command=lambda: show("/"))
    butMult.configure(command=lambda: show("*"))
    but9.configure(command=lambda: show("9"))
    but8.configure(command=lambda: show("8"))
    but7.configure(command=lambda: show("7"))
    butSub.configure(command=lambda: show("-"))
    but6.configure(command=lambda: show("6"))
    but5.configure(command=lambda: show("5"))
    but4.configure(command=lambda: show("4"))
    butAdd.configure(command=lambda: show("+"))
    but3.configure(command=lambda: show("3"))
    but2.configure(command=lambda: show("2"))
    but1.configure(command=lambda: show("1"))
    butDecimal.configure(command=lambda: show("."))
    but0.configure(command=lambda: show("0"))
    butEquals.configure(command=lambda: solve())


if __name__ == '__main__':
    placeButtons()
    addButtonFeatures()
    wn.mainloop()

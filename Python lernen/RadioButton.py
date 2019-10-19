from tkinter import *

root = Tk()
root.title('Timer Setting')
root.resizable(width=False, height=False)

v = IntVar()
v.set(100)  # initializing the choice, i.e. Python

languages = [
    ("Timer  25ms", 25),
    ("Timer  50ms", 50),
    ("Timer 100ms", 100),
    ("Timer 150ms", 150),
    ("Timer 200ms", 200)]


def ShowChoice():
    print(v.get())


Label(root,
      text=""" Choose your favourite
programming language: """,
      justify=LEFT,
      padx=20).pack()

for txt, val in languages:
    Radiobutton(root,
                text=txt,
                indicatoron=0,
                width=25,
                padx=50,
                variable=v,
                command=ShowChoice,
                value=val).pack(anchor=W)


mainloop()

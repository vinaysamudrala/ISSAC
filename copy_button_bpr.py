import pyperclip
import tkinter
import os

os.system('cmd /k "pip install pyperclip"')

def a1f():
    pyperclip.copy("Bill_To_1: ")

def a2f():
    pyperclip.copy("Bill_To_Vlaue_1:")

def a3f():
    pyperclip.copy("Ship_To_1: ")

def a4f():
    pyperclip.copy("Ship_To_Vertical_Value_1: ")

def b1f():
    pyperclip.copy("Bill_To_Vertical_1: ")

def b2f():
    pyperclip.copy("Bill_To_Vertical_Value_1:")

def b3f():
    pyperclip.copy("Ship_To_Vertical_1: ")

def b4f():
    pyperclip.copy("Ship_To_Vertical_Value_1: ")

def c1f():
    pyperclip.copy("PO_Number_1: ")

def c2f():
    pyperclip.copy("PO_Number_Value_1: ")

def c3f():
    pyperclip.copy("Proposal_Number_1: ")

def c4f():
    pyperclip.copy("Proposal_Number_Value_1: ")

def d1f():
    pyperclip.copy("Bill_To_1: ")

def d2f():
    pyperclip.copy("Bill_To_Vlaue_1:")

def d3f():
    pyperclip.copy("Quote_Number_1: ")

def d4f():
    pyperclip.copy("Quote_Number_Value_1: ")

def e1f():
    pyperclip.copy("Bill_To_Vertical_1: ")

def e2f():
    pyperclip.copy("Bill_To_Vertical_Value_1:")

def e3f():
    pyperclip.copy("Ship_To_Vertical_1: ")

def e4f():
    pyperclip.copy("Ship_To_Vertical_Value_1: ")

def f1f():
    pyperclip.copy("PO_Number_1: ")

def f2f():
    pyperclip.copy("PO_Number_Value_1: ")

def f3f():
    pyperclip.copy("Proposal_Number_1: ")

def f4f():
    pyperclip.copy("Proposal_Number_Value_1: ")


a1=tkinter.Button(text="Bill_To_1:")
a1.config(height=1,width=20,command=a1f)
a1.grid(row=0, column=0)
a2=tkinter.Button(text="Bill_To_Vlaue_1:")
a2.config(height=1,width=20,command=a2f)
a2.grid(row=0, column=1)
a3=tkinter.Button(text="Ship_To_1:")
a3.config(height=1,width=20,command=a3f)
a3.grid(row=0, column=2)
a4=tkinter.Button(text="Ship_To_Value_1:")
a4.config(height=1,width=20,command=a4f)
a4.grid(row=0, column=3)

b1=tkinter.Button(text="Bill_To_Vertical_1:")
b1.config(height=1,width=20,command=b1f)
b1.grid(row=1, column=0)
b2=tkinter.Button(text="Bill_To_Vertical_Value_1:")
b2.config(height=1,width=20,command=b2f)
b2.grid(row=1, column=1)
b3=tkinter.Button(text="Ship_To_Vertical_1:")
b3.config(height=1,width=20,command=b3f)
b3.grid(row=1, column=2)
b4=tkinter.Button(text="Ship_To_Vertical_Value_1:")
b4.config(height=1,width=20,command=b4f)
b4.grid(row=1, column=3)

c1=tkinter.Button(text="PO_Number_1:")
c1.config(height=1,width=20,command=b1f)
c1.grid(row=2, column=0)
c2=tkinter.Button(text="PO_Number_Value_1:")
c2.config(height=1,width=20,command=b2f)
c2.grid(row=2, column=1)
c3=tkinter.Button(text="Proposal_Number_1: ")
c3.config(height=1,width=20,command=b3f)
c3.grid(row=2, column=2)
c4=tkinter.Button(text="Proposal_Number_Value_1: ")
c4.config(height=1,width=20,command=b4f)
c4.grid(row=2, column=3)

d1=tkinter.Button(text="Quote_Number_1:")
d1.config(height=1,width=20,command=b1f)
d1.grid(row=3, column=0)
d2=tkinter.Button(text="Quote_Number_Value_1:")
d2.config(height=1,width=20,command=b2f)
d2.grid(row=3, column=1)
d3=tkinter.Button(text="Contract_Number_1:")
d3.config(height=1,width=20,command=b3f)
d3.grid(row=3, column=2)
d4=tkinter.Button(text="Contract_Number_Value_1:")
d4.config(height=1,width=20,command=b4f)
d4.grid(row=3, column=3)

tkinter.mainloop()

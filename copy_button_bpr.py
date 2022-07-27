
import tkinter
import pip

#pip.main(["install", "--user", "pyperclip"])

import pyperclip

vinay=tkinter.Frame()
vinay.master.title("BPR click to copy")

def a1f():
    pyperclip.copy("Bill_To_1: ")
def a2f():
    pyperclip.copy("Bill_To_Value_1: ")
def a3f():
    pyperclip.copy("Ship_To_1: ")
def a4f():
    pyperclip.copy("Ship_To_Value_1: ")

def b1f():
    pyperclip.copy("Bill_To_Vertical_1: ")
def b2f():
    pyperclip.copy("Bill_To_Vertical_Value_1: ")
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
    pyperclip.copy("Quote_Number_1: ")
def d2f():
    pyperclip.copy("Quote_Number_Value_1: ")
def d3f():
    pyperclip.copy("Contract_Number_1: ")
def d4f():
    pyperclip.copy("Contract_Number_Value_1: ")

def e1f():
    pyperclip.copy("Product_Number_1: ")
def e2f():
    pyperclip.copy("Product_Number_Value_1: ")
def e3f():
    pyperclip.copy("Description_1: ")
def e4f():
    pyperclip.copy("Description_Value_1: ")


def f1f():
    pyperclip.copy("Quantity_1: ")
def f2f():
    pyperclip.copy("Quantity_Value_1: ")
def f3f():
    pyperclip.copy("Unit_Price_1: ")
def f4f():
    pyperclip.copy("Unit_Price_Value_1: ")

def g1f():
    pyperclip.copy("Extended_Product_Price_1: ")
def g2f():
    pyperclip.copy("Extended_Product_Price_Value_1: ")
def g3f():
    pyperclip.copy("Total_Amount_1: ")
def g4f():
    pyperclip.copy("Total_Amount_Value_1: ")

def h1f():
    pyperclip.copy("Customer_email_1: ")
def h2f():
    pyperclip.copy("Customer_email_Value_1: ")
def h3f():
    pyperclip.copy("Attention_(Contact Name)_1: ")
def h4f():
    pyperclip.copy("Attention_(Contact Name)_Value_1: ")


a1=tkinter.Button(text="Bill_To_1:")
a1.config(height=1,width=20,command=a1f)
a1.grid(row=0, column=0)
a2=tkinter.Button(text="Bill_To_Value_1:")
a2.config(height=1,width=20,command=a2f)
a2.grid(row=0, column=1)
a3=tkinter.Button(text="Ship_To_1:")
a3.config(height=1,width=20,command=a3f)
a3.grid(row=0, column=2)
a4=tkinter.Button(text="Ship_To_Value_1:")
a4.config(height=1,width=20,command=a4f)
a4.grid(row=0, column=3)

b1=tkinter.Button(text="Bill_To_Vertical_1:")
b1.config(height=1,width=20,command=b1f, background='sky blue')
b1.grid(row=1, column=0)
b2=tkinter.Button(text="Bill_To_Vertical_Value_1:")
b2.config(height=1,width=20,command=b2f, background='sky blue')
b2.grid(row=1, column=1)
b3=tkinter.Button(text="Ship_To_Vertical_1:")
b3.config(height=1,width=20,command=b3f, background='sky blue')
b3.grid(row=1, column=2)
b4=tkinter.Button(text="Ship_To_Vertical_Value_1:")
b4.config(height=1,width=20,command=b4f, background='sky blue')
b4.grid(row=1, column=3)

c1=tkinter.Button(text="PO_Number_1:")
c1.config(height=1,width=20,command=c1f)
c1.grid(row=2, column=0)
c2=tkinter.Button(text="PO_Number_Value_1:")
c2.config(height=1,width=20,command=c2f)
c2.grid(row=2, column=1)
c3=tkinter.Button(text="Proposal_Number_1: ")
c3.config(height=1,width=20,command=c3f)
c3.grid(row=2, column=2)
c4=tkinter.Button(text="Proposal_Number_Value_1: ")
c4.config(height=1,width=20,command=c4f)
c4.grid(row=2, column=3)

d1=tkinter.Button(text="Quote_Number_1:")
d1.config(height=1,width=20,command=d1f, background='sky blue')
d1.grid(row=3, column=0)
d2=tkinter.Button(text="Quote_Number_Value_1:")
d2.config(height=1,width=20,command=d2f, background='sky blue')
d2.grid(row=3, column=1)
d3=tkinter.Button(text="Contract_Number_1:")
d3.config(height=1,width=20,command=d3f, background='sky blue')
d3.grid(row=3, column=2)
d4=tkinter.Button(text="Contract_Number_Value_1:")
d4.config(height=1,width=20,command=d4f, background='sky blue')
d4.grid(row=3, column=3)

e1=tkinter.Button(text="Product_Number_1:")
e1.config(height=1,width=20,command=e1f)
e1.grid(row=4, column=0)
e2=tkinter.Button(text="Product_Number_Value_1:")
e2.config(height=1,width=20,command=e2f)
e2.grid(row=4, column=1)
e3=tkinter.Button(text="Description_1:")
e3.config(height=1,width=20,command=e3f)
e3.grid(row=4, column=2)
e4=tkinter.Button(text="Description_Value_1:")
e4.config(height=1,width=20,command=e4f)
e4.grid(row=4, column=3)

f1=tkinter.Button(text="Quantity_1:")
f1.config(height=1,width=20,command=f1f, background='sky blue')
f1.grid(row=5, column=0)
f2=tkinter.Button(text="Quantity_Value_1:")
f2.config(height=1,width=20,command=f2f, background='sky blue')
f2.grid(row=5, column=1)
f3=tkinter.Button(text="Unit_Price_1:")
f3.config(height=1,width=20,command=f3f, background='sky blue')
f3.grid(row=5, column=2)
f4=tkinter.Button(text="Unit_Price_Value_1:")
f4.config(height=1,width=20,command=f4f, background='sky blue')
f4.grid(row=5, column=3)

g1=tkinter.Button(text="Extended_Product_Price_1:")
g1.config(height=1,width=20,command=g1f)
g1.grid(row=6, column=0)
g2=tkinter.Button(text="Extended_Product_Price_Value_1:")
g2.config(height=1,width=20,command=g2f)
g2.grid(row=6, column=1)
g3=tkinter.Button(text="Total_Amount_1:")
g3.config(height=1,width=20,command=g3f)
g3.grid(row=6, column=2)
g4=tkinter.Button(text="Total_Amount_Value_1:")
g4.config(height=1,width=20,command=g4f)
g4.grid(row=6, column=3)

h1=tkinter.Button(text="Customer_email_1:")
h1.config(height=2,width=20,command=h1f, background='sky blue')
h1.grid(row=7, column=0)
h2=tkinter.Button(text="Customer_email_Value_1:")
h2.config(height=2,width=20,command=h2f, background='sky blue')
h2.grid(row=7, column=1)
h3=tkinter.Button(text="Attention_(Contact Name)_1:")
h3.config(height=2,width=20,command=h3f, background='sky blue')
h3.grid(row=7, column=2)
h4=tkinter.Button(text="Attention_(Contact \n Name)_Value_1:")
h4.config(height=2,width=20,command=h4f, background='sky blue')
h4.grid(row=7, column=3)

tkinter.mainloop()

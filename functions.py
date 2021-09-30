from math import *
import testing as tk
from tkinter import *
from m import check
def nfactorial(k):# function for computing factorial
    t = k
    k  = 1
    for i in range(1,t+1):
        k *= i
    return k

def ncr(a, b):#ncr function n =a , r=b
    if isinstance(a, float) or isinstance(b, float):
        raise ValueError from None
    t = int(a)-int(b)#computing n-r
    if a < 0 or b < 0 or t < 0:
        raise ValueError from None 
    c = max(b, t)    #Calculates max value between b and t
    d = min(b, t)    #Calculates min value between b and t
    n1 = 1
    for i in range(a, c, -1):
        n1 *= i
    n2 = nfactorial(d)
    n3 = n1/n2
    return n3

def npr(a, b):
    if isinstance(a, float) or isinstance(b, float):
        raise ValueError from None
    n1 = nfactorial(int(a))#computing n!
    t = int(a)-int(b)#computing n-r
    if a < 0 or b < 0 or t < 0:
        raise ValueError from None
    n3 = nfactorial(t)#computing n-r!
    return n1/n3#npr result

def e_value():
    tk.en.insert(len(tk.en.get()), 'e')# e value of 2.718281828459045

def modulo():
    if tk.obj.op <= 2:# checking whether number entered is less than 2
        tk.obj.op = 0
    tk.en.insert(len(tk.en.get()), '%')# modulus function

def backspace():
    tk.en.delete(len(tk.en.get())-1, END)# deleting the last character of the display

def power():
    check()
    tk.en.insert(len(tk.en.get()), 'pow(')#inserting str pow( ) for power function

def facto():
    check()
    tk.en.insert(len(tk.en.get()), '!')#inserting ! symbol whenever n! is clicked
def nCr_append():
    check()
    tk.en.insert(len(tk.en.get()), 'C')#inserting C after n is entered 
def nPr_append():
    check()
    tk.en.insert(len(tk.en.get()), 'P')# inserting P after n is inserted
def nroot(a, b):
    check()#checking whether it is less than 2
    return float(a) ** (1/float(b))# computing nth root where a represents 
def modulus():
    tk.en.insert(len(tk.en.get()),'abs(')

def add():
    tk.obj.op += 1# whenever the operators are used this is incremented
    tk.en.insert(len(tk.en.get()), '+')#inserting the respective operator
    
def sub():
    tk.obj.op += 1
    tk.en.insert(len(tk.en.get()), '-')

def mul():
    tk.obj.op += 1
    tk.en.insert(len(tk.en.get()), '*')

def div():
    tk.obj.op += 1
    tk.en.insert(len(tk.en.get()), '/')

def expo():
    tk.en.insert(len(tk.en.get()), 'E')

def repeat():
    tk.obj.error_check()#checks whether there is an error 
    tk.obj.f = Frame(tk.root, padx=30, pady=10, bg="black")
    tk.obj.f.grid(row=6, column=0)
    mylabel = Label(tk.obj.f, text='INVALID INPUT', font=('arial',20,'bold'), fg="red", bg="black").grid(row=6, column=0)
    tk.obj.err = 1#ERROR MESSAGE :INVALID INPUT is dispalyed whenever the invalid input is entered

def d_to_d():
    try:
        o = 0
        c = int(tk.en.get())
        tk.en.delete(0, END)
    except:
        o = 1
    try :
        if o == 0:
            tk.en.insert(0,str(c))
        else:
            raise SyntaxError from None
    except SyntaxError:
        repeat()

def b_to_b():
    try:
        o = 0
        c = bin(int(tk.en.get(), 2))
        tk.en.delete(0, END)
    except:
        o = 1
    try :
        if o == 0:
            tk.en.insert(0,str(c))
        else:
            raise SyntaxError from None
    except SyntaxError:
        repeat()

def d_to_o():
    try:# o=1 becomes one whenever there is an error in the input
        o = 0
        c = oct(int(tk.en.get()))# int() converts the string to the integer and then the oct() converts it into the octal
        tk.en.delete(0, END)#deleting the entire string
    except:
        o = 1
    try :
        if o == 0:
            tk.en.insert(0,str(c))# inserting the new computed value
        else:
            raise SyntaxError from None
    except SyntaxError:
        repeat()# this function is called whenever there's an error
def d_to_b():
    try:
        o = 0
        c = bin(int(tk.en.get()))
        tk.en.delete(0, END)
    except:
        o = 1
    try:
        if o == 0:
            tk.en.insert(0,str(c))
        else:
            raise SyntaxError from None
    except SyntaxError:
        repeat()
def d_to_h():
    try:
        o = 0
        c = hex(int(tk.en.get())).swapcase()
        c = c[0] + 'x' + c[2:]
        tk.en.delete(0, END)
    except:
        o = 1
    try:
        if o == 0:
            tk.en.insert(0,str(c))
        else:
            raise SyntaxError from None
    except SyntaxError:
        repeat()
def o_to_b():
    try:
        o = 0
        c = bin(int(tk.en.get(),8))
        tk.en.delete(0, END)
    except:
        o = 1
    try:
        if o == 0:
            tk.en.insert(0,str(c))
        else:
            raise SyntaxError from None
    except SyntaxError:
        repeat()
def o_to_h():
    try:
        o = 0
        c = hex(int(tk.en.get(),8)).swapcase()
        c = c[0] + 'x' + c[2:]
        tk.en.delete(0, END)
    except:
        o = 1
    try:
        if o == 0:
            tk.en.insert(0,str(c))
        else:
            raise SyntaxError from None
    except SyntaxError:
        repeat()
def o_to_d():
    try:
        o = 0
        c = int(tk.en.get(),8)
        tk.en.delete(0, END)
    except:
        o = 1
    try:
        if o == 0:
            tk.en.insert(0,str(c))
        else:
            raise SyntaxError from None
    except SyntaxError:
        repeat()
        
def logarithm():#computing logarithm for any base
    if tk.obj.op <= 2:
        tk.obj.op = 0
    tk.en.insert(len(tk.en.get()), 'log(') # inserting str log( for computing the logarithm
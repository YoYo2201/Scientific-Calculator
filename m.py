from math import *
from tkinter import *
import testing as tk

def check():
    if tk.obj.op <= 2:
        tk.obj.op = 0
    
def _sin_():
    check()
    tk.en.insert(len(tk.en.get()), 'sin(')
def _cos_():
    check()
    tk.en.insert(len(tk.en.get()), 'cos(')
def _tan_():
    check()
    tk.en.insert(len(tk.en.get()), 'tan(')
def _asin_():
    check()
    tk.en.insert(len(tk.en.get()), 'asin(')
def _acos_():
    check()
    tk.en.insert(len(tk.en.get()), 'acos(')
def _atan_():
    check()
    tk.en.insert(len(tk.en.get()), 'atan(')
def po():
    check()
    tk.en.insert(len(tk.en.get()), '(')
def pc():
    check()
    tk.en.insert(len(tk.en.get()), ')')
def _pi_():
    tk.en.insert(len(tk.en.get()), 'π')
def dec():
    check()
    tk.en.insert(len(tk.en.get()), '.')
def degree():
    check()
    tk.en.insert(len(tk.en.get()), '\u00B0')
def comma():
    check()
    tk.en.insert(len(tk.en.get()), ',')
def sqrt():
    check()
    tk.en.insert(len(tk.en.get()), '\u221A')
def nth_root():
    check()
    tk.en.insert(len(tk.en.get()), 'nroot(')

def repeat():
    tk.obj.error_check()
    tk.obj.f = Frame(tk.root, padx=30, pady=10, bg="black")
    tk.obj.f.grid(row=6, column=0)
    mylabel = Label(tk.obj.f, text='INVALID INPUT', font=('arial',20,'bold'), fg="red", bg="black").grid(row=6, column=0)
    tk.obj.err = 1

def o_to_o():
    try:
        o = 0
        c = oct(int(tk.en.get(), 8))
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

def h_to_h():
    try:
        o = 0
        c = hex(int(tk.en.get(), 16)).swapcase()
        c = c[0] + 'x' + c[2:]
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

def h_to_d():
    try:
        o = 0
        c = int(tk.en.get(),16)
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
def h_to_o():
    try:
        o = 0
        c = oct(int(tk.en.get(),16))
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

def h_to_b():
    try:
        o = 0
        c = bin(int(tk.en.get(),16))
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

def b_to_d():
    try:
        o = 0
        c = int(tk.en.get(),2)
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

def b_to_o():
    try:
        o = 0
        c = oct(int(tk.en.get(),2))
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

def b_to_h():
    try:
        o = 0
        c = hex(int(tk.en.get(),2)).swapcase()
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

def cli(n):  # for hexadecimal digits
    curr=tk.en.get()
    tk.en.delete(0,END)
    curr=str(curr) + str(n)
    tk.en.insert(0, curr)
    
def conv_equal():
    FROM = tk.obj.from_drop.get()
    TO = tk.obj.to_drop.get()
    if FROM == 'Select' or TO == 'Select':
        tk.obj.error_check()
        tk.obj.f = Frame(tk.root, padx=30, pady=10, bg="black")
        tk.obj.f.grid(row=6, column=0)
        mylabel = Label(tk.obj.f, text='PLEASE SELECT A CONVERSION', font=('arial',20,'bold'), fg="red", bg="black").grid(row=6, column=0)
        tk.obj.err = 1
    elif FROM == 'Decimal' and TO == 'Decimal':
        from functions import d_to_d
        d_to_d()
    elif FROM == 'Decimal' and TO == 'Binary':
        from functions import d_to_b
        d_to_b()
    elif FROM == 'Decimal' and TO == 'Octal':
        from functions import d_to_o
        d_to_o()
    elif FROM == 'Decimal' and TO == 'HexaDecimal':
        from functions import d_to_h
        d_to_h()
    elif FROM == 'Binary' and TO == 'Binary':
        from functions import b_to_b
        b_to_b()
    elif FROM == 'Binary' and TO == 'Decimal':
        b_to_d()
    elif FROM == 'Binary' and TO == 'Octal':
        b_to_o()
    elif FROM == 'Binary' and TO == 'HexaDecimal':
        b_to_h()
    elif FROM == 'Octal' and TO == 'Octal':
        o_to_o()
    elif FROM == 'Octal' and TO == 'Decimal':
        from functions import o_to_d
        o_to_d()
    elif FROM == 'Octal' and TO == 'Binary':
        from functions import o_to_b
        o_to_b()
    elif FROM == 'Octal' and TO == 'HexaDecimal':
        from functions import o_to_h
        o_to_h()
    elif FROM == 'HexaDecimal' and TO == 'HexaDecimal':
        h_to_h()
    elif FROM == 'HexaDecimal' and TO == 'Decimal':
        h_to_d()
    elif FROM == 'HexaDecimal' and TO == 'Binary':
        h_to_b()
    elif FROM == 'HexaDecimal' and TO == 'Octal':
        h_to_o()
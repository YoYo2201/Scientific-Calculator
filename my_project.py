from tkinter import *
from tkinter import ttk
import testing as tk
import m
import functions as func
import tkinter.messagebox

tk.root = Tk()                                      #tk.root is the window created for calculator
tk.root.title("Scientific calculator")
tk.root.configure(background="black")               #background colour for the window
tk.root.resizable(height=FALSE,width=FALSE)         #disabling the resizable feature


class Type():
    def __init__(self):
        self.p = 0
        self.q = 0                             #initializing p and q to zero.Both are set to 1 in converesion method

    def iExit(self):
        iExit = tkinter.messagebox.askyesno("Scientific calculator", "Confirm if you want to exit")
        if iExit == 1:                         #iExit contains the value 1 if clicked on yes
            tk.root.destroy()
            return

    def Scientific(self):
        if tk.obj.err == 1:                    #checking any errors if present and then calling clear method
            tk.obj.clear()
        try:
            if self.q == 0:
                tk.obj.variable = 0
                tk.obj.fr1.destroy()
        except:
            pass
        self.curr = str(tk.en.get())                #To get the current value in entry widget
        self.calc.destroy()                         #destroying the frame of buttons
        self.fr.destroy()                           #destroying the entry widget frame
        self.fr = Frame(tk.root, bg="black")
        self.fr.grid(row=0, column=0)
        tk.en = Entry(self.fr, font=('arial', 20, 'bold'), bd=30, width=62, justify=LEFT)
        tk.en.grid(row=0, column=0, columnspan=8)
        tk.en.bind("<Key>", tk.obj.check_for_enter)
        tk.en.insert(0, self.curr)
        self.Buttons()                              #creating the buttons of standard calculator in scientific one

        #creating buttons for scientific calculator
        Pi_btn = Button(self.calc, text='π', width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="black",
                        fg='white', command=m._pi_).grid(row=1, column=4, pady=1)
        cos_btn = Button(self.calc, text='cos', width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="black",
                         fg='white', command=m._cos_).grid(row=1, column=5, pady=1)
        tan_btn = Button(self.calc, text='tan', width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="black",
                         fg='white', command=m._tan_).grid(row=1, column=6, pady=1)
        sin_btn = Button(self.calc, text='sin', width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="black",
                         fg='white', command=m._sin_).grid(row=1, column=7, pady=1)

        e_btn = Button(self.calc, text='e', width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="black", fg='white',
                       command=func.e_value).grid(row=2, column=4, pady=1)
        acos_btn = Button(self.calc, text='acos', width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg='black',
                          fg='white', command=m._acos_).grid(row=2, column=5, pady=1)
        atan_btn = Button(self.calc, text='atan', width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg='black',
                          fg='white', command=m._atan_).grid(row=2, column=6, pady=1)
        asin_btn = Button(self.calc, text='asin', width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg='black',
                          fg='white', command=m._asin_).grid(row=2, column=7, pady=1)

        nCr_btn = Button(self.calc, text='nCr', width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="black",
                         fg='white', command=func.nCr_append).grid(row=3, column=4, pady=1)
        exp_btn = Button(self.calc, text='exp', width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg='black',
                         fg='white', command=func.expo).grid(row=3, column=5, pady=1)
        mod_btn = Button(self.calc, text='mod', width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg='black',
                         fg='white',command=func.modulus).grid(row=3, column=6, pady=1)
        fact_btn = Button(self.calc, text='!', width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg='black',
                          fg='white', command=func.facto).grid(row=3, column=7, pady=1)

        nPr_btn = Button(self.calc, text='nPr', width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="black",
                         fg='white', command=func.nPr_append).grid(row=4, column=4, pady=1)
        deg_btn = Button(self.calc, text='deg', width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg='black',
                         fg='white', command=m.degree).grid(row=4, column=5, pady=1)
        comma_btn = Button(self.calc, text=',', width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg='black',
                           fg='white', command=m.comma).grid(row=4, column=6, pady=1)
        pwr_btn = Button(self.calc, text='pow', width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg='black',
                         fg='white', command=func.power).grid(row=4, column=7, pady=1)

        log_btn = Button(self.calc, text='log', width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="black",
                         fg='white', command=func.logarithm).grid(row=5, column=4, pady=1)
        nth_root_btn = Button(self.calc, text='nth root', width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                              bg="black", fg='white', command=m.nth_root).grid(row=5, column=5, pady=1)
        obrac_btn = Button(self.calc, text='(', width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="black",
                           fg='white', command=m.po).grid(row=5, column=6, pady=1)
        cbrac_btn = Button(self.calc, text=')', width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="black",
                           fg='white', command=m.pc).grid(row=5, column=7, pady=1)

    def sel(self):
        #some of the buttons for Standard calculator
        sqrt_btn = Button(self.calc, text='\u221A', width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                          bg="black", fg='white', command=m.sqrt).grid(row=1, column=2, pady=1)
        add_btn = Button(self.calc, text='+', width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                         bg="black", fg='white', command=func.add).grid(row=1, column=3, pady=1)
        sub_btn = Button(self.calc, text='-', width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                         bg="black", fg='white', command=func.sub).grid(row=2, column=3, pady=1)
        mul_btn = Button(self.calc, text='x', width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                         bg="black", fg='white', command=func.mul).grid(row=3, column=3, pady=1)
        div_btn = Button(self.calc, text='/', width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                         bg="black", fg='white', command=func.div).grid(row=4, column=3, pady=1)
        Per_btn = Button(self.calc, text='%', width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                         bg="black", fg='white', command=func.modulo).grid(row=5, column=2, pady=1)

    def alpha_sel(self):
        #Buttons for the conversion part
        A_btn = Button(self.calc, text='A', width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                       bg="black", fg='white', command=lambda: m.cli('A')).grid(row=1 + self.q, column=2, pady=1)
        B_btn = Button(self.calc, text='B', width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                       bg="black", fg='white', command=lambda: m.cli('B')).grid(row=1 + self.q, column=3, pady=1)
        C_btn = Button(self.calc, text='C', width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                       bg="black", fg='white', command=lambda: m.cli('C')).grid(row=2 + self.q, column=3, pady=1)
        D_btn = Button(self.calc, text='D', width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                       bg="black", fg='white', command=lambda: m.cli('D')).grid(row=3 + self.q, column=3, pady=1)
        E_btn = Button(self.calc, text='E', width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                       bg="black", fg='white', command=lambda: m.cli('E')).grid(row=4 + self.q, column=3, pady=1)
        F_btn = Button(self.calc, text='F', width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                       bg="black", fg='white', command=lambda: m.cli('F')).grid(row=5 + self.q, column=2, pady=1)

    def Buttons(self):
        self.calc = Frame(tk.root, bg='black')
        self.calc.grid(row=1 + self.q, column=0)
        nums = "789456123"
        i = 0
        num_btn = []                                    #empty list for appending buttons(from 1 to 9) into it
        for j in range(2, 5):
            for k in range(3):
                num_btn.append(
                    Button(self.calc, width=6, height=2, font=('arial', 20, 'bold'), fg='white', bg="black", bd=4,
                           text=nums[i]))
                num_btn[i].grid(row=j + self.q, column=k, pady=1)
                num_btn[i]["command"] = lambda n=nums[i]: tk.obj.click(n)
                i += 1

        Backspace_btn = Button(self.calc, text='<--', width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                               bg="black", fg='white', command=func.backspace).grid(row=1 + self.q, column=0, pady=1)
        ClearAll_btn = Button(self.calc, text='CE', width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                              bg="black", fg='white', command=tk.obj.clear).grid(row=1 + self.q, column=1, pady=1)
        zero_btn = Button(self.calc, text='0', width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                          bg="black", fg='white', command=lambda: tk.obj.click(0)).grid(row=5 + self.q, column=0,
                                                                                        pady=1)
        dot_btn = Button(self.calc, text='.', width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                         bg="black", fg='white', command=m.dec).grid(row=5 + self.q, column=1, pady=1)
        equal_btn = Button(self.calc, text='=', width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                           bg="black", fg='white', command=tk.obj.equal).grid(row=5 + self.q, column=3, pady=1)
        if self.p == 0:
            self.sel()                              #calling sel method if self.p=0
        else:
            self.p = 0                              #changing self.p=1 to self.p=0
            self.alpha_sel()                        #alpha_sel method is called

    def Standard(self):
        if tk.obj.err == 1:
            tk.obj.clear()                          #if error(variable->err) has value one we call clear function
        try:
            self.curr = str(tk.en.get())
        except:
            pass
        try:
            self.calc.destroy()
            self.fr.destroy()
        except AttributeError:
            pass
        try:
            if self.q == 0:
                tk.obj.variable = 0
                tk.obj.fr1.destroy()
        except:
            pass
        self.fr = Frame(tk.root, bg="black")         #recreating fr frame for making the entry widget
        self.fr.grid(row=0 + self.q, column=0)
        tk.en = Entry(self.fr, font=('arial', 20, 'bold'), bd=30, width=29, justify=LEFT)
        tk.en.grid(row=0 + self.q, column=0, columnspan=4, pady=1)
        tk.en.bind("<Key>", tk.obj.check_for_enter)  #binding the key pressed from keyboard to check_for_enter method
        try:
            tk.en.insert(0, self.curr)
        except AttributeError:
            pass
        self.Buttons()

    def Conversion(self):
        if tk.obj.err == 1:
            tk.obj.clear()
        try:
            self.curr = str(tk.en.get())
            self.fr.destroy()
        except:
            pass
        self.p = 1                                    #"p" and "variable" are set to 1 for the method Conversion
        tk.obj.variable = 1
        tk.obj.fr1 = Frame(tk.root)
        tk.obj.fr1.grid(row=0, column=0)
        Label(tk.obj.fr1, text=' From: ', font=('arial', 18, 'bold'),
              fg='white', bg='black').grid(row=0, column=0)
        tk.obj.from_drop = ttk.Combobox(tk.obj.fr1, value=["Select", "Decimal", "Binary", "Octal", "HexaDecimal"])
        tk.obj.from_drop.current(0)                #creating the dropdown box and setting its initial value to "Select"
        tk.obj.from_drop.grid(row=0, column=1)
        Label(tk.obj.fr1, text=' To: ', font=('arial', 18, 'bold'),
              fg='white', bg='black').grid(row=0, column=2)
        tk.obj.to_drop = ttk.Combobox(tk.obj.fr1, value=["Select", "Decimal", "Binary", "Octal", "HexaDecimal"])
        tk.obj.to_drop.current(0)
        tk.obj.to_drop.grid(row=0, column=3)
        self.q = 1                                  #q is set to 1 in this method
        self.Standard()
        self.q = 0


objd = Type()
objd.Standard()                                      #calling the Standard method
menubar = Menu(tk.root)                              #creating a Menu in root window
filemenu = Menu(menubar, tearoff=0)                  #creating a filemenu inside menu bar
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Standard", command=objd.Standard)
filemenu.add_command(label="Scientific calculator", command=objd.Scientific)
filemenu.add_command(label="Conversion", command=objd.Conversion)          #addition of commands
filemenu.add_separator()
filemenu.add_command(label="Exit", command=objd.iExit)
Editmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=Editmenu)
Editmenu.add_command(label="Cut")
Editmenu.add_command(label="Copy")
Editmenu.add_separator()                             #adding a seperator line between commands
Editmenu.add_command(label="Paste")
helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="View Help")
tk.root.config(menu=menubar)
tk.root.mainloop()
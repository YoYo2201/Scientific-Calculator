from math import *    # math module is imported
from tkinter import *       # tkinter module is imported
from functions import ncr          # ncr() is imported from functions.py
from functions import npr          # npr() is imported from functions.py
from functions import nroot        # nroot() is imported from functions.py
en = 0         # used as an object for Entry field
root = 0      # used as an object for main frame
class Calculator():
    def __init__(self):          # Constructor for class Calculator
        self.c = 0       # used to store strings which we get from entry field
        self.op = 0             # used to count the number of times an operator is clicked in continuous manner 
        self.err = 0       # used to check if there is an error or not
        self.variable = 0         # used to check if conversion window is active or not
        self.fr1 = 0        # used as a frame in conversion window
        self.from_drop = 0        # used as a frame for combobox
        self.to_drop = 0          # used as a frame for combobox
        self.check = 0
    
    def error_check(self):      # destroys the error frame if it is active
        try:
            self.f.destroy()
        except AttributeError:
            pass

    def click(self, n):          # To insert the digits in the entry field of calculator
        if self.op <= 2:   # If the number of times an operator is clicked is less than or equal to 2....
            self.op = 0
        curr = en.get()    # The string from the entry field is stored in the variable curr
        en.delete(0, END)     # The string present in the entry field is deleted
        curr = str(curr) + str(n)
        en.insert(0, curr)
    
    def error(self):    # If any of the error occurs which is unexpected and not known then this function will be called...
        self.error_check()
        self.f = Frame(root, padx=30, pady=10, bg="black")
        self.f.grid(row=6, column=0)
        label = Label(self.f, text='ERROR', font=('arial',20,'bold'), fg="red", bg="black").grid(row=6, column=0)
        self.err = 1

    def check_for_pi(self, c):
        for i in c:
            if i == 'π':
                c = c.replace(i, '3.141592653589793')    # Replaces the symbol π with 'pi' to compute the value
                break
        return c
    
    def fact_condition(self, c, g, k, i):     # A sub-function of check_for_factorial()
        if g == 1:
            c = c[:k+1] + "gamma(1+" + c[k+1:]       # If the number is floating then gamma(1+n) must be calculated
            i += 7
        else:
            c = c[:k+1] + "factorial(" + c[k+1:]     # If the number is integral then factorial of that number must be calculated
            i += 9
        return c

    def check_for_factorial(self, c):    # checks if the expression in the entry field contains symbol of factorial, i.e, '!'
        i = 0
        while(1):
            g = 0   # initializes to one if factorial of a floating number is to be calculated
            var = 0
            if i >= len(c):
                break
            if c[i] == '!':
                j = i - 1
                c = c.replace(c[i], ')', 1)    # replaces '!' with ')' (one at a time)
                try:
                    if isinstance(int(c[j]), int):      # checks if the character of the string can be converted into integer or not
                        for k in range(j, -1, -1):
                            if c[k] == '.':
                                g = 1
                            elif True:
                                try:
                                    isinstance(int(c[k]), int)
                                except ValueError:
                                    c = self.fact_condition(c, g, k, i)
                                    break
                            if k == 0:     # If the control reaches at the start of the string
                                if g == 1:
                                    c = "gamma(1+" + c[:]
                                    i += 7 
                                else:
                                    c = "factorial(" + c[:]
                                    i += 9
                                break
                            else:
                                pass
                    else:
                        pass
                except ValueError:         # If the character can't be converted into integer...
                    for k in range(j, -1, -1):
                        if c[k] == ')':
                            var += 1
                        elif c[k] == '(':
                            var -= 1
                        elif c[k] == '.':
                            g = 1
                        if var == 0:
                            c = self.fact_condition(c, g, k, i)
                            break
                except IndexError:
                    self.exc()         # Function which displays error when syntax is wrong
                except:
                    self.error()
            i += 1
        return c

    def check_for_degree(self, c):       # Checks if the degree symbol is used to calculate value from degree into radians
        i = 0
        while(1):
            if i >= len(c):
                break
            var = 0
            if c[i] == '\u00B0':
                j = i - 1
                c = c.replace(c[i], ')', 1)    # Replaces degree symbol with ')'
                try:
                    if isinstance(int(c[j]), int):     # checks if the character of the string can be converted into integer or not
                        for k in range(j, -1, -1):
                            if c[k] == '.':
                                pass
                            elif True:
                                try:
                                    isinstance(int(c[k]), int)
                                except ValueError:
                                    c = c[:k+1] + "radians(" + c[k+1:]        # Adds 'radians(' at appropriate place to make it look like : radians(n)
                                    i += 7
                                    break
                            if k == 0:
                                c = "radians(" + c[:]
                                i += 7
                                break
                            else:
                                pass
                    else:
                        pass
                except ValueError:              # If the character can't be converted into integer...
                    for k in range(j, -1, -1):
                        if c[k] == ')':
                            var += 1
                        elif c[k] == '(':
                            var -= 1
                        if var == 0:
                            c = c[:k+1] + "radians(" + c[k+1:]
                            i += 7
                            break
                except IndexError:
                    self.exc()
                except:
                    self.error()
            i += 1
        return c
    
    def per_or_com(self, p, q, c):          # checks if user wants to calculate permutation/combination
        i = 0
        while(1):
            if i >= len(c):
                break
            var = 0
            if c[i] == p:        # p will be either 'C' or 'P'
                j = i - 1
                c = c.replace(c[i], ',', 1)
                try:              # For the first part of nCr/nPr
                    if isinstance(int(c[j]), int):     # checks if the character of the string can be converted into integer or not
                        for k in range(j, -1, -1):
                            if c[k] == '.':
                                pass
                            elif True:
                                try:
                                    isinstance(int(c[k]), int)
                                except ValueError:
                                    c = c[:k+1] + q + c[k+1:]         # q will be either 'ncr(' or 'npr(' ...     { based on the names of the functions in functions.py }
                                    i += 4
                                    break
                            if k == 0:
                                c = q + c[:]
                                i += 4
                                break
                            else:
                                pass
                except ValueError:                     # If the character can't be converted into integer...
                    for k in range(j, -1, -1):
                        if c[k] == ')':
                            var += 1
                        elif c[k] == '(':
                            var -= 1
                        if var == 0:
                            c = c[:k] + q + c[k:]
                            i += 4
                            break
                except IndexError:
                    self.exc()
                except:
                    self.error()
                j = i + 1
                try:           # For the second part of nCr/nPr
                    if isinstance(int(c[j]), int):        # checks if the character of the string can be converted into integer or not
                        for k in range(j, len(c)):
                            if c[k] == '.':
                                pass
                            elif True:
                                try:
                                    isinstance(int(c[k]), int)
                                except ValueError:
                                    c = c[:k] + ")" + c[k:]
                                    i = k + 1
                                    break
                            if k == (len(c) - 1):
                                c = c[:] + ")"
                                i = k + 1
                                break
                            else:
                                pass 
                except ValueError:                     # If the character can't be converted into integer...
                    for k in range(j, len(c)):
                        if c[k] == ')':
                            var += 1
                        elif c[k] == '(':
                            var -= 1
                        if var == 0:
                            c = c[:k] + ")" + c[k:]
                            i = k + 1
                            break
                except IndexError:
                    self.exc()
                except:
                    self.error()
            i += 1
        return c

    def check_for_combination(self, c):          # When nCr is to be calculated
        p = 'C'
        q = "ncr("
        c = self.per_or_com(p, q, c)
        return c
    
    def check_for_permutation(self, c):        # When nPr is to be calculated
        p = 'P'
        q = "npr("
        c = self.per_or_com(p, q, c)
        return c

    def check_for_root(self, c):        # When square root is to be calculated
        i = 0
        while(1):
            if i >= len(c):
                break
            var = 0
            if c[i] == '\u221A':
                c = c.replace(c[i], '(', 1)         # Replaces the symbol of square root with '('
                if i == 0:
                    c = "nroot" + c[:]         # nroot() is function defined in functions.py
                else:
                    c = c[:i] + "nroot" + c[i:]
                i += 5
                j = i + 1
                try:
                    if isinstance(int(c[j]), int):      # checks if the character of the string can be converted into integer or not
                        for k in range(j, len(c)):
                            if c[k] == '.':
                                pass
                            elif True:
                                try:
                                    isinstance(int(c[k]), int)
                                except ValueError:
                                    c = c[:k] + ",2)" + c[k:]     # As square root is to be calculated, so ',2)' is added in the string so that it looks like nroot(n, 2)
                                    i = k + 3
                                    break
                            if k == (len(c) - 1):
                                c = c[:] + ",2)"
                                i = k + 3
                                break
                            else:
                                pass
                except ValueError:                      # If the character can't be converted into integer...
                    for k in range(j, len(c)):
                        if c[k] == '(':
                            var += 1
                        elif c[k] == ')':
                            var -= 1
                        if var == 0:
                            c = c[:k+1] + ",2)" + c[k+1:]
                            i = k + 2
                            break
                except IndexError:
                    self.exc()
                except:
                    self.error()
                
            i += 1
        return c

    def index(self, c):
        c = self.check_for_pi(c)
        c = self.check_for_degree(c)
        c = self.check_for_factorial(c)
        c = self.check_for_combination(c)
        c = self.check_for_permutation(c)
        c = self.check_for_root(c)
        self.check = 0
        if self.err == 1:
            self.err = 0
            self.f.destroy()
        try:
            eval(c)
            en.delete(0, END)
        except:
            pass
        try:
            if str(float(eval(c))) == '-0.0':
                en.insert(0, '0.0')
            else:
                en.insert(0, str(float(eval(c))))    # Calcultion of the expression using eval()...    { built-in function }
        except SyntaxError:
            if len(c) == 0:
                en.insert(0, '0.0')          # If the entry field is empty and when '=' is pressed then it will result into Syntax Error
            elif self.op >= 0:
                self.exc()
        except ZeroDivisionError:     # When expression of type n/0 is performed
            self.error_check()
            self.f = Frame(root, padx=30, pady=10, bg="black")
            self.f.grid(row=6, column=0)
            label = Label(self.f, text='DIVISION BY ZERO IS UNDEFINED', font=('arial',20,'bold'), fg="red", bg="black").grid(row=6, column=0)
            self.err = 1
        except NameError:
            self.exc()
        except TypeError:
            self.exc()
        except ValueError:        # When value is not in domain
            self.error_check()
            self.f = Frame(root, padx=30, pady=10, bg="black")
            self.f.grid(row=6, column=0)
            label = Label(self.f, text='MATH DOMAIN ERROR', font=('arial',20,'bold'), fg="red", bg="black").grid(row=6, column=0)
            self.err = 1
        except OverflowError:       # When a very large value gets after the evaluation
            self.error_check()
            self.f = Frame(root, padx=30, pady=10, bg="black")
            self.f.grid(row=6, column=0)
            label = Label(self.f, text='MATH RANGE ERROR', font=('arial',20,'bold'), fg="red", bg="black").grid(row=6, column=0)
            self.err = 1
        except:
            self.error()

    def calc_equal(self):        # When '=' is pressed in Standard/Scientific Calculator
        if self.op > 2:
            self.exc()
        else:
            c = str(en.get())
            self.index(c)

    def equal(self):      # When '=' is pressed
        if self.variable == 0:
            self.calc_equal()
        else:
            from m import conv_equal
            conv_equal()       # When '=' is pressed in the Conversion Calculator

   # ----------------------Destroys the error frames and clears the Entry Field---------------------------
    def clear(self):      # When 'CE' button is pressed
        if self.op >= 0:
            self.error_check()
        if self.err == 1:
            self.err = 0
            self.f.destroy()
        self.op = 0
        self.var = 0
        try:
            en.delete(0, END)
        except AttributeError:
            pass
    # ----------------------------------------------------------------------------------------------------
    def exc(self):        # Displays error when there is any Syntax Error
        self.error_check()
        self.f = Frame(root, padx=40, pady=10, bg="black")
        self.f.grid(row=6, column=0)
        mylabel = Label(self.f, text='MALFORMED EXPRESSION', font=('arial',20,'bold'), fg="red", bg="black").grid(row=6, column=0)
        self.err = 1

    def check_for_enter(self, event):      # Checks if the Enter key and bar key is pressed from keyboard
        if event.keysym == 'Return':
            self.equal()
        elif event.keysym == 'bar':
            self.check += 1

obj = Calculator()          # Object to class Calculator
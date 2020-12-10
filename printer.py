# Branch David
# Printer
# Nov 13 2020

from checker import *
from tkinter import messagebox

def show_error(fn, num, line):


    errorText = "File " + str(fn) + " line " + str(num + 1) + "\n\t" + str(line) + "\n" + str(errorList[-1])
    messagebox.showerror("Message Box", errorText)

def print_lexemes():

    print("\nLexemes")
    for i in tokens:
        print(i)
    print()


def print_vars():
    print("\nVariables")
    for i in variables:
        print(i, "=", variables[i])
    print()
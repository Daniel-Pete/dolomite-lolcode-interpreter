# Branch David
# Printer
# Nov 13 2020

from checker import *

def show_error(fn, num, line):

    print("File", fn, "line", num + 1)
    print("\n\t", line, "\n")
    print(ERROR)

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

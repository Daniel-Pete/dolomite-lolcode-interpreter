# Branch David
# Lexical Analyser
# Nov 13 2020

import re

file = "data/sample.txt"

r_numbr = "^-?[0-9]+$"
r_numbar = "^-?[0-9]*\.[0-9]+$"
r_varident = "^[a-zA-Z]+[a-zA-Z0-9\_]*$"



def tokenize(fn):

    f = open(fn, "r")

    for line in f:
        for elem in line.split():
            if re.match(r_numbr, elem):
                print("NUMBR Identifier:", elem)
            if re.match(r_numbar, elem):
                print("NUMBAR Identifier:", elem)
            if re.match(r_varident, elem):
                print("Variable Identifier:",elem)




def main():

    tokenize(file)


main()

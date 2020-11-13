# Branch David
# Lexical Analyser
# Nov 13 2020

import re

file = "data/sample.txt"


r_loop = "^[a-zA-Z]+[a-zA-Z0-9\_]*$"

r_hai = "^HAI$"
r_ktb = "^KTHXBYE"
r_iha = "(I HAS A) ([a-zA-Z]+[a-zA-Z0-9\_]*)"
r_ihai = "(I HAS A) ([a-zA-Z]+[a-zA-Z0-9\_]*) (ITZ) (-?[0-9]+|-?[0-9]*\.[0-9]+)"


def tokenize(fn):

    f = open(fn, "r")

    for line in f:

        line = line.strip("\n")

        

        try:
            x = re.match(r_ihai, line).groups()
            print("Variable Declaration:" ,x[0])
            print("Variable Identifier:"  ,x[1])
            print("Variable Assignment:"  ,x[2])
            print("Literal:"  ,x[3])
            
            print()
            continue
            
        except:
            pass

        try:
            x = re.match(r_iha, line).groups()
            print("Variable Declaration:", x[0])
            print("Variable Identifier:", x[1])
            print()
            continue
        except:
            pass

        if re.match(r_hai, line) or re.match(r_ktb, line):
            print("Code Delimiter:",line)
            print()
        

        



def main():

    tokenize(file)


main()

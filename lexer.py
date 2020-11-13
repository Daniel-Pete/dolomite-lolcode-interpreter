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




def is_var_assign(line):

    try:
        x = re.match(r_ihai, line).groups()
        print("Variable Declaration:", x[0])
        print("Variable Identifier:", x[1])
        print("Variable Assignment:", x[2])
        print("Literal:", x[3], "\n")

        return True
    except:
        pass

    return False


def is_var_declare(line):
    try:
        x = re.match(r_iha, line).groups()
        print("Variable Declaration:", x[0])
        print("Variable Identifier:", x[1], "\n")

        return True

    except:
        pass

    return False

def is_code_delimiter(line):

    if re.match(r_hai, line) or re.match(r_ktb, line):
        print("Code Delimiter:", line, "\n")
        return True


    return False


def tokenize(fn):

    f = open(fn, "r")

    for line in f:

        line = line.strip("\n")

        if is_var_assign(line): continue
        if is_var_declare(line): continue
        if is_code_delimiter(line): continue
            
        

    

def main():

    tokenize(file)


main()

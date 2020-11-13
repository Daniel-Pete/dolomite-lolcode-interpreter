# Branch David
# Lexical Analyser
# Nov 13 2020

import re

file = "data/sample.txt"


R_LOOP = "^[a-zA-Z]+[a-zA-Z0-9\_]*$"
R_HAI = "^HAI$"
R_KTB = "^KTHXBYE"
R_IHA = "(I HAS A) ([a-zA-Z]+[a-zA-Z0-9\_]*)"
R_STR = "\"[^\"]*\""
R_NUMBR = "-?[0-9]+"
R_NUMBAR = "-?[0-9]*\.[0-9]"
R_IHAI = "(I HAS A) ([a-zA-Z]+[a-zA-Z0-9\_]*) (ITZ) (-?[0-9]*\.[0-9]+|-?[0-9]+|\"[^\"]*\")"
R_VISI = "(VISIBLE) (-?[0-9]*\.[0-9]+|-?[0-9]+|[a-zA-Z]+[a-zA-Z0-9\_]*)"
R_GIME = "(GIMMEH) ([a-zA-Z]+[a-zA-Z0-9\_]*)"
R_BTW = "(BTW) ([a-zA-Z0-9\_\s]*)"



def is_var_assign(line):

    try:


        x = re.match(R_IHAI, line).groups()
        print("Variable Declaration:", x[0])
        print("Variable Identifier:", x[1])
        print("Variable Assignment:", x[2])


        if re.match(R_STR, x[3]):
            new = x[3].strip('"')
            print("String Literal:",new)

        elif re.match(R_NUMBAR, x[3]):
            print("Numbar Literal:", x[3])  

        elif re.match(R_NUMBR, x[3]):
            print("Numbr Literal:", x[3])




        return True

    except:
        pass

    return False


def is_var_declare(line):

    try:
        x = re.match(R_IHA, line).groups()
        print("Variable Declaration:", x[0])
        print("Variable Identifier:", x[1])

        return True

    except:
        pass

    return False

def is_code_delimiter(line):

    if re.match(R_HAI, line) or re.match(R_KTB, line):
        print("Code Delimiter:", line)
        return True


    return False

def is_print(line):
    try:
        x = re.match(R_VISI, line).groups()
        print("Print Identifier:",x[0])
        print("Variable Identifier:",x[1])

        return True
    except:
        pass

    return False

def is_input(line):

    
    try:
        x = re.match(R_GIME, line).groups()
        print("Input Identifier:",x[0])
        print("Variable Identifier:",x[1])

        return True
    except:
        pass

    return False

def is_comment(line):

    try:
        x = re.match(R_BTW, line).groups()
        print("Comment Identifier:", x[0])
        print("Comment:", x[1])

        return True
    except:
        pass

    return False



def analyze(fn):

    f = open(fn, "r")

    for line in f:

        line = line.strip("\n")

        print()

        if is_var_assign(line): continue
        if is_var_declare(line): continue
        if is_code_delimiter(line): continue
        if is_print(line): continue
        if is_input(line): continue
        if is_comment(line): continue


    

def main():

    analyze(file)


main()

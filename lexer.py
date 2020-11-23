# Branch David
# Lexical Analyser
# Nov 13 2020

import re

file = "data/sample.txt"


# Regular Expressions Used

R_LOOP = "^[a-zA-Z]+[a-zA-Z0-9\_]*$"
R_HAI = "^HAI$"
R_KTB = "^KTHXBYE$"
R_STR = "\"[^\"]*\""
R_NUMBR = "-?[0-9]+"
R_NUMBAR = "-?[0-9]*\.[0-9]"

R_IHA = "(\s*)(I HAS A) ([a-zA-Z]+[a-zA-Z0-9\_]*)"
R_IHAI = "(\s*)(I HAS A) ([a-zA-Z]+[a-zA-Z0-9\_]*) (ITZ) (-?[0-9]*\.[0-9]+|-?[0-9]+|\"[^\"]*\")"
R_VISI = "(\s*)(VISIBLE) (-?[0-9]*\.[0-9]+|-?[0-9]+|[a-zA-Z]+[a-zA-Z0-9\_]*)"
R_GIME = "(\s*)(GIMMEH) ([a-zA-Z]+[a-zA-Z0-9\_]*)"
R_BTW = "(BTW) ([a-zA-Z0-9\_\s]*)"


def is_var_assign(line):

    # Checks if the 
    # line is variable 
    # assignment

    try:

        # Access the matches
        # through the use of groups

        x = re.match(R_IHAI, line).groups()
        print("Variable Declaration:", x[1])
        print("Variable Identifier:", x[2])
        print("Variable Assignment:", x[3])

        # If the variable matches a string
        # the string is stripped of its
        # quotation marks

        if re.match(R_STR, x[4]):
            new = x[4].strip('"')
            print("String Literal:",new)

        elif re.match(R_NUMBAR, x[4]):
            print("Numbar Literal:", x[4])  

        elif re.match(R_NUMBR, x[4]):
            print("Numbr Literal:", x[4])


        return True

    except:
       
        pass

    # If it doesn't match
    # the next 

    return False


def is_var_declare(line):

    # Checks if the 
    # line is for variable
    # declaration

    try:
        x = re.match(R_IHA, line).groups()
        print("Variable Declaration:", x[1])
        print("Variable Identifier:", x[2])

        return True

    except:
        pass

    return False

def is_code_delimiter(line):

    # Checks if the 
    # line is either HAI
    # or KTHXBYE

    if re.match(R_HAI, line) or re.match(R_KTB, line):
        print("Code Delimiter:", line)
        return True


    return False

def is_print(line):

    # Checks if the line
    # is for printing

    try:

        x = re.match(R_VISI, line).groups()
        print("Print Identifier:",x[0])
        print("Variable Identifier:",x[1])

        return True
    except:
        pass

    return False

def is_input(line):

    # Checks if the line
    # asks for an input

    try:
        x = re.match(R_GIME, line).groups()
        print("Input Identifier:",x[0])
        print("Variable Identifier:",x[1])

        return True
    except:
        pass

    return False

def is_comment(line):

    # Checks if the 
    # line is a comment

    try:
        x = re.match(R_BTW, line).groups()
        print("Comment Identifier:", x[0])
        print("Comment:", x[1])

        return True
    except:
        pass

    return False



def tokenize(fn):

    f = open(fn, "r")

    for num, line in enumerate(f):

        # Each line in the file
        # is checked for a match
        # Once the line matches a 
        # certain construct then it 
        # skips to the next iteration

        line = line.strip("\n")

        print()

        if is_var_assign(line): continue
        if is_var_declare(line): continue
        if is_code_delimiter(line): continue
        if is_print(line): continue
        if is_input(line): continue
        if is_comment(line): continue
        else:
            print("Invalid Syntax on Line",num + 1,line)
            break
 

def main():
    tokenize(file)

main()
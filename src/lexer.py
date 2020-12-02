# Branch David
# Lexical Analyser
# Nov 13 2020

from checker import *

file = "../data/sample.txt"


def tokenize(fn):

    f = open(fn, "r")
    TOGGLE = "O"

    for num, line in enumerate(f):

        # Each line in the file
        # is checked for a match
        # Once the line matches a 
        # certain construct then it 
        # skips to the next iteration

        line = line.strip("\n")
        
        if TOGGLE == "O":

            if is_hai(line):
                TOGGLE = "STATEMENT"
                continue

            else:
                print("Invalid Syntax on Line", num + 1, line)
                break

        elif TOGGLE == "STATEMENT":

            if is_var_assign(line): continue
            elif is_var_declare(line): continue
            elif is_print(line): continue
            elif is_input(line): continue
            elif is_comment(line): continue

            elif is_multicomment(line):
                TOGGLE = "MULTICOMMENT"
                continue

            elif is_bye(line): break
            elif is_anyof(line): continue

            else:
                print("Invalid Syntax on Line", num + 1, line)
                break
        
        elif TOGGLE == "MULTICOMMENT":

            if is_end_multicomment(line):
                TOGGLE = "STATEMENT"
                continue

            elif is_documentation(line):
                continue

            else:
                print("Invalid Syntax on Line", num + 1, line)
                break


            

            # if is_if_then(line): 
            #     continue
            # if is_end_if(line): 
            #     continue
            # if is_if(line): 
            #     continue

            # if is_else(line): continue
            # if is_switch(line): continue
            # if is_case(line): continue
            # if is_end_case(line): continue
        
        
 

def display(ds):
    print("Data Set")
    for i in ds:
        print(i)

def main():
    tokenize(file)
    display(dataset)


main()

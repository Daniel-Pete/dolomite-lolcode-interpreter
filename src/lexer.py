# Branch David
# Lexical Analyser
# Nov 13 2020

from checker import *

file = "../data/sample.txt"


def tokenize(fn):


    try:
        f = open(fn, "r")
    except:
        print("File Error: file named", fn,"cannot be found")
        return

    TOGGLE = "START"

    for num, line in enumerate(f):

        # Each line in the file is checked for a match
        # Once the line matches a 
        # certain construct then it 
        # skips to the next iteration

        line = line.strip("\n")
        
        if TOGGLE == "START":

            if is_hai(line):
                TOGGLE = "STATEMENT"
                continue
            elif is_comment(line):
                continue

            else:
                show_error(fn, num, line)
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

            elif is_bye(line): 
                TOGGLE = "END"
                continue

            elif is_anyof(line): continue

            else:
                show_error(fn, num, line)
                break
        
        elif TOGGLE == "MULTICOMMENT":

            if is_end_multicomment(line):
                TOGGLE = "STATEMENT"
                continue

            elif is_documentation(line):
                continue

            else:
                show_error(fn, num, line)
                break
        
        elif TOGGLE == "END":

            if line:
                show_error(fn, num, line)
                break

        elif TOGGLE == "MULTICOMMENT" and is_bye(line):

            show_error(fn, num, line)
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
        
        
 

def print_lexemes():
    
    print("\nLexemes")
    for i in dataset:
        print(i)
    print()

def print_vars():
    print("\nVariables")
    for i in varset:
        print(i,"=",varset[i])
    print()

def main():
    tokenize(file)

    # print_lexemes()
    print_vars()

main()

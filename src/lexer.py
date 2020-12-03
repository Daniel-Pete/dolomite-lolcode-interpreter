# Branch David
# Lexical Analyser
# Nov 13 2020

from printer import *

file = "../data/sample.lol"


global TOGGLE 
TOGGLE = "START"


def start_grammar(line):
    global TOGGLE

    if is_hai(line):
        TOGGLE = "STATEMENT"
        return True
    elif is_comment(line):
        return True

    return False

def statement_grammar(line):

    global TOGGLE

    if (is_var_initialize(line) or
        is_var_declare(line) or
        is_var_assign(line) or
        is_print(line) or
        is_input(line) or 
        is_comment(line)):

        return True


    elif is_multicomment(line):
        TOGGLE = "MULTICOMMENT"
        return True

    elif is_bye(line):
        TOGGLE = "END"
        return True

    elif is_if_then(line):
        TOGGLE = "IF-THEN"
        return True

    elif is_anyof(line):
        return True

    return False

def comment_grammar(line):
    global TOGGLE

    if is_end_multicomment(line):
        TOGGLE = "STATEMENT"
        return True
        
    elif is_documentation(line): 
        return True

    return False

def if_then_grammar(line):

    global TOGGLE

    if is_if(line):
        return True
    elif is_else(line):
        return True
    elif is_end_if(line):
        TOGGLE = "STATEMENT"
        return True

def tokenize(fn):

    global TOGGLE

    try:
        f = open(fn, "r")
    except:
        print("File Error: file named", fn,"cannot be found")
        return

    

    for num, line in enumerate(f):

        # Each line in the file is checked for a match
        # Once the line matches a 
        # certain construct then it 
        # skips to the next iteration

        line = line.strip("\n")

        
        
        if TOGGLE == "START":

            if start_grammar(line):
                continue
            else:
                show_error(fn, num, line)
                break

        elif TOGGLE == "STATEMENT":

            if statement_grammar(line):
                continue
            else:
                show_error(fn, num, line)
                break
        
        elif TOGGLE == "MULTICOMMENT":

            if comment_grammar(line):
                continue
            else:
                show_error(fn, num, line)
                break

        elif TOGGLE == "IF-THEN":

            if if_then_grammar(line):
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
        
    

            
            # if is_end_if(line): continue
            # if is_if(line): continue

            # if is_else(line): continue
            # if is_switch(line): continue
            # if is_case(line): continue
            # if is_end_case(line): continue
        
    

def main():
    tokenize(file)

    # print_lexemes()
    # print_vars()

main()

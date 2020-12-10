# Branch David
# Lexical Analyser
# Nov 13 2020

from printer import *

# file = "data/sample.lol"
# file = sys.argv[1]


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

    if is_var_initialize(line): return True

    elif is_var_declare(line): return True
        
    elif (is_var_assign(line) or
        is_print(line) or
        is_input(line) or
        is_comment(line) or
        is_smoosh(line)):

        return True

    elif (is_multicomment_a(line) or
        is_multicomment_b(line)):
        TOGGLE = "MULTICOMMENT"
        return True

    elif is_bye(line):
        TOGGLE = "END"
        return True

    elif is_if_then(line):
        TOGGLE = "IF-THEN"
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

def empty(line):

    if is_empty(line):
        return True

def tokenize(fn):
    global TOGGLE

    # Reset lists and dictionary
    if len(tokens) != 0 or len(variables) != 0:
        tokens.clear()
        variables.clear()
        terminalPrint.clear()
        TOGGLE = "START"
    
    try:
        with open(fn, "r") as f:
            for num, line in enumerate(f):

                # Each line in the file is checked for a match
                # Once the line matches a 
                # certain construct then it 
                # skips to the next iteration

                line = line.strip("\n")


                if empty(line):
                    continue
                
                elif TOGGLE == "START":

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
        

            outList = [tokens, variables, terminalPrint]

            return outList
    except:
        print("File Error: file named", fn,"cannot be found")
        return

    

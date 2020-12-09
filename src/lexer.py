from printer import *

file = "lolcode/sample.lol"

global TOGGLE, SUBTOGGLE, CONTROL_FLAG

TOGGLE = START
SUBTOGGLE = START
CONTROL_FLAG = None


def empty(line):

    if is_empty(line):
        return True


def start_grammar(line):
    global TOGGLE, SUBTOGGLE

    if is_hai(line):
        TOGGLE = STATEMENT
        SUBTOGGLE = STATEMENT
        return True

    elif is_comment(line):
        return True

    return False


def is_statement(line):

    global TOGGLE

    if is_var_initialize(line):
        return True

    elif is_var_declare(line):
        return True

    elif (is_var_assign(line) or
          is_print(line) or
          is_input(line) or
          is_comment(line) or
          is_smoosh(line)):

          return True

    elif (is_multicomment_a(line) or
          is_multicomment_b(line)):
        
        return True

    elif is_expression(line) != None:
        return True


    return False


def statement_grammar(line):


    global TOGGLE, SUBTOGGLE, CONTROL_FLAG


    if is_statement(line):
        return True

    elif is_bye(line):
        TOGGLE = END
        return True

    elif is_if_then(line):
        TOGGLE = IF
        SUBTOGGLE = IF
        CONTROL_FLAG = eval(variables["IT"])

        return True


    return False

def comment_grammar(line):
    global TOGGLE

    if is_end_multicomment(line):

        TOGGLE = STATEMENT
        return True

    elif is_documentation(line): 
        return True

    return False

def if_grammar(line):

    global TOGGLE, SUBTOGGLE, CONTROL_FLAG

 
    if CONTROL_FLAG == True:

        if is_end_if(line):
            return False

        elif is_if(line) and SUBTOGGLE == IF:
            SUBTOGGLE = STATEMENT
            return True

        elif is_statement(line) and SUBTOGGLE == STATEMENT:
            return True

        elif is_else(line) and SUBTOGGLE != IF:
            TOGGLE = ELSE
            SUBTOGGLE = SKIP
            return True
        

    elif CONTROL_FLAG == False:

        if is_end_if(line):
            return False

        elif is_if(line) and SUBTOGGLE == IF:
            SUBTOGGLE = SKIP
            return True

        elif is_else(line) and SUBTOGGLE != IF:
            TOGGLE = ELSE
            SUBTOGGLE = STATEMENT
            return True

        elif SUBTOGGLE == SKIP:
            return True
    

        
    return False

def else_grammar(line):

    global TOGGLE, SUBTOGGLE, CONTROL_FLAG

    

    if CONTROL_FLAG == False:

        if is_statement(line) and SUBTOGGLE == STATEMENT:
            return True

        elif is_end_if(line):
            TOGGLE = STATEMENT
            SUBTOGGLE = START
            return True

    elif CONTROL_FLAG == True:

        if is_end_if(line):
            
            TOGGLE = STATEMENT
            SUBTOGGLE = START
            CONTROL_FLAG = None
            return True

        elif SUBTOGGLE == SKIP:
            return True



    return False



def tokenize(fn):

    global TOGGLE, SUBTOGGLE, CONTROL_FLAG

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

        if empty(line):
            continue

        elif TOGGLE == START:

            if start_grammar(line):
                continue
            else:
                show_error(fn, num, line)
                return

        elif TOGGLE == STATEMENT:

            if statement_grammar(line):
                continue
            else:
                show_error(fn, num, line)
                return
        
        elif TOGGLE == MULTICOMMENT:

            if comment_grammar(line):
                continue
            else:
                show_error(fn, num, line)
                return

        elif TOGGLE == IF:
            if if_grammar(line):
                continue
            else:
                show_error(fn, num, line)
                return

        elif TOGGLE == ELSE:

            if else_grammar(line):
                continue
            else:
                show_error(fn, num, line)
                return

        elif TOGGLE == MULTICOMMENT and is_bye(line):
            show_error(fn, num, line)
            return

        elif TOGGLE == END:

            if line:
                show_error(fn, num, line)
                return
    
    # If program ends without KTHXBYE
    # then it will be an error.

    if TOGGLE != END:
        show_error(fn, num, line)
    

def main():
    tokenize(file)
    # print_lexemes()
    # print_vars()    

main()

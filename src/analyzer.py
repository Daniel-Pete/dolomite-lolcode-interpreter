from printer import *

file = "lolcode/sample.lol"

global TOGGLE, SUBTOGGLE, CONTROL_FLAG, CASE_FLAG
global MATCHED_FLAG, GTFO_FLAG

TOGGLE = START
SUBTOGGLE = START

CONTROL_FLAG = None
CASE_FLAG = None
MATCHED_FLAG = False
GTFO_FLAG = False


def start_grammar(line):    
    global TOGGLE, SUBTOGGLE

    if is_hai(line):
        TOGGLE = STATEMENT
        SUBTOGGLE = STATEMENT
        return True

    elif is_comment(line):
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

        try:
            CONTROL_FLAG = eval(variables[IT])
        except:
            return False

        return True

    elif is_switch(line):
        TOGGLE = OMG 
        SUBTOGGLE = START

        try:
            CONTROL_FLAG = eval(variables[IT])
        except:
            return False

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

        if is_oic(line):
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

        if is_oic(line):
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

        if (is_statement(line) and
            SUBTOGGLE == STATEMENT):
            return True

        elif is_oic(line):
            TOGGLE = STATEMENT
            SUBTOGGLE = START
            return True

    elif CONTROL_FLAG == True:

        if is_oic(line):                        
            TOGGLE = STATEMENT
            SUBTOGGLE = START
            CONTROL_FLAG = None
            return True

        elif SUBTOGGLE == SKIP:
            return True

    return False


def omg_grammar(line):

    global TOGGLE, SUBTOGGLE, CONTROL_FLAG, CASE_FLAG
    global MATCHED_FLAG, GTFO_FLAG

    if (is_case(line) and 
        SUBTOGGLE == STATEMENT):
        return True
    
    elif (is_case(line) and 
          SUBTOGGLE != LAST_CASE):

        CASE_FLAG = is_case(line)

        if CASE_FLAG == CONTROL_FLAG:
            SUBTOGGLE = STATEMENT
            MATCHED_FLAG = True
            return True
        else:
            SUBTOGGLE = SKIP
            return True  

    elif is_gtfo(line) and MATCHED_FLAG == True:
        SUBTOGGLE = SKIP
        GTFO_FLAG = True
        return True
    
    elif is_gtfo(line):
        SUBTOGGLE = SKIP
        return True

    elif is_end_case(line):
        SUBTOGGLE = LAST_CASE
        return True

    elif (is_oic(line) and 
          SUBTOGGLE == LAST_CASE):

        TOGGLE = STATEMENT
        SUBTOGGLE = START
        CONTROL_FLAG = None
        CASE_FLAG = None
        MATCHED_FLAG = False

        return True
    
    elif (is_oic(line) and 
          SUBTOGGLE != LAST_CASE):

        return False

    elif SUBTOGGLE == SKIP:
        return True

    elif SUBTOGGLE == LAST_CASE:


        if (MATCHED_FLAG == False or
            GTFO_FLAG == False):
            if is_statement(line):
                return True
        
        else:
            return True

    elif (is_statement(line) and 
         (SUBTOGGLE == STATEMENT)):

        return True
    

    return False

def analyze(fn):

    global TOGGLE, SUBTOGGLE

    try:
        f = open(fn, "r")

    except:
        print(FILE_ERROR)
        return

    for num, line in enumerate(f):

        # Each line in the file is checked 
        # for a match. Once the line matches a 
        # certain construct then it 
        # skips to the next iteration

        line = line.strip("\n")

        if is_empty(line):
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

        elif TOGGLE == OMG:

            if omg_grammar(line):
                continue
            else:
                show_error(fn, num, line)
                return

        elif (TOGGLE == MULTICOMMENT 
            and is_bye(line)):

            show_error(fn, num, line)
            return

        elif TOGGLE == END:

            if line:
                show_error(fn, num, line)
                return
    
    # If program ends without KTHXBYE
    # then it will result into an error.
    
    if TOGGLE != END:
        show_error(fn, num, line)
    
    

def main():
    analyze(file)

main()
from printer import *
from tkinter import messagebox

global TOGGLE, SUBTOGGLE, CONTROL_FLAG
global CASE_FLAG, MATCHED_FLAG, GTFO_FLAG

TOGGLE = START
SUBTOGGLE = START

CONTROL_FLAG = None
CASE_FLAG = None
MATCHED_FLAG = False
GTFO_FLAG = False

def is_empty(line):

    if re.match(R_EMPTY, line):
        return True

    return False

def start_grammar(line):    
    global TOGGLE, SUBTOGGLE

    # When the TOGGLE is set to START
    # the only lines allowed are HAI
    # and comment

    if is_hai(line):
        TOGGLE = STATEMENT
        SUBTOGGLE = STATEMENT
        return True

    elif is_comment(line):
        return True

    return False

def is_statement(line):

    global TOGGLE

    # When the TOGGLE is set to
    # STATEMENT, these are the
    # only lines allowed

    if is_multicomment_a(line):
        TOGGLE = MULTICOMMENT
        return True

    elif is_multicomment_b(line):
        TOGGLE = MULTICOMMENT
        return True

    if is_var_initialize(line):
        return True

    elif is_var_declare(line):
        return True

    elif is_var_assign(line):
        return True
    elif is_print(line):
        return True
    elif is_input(line):
        return True
    elif is_comment(line):
        return True
    elif is_smoosh(line):
        return True
    elif is_smoosh(line):
        return True
    elif is_empty(line):
        return True

    elif is_expression(line):
        return True

    return False

def statement_grammar(line):

    global TOGGLE, SUBTOGGLE, CONTROL_FLAG

    if is_bye(line):
        TOGGLE = END
        return True

    elif is_statement(line):
        return True

    elif is_if_then(line):

        # Once a O RLY? is encountered
        # the TOGGLE and SUBTOGGLE is set to IF
        
        TOGGLE = IF
        SUBTOGGLE = IF

        try:

            # The CONTROL_FLAG is used
            # to determine which part of
            # the if-else block to execute

            CONTROL_FLAG = eval(variables[IT])
        except:
            return False

        return True

    elif is_switch(line):
        TOGGLE = OMG 
        SUBTOGGLE = START

        try:

            # The CONTROL_FLAG is used
            # to determine which part of
            # the switch block to execute

            CONTROL_FLAG = eval(variables[IT])
        except:
            return False

        return True

    return False


def comment_grammar(line):
    global TOGGLE

    if is_end_multicomment(line):

        # If TLDR is detected, then the 
        # TOGGLE is set to statement.

        TOGGLE = STATEMENT
        return True

    elif is_documentation(line): 

        # Otherwise, the following 
        # statements are treated as 
        # documentation

        return True

    return False

def if_grammar(line):

    global TOGGLE, SUBTOGGLE, CONTROL_FLAG
 
    if CONTROL_FLAG == True:

        if is_oic(line):

            # If OIC is seen without a
            # YA RLY, then it will error

            return False

        elif is_if(line) and SUBTOGGLE == IF:

            # If the line starts with IF
            # then the succeeding statements
            # are executed

            SUBTOGGLE = STATEMENT
            return True

        elif is_statement(line) and SUBTOGGLE == STATEMENT:

            # If the line is a statement
            # and the SUBTOGGLE is statement
            # then the lines are executed

            return True

        elif is_else(line) and SUBTOGGLE != IF:

            # If the statement is ELSE
            # and SUBTOGGLE is STATEMENT or SKIP
            # then the TOGGLE and SUBTOGGLE are
            # changed so that it knows what to expect next

            TOGGLE = ELSE
            SUBTOGGLE = SKIP
            return True

    
    # If CONTROL_FLAG == FALSE then the 
    # lines under IF will not execute
        
    elif CONTROL_FLAG == False:

        if is_oic(line):

            # If it ends with OIC 
            # without seeing YA RLY and NO WAI
            # then it would error

            return False

        elif is_if(line) and SUBTOGGLE == IF:

            # If it encounters an IF
            # the lines under IF would not execute

            SUBTOGGLE = SKIP
            return True

        elif is_else(line) and SUBTOGGLE != IF:

            # If it encounters an else
            # the toggles are changed so that 
            # it will execute the next statements

            TOGGLE = ELSE
            SUBTOGGLE = STATEMENT
            return True

        elif SUBTOGGLE == SKIP:

            # Skip analysis of the line

            return True
        
    return False

def else_grammar(line):

    global TOGGLE, SUBTOGGLE, CONTROL_FLAG

    if CONTROL_FLAG == False:

        # The statements under NO WAI
        # will execute when CONTROL_FLAG 
        # is false

        if (is_statement(line) and
            SUBTOGGLE == STATEMENT):
            return True

        elif is_oic(line):

            # When OIC is encountered
            # the toggles are reset 

            TOGGLE = STATEMENT
            SUBTOGGLE = START
            CONTROL_FLAG = None
            return True

    elif CONTROL_FLAG == True:

        # When CONTROL_FLAG is True, then
        # the statements under YA RLY
        # have already executed. The 
        # interpreter is waiting for OIC
        # to finish the if-else block


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


    # This part handles the logic when 
    # executing a Switch Case block

    if (is_case(line) and 
        SUBTOGGLE == STATEMENT):

        # If it sees that it's an OMG
        # then it will proceed to the next
        # statement

        return True
    
    elif (is_case(line) and 
          SUBTOGGLE != LAST_CASE):

        CASE_FLAG = is_case(line)

        if CASE_FLAG == CONTROL_FLAG:

            # If it matches, then the subsequent
            # statements will be executed 

            SUBTOGGLE = STATEMENT
            MATCHED_FLAG = True
            return True

        else:
            # If it doesn't match 
            # then skip
            
            SUBTOGGLE = SKIP
            return True  

    elif is_gtfo(line) and MATCHED_FLAG == True:

        # If GTFO is encountered, then 
        # succeeding blocks will be executed

        SUBTOGGLE = SKIP
        GTFO_FLAG = True
        return True
    
    elif is_gtfo(line):

        # If GTFO, then succeeding lines
        # will be ignored.

        SUBTOGGLE = SKIP
        return True

    elif is_end_case(line):
        SUBTOGGLE = LAST_CASE
        return True

    elif (is_oic(line) and 
          SUBTOGGLE == LAST_CASE):

        # Reset FLAGS when OIC is encountered

        TOGGLE = STATEMENT
        SUBTOGGLE = START
        CONTROL_FLAG = None
        CASE_FLAG = None
        MATCHED_FLAG = False

        return True
    
    elif (is_oic(line) and 
          SUBTOGGLE != LAST_CASE):

        # If an OIC is encountered
        # without an OMGWTF, then it would 
        # result into an error

        return False

    elif SUBTOGGLE == SKIP:
        return True

    elif SUBTOGGLE == LAST_CASE:

        # If there has been no matching case
        # or GTFO, then the OMGWTF would execute

        if (MATCHED_FLAG == False or
            GTFO_FLAG == False):
            if is_statement(line):
                return True
        
        # Otherwise, it would be skipped

        else:
            return True

    elif (is_statement(line) and 
         (SUBTOGGLE == STATEMENT)):

        # Execute if it's a statement

        return True
    

    return False


def analyze(fn):

    global TOGGLE, SUBTOGGLE, CONTROL_FLAG, CASE_FLAG
    global MATCHED_FLAG, GTFO_FLAG

    # Reset lists and dictionary
    if len(tokens) != 0 or len(variables) != 0:

        tokens.clear()
        variables.clear()
        terminalPrint.clear()
        errorList.clear()
        
        TOGGLE = START
        SUBTOGGLE = START
        CONTROL_FLAG = None
        CASE_FLAG = None
        MATCHED_FLAG = False
        GTFO_FLAG = False

    try:

        with open(fn, "r") as f:
            for num, line in enumerate(f):

                # Each line in the file undergoes
                # lexical, syntax, and semantic 
                # analysis handled by the different 
                # functions below that will check
                # what kind of statement it is

                line = line.strip("\n")

                if is_empty(line):
                    continue

                elif TOGGLE == START:

                    if start_grammar(line):
                        continue
                    else:
                        errorList.append(SYNTAX_ERROR_HAI)
                        show_error(fn, num, line)
                        return [tokens, variables, terminalPrint]

                elif TOGGLE == STATEMENT:

                    if statement_grammar(line):
                        continue
                    else:
                        errorList.append(SYNTAX_ERROR_EXPECT)
                        show_error(fn, num, line)
                        return [tokens, variables, terminalPrint]
                
                elif TOGGLE == MULTICOMMENT:

                    if comment_grammar(line):
                        continue
                    else:
                        errorList.append(SYNTAX_ERROR_COMMENT)
                        show_error(fn, num, line)
                        return [tokens, variables, terminalPrint]

                elif TOGGLE == IF:
                    if if_grammar(line):
                        continue
                    else:
                        show_error(fn, num, line)
                        return [tokens, variables, terminalPrint]

                elif TOGGLE == ELSE:

                    if else_grammar(line):
                        continue
                    else:
                        show_error(fn, num, line)
                        return [tokens, variables, terminalPrint]

                elif TOGGLE == OMG:

                    if omg_grammar(line):
                        continue
                    else:
                        show_error(fn, num, line)
                        return [tokens, variables, terminalPrint]

                elif (TOGGLE == MULTICOMMENT 
                    and is_bye(line)):

                    show_error(fn, num, line)
                    return [tokens, variables, terminalPrint]

                elif TOGGLE == END:

                    if line:
                        errorList.append(SYNTAX_ERROR_CLOSED)
                        show_error(fn, num, line)
                        return [tokens, variables, terminalPrint]
            
            # If program ends without KTHXBYE
            # then it will result into an error.
            
            if TOGGLE != END:
                errorList.append(SYNTAX_ERROR_NOT_CLOSED)
                show_error(fn, num, line)

            return [tokens, variables, terminalPrint]


    except:
        messagebox.showerror("Message Box", "File Error: File not found")
        return

import re
from regex import *
from tkinter import simpledialog

global ERROR
ERROR = SYNTAX_ERROR

tokens = []
variables = {}
terminalPrint = []

def is_empty(line):

    if re.match(R_EMPTY, line):
        return True

    return False

def is_statement(line):

    if is_var_initialize(line):
        return True

    elif is_var_declare(line):
        return True

    elif (is_var_assign(line)):
        return True

    elif(is_print(line) or
          is_input(line) or
          is_comment(line) or
          is_smoosh(line) or
          is_empty(line)):

        return True

    elif (is_multicomment_a(line) or
          is_multicomment_b(line)):
        
        return True


    elif is_expression(line):
        return True
    
    return False


def is_var_initialize(line):

    # Checks if the
    # line is variable
    # assignment

    try:

        # Access the matches
        # through the use of groups

        match = re.match(R_IHAI, line).groups()
        
        tokens.append([VAR_DEC, str(match[1])])
        tokens.append([VAR_IDENT, str(match[2])])

        if match[3]: 
            tokens.append([VAR_ASS, str(match[3])])


        if re.match(R_WIN, str(match[4])):
            tokens.append([TROOF_LIT, match[4]])
            variables[str(match[2])] = str(match[4])
            return True

        elif re.match(R_FAIL, str(match[4])):
            tokens.append([TROOF_LIT, match[4]])
            variables[str(match[2])] = str(match[4])
            return True

        elif re.match(R_VARIDENT, match[4]):

            # For assignment from
            # another variable, it must first
            # check if the other variable exists.

            if variables.__contains__(match[4]):
                variables[str(match[2])] = variables[match[4]]
                return True

            else:
                return False

        elif re.match(R_STR, str(match[4])):

            # If the variable matches a string
            # the string is stripped of its
            # quotation marks

            new = match[4].strip('"')
            tokens.append([STR_LIT, new])

        elif re.match(R_NUMBAR, match[4]):

            tokens.append([NBR_LIT, match[4]])

        elif re.match(R_NUMBR, match[4]):

            tokens.append([NBAR_LIT, match[4]])

        elif is_expression(match[4]):

            variables[match[2]] = variables[IT]
            return True

        variables[str(match[2])] = match[4]


        return True

    except:

        pass
    
    return False


def is_var_declare(line):

    # Checks if the
    # line is for variable
    # declaration

    try:
        
        match = re.match(R_IHA, line).groups()

        tokens.append([VAR_DEC, match[1]])
        tokens.append([VAR_IDENT, match[2]])

        variables[str(match[2])] = None 

        return True

    except:
        pass
    return False

def is_var_assign(line):

    try:

        match = re.match(R_ASS, line).groups()


        if variables.__contains__(match[1]):
                                    
            if is_expression(match[3]):

                variables[match[1]] = variables[IT]
                return True

            elif re.match(R_TROOF, match[3]):
                variables[match[1]] = match[3]
            
            elif re.match(R_VARIDENT, match[3]):

                if variables.__contains__(match[3]):
                    
                    variables[str(match[1])] = variables[match[3]]
                    return True

                else:
                    return False
            
            elif re.match(R_NUMBAR, match[3]):
                variables[match[1]] = match[3]

            elif re.match(R_NUMBR, match[3]):
                variables[match[1]] = match[3]

            elif re.match(R_STR, match[3]):
                variables[match[1]] = match[3]

            
            tokens.append([VAR_IDENT, match[1]])
            tokens.append([VAR_ASS, match[2]])

            return True

        else:
            return False
    
    except:
        pass

    return False



def is_hai(line):

    # Checks if the
    # line is either HAI
    # or KTHXBYE

    if re.match(R_HAI, line):
        tokens.append([COD_DEL, line])
        variables[IT] = None
        return True

    return False

def is_bye(line):

    if re.match(R_KTB, line):
        tokens.append([COD_DEL, line])
        return True

    return False 

# prompt to get input from user
def getInputFromUser():
    gimmeInput = simpledialog.askstring("GIMME INPUT", "Enter your input")
    return gimmeInput

def is_input(line):

    # Checks if the line
    # asks for an input

    global ERROR
    try:

        match = re.match(R_GIME, line).groups()
        tokens.append([INPUT_ID, match[0]])
        tokens.append([VAR_IDENT, match[1]])

        
        if variables.__contains__(match[2]):
            variables[match[2]] = getInputFromUser()

        else:
            ERROR = VAR_ERROR
            return False

        return True

    except:
        pass

    return False


def is_comment(line):

    # Checks if the
    # line is a comment

    try:
        match = re.match(R_BTW, line).groups()
        tokens.append([COM_ID, match[1]])
        tokens.append([COM, match[2]])

        return True
    except:
        pass

    return False


def is_if_then(line):

    # Checks if line
    # is O RLY?

    try:
        match = re.match(R_ORLY, line).groups()
        tokens.append([CF_KEY, match[1]])
        return True
    except:
        pass

    return False


def is_oic(line):

    # Checks if the line is
    # OIC

    try:
        match = re.match(R_OIC, line).groups()
        tokens.append([CF_KEY, match[1]])
        return True
    except:
        pass

    return False


def is_if(line):

    # Checks if line 
    # is YA RLY

    try:
        match = re.match(R_YARLY, line).groups()
        tokens.append([CF_KEY, match[1]])
        return True
    except:
        pass

    return False


def is_else(line):

    # Checks if line 
    # is NO WAI

    try:
        match = re.match(R_NOWAI, line).groups()
        tokens.append([CF_KEY, match[1]])
        return True
    except:
        pass

    return False


def is_switch(line):

    # Checks if line is for Switch Statement

    try:
        match = re.match(R_WTF, line).groups()
        tokens.append([CF_KEY, match[1]])
        return True
    except:
        pass

    return False


def is_case(line):

    # Checks if line is OMG


    try:
        match = re.match(R_OMG, line).groups()
        tokens.append([CF_KEY, match[1]])
        tokens.append([VAL_LIT, match[2]])


        return eval(match[2])

    except:
        pass

    return False

def is_end_case(line):

    # Checks if line is OMGWTF

    try:
        match = re.match(R_OMGWTF, line).groups()
        tokens.append([CF_KEY, match[1]])

        return True
    except:
        pass

    return False

def is_gtfo(line):

    try:

        match = re.match(R_GTFO, line).groups()
        tokens.append([CF_KEY, match[1]])

        return True

    except:
        pass

    return False


def is_multicomment_a(line):

    # For documentation that will span
    # multiple lines. In this case
    # there is documentation after OBTW

    try:
        match = re.match(R_OBTW, line).groups()
        tokens.append([COM_DEL, match[1]])

        if match[2]:
            tokens.append([DOC_ID, match[3]])
        return True
    except:
        pass

    return False

def is_multicomment_b(line):

    # For documentation
    # that will span multiple 
    # lines

    try:
        match = re.match(R_OBTW2, line).groups()
        tokens.append([COM_DEL, match[1]])

        return True

    except:
        pass

    return False


def is_end_multicomment(line):

    # For TLDR which will signify the end of
    # documentation

    try:
        match = re.match(R_TLDR, line).groups()
        tokens.append([COM_DEL, match[1]])

        return True
    except:
        pass

    return False

def is_documentation(line):

    # All lines after 
    # OBTW will be ignored 

    tokens.append([DOC_ID, line])
    return True


def concatenation(match):

    NEWLINE_FLAG = False

    floats = re.findall(R_NUMBAR, match)
    ints = re.findall(R_NUMBR, match)

    wins = re.findall(R_WIN, match)
    fails = re.findall(R_FAIL, match)

    strings = re.findall(R_STR, match)
    strings = [i.strip('"') for i in strings]
    
    # If there are string quotes, then it
    # will be split using '"'. Otherwise, it will
    # be split with space.

    if '"' in match:
        to_concat = [str(i) for i in match.split('"') if i != '']
    else:
        to_concat = [str(i).strip() for i in match.split() if i != '']
    
    if to_concat[-1].strip() == '!': 
        NEWLINE_FLAG = True
    
    for i, j in enumerate(to_concat):

        if j not in strings:

            # There are cases wherein
            # the variables are joined
            # in a single string.
            # This code block addresses this problem

            x = j.split()
            x = x[::-1]
            to_concat.pop(i)

            for elem in x:
                to_concat.insert(i, elem)

    concat = []

    for i in to_concat:

        if variables.__contains__(i):

            # If the value is a variable
            # then it's type will be first
            # checked. If it's none, then it will
            # error.

            if variables[i] != None:
                concat.append(variables[i])
            else:
                return "UNDEFINED"

        elif (i in strings or
                i in ints or
                i in floats or
                i in wins or 
                i in fails):

            concat.append(i)

        else:

            if NEWLINE_FLAG == True:
                continue
            else:
                return "UNDEFINED"

    return (concat, NEWLINE_FLAG)



def is_smoosh(line):

    try:

        match = re.match(R_SMOOSH, line).groups()
        tokens.append([CAT_OP, match[1]])

        # Find all the matches inside the string.

        concat = concatenation(match[2])

        if concat:

            variables[IT] = ''.join(concat[0])
            return True

        else:
            return False

    except:
        pass

    return False


def is_print(line):

    # Checks if the line
    # is for printing
    global ERROR

    try:


        match = re.match(R_VISI, line).groups()
        tokens.append([PRINT_ID, match[1]])

        concat = concatenation(match[2])

        if concat == "UNDEFINED":

            return False

        elif concat:

            if concat[1]:
                print(''.join(concat[0]).strip('"'), end = "")
                terminalPrint.append(''.join(concat[0]).strip('"'), end = "")
            else:
                print(''.join(concat[0]).strip('"'))
                terminalPrint.append(''.join(concat[0]).strip('"'))
            
            return True

        else:


            try:
                is_expression(match[2])
                return True
            except:
                return False


        return False

    except:
        pass

    return False


def solve_arithmetic(exp):

    if re.match(R_NUMBAR, exp) or re.match(R_NUMBR, exp):
        return(eval(exp))

    # Check if Addition
    if re.match(R_ADDITION, exp):
        groups = re.match(R_ADDITION, exp).groups()

        arg1 = check_aritharg(groups[3])
        arg2 = check_aritharg(groups[5])
        if arg1 != None and arg2 != None:
            result = arg1+arg2
            return(solve_arithmetic(groups[1]+str(result)+groups[6]))

    # Check if SUBTRACTION
    if re.match(R_SUBTRACTION, exp):
        groups = re.match(R_SUBTRACTION, exp).groups()

        arg1 = check_aritharg(groups[3])
        arg2 = check_aritharg(groups[5])
        if arg1 != None and arg2 != None:
            result = arg1-arg2
            return(solve_arithmetic(groups[1]+str(result)+groups[6]))

    # Check if MULTIPLICATION
    if re.match(R_MULTIPLICATION, exp):
        groups = re.match(R_MULTIPLICATION, exp).groups()

        arg1 = check_aritharg(groups[3])
        arg2 = check_aritharg(groups[5])
        if arg1 != None and arg2 != None:
            result = arg1*arg2
            return(solve_arithmetic(groups[1]+str(result)+groups[6]))

    # Check if DIVISION
    if re.match(R_DIVISION, exp):
        groups = re.match(R_DIVISION, exp).groups()

        arg1 = check_aritharg(groups[3])
        arg2 = check_aritharg(groups[5])
        if arg1 != None and arg2 != None:
            result = arg1/arg2
            return(solve_arithmetic(groups[1]+str(result)+groups[6]))

    # Check if MODULO
    if re.match(R_MODULO, exp):
        groups = re.match(R_MODULO, exp).groups()

        arg1 = check_aritharg(groups[3])
        arg2 = check_aritharg(groups[5])
        if arg1 != None and arg2 != None:
            result = arg1 % arg2
            return(solve_arithmetic(groups[1]+str(result)+groups[6]))

    # Check if MAX
    if re.match(R_MAX, exp):
        groups = re.match(R_MAX, exp).groups()

        arg1 = check_aritharg(groups[3])
        arg2 = check_aritharg(groups[5])
        if arg1 != None and arg2 != None:
            result = max(arg1, arg2)
            return(solve_arithmetic(groups[1]+str(result)+groups[6]))

    # Check if MIN
    if re.match(R_MIN, exp):
        groups = re.match(R_MIN, exp).groups()

        arg1 = check_aritharg(groups[3])
        arg2 = check_aritharg(groups[5])
        if arg1 != None and arg2 != None:
            result = min(arg1, arg2)
            return(solve_arithmetic(groups[1]+str(result)+groups[6]))

    return None


def solve_boolean(exp):

    # Base case
    if re.match(R_BOOLEAN, exp):
        if exp == "True":
            return("WIN")
        elif exp == "False":
            return("FAIL")

    # Base case for infinite and
    if re.match(R_INFAND_BASE, exp):
        groups = re.match(R_INFAND_BASE, exp).groups()
        arg = check_boolarg(groups[2])

        if arg != None:
            if arg == True:
                return("WIN")
            elif arg == False:
                return("FAIL")

    # Base case for infinite or
    if re.match(R_INFOR_BASE, exp):
        groups = re.match(R_INFOR_BASE, exp).groups()
        arg = check_boolarg(groups[2])

        if arg != None:
            if arg == True:
                return("WIN")
            elif arg == False:
                return("FAIL")

    # Check if "not" boolean operation
    if re.match(R_NOT, exp):
        groups = re.match(R_NOT, exp).groups()

        arg1 = check_boolarg(groups[3])
        if arg1 != None:
            result = not arg1
            return(solve_boolean(groups[1]+str(result)+groups[4]))

    # Check if "and" boolean operation
    if re.match(R_AND, exp):
        groups = re.match(R_AND, exp).groups()

        arg1 = check_boolarg(groups[3])
        arg2 = check_boolarg(groups[5])
        if arg1 != None and arg2 != None:
            result = arg1 and arg2
            return(solve_boolean(groups[1]+str(result)+groups[6]))

    # Check if "or" boolean operation
    if re.match(R_OR, exp):
        groups = re.match(R_OR, exp).groups()

        arg1 = check_boolarg(groups[3])
        arg2 = check_boolarg(groups[5])
        if arg1 != None and arg2 != None:
            result = arg1 or arg2
            return(solve_boolean(groups[1]+str(result)+groups[6]))

    # Check if "xor" boolean operation
    if re.match(R_XOR, exp):
        groups = re.match(R_XOR, exp).groups()

        arg1 = check_boolarg(groups[3])
        arg2 = check_boolarg(groups[5])
        if arg1 != None and arg2 != None:
            result = arg1 ^ arg2
            return(solve_boolean(groups[1]+str(result)+groups[6]))

    # Check if "and" boolean operation
    if re.match(R_INFINITE_AND, exp):
        groups = re.match(R_INFINITE_AND, exp).groups()

        arg1 = check_boolarg(groups[2])
        arg2 = check_boolarg(groups[4])
        if arg1 != None and arg2 != None:
            result = arg1 and arg2
            return(solve_boolean(groups[1]+" "+str(result)+groups[5]))

    # Check if "and" boolean operation
    if re.match(R_INFINITE_OR, exp):
        groups = re.match(R_INFINITE_OR, exp).groups()

        arg1 = check_boolarg(groups[2])
        arg2 = check_boolarg(groups[4])
        if arg1 != None and arg2 != None:
            result = arg1 or arg2
            return(solve_boolean(groups[1]+" "+str(result)+groups[5]))

    return None


def solve_comparison(exp):

    # Base case
    if re.match(R_BOOLEAN, exp):
        if exp == "True":
            return("WIN")
        elif exp == "False":
            return("FAIL")

    # Check if MAX
    if re.match(R_MAX, exp):
        groups = re.match(R_MAX, exp).groups()

        arg1 = check_aritharg(groups[3])
        arg2 = check_aritharg(groups[5])
        if arg1 != None and arg2 != None:
            result = max(arg1, arg2)
            return(solve_comparison(groups[1]+str(result)+groups[6]))

    # Check if MIN
    if re.match(R_MIN, exp):
        groups = re.match(R_MIN, exp).groups()

        arg1 = check_aritharg(groups[3])
        arg2 = check_aritharg(groups[5])
        if arg1 != None and arg2 != None:
            result = min(arg1, arg2)
            return(solve_comparison(groups[1]+str(result)+groups[6]))

    # Check if Equal
    if re.match(R_EQUAL_COMPARISON, exp):
        groups = re.match(R_EQUAL_COMPARISON, exp).groups()

        arg1 = check_comparg(groups[3])
        arg2 = check_comparg(groups[5])
        if arg1 != None and arg2 != None:
            if type(arg1) != type(arg2):
                return("FAIL")
            result = arg1 == arg2
            return(solve_comparison(groups[1]+str(result)+groups[6]))

    # Check if Not Equal
    if re.match(R_NOTEQUAL_COMPARISON, exp):
        groups = re.match(R_NOTEQUAL_COMPARISON, exp).groups()

        arg1 = check_comparg(groups[3])
        arg2 = check_comparg(groups[5])
        if arg1 != None and arg2 != None:
            if type(arg1) != type(arg2):
                return("FAIL")
            result = arg1 != arg2
            return(solve_comparison(groups[1]+str(result)+groups[6]))

    return None


def check_aritharg(arg):
    # line/string is either a literal or variable
    if re.match(R_STR, arg):
        new = arg.strip('"')
        # tokens.append(["String Literal", new])
        return(str(new))

    elif re.match(R_NUMBAR, arg):
        # tokens.append(["Numbar Literal", arg])
        return(eval(arg))

    elif re.match(R_NUMBR, arg):
        # tokens.append(["Numbr Literal", arg])
        return(eval(arg))

    elif re.match(R_VARIABLE, arg):
        if variables.__contains__(arg):
            # tokens.append(["Variable Identifier", arg])
            return(eval(variables[arg]))

    return None


def check_boolarg(arg):
    if re.match(R_BOOLEAN, arg):
        return(eval(arg))

    elif re.match(R_VARIABLE, arg):
        if variables.__contains__(arg):
            if variables[arg] == "WIN":
                return True
            elif variables[arg] == "FAIL":
                return False
            # tokens.append(["Variable Identifier", arg])
            return(eval(variables[arg]))

        

    return None


def check_comparg(arg):
    retarg = check_aritharg(arg)
    if retarg != None:
        return retarg
    retarg = check_boolarg(arg)
    if retarg != None:
        return retarg

    return None

# fxn that checks if the line is an expression and returns the evaluated result


def is_expression(line):

    # Check if literal/variable only
    aritharg = check_aritharg(line.strip(" "))

    if aritharg:        
        variables[IT] = str(aritharg)
        return True

    # arithmetic is final evaluated arithmetic expression
    arithmethic = solve_arithmetic(line)

    # Valid arithmetic expression
    if arithmethic != None:
        variables[IT] = str(arithmethic)
        return True

    # boolean is final evaluated boolean expression
    boolline = line
    boolline = boolline.replace("WIN", "True")
    boolline = boolline.replace("FAIL", "False")

    boolean = solve_boolean(boolline)

    # Valid boolean expression
    if boolean != None:
        variables[IT] = str(boolean)
        return True

    # compare is final evaluated compare expression

    compare = solve_comparison(line)

    # Valid comparison expression
    if compare != None:
        variables[IT] = str(compare)
        return True

    # Invalid Expression
    return False

# Tool fxn to process


def process_bool(line):
    line = line.replace("WIN", "True")
    line = line.replace("FAIL", "False")

    return(line)
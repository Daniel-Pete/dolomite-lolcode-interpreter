import re
from regex3 import *

tokens = []
variables = {}

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

        if match[3]: tokens.append([VAR_ASS, str(match[3])])


        if re.match(R_VARIDENT, match[4]):

            # For assignment from
            # another variable, it must first
            # check if the other variable exists.

            try:
                if variables.__contains__(match[4]):
                    
                    variables[str(match[2])] = variables[match[4]]
                    return True
            except:
                return False

        elif re.match(R_STR, match[4]):

            # If the variable matches a string
            # the string is stripped of its
            # quotation marks

            new = match[4].strip('"')
            tokens.append([STR_LIT, new])

        elif re.match(R_NUMBAR, match[4]):
            tokens.append([NBR_LIT, match[4]])

        elif re.match(R_NUMBR, match[4]):
            tokens.append([NBAR_LIT, match[4]])

        variables[str(match[2])] = match[4]


        return True

    except:

        pass
    
    return False

def is_code_delimiter(line):

    # Checks if the
    # line is either HAI
    # or KTHXBYE

    if re.match(R_HAI, line) or re.match(R_KTB, line):
        tokens.append(["Code Connector", line])
        return True

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
            result = arg1%arg2
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
    if re.match(R_BOOLEAN, exp):
        return(eval(exp))
    
    # Check if "not" boolean operation
    if re.match(R_NOT, exp):
        groups = re.match(R_NOT, exp).groups()

        arg1 = check_boolarg(groups[3])
        if arg1 != None:
            result = not arg1
            return(solve_boolean(groups[1]+str(result)+groups[4]))


    return None

def check_boolarg(arg):
    if re.match(R_BOOLEAN, arg):
        return(eval(arg))

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

    else: return False

# fxn that checks if the line is an expression and returns the evaluated result
def is_expression(line):
    # Check if literal/variable only
    aritharg = check_aritharg(line.strip(" "))
    if aritharg: return aritharg


    # arithmetic is final evaluated arithmetic expression
    arithmethic = solve_arithmetic(line)

    # Valid arithmetic expression
    if arithmethic != None:
        return arithmethic

    # boolean is final evaluated boolean expression
    boolline = line
    boolline = boolline.replace("WIN", "True")
    boolline = boolline.replace("FAIL", "False")

    boolean = solve_boolean(boolline)

    # Valid boolean expression
    if boolean != None:
        return boolean

    # Invalid Expression
    return None

# Tool fxn to process 
def process_bool(line):
    line = line.replace("WIN", "True")
    line = line.replace("FAIL", "False")

    return(line)
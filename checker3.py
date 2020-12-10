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
    # Base case
    if re.match(R_BOOLEAN, exp):
        if exp == "True": return("WIN")
        elif exp == "False": return("FAIL")

    # Base case for infinite and
    if re.match(R_INFAND_BASE, exp):
        groups = re.match(R_INFAND_BASE, exp).groups()
        arg = check_boolarg(groups[2])

        if arg != None:
            return(arg)

    # Base case for infinite or
    if re.match(R_INFOR_BASE, exp):
        groups = re.match(R_INFOR_BASE, exp).groups()
        arg = check_boolarg(groups[2])

        if arg != None:
            return(arg)
    
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
    print("exp", exp)
    # Base case
    if re.match(R_BOOLEAN, exp):
        if exp == "True": return("WIN")
        elif exp == "False": return("FAIL")

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
            if variables[arg] == "WIN": return True
            elif variables[arg] == "FAIL": return False
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

    # compare is final evaluated compare expression

    compare = solve_comparison(line)

    # Valid comparison expression
    if compare != None:
        return compare

    # Invalid Expression
    return None

# Tool fxn to process 
def process_bool(line):
    line = line.replace("WIN", "True")
    line = line.replace("FAIL", "False")

    return(line)
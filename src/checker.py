import re
from regex import *

global ERROR
ERROR = SYNTAX_ERROR


tokens = []
variables = {}

def is_empty(line):

    if re.match(R_EMPTY, line):
        return True

    return False

def is_statement(line):

    if is_var_initialize(line):
        return True

    elif is_var_declare(line):
        return True

    elif (is_var_assign(line) or
          is_print(line) or
          is_input(line) or
          is_comment(line) or
          is_smoosh(line) or
          is_empty(line)):

        return True

    elif (is_multicomment_a(line) or
          is_multicomment_b(line)):

        return True

    elif is_expression(line) != None:
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

            tokens.append([VAR_IDENT, match[1]])
            tokens.append([VAR_ASS, match[2]])

            variables[match[1]] = match[3]

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



def is_input(line):

    # Checks if the line
    # asks for an input

    global ERROR
    try:

        match = re.match(R_GIME, line).groups()
        tokens.append([INPUT_ID, match[0]])
        tokens.append([VAR_IDENT, match[1]])

        
        if variables.__contains__(match[2]):
            variables[match[2]] = input()

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


    if is_expression(match):
        print(variables[IT])
        return "EXPRESSION"

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
                return

        elif (i in strings or
                i in ints or
                i in floats or
                i in wins or 
                i in fails):

            concat.append(i)

        else:
            return 

    return concat



def is_smoosh(line):

    try:

        match = re.match(R_SMOOSH, line).groups()
        tokens.append([CAT_OP, match[1]])

        # Find all the matches inside the string.

        concat = concatenation(match[2])

        if concat:
            variables[IT] = ''.join(concat)
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

        if concat == "EXPRESSION":
            return True
        elif concat:
            print(''.join(concat).strip('"'))
            return True

        else:
            return False

    except:
        pass

    return False



# Functions from Ged's Branch
# Used for parsing expressions

def is_equal_comparison(line, expression):

    try:
        category = ""
        x = re.match(RE_EQUAL_Comparison, line).groups()

        expression += "("

        if(is_min_or_max(x[2]) != False):
            category = is_min_or_max(x[2])

        tokens.append([category+EQ_OP, x[1]])

        op1_exp = arithmetic_type_checker(x[2], expression)
        if(op1_exp == False):
            return False
        else:
            expression = op1_exp[1]
            expression += op1_exp[0]

        tokens.append([EQ_COM_CXT, x[3]])
        expression += " == "

        op2_exp = arithmetic_type_checker(x[4], expression)
        if(op2_exp == False):
            return False
        else:
            expression = op2_exp[1]
            expression += op2_exp[0]

        expression += ")"

        return(expression)
    except:
        pass

    return False


def is_notequal_comparison(line, expression):

    try:

        category = ""
        x = re.match(RE_NOTEQUAL_Comparison, line).groups()

        expression += "("
        if(is_min_or_max(x[2]) != False):
            category = is_min_or_max(x[2])

        if category == "":
            category = "NE"
        elif category == "LT":
            category = "GT"
        elif category == "GT":
            category = "LT"

        tokens.append([category+COM_OP, x[1]])

        op1_exp = arithmetic_type_checker(x[2], expression)
        if(op1_exp == False):
            return False
        else:
            expression = op1_exp[1]
            expression += op1_exp[0]

        tokens.append([category+COM_CXT, x[3]])
        expression += " != "

        op2_exp = arithmetic_type_checker(x[4], expression)
        if(op2_exp == False):
            return False
        else:
            expression = op2_exp[1]
            expression += op2_exp[0]

        expression += ")"

        return(expression)

    except:
        pass

    return False


def is_min_or_max(line):

    if re.match(RE_MAX, line):
        return "GT"
    elif re.match(RE_MIN, line):
        return "LT"

    return False


def is_addition(line, expression):

    try:

        x = re.match(RE_ADDITION, line).groups()
        tokens.append([ADD_OP, x[1]])

        expression += "("
        op1_exp = arithmetic_type_checker(x[2], expression)
        if(op1_exp == False):
            return False
        else:
            expression = op1_exp[1]
            expression += op1_exp[0]

        tokens.append([ADD_CXT, x[3]])
        expression += "+"

        op2_exp = arithmetic_type_checker(x[4], expression)
        if(op2_exp == False):
            return False
        else:
            expression = op2_exp[1]
            expression += op2_exp[0]

        expression += ")"

        return(expression)

    except:
        pass

    return False


def is_subtraction(line, expression):

    try:
        
        x = re.match(RE_SUBTRACTION, line).groups()
        tokens.append([SUB_OP, x[1]])

        expression += "("
        op1_exp = arithmetic_type_checker(x[2], expression)
        if(op1_exp == False):
            return False
        else:
            expression = op1_exp[1]
            expression += op1_exp[0]

        tokens.append([SUB_CXT, x[3]])
        expression += "-"

        op2_exp = arithmetic_type_checker(x[4], expression)
        if(op2_exp == False):
            return False
        else:
            expression = op2_exp[1]
            expression += op2_exp[0]

        expression += ")"

        return(expression)

    except:

        pass

    return False


def is_multiplication(line, expression):

    try:

        x = re.match(RE_MULTIPLICATION, line).groups()
        tokens.append([MUL_OP, x[1]])

        expression += "("
        op1_exp = arithmetic_type_checker(x[2], expression)
        if(op1_exp == False):
            return False
        else:
            expression = op1_exp[1]
            expression += op1_exp[0]

        tokens.append([MUL_CXT, x[3]])
        expression += "*"

        op2_exp = arithmetic_type_checker(x[4], expression)

        if(op2_exp == False):
            return False

        else:
            expression = op2_exp[1]
            expression += op2_exp[0]

        expression += ")"

        return(expression)
    except:
        pass

    return False


def is_division(line, expression):

    try:
        x = re.match(RE_DIVISION, line).groups()
        tokens.append([DIV_OP, x[1]])

        expression += "("
        op1_exp = arithmetic_type_checker(x[2], expression)
        if(op1_exp == False):
            return False
        else:
            expression = op1_exp[1]
            expression += op1_exp[0]

        tokens.append([DIV_CXT, x[3]])
        expression += "/"

        op2_exp = arithmetic_type_checker(x[4], expression)
        if(op2_exp == False):
            return False
        else:
            expression = op2_exp[1]
            expression += op2_exp[0]

        expression += ")"

        return(expression)

    except:
        pass

    return False


def is_max(line, expression):

    try:

        x = re.match(RE_MAX, line).groups()
        tokens.append([MAX_OP, x[1]])

        expression += "("
        op1_exp = arithmetic_type_checker(x[2], expression)
        if(op1_exp == False):
            return False
        else:
            expression = op1_exp[1]
            expression += "max("+op1_exp[0]

        tokens.append([MAX_CXT, x[3]])
        expression += ","

        op2_exp = arithmetic_type_checker(x[4], expression)
        if(op2_exp == False):
            return False
        else:
            expression = op2_exp[1]
            expression += op2_exp[0]+")"

        expression += ")"

        return(expression)
    except:
        pass

    return False


def is_min(line, expression):
    try:
        x = re.match(RE_MIN, line).groups()
        tokens.append([MIN_OP, x[1]])

        expression += "("
        op1_exp = arithmetic_type_checker(x[2], expression)
        if(op1_exp == False):
            return False
        else:
            expression = op1_exp[1]
            expression += "min("+op1_exp[0]

        tokens.append([MIN_CXT, x[3]])
        expression += ","

        op2_exp = arithmetic_type_checker(x[4], expression)

        if(op2_exp == False):
            return False

        else:
            expression = op2_exp[1]
            expression += op2_exp[0]+")"

        expression += ")"

        return(expression)
    except:
        pass

    return False

# fxn to check and handle arguments/operands
# of arithmetic operations


def arithmetic_type_checker(line, expression):

    # Check first if it's an arithmetic operation 
    # and will recall the fxn to handle them

    summ = is_addition(line, expression)
    if summ != False:
        return(["", summ])

    diff = is_subtraction(line, expression)
    if diff != False:
        return(["", diff])

    prod = is_multiplication(line, expression)
    if prod != False:
        return(["", prod])

    quot = is_division(line, expression)
    if quot != False:
        return(["", quot])

    maxed = is_max(line, expression)
    if maxed != False:
        return(["", maxed])

    mined = is_min(line, expression)
    if mined != False:
        return(["", mined])

    equaled = is_equal_comparison(line, expression)
    if equaled != False:
        return(["", equaled])

    notequaled = is_notequal_comparison(line, expression)
    if notequaled != False:
        return(["", notequaled])

    # line/string is either a literal or variable
    if re.match(R_STR, line):
        new = line.strip('"')
        tokens.append([STR_LIT, new])
        return([str(new), expression])

    elif re.match(R_NUMBAR, line):
        tokens.append([NBAR_LIT, line])
        return([str(line), expression])

    elif re.match(R_NUMBR, line):
        tokens.append([NBR_LIT, line])
        return([str(line), expression])

    elif re.match(R_VARIABLE, line):
        if variables.__contains__(line):
            tokens.append([VAR_IDENT, line])
            return([str(variables[line]), expression])

    # if no matches == invalid data type 
    # for arithmetic operations

    else:
        return False

# Boolean Operations


def is_and(line, mode, expression):
    try:

        x = re.match(RE_AND, line).groups()
        tokens.append([AND_OP, x[1]])

        expression += "("
        op1_exp = boolean_type_checker(x[2], 0, expression)

        if(op1_exp == False):
            return False
        else:
            expression = op1_exp[1]
            expression += op1_exp[0]

        tokens.append([AND_CXT, x[3]])
        expression += " and "
        op2_exp = boolean_type_checker(x[4], mode, expression)

        if(op2_exp == False):
            return False
        else:
            expression = op2_exp[1]
            expression += op2_exp[0]

        if mode == 0:
            expression += ")"

        return(expression)

    except:
        pass

    return False


def is_or(line, mode, expression):

    try:

        x = re.match(RE_OR, line).groups()
        tokens.append([OR_OP, x[1]])

        expression += "("
        op1_exp = boolean_type_checker(x[2], 0, expression)

        if(op1_exp == False):
            return False
        else:
            expression = op1_exp[1]
            expression += op1_exp[0]

        tokens.append([OR_CXT, x[3]])
        expression += " or "
        op2_exp = boolean_type_checker(x[4], mode, expression)

        if(op2_exp == False):
            return False
        else:
            expression = op2_exp[1]
            expression += op2_exp[0]

        if mode == 0:
            expression += ")"

        return(expression)
    except:
        pass

    return False


def is_xor(line, mode, expression):

    try:

        x = re.match(RE_XOR, line).groups()
        tokens.append([XOR_OP, x[1]])

        expression += "("
        op1_exp = boolean_type_checker(x[2], 0, expression)

        if(op1_exp == False):
            return False
        else:
            expression = op1_exp[1]
            expression += op1_exp[0]

        tokens.append([XOR_CXT, x[3]])
        expression += " ^ "
        op2_exp = boolean_type_checker(x[4], mode, expression)

        if(op2_exp == False):
            return False
        else:
            expression = op2_exp[1]
            expression += op2_exp[0]

        if mode == 0:
            expression += ")"

        return(expression)

    except:
        pass

    return False


def is_not(line, mode, expression):

    try:

        x = re.match(RE_NOT, line).groups()

        tokens.append([NOT_OP, x[1]])
        expression += "("
        op1_exp = boolean_type_checker(x[2], 0, expression)

        if(op1_exp == False):
            return False
        else:
            expression = op1_exp[1]
            expression += "not " + op1_exp[0]

        if mode == 0:
            expression += ")"

        return(expression)

    except:
        pass

    return False


def is_infinite_and(line, expression):
    try:

        x = re.match(RE_INFINITE_AND, line).groups()
        tokens.append([INF_AND_OP, x[1]])
        op1_exp = boolean_type_checker(x[2], "And", expression)
        if(op1_exp == False):
            return False
        else:
            expression = op1_exp[1]
            expression += op1_exp[0]

        return(expression)
        
    except:
        pass

    return False


def is_infinite_or(line, expression):
    try:
        x = re.match(RE_INFINITE_OR, line).groups()
        tokens.append([INF_AND_OP, x[1]])
        op1_exp = boolean_type_checker(x[2], "Or", expression)
        if(op1_exp == False):
            return False
        else:
            expression = op1_exp[1]
            expression += op1_exp[0]

        return(expression)
    except:
        pass

    return False

# fxn to check and handle arguments/operands 
# of boolean operations


def boolean_type_checker(line, mode, expression):

    # Check if line/string is either a 
    # troof literal or variable

    if re.match(R_TROOF, line):
        tokens.append([TROOF_LIT, line])
        return([str(line), expression])

    if re.match(R_VARIABLE, line):
        if variables.__contains__(line):
            tokens.append([VAR_IDENT, line])
            return([str(variables[line]), expression])

    # To handle last 2 strings 
    # (literal/variable and delimiter)

    end_strings = line.split(" ")

    if len(end_strings) == 2:

        if re.match(R_TROOF, end_strings[0]):
            tokens.append([TROOF_LIT, end_strings[0]])
            arg1 = str(end_strings[0])

        elif re.match(R_VARIABLE, end_strings[0]):

            # Check if variable exists in 
            # variables dictionary

            if variables.__contains__(end_strings[0]):
                tokens.append([VAR_IDENT, end_strings[0]])
                arg1 = str(variables[end_strings[0]])

            # Variable referenced does not exist
            else:
                return False

        if re.match(RE_INFBOOL_DELIMITER, end_strings[1]):
            tokens.append(["Infinite "+mode+" Delimiter", end_strings[1]])

        return([arg1 + ")", expression])

    elif(mode == 0):

        # Mode 0 expects 1 troof literal only, 
        # otherwise it's an error

        return False       

    # Check if line/string is a boolean operation and 
    # will recall the fxn to handle them

    anded = is_and(line, mode, expression)
    if anded != False:
        return(["", anded])

    ored = is_or(line, mode, expression)
    if ored != False:
        return(["", ored])

    xored = is_xor(line, mode, expression)
    if xored != False:
        return(["", xored])

    noted = is_not(line, mode, expression)
    if noted != False:
        return(["", noted])

    # To handle the AN connector 
    # for infinite arity

    try:

        x = re.match(RE_INFBOOL_CONNECTOR, line).groups()
        op1_exp = boolean_type_checker(x[0], 0, expression)

        if(op1_exp == False):
            return False

        else:

            tokens.append([mode+" Connector", x[1]])
            expression = op1_exp[1]
            expression += op1_exp[0] + ") " + mode.lower() + " "
            op2_exp = boolean_type_checker(x[2], mode, expression)

            if(op2_exp == False):
                return False
            else:
                expression = op2_exp[1]
                expression += op2_exp[0]
                return(["", expression])

    except:
        pass

    return False


# fxn that checks if the line is an 
# expression and returns the evaluated result

def is_expression(line):

    add = is_addition(line, "")
    if add:
        variables[IT] = str(eval(add))
        return True

    diff = is_subtraction(line, "")
    if diff:
        variables[IT] = str(eval(diff))
        return True

    prod = is_multiplication(line, "")
    if prod:
        variables[IT] = str(eval(prod))
        return True

    quot = is_division(line, "")
    if quot:
        variables[IT] = str(eval(quot))
        return True

    maxed = is_max(line, "")
    if maxed:
        variables[IT] = str(eval(maxed))
        return True

    mined = is_min(line, "")
    if mined:
        variables[IT] = str(eval(mined))
        return True

    equal = is_equal_comparison(line, "")
    if equal:
        variables[IT] = str(eval(equal))
        return True

    notequal = is_notequal_comparison(line, "")
    if notequal:
        variables[IT] = str(eval(notequal))
        return True

    anded = is_and(line, 0, "")
    if anded:
        anded = process_bool(anded)
        variables[IT] = str(eval(anded))
        return True

    ored = is_or(line, 0, "")
    if ored:
        ored = process_bool(ored)
        variables[IT] = str(eval(ored))
        return True

    xored = is_xor(line, 0, "")
    if xored:
        xored = process_bool(xored)
        variables[IT] = str(eval(xored))
        return True

    noted = is_not(line, 0, "")
    if noted:
        noted = process_bool(noted)
        variables[IT] = str(eval(noted))
        return True

    infanded = is_infinite_and(line, "")
    if infanded:
        infanded = process_bool(infanded)
        variables[IT] = str(eval(infanded))
        return True

    infored = is_infinite_or(line, "")
    if infored:
        infored = process_bool(infored)
        variables[IT] = str(eval(infored))
        return True

    return None

# Tool fxn 
# to process

def process_bool(line):
    line = line.replace("WIN", "True")
    line = line.replace("FAIL", "False")

    return(line)
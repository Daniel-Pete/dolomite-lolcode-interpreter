import re
from regex import *

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

def is_equal_comparison(line):
    try:
        category = ""

        x = re.match(RE_EQUAL_Comparison, line).groups()
        if(is_min_or_max(x[2]) != False):
            category = is_min_or_max(x[2])
        
        tokens.append([category+"Eq Comparison Operator", x[1]])
        if(arithmetic_type_checker(x[2]) == False): return False
        tokens.append([category+"Eq Comparison Connector", x[3]])
        if(arithmetic_type_checker(x[4]) == False): return False

        return True
    except:
        pass
    
    return False

def is_notequal_comparison(line):
    try:
        category = ""

        x = re.match(RE_NOTEQUAL_Comparison, line).groups()
        if(is_min_or_max(x[2]) != False):
            category = is_min_or_max(x[2])
        
        if category == "": category = "NE"
        tokens.append([category+" Comparison Operator", x[1]])
        if(arithmetic_type_checker(x[2]) == False): return False
        tokens.append([category+" Comparison Connector", x[3]])
        if(arithmetic_type_checker(x[4]) == False): return False

        return True
    except:
        pass

    return False

def is_min_or_max(line):
    if re.match(RE_MAX, line): return "GT"
    elif re.match(RE_MIN, line): return "LT"

    return False

def is_addition(line, expression):
    try:
        x = re.match(RE_ADDITION, line).groups()
        tokens.append(["Addition Operator", x[1]])

        expression += "("
        op1_exp = arithmetic_type_checker(x[2], expression)
        if(op1_exp == False): return False
        else:
            expression = op1_exp[1]
            expression += op1_exp[0]

        tokens.append(["Addition Connector", x[3]])
        expression+="+"

        op2_exp = arithmetic_type_checker(x[4], expression)
        if(op2_exp == False): return False
        else: 
            expression = op2_exp[1]
            expression += op2_exp[0]

        expression+=")"
    
        return(expression)
    except:
        pass

    return False

def is_subtraction(line, expression):
    try:
        x = re.match(RE_SUBTRACTION, line).groups()
        tokens.append(["Subtraction Operator", x[1]])

        expression += "("
        op1_exp = arithmetic_type_checker(x[2], expression)
        if(op1_exp == False): return False
        else:
            expression = op1_exp[1] 
            expression += op1_exp[0]

        tokens.append(["Subtraction Connector", x[3]])
        expression+="-"

        op2_exp = arithmetic_type_checker(x[4], expression)
        if(op2_exp == False): return False
        else: 
            expression = op2_exp[1]
            expression += op2_exp[0]

        expression+=")"
    
        return(expression)
    except:
        pass

    return False

def is_multiplication(line, expression):
    try:
        x = re.match(RE_MULTIPLICATION, line).groups()
        tokens.append(["Multiplication Operator", x[1]])

        expression += "("
        op1_exp = arithmetic_type_checker(x[2], expression)
        if(op1_exp == False): return False
        else:
            expression = op1_exp[1] 
            expression += op1_exp[0]

        tokens.append(["Multiplication Connector", x[3]])
        expression+="*"

        op2_exp = arithmetic_type_checker(x[4], expression)
        if(op2_exp == False): return False
        else: 
            expression = op2_exp[1]
            expression += op2_exp[0]

        expression+=")"
    
        return(expression)
    except:
        pass

    return False

def is_division(line, expression):
    try:
        x = re.match(RE_DIVISION, line).groups()
        tokens.append(["Division Operator", x[1]])

        expression += "("
        op1_exp = arithmetic_type_checker(x[2], expression)
        if(op1_exp == False): return False
        else:
            expression = op1_exp[1] 
            expression += op1_exp[0]

        tokens.append(["Division Connector", x[3]])
        expression+="/"

        op2_exp = arithmetic_type_checker(x[4], expression)
        if(op2_exp == False): return False
        else: 
            expression = op2_exp[1]
            expression += op2_exp[0]

        expression+=")"
    
        return(expression)
    except:
        pass

    return False

def is_max(line):
    try:
        x = re.match(RE_MAX, line).groups()
        tokens.append(["Max Operator", x[1]])
        if(arithmetic_type_checker(x[2]) == False): return False
        tokens.append(["Max Connector", x[3]])
        if(arithmetic_type_checker(x[4]) == False): return False
    
        return True
    except:
        pass

    return False

def is_min(line):
    try:
        x = re.match(RE_MIN, line).groups()
        tokens.append(["Min Operator", x[1]])
        if(arithmetic_type_checker(x[2]) == False): return False
        tokens.append(["Min Connector", x[3]])
        if(arithmetic_type_checker(x[4]) == False): return False
    
        return True
    except:
        pass

    return False

# fxn to check and handle arguments/operands of arithmetic operations
def arithmetic_type_checker(line, expression):
    # Check first if it's an arithmetic operation and will recall the fxn to handle them
    summ = is_addition(line, expression)
    if summ != False: return(["",summ])
    diff = is_subtraction(line, expression)
    if diff != False: return(["",diff])
    prod = is_multiplication(line, expression)
    if prod != False: return(["",prod])
    quot = is_division(line, expression)
    if quot != False: return(["",quot])
    
    # line/string is either a literal or variable
    if re.match(R_STR, line):
        new = line.strip('"')
        tokens.append(["String Literal", new])
        return([str(new), expression])

    elif re.match(R_NUMBAR, line):
        tokens.append(["Numbar Literal", line])
        return([str(line), expression])

    elif re.match(R_NUMBR, line):
        tokens.append(["Numbr Literal", line])
        return([str(line), expression])

    elif re.match(R_VARIABLE, line):
        if variables.__contains__(line):
            tokens.append(["Variable Identifier", line])
            return([str(variables[line]), expression])

    # if no matches == invalid data type for arithmetic operations
    else: return False

# Boolean Operations
def is_and(line, mode, expression):
    try:
        x = re.match(RE_AND, line).groups()
        tokens.append(["And Operator", x[1]])

        expression += "("
        op1_exp = boolean_type_checker(x[2], 0, expression)
        if(op1_exp == False): return False
        else:
            expression = op1_exp[1]
            expression += op1_exp[0]

        tokens.append(["And Connector", x[3]])
        expression+=" and "

        op2_exp = boolean_type_checker(x[4], mode, expression)
        if(op2_exp == False): return False
        else: 
            expression = op2_exp[1]
            expression += op2_exp[0]

        if mode == 0: expression+=")"
        return(expression)
    except:
        pass

    return False

def is_or(line, mode, expression):
    try:
        x = re.match(RE_OR, line).groups()
        tokens.append(["Or Operator", x[1]])

        expression += "("
        op1_exp = boolean_type_checker(x[2], 0, expression)
        if(op1_exp == False): return False
        else:
            expression = op1_exp[1] 
            expression += op1_exp[0]

        tokens.append(["Or Connector", x[3]])
        expression+=" or "

        op2_exp = boolean_type_checker(x[4], mode, expression)
        if(op2_exp == False): return False
        else: 
            expression = op2_exp[1]
            expression += op2_exp[0]

        if mode == 0: expression+=")"
    
        return(expression)
    except:
        pass

    return False

def is_xor(line, mode, expression):
    try:
        x = re.match(RE_XOR, line).groups()
        tokens.append(["Xor Operator", x[1]])

        expression += "("
        op1_exp = boolean_type_checker(x[2], 0, expression)
        if(op1_exp == False): return False
        else:
            expression = op1_exp[1] 
            expression += op1_exp[0]

        tokens.append(["Xor Connector", x[3]])
        expression+=" ^ "

        op2_exp = boolean_type_checker(x[4], mode, expression)
        if(op2_exp == False): return False
        else: 
            expression = op2_exp[1]
            expression += op2_exp[0]

        if mode == 0: expression+=")"
    
        return(expression)
    except:
        pass

    return False

def is_not(line, mode, expression):
    try:
        x = re.match(RE_NOT, line).groups()
        tokens.append(["Not Operator", x[1]])
        expression += "("
        op1_exp = boolean_type_checker(x[2], 0, expression)
        if(op1_exp == False): return False
        else:
            expression = op1_exp[1]
            expression += "not " + op1_exp[0]

        if mode == 0: expression+=")"
    
        return(expression)
    except:
        pass

    return False

def is_infinite_and(line, expression):
    try:
        x = re.match(RE_INFINITE_AND, line).groups()
        tokens.append(["Infinite And Operator", x[1]])
        op1_exp = boolean_type_checker(x[2], "And", expression)
        if(op1_exp == False): return False
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
        tokens.append(["Infinite And Operator", x[1]])
        op1_exp = boolean_type_checker(x[2], "Or", expression)
        if(op1_exp == False): return False
        else:
            expression = op1_exp[1]
            expression += op1_exp[0]

        return(expression)
    except:
        pass

    return False

# fxn to check and handle arguments/operands of boolean operations
def boolean_type_checker(line, mode, expression):
    # Check if line/string is either a troof literal or variable
    if re.match(R_TROOF, line):
        tokens.append(["TROOF Literal", line])
        return([str(line), expression])

    if re.match(R_VARIABLE, line):
        if variables.__contains__(line):
            tokens.append(["Variable Identifier", line])
            return([str(variables[line]), expression])

    # To handle last 2 strings (literal/variable and delimiter)
    end_strings = line.split(" ")
    if len(end_strings) == 2:
        if re.match(R_TROOF, end_strings[0]):
            tokens.append(["TROOF Literal", end_strings[0]])
            arg1 = str(end_strings[0])
        elif re.match(R_VARIABLE, end_strings[0]):
            # Check if variable exists in variables dictionary
            if variables.__contains__(end_strings[0]):
                tokens.append(["Variable Identifier", end_strings[0]])
                arg1 = str(variables[end_strings[0]])
            # Variable referenced does not exist
            else:
                return False
            
        if re.match(RE_INFBOOL_DELIMITER, end_strings[1]):
            tokens.append(["Infinite "+mode+" Delimiter", end_strings[1]])
        
        return([arg1 + ")", expression])

    elif(mode == 0): return False       # Mode 0 expects 1 troof literal only, otherwise it's an error
    
    # Check if line/string is a boolean operation and will recall the fxn to handle them
    anded = is_and(line, mode, expression)
    if anded != False: return(["", anded])
    ored = is_or(line, mode, expression)
    if ored != False: return(["", ored])
    xored = is_xor(line, mode, expression)
    if xored != False: return(["", xored])
    noted = is_not(line, mode, expression)
    if noted != False: return(["", noted])


    # To handle the AN connector for infinite arity
    try:
        x=re.match(RE_INFBOOL_CONNECTOR, line).groups()
        op1_exp = boolean_type_checker(x[0], 0, expression)
        if(op1_exp == False): return False
        else:
            tokens.append([mode+" Connector", x[1]])
            expression = op1_exp[1]
            expression += op1_exp[0] + ") " + mode.lower() + " "
            op2_exp = boolean_type_checker(x[2], mode, expression)
            if(op2_exp == False): return False
            else:
                expression = op2_exp[1]
                expression += op2_exp[0]
                return(["", expression])
    
    except:
        pass


    return False

# Assignment Statement
def is_assign(line):
    try:
        x = re.match(RE_ASSIGN, line).groups()
        if(re.match(R_VARIABLE, x[1])):
            tokens.append(["Variable Identifier", x[1]])
        else: return False

        tokens.append(["Assignment Operator", x[2]])

        # Check if final argument is either a literal or variable
        if re.match(R_TROOF, x[3]):
            tokens.append(["TROOF Literal", x[3]])
            return True

        if re.match(R_STR, x[3]):
            new = x[3].strip('"')
            tokens.append(["String Literal", new])
            return True

        if re.match(R_NUMBAR, x[3]):
            tokens.append(["Numbar Literal", x[3]])
            return True

        if re.match(R_NUMBR, x[3]):
            tokens.append(["Numbr Literal", x[3]])
            return True

        if re.match(R_VARIABLE, x[3]):
            tokens.append(["Variable Identifier", x[3]])
            return True

        # It is an expression
        if(boolean_type_checker(x[3], 0) != False): return True
        if(arithmetic_type_checker(x[3]) != False): return True

        return True
    except:
        pass

    return False

# fxn that checks if the line is an expression and returns the evaluated result
def is_expression(line):
    add = is_addition(line, "")
    if add: return eval(add)
    diff = is_subtraction(line, "")
    if diff: return eval(diff)
    prod = is_multiplication(line, "")
    if prod: return eval(prod)
    quot = is_division(line, "")
    if quot: return eval(quot)

    anded = is_and(line, 0, "")
    if anded:
        anded = process_bool(anded)
        return eval(anded)

    ored = is_or(line, 0, "")
    if ored:
        ored = process_bool(ored)
        return eval(ored)

    xored = is_xor(line, 0, "")
    if xored:
        xored = process_bool(xored)
        return eval(xored)

    noted = is_not(line, 0, "")
    if noted:
        noted = process_bool(noted)
        return eval(noted)

    infanded = is_infinite_and(line, "")
    if infanded:
        infanded = process_bool(infanded)
        return eval(infanded)

    infored = is_infinite_or(line, "")
    if infored:
        infored = process_bool(infored)
        return eval(infored)

    return None

# Tool fxn to process 
def process_bool(line):
    line = line.replace("WIN", "True")
    line = line.replace("FAIL", "False")

    return(line)
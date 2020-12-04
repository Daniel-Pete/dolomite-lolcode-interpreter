import re
from regex import *

dataset = []

def is_var_assign(line):

    # Checks if the
    # line is variable
    # assignment

    try:

        # Access the matches
        # through the use of groups

        x = re.match(R_IHAI, line).groups()
        dataset.append(["Variable Declaration", str(x[1])])
        dataset.append(["Variable Identifier", str(x[2])])
        dataset.append(["Variable Assignment", str(x[3])])

        # If the variable matches a string
        # the string is stripped of its
        # quotation marks

        if re.match(R_STR, x[4]):
            new = x[4].strip('"')
            dataset.append(["String Literal", new])

        elif re.match(R_NUMBAR, x[4]):
            dataset.append(["Numbar Literal", x[4]])

        elif re.match(R_NUMBR, x[4]):
            dataset.append(["Numbr Literal", x[4]])

        return True

    except:

        pass

    # If it doesn't match
    # the next

    return False


def is_var_declare(line):

    # Checks if the
    # line is for variable
    # declaration

    try:
        x = re.match(R_IHA, line).groups()
        dataset.append(["Variable Declaration", x[1]])
        dataset.append(["Variable Identifier", x[2]])

        return True

    except:
        pass

    return False


def is_code_delimiter(line):

    # Checks if the
    # line is either HAI
    # or KTHXBYE

    if re.match(R_HAI, line) or re.match(R_KTB, line):
        dataset.append(["Code Connector", line])
        return True

    return False


def is_print(line):

    # Checks if the line
    # is for printing

    try:

        x = re.match(R_VISI, line).groups()
        dataset.append(["Print Identifier", x[0]])
        dataset.append(["Variable Identifier", x[1]])

        return True
    except:
        pass

    return False


def is_input(line):

    # Checks if the line
    # asks for an input

    try:
        x = re.match(R_GIME, line).groups()
        dataset.append(["Input Identifier", x[0]])
        dataset.append(["Variable Identifier", x[1]])

        return True
    except:
        pass

    return False


def is_comment(line):

    # Checks if the
    # line is a comment

    try:
        x = re.match(R_BTW, line).groups()
        dataset.append(["Comment Identifier", x[1]])
        dataset.append(["Comment", x[2]])

        return True
    except:
        pass

    return False


def is_if_then(line):

    try:
        x = re.match(R_ORLY, line).groups()
        dataset.append(["Control Flow Keyword", x[1]])
        return True
    except:
        pass

    return False


def is_end_if(line):

    try:
        x = re.match(R_OIC, line).groups()
        dataset.append(["Control Flow Keyword", x[1]])
        return True
    except:
        pass

    return False


def is_if(line):

    try:
        x = re.match(R_YARLY, line).groups()
        dataset.append(["Control Flow Keyword", x[1]])
        return True
    except:
        pass

    return False


def is_else(line):

    try:
        x = re.match(R_NOWAI, line).groups()
        dataset.append(["Control Flow Keyword", x[1]])
        return True
    except:
        pass

    return False


def is_switch(line):

    try:
        x = re.match(R_NOWAI, line).groups()
        dataset.append(["Control Flow Keyword", x[1]])
        return True
    except:
        pass

    return False


def is_switch(line):

    try:
        x = re.match(R_WTF, line).groups()
        dataset.append(["Control Flow Keyword", x[1]])
        return True
    except:
        pass

    return False


def is_case(line):

    try:
        x = re.match(R_OMG, line).groups()
        dataset.append(["Control Flow Keyword", x[1]])
        dataset.append(["Value Literal", x[2]])

        return True
    except:
        pass

    return False

def is_end_case(line):

    try:
        x = re.match(R_OMGWTF, line).groups()
        dataset.append(["Control Flow Keyword", x[1]])

        return True
    except:
        pass

    return False

def is_equal_comparison(line):
    try:
        category = ""

        x = re.match(RE_EQUAL_Comparison, line).groups()
        if(is_min_or_max(x[2]) != False):
            category = is_min_or_max(x[2])
        
        dataset.append([category+"Eq Comparison Operator", x[1]])
        if(arithmetic_type_checker(x[2]) == False): return False
        dataset.append([category+"Eq Comparison Connector", x[3]])
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
        dataset.append([category+" Comparison Operator", x[1]])
        if(arithmetic_type_checker(x[2]) == False): return False
        dataset.append([category+" Comparison Connector", x[3]])
        if(arithmetic_type_checker(x[4]) == False): return False

        return True
    except:
        pass

    return False

def is_min_or_max(line):
    if re.match(RE_MAX, line): return "GT"
    elif re.match(RE_MIN, line): return "LT"

    return False

def is_addition(line):
    try:
        x = re.match(RE_ADDITION, line).groups()
        dataset.append(["Addition Operator", x[1]])
        if(arithmetic_type_checker(x[2]) == False): return False
        dataset.append(["Addition Connector", x[3]])
        if(arithmetic_type_checker(x[4]) == False): return False
    
        return True
    except:
        pass

    return False

def is_subtraction(line):
    try:
        x = re.match(RE_SUBTRACTION, line).groups()
        dataset.append(["Subtraction Operator", x[1]])
        if(arithmetic_type_checker(x[2]) == False): return False
        dataset.append(["Subtraction Connector", x[3]])
        if(arithmetic_type_checker(x[4]) == False): return False
    
        return True
    except:
        pass

    return False

def is_multiplication(line):
    try:
        x = re.match(RE_MULTIPLICATION, line).groups()
        dataset.append(["Multiplication Operator", x[1]])
        if(arithmetic_type_checker(x[2]) == False): return False
        dataset.append(["Multiplication Connector", x[3]])
        if(arithmetic_type_checker(x[4]) == False): return False
    
        return True
    except:
        pass

    return False

def is_division(line):
    try:
        x = re.match(RE_DIVISION, line).groups()
        dataset.append(["Division Operator", x[1]])
        if(arithmetic_type_checker(x[2]) == False): return False
        dataset.append(["Division Connector", x[3]])
        if(arithmetic_type_checker(x[4]) == False): return False
    
        return True
    except:
        pass

    return False

def is_max(line):
    try:
        x = re.match(RE_MAX, line).groups()
        dataset.append(["Max Operator", x[1]])
        if(arithmetic_type_checker(x[2]) == False): return False
        dataset.append(["Max Connector", x[3]])
        if(arithmetic_type_checker(x[4]) == False): return False
    
        return True
    except:
        pass

    return False

def is_min(line):
    try:
        x = re.match(RE_MIN, line).groups()
        dataset.append(["Min Operator", x[1]])
        if(arithmetic_type_checker(x[2]) == False): return False
        dataset.append(["Min Connector", x[3]])
        if(arithmetic_type_checker(x[4]) == False): return False
    
        return True
    except:
        pass

    return False

# fxn to check and handle arguments/operands of arithmetic operations
def arithmetic_type_checker(line):
    # Check first if it's an arithmetic operation and will recall the fxn to handle them
    if is_addition(line): return ""
    if is_subtraction(line): return ""
    if is_multiplication(line): return ""
    if is_division(line): return ""
    if is_min(line): return "LT"
    if is_max(line): return "GT"
    
    # line/string is either a literal or variable
    if re.match(R_STR, line):
        new = line.strip('"')
        dataset.append(["String Literal", new])

    elif re.match(R_NUMBAR, line):
        dataset.append(["Numbar Literal", line])

    elif re.match(R_NUMBR, line):
        dataset.append(["Numbr Literal", line])

    elif re.match(R_VARIABLE, line):
        dataset.append(["Variable Identifier", line])

    # if no matches == invalid data type for arithmetic operations
    else: return False

# Boolean Operations
def is_and(line, mode):
    try:
        x = re.match(RE_AND, line).groups()
        dataset.append(["And Operator", x[1]])
        if(boolean_type_checker(x[2], 0) == False): return False
        dataset.append(["And Connector", x[3]])
        if(boolean_type_checker(x[4], mode) == False): return False
    
        return True
    except:
        pass

    return False

# Boolean Operations
def is_or(line, mode):
    try:
        x = re.match(RE_OR, line).groups()
        dataset.append(["Or Operator", x[1]])
        if(boolean_type_checker(x[2], 0) == False): return False
        dataset.append(["Or Connector", x[3]])
        if(boolean_type_checker(x[4], mode) == False): return False
    
        return True
    except:
        pass

    return False

# Boolean Operations
def is_xor(line, mode):
    try:
        x = re.match(RE_XOR, line).groups()
        dataset.append(["Xor Operator", x[1]])
        if(boolean_type_checker(x[2], 0) == False): return False
        dataset.append(["Xor Connector", x[3]])
        if(boolean_type_checker(x[4], mode) == False): return False
    
        return True
    except:
        pass

    return False

# Boolean Operations
def is_not(line, mode):
    try:
        x = re.match(RE_NOT, line).groups()
        dataset.append(["Not Operator", x[1]])
        if(boolean_type_checker(x[2], mode) == False): return False

        return True
    except:
        pass

    return False

def is_infinite_and(line):
    try:
        x = re.match(RE_INFINITE_AND, line).groups()
        dataset.append(["Infinite And Operator", x[1]])
        if(boolean_type_checker(x[2], "And") == False): return False

        return True
    except:
        pass

    return False

def is_infinite_or(line):
    try:
        x = re.match(RE_INFINITE_OR, line).groups()
        dataset.append(["Infinite Or Operator", x[1]])
        if(boolean_type_checker(x[2], "Or") == False): return False

        return True
    except:
        pass

    return False

# fxn to check and handle arguments/operands of boolean operations
def boolean_type_checker(line, mode):
    # Check if line/string is either a troof literal or variable
    if re.match(R_TROOF, line):
        dataset.append(["TROOF Literal", line])
        return True

    if re.match(R_VARIABLE, line):
        dataset.append(["Variable Identifier", line])
        return True

    elif(mode == 0): return False       # Mode 0 expects 1 troof literal only, otherwise it's an error

    # Check if line/string is a boolean operation and will recall the fxn to handle them
    if is_and(line, mode): return
    if is_or(line, mode): return
    if is_xor(line, mode): return
    if is_not(line, mode): return

    # To handle the AN connector for infinite arity
    try:
        x=re.match(RE_INFBOOL_CONNECTOR, line).groups()
        boolean_type_checker(x[0], 0)
        dataset.append([mode+" Connector", x[1]])
        boolean_type_checker(x[2], mode)
        return
    
    except:
        pass


    return False

# Assignment Statement
def is_assign(line):
    try:
        x = re.match(RE_ASSIGN, line).groups()
        if(re.match(R_VARIABLE, x[1])):
            dataset.append(["Variable Identifier", x[1]])
        else: return False

        dataset.append(["Assignment Operator", x[2]])

        # Check if final argument is either a literal or variable
        if re.match(R_TROOF, x[3]):
            dataset.append(["TROOF Literal", x[3]])
            return True

        if re.match(R_STR, x[3]):
            new = x[3].strip('"')
            dataset.append(["String Literal", new])

        if re.match(R_NUMBAR, x[3]):
            dataset.append(["Numbar Literal", x[3]])

        if re.match(R_NUMBR, x[3]):
            dataset.append(["Numbr Literal", x[3]])

            if re.match(R_VARIABLE, x[3]):
                dataset.append(["Variable Identifier", x[3]])
                return True

        # It is an expression
        if(boolean_type_checker(x[3], 0) == False): return False
        if(arithmetic_type_checker(x[3]) == False): return False

        return True
    except:
        pass

    return False
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
        dataset.append(["Code Delimiter", line])
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
        x = re.match(RE_EQUAL_Comparison, line).groups()
        dataset.append(["Eq Comparison Operator", x[1]])
        dataset.append(["Eq Comparison Operand", x[2]])
        dataset.append(["Eq Comparison Delimiter", x[3]])
        dataset.append(["Eq Comparison Operand", x[4]])

        return True
    except:
        pass
    
    return False

def is_notequal_comparison(line):
    try:
        x = re.match(RE_NOTEQUAL_Comparison, line).groups()
        dataset.append(["NE Comparison Operator", x[1]])
        dataset.append(["NE Comparison Operand", x[2]])
        dataset.append(["NE Comparison Delimiter", x[3]])
        dataset.append(["NE Comparison Operand", x[4]])

        return True
    except:
        pass

    return False

def is_addition(line):
    try:
        x = re.match(RE_ADDITION, line).groups()
        dataset.append(["Addition Operator", x[1]])
        if(type_checker(x[2]) == False): return False
        dataset.append(["Addition Delimiter", x[3]])
        type_checker(x[4])
    
        return True
    except:
        pass

    return False

def is_subtraction(line):
    try:
        x = re.match(RE_SUBTRACTION, line).groups()
        dataset.append(["Subtraction Operator", x[1]])
        if(type_checker(x[2]) == False): return False
        dataset.append(["Subtraction Delimiter", x[3]])
        type_checker(x[4])
    
        return True
    except:
        pass

    return False

def is_multiplication(line):
    try:
        x = re.match(RE_MULTIPLICATION, line).groups()
        dataset.append(["Multiplication Operator", x[1]])
        if(type_checker(x[2]) == False): return False
        dataset.append(["Multiplication Delimiter", x[3]])
        type_checker(x[4])
    
        return True
    except:
        pass

    return False

def is_division(line):
    try:
        x = re.match(RE_DIVISION, line).groups()
        dataset.append(["Division Operator", x[1]])
        if(type_checker(x[2]) == False): return False
        dataset.append(["Division Delimiter", x[3]])
        type_checker(x[4])
    
        return True
    except:
        pass

    return False

def is_max(line):
    try:
        x = re.match(RE_MAX, line).groups()
        dataset.append(["Max Operator", x[1]])
        if(type_checker(x[2]) == False): return False
        dataset.append(["Max Delimiter", x[3]])
        type_checker(x[4])
    
        return True
    except:
        pass

    return False

def is_max(line):
    try:
        x = re.match(RE_MIN, line).groups()
        dataset.append(["Min Operator", x[1]])
        if(type_checker(x[2]) == False): return False
        dataset.append(["Min Delimiter", x[3]])
        if(type_checker(x[4]) == False): return False
    
        return True
    except:
        pass

    return False

def type_checker(line):
    # Check first if it's an arithmetic operation and will recall the fxn to handle them
    if is_addition(line): return
    if is_subtraction(line): return
    if is_multiplication(line): return
    if is_division(line): return

    if re.match(R_STR, line):
        new = line.strip('"')
        dataset.append(["String Literal", new])

    elif re.match(R_NUMBAR, line):
        dataset.append(["Numbar Literal", line])

    elif re.match(R_NUMBR, line):
        dataset.append(["Numbr Literal", line])

    # if no matches == invalid data type for arithmetic operations
    else return False
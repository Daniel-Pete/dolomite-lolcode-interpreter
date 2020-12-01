# Branch David
# Lexical Analyser
# Nov 13 2020

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

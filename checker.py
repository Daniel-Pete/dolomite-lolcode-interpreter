# Branch David
# Checker
# Nov 13 2020

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
    # or KTHmatchBYE

    if re.match(R_HAI, line):
        tokens.append([COD_DEL, line])
        return True

    return False

def is_bye(line):

    if re.match(R_KTB, line):
        tokens.append([COD_DEL, line])
        return True

    return False



def concatenation(match):

    ints = re.findall(R_NUMBR, match)
    floats = re.findall(R_NUMBAR, match)
    strings = re.findall(R_STR, match)
    strings = [i.strip('"\'') for i in strings]

    # If there are string quotes, then it
    # will be split using '"'. Otherwise, it will
    # be split with space.

    if '"' in match:
        to_concat = [str(i).strip() for i in match.split('"') if i != '']
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
                i in floats):
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
            variables["IT"] = ''.join(concat)
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

        if concat:
            # print(''.join(concat))
            terminalPrint.append(''.join(concat).strip('"'))
            return True

        else:
            return False

    except:
        pass

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


def is_end_if(line):

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

        return True
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

    # All lines after OBTW
    # will be ignored 

    tokens.append([DOC_ID, line])
    return True

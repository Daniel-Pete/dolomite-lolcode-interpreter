# Branch David
# Checker
# Nov 13 2020

import re
from regex import *

global ERROR
ERROR = SYNTAX_ERROR


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

        # If the variable matches a string
        # the string is stripped of its
        # quotation marks

        if re.match(R_STR, match[4]):
            
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



def is_print(line):

    # Checks if the line
    # is for printing
    global ERROR

    try:

        match = re.match(R_VISI, line).groups()
        tokens.append([PRINT_ID, match[1]])
        tokens.append([VAR_IDENT, match[2]])

        if variables.__contains__(match[2]):

            if variables[match[2]] == None:
                ERROR = VAR_ERROR
                return False
            else:
                print(variables[match[2]].strip('"'))
        
        elif (re.match(R_NUMBR, match[2]) or 
            re.match(R_NUMBAR, match[2])):

            print(match[2])

        elif re.match(R_STR, match[2]):
            string = match[2].strip('"')
            print(string)

        else:
            ERROR = VAR_ERROR
            return False

            
        return True

    except:
        pass

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

    try:
        match = re.match(R_ORLY, line).groups()
        tokens.append([CF_KEY, match[1]])
        return True
    except:
        pass

    return False


def is_end_if(line):

    try:
        match = re.match(R_OIC, line).groups()
        tokens.append([CF_KEY, match[1]])
        return True
    except:
        pass

    return False


def is_if(line):

    try:
        match = re.match(R_YARLY, line).groups()
        tokens.append([CF_KEY, match[1]])
        return True
    except:
        pass

    return False


def is_else(line):

    try:
        match = re.match(R_NOWAI, line).groups()
        tokens.append([CF_KEY, match[1]])
        return True
    except:
        pass

    return False


def is_switch(line):

    try:
        match = re.match(R_WTF, line).groups()
        tokens.append([CF_KEY, match[1]])
        return True
    except:
        pass

    return False


def is_case(line):

    try:
        match = re.match(R_OMG, line).groups()
        tokens.append([CF_KEY, match[1]])
        tokens.append([VAL_LIT, match[2]])

        return True
    except:
        pass

    return False

def is_end_case(line):

    try:
        match = re.match(R_OMGWTF, line).groups()
        tokens.append([CF_KEY, match[1]])

        return True
    except:
        pass

    return False

def is_multicomment(line):

    try:
        match = re.match(R_OBTW, line).groups()
        tokens.append([COM_DEL, match[1]])

        if match[2]:
            tokens.append([DOC_ID, match[2]])


        return True
    except:
        pass

    return False


def is_end_multicomment(line):

    try:
        match = re.match(R_TLDR, line).groups()
        tokens.append([COM_DEL, match[1]])

        return True
    except:
        pass

    return False

def is_documentation(line):

    tokens.append([DOC_ID, line])
    return True


def is_anyof(line):

    try:

        match = re.match(R_ANYOF, line).groups()
        tokens.append([BOOL_OP, match[1]])
        tokens.append([VAR_IDENT, match[2]])

        
        if re.match(R_INFINITE_TROOF, match[3]):

            for i in re.findall(R_INFINITE_TROOF, match[3]):
                
                i = i.split()
                tokens.append([CON_KEY, i[0]])
                tokens.append([TROOF_LIT, i[1]])

        else:
            return False


        return True

    except:
        pass

    return False
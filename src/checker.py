# Branch David
# Lexical Analyser
# Nov 13 2020

import re
from regex import *

global ERROR
ERROR = SYNTAX_ERROR


dataset = []
varset = {}

def show_error(fn, num, line):

    
    print("File", fn, "line", num + 1)
    print("\n\t", line, "\n")
    print(ERROR)


def is_var_assign(line):

    # Checks if the
    # line is variable
    # assignment

    try:

        # Access the matches
        # through the use of groups

        x = re.match(R_IHAI, line).groups()
        
        dataset.append([VAR_DEC, str(x[1])])
        dataset.append([VAR_IDENT, str(x[2])])

        if x[3]: dataset.append([VAR_ASS, str(x[3])])

        # If the variable matches a string
        # the string is stripped of its
        # quotation marks

        if re.match(R_STR, x[4]):
            
            new = x[4].strip('"')
            dataset.append([STR_LIT, new])

        elif re.match(R_NUMBAR, x[4]):
            dataset.append([NBR_LIT, x[4]])

        elif re.match(R_NUMBR, x[4]):
            dataset.append([NBAR_LIT, x[4]])

        varset[str(x[2])] = x[4]


        return True

    except:

        pass
    
    return False


def is_var_declare(line):

    # Checks if the
    # line is for variable
    # declaration

    try:
        
        x = re.match(R_IHA, line).groups()

        dataset.append([VAR_DEC, x[1]])
        dataset.append([VAR_IDENT, x[2]])

        varset[str(x[2])] = None 

        return True

    except:

        pass

    return False


def is_hai(line):

    # Checks if the
    # line is either HAI
    # or KTHXBYE

    if re.match(R_HAI, line):
        dataset.append([COD_DEL, line])
        return True

    return False

def is_bye(line):

    if re.match(R_KTB, line):
        dataset.append([COD_DEL, line])
        return True

    return False



def is_print(line):

    # Checks if the line
    # is for printing
    global ERROR

    try:

        x = re.match(R_VISI, line).groups()
        dataset.append([PRINT_ID, x[1]])
        dataset.append([VAR_IDENT, x[2]])

        if varset.__contains__(x[2]):
            print(varset[x[2]])
        
        elif (re.match(R_NUMBR, x[2]) or 
            re.match(R_NUMBAR, x[2])):

            print(x[2])

        elif re.match(R_STR, x[2]):
            string = x[2].strip('"')
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
        x = re.match(R_GIME, line).groups()
        dataset.append([INPUT_ID, x[0]])
        dataset.append([VAR_IDENT, x[1]])

        
        if varset.__contains__(x[2]):
            varset[x[2]] = input()

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
        x = re.match(R_BTW, line).groups()
        dataset.append([COM_ID, x[1]])
        dataset.append([COM, x[2]])

        return True
    except:
        pass

    return False


def is_if_then(line):

    try:
        x = re.match(R_ORLY, line).groups()
        dataset.append([CF_KEY, x[1]])
        return True
    except:
        pass

    return False


def is_end_if(line):

    try:
        x = re.match(R_OIC, line).groups()
        dataset.append([CF_KEY, x[1]])
        return True
    except:
        pass

    return False


def is_if(line):

    try:
        x = re.match(R_YARLY, line).groups()
        dataset.append([CF_KEY, x[1]])
        return True
    except:
        pass

    return False


def is_else(line):

    try:
        x = re.match(R_NOWAI, line).groups()
        dataset.append([CF_KEY, x[1]])
        return True
    except:
        pass

    return False


def is_switch(line):

    try:
        x = re.match(R_WTF, line).groups()
        dataset.append([CF_KEY, x[1]])
        return True
    except:
        pass

    return False


def is_case(line):

    try:
        x = re.match(R_OMG, line).groups()
        dataset.append([CF_KEY, x[1]])
        dataset.append([VAL_LIT, x[2]])

        return True
    except:
        pass

    return False

def is_end_case(line):

    try:
        x = re.match(R_OMGWTF, line).groups()
        dataset.append([CF_KEY, x[1]])

        return True
    except:
        pass

    return False

def is_multicomment(line):

    try:
        x = re.match(R_OBTW, line).groups()
        dataset.append([COM_DEL, x[1]])

        if x[2]:
            dataset.append([DOC_ID, x[2]])



        return True
    except:
        pass

    return False


def is_end_multicomment(line):

    try:
        x = re.match(R_TLDR, line).groups()
        dataset.append([COM_DEL, x[1]])

        return True
    except:
        pass

    return False

def is_documentation(line):

    dataset.append([DOC_ID, line])
    return True


def is_anyof(line):

    try:

        x = re.match(R_ANYOF, line).groups()
        dataset.append([BOOL_OP, x[1]])
        dataset.append([VAR_IDENT, x[2]])

        
        if re.match(R_INFINITE_TROOF, x[3]):

            for i in re.findall(R_INFINITE_TROOF, x[3]):
                
                i = i.split()
                dataset.append([CON_KEY, i[0]])
                dataset.append([TROOF_LIT, i[1]])

        else:
            return False


        return True

    except:
        pass

    return False

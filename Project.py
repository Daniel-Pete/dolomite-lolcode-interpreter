import re

def loadInput():
    inputlist = []
    inputstring = ""
    returnlist = []

    try: 
        texthandle = open("input.txt", "r")
        # Read the whole input file and assign it to a string
        inputstring = texthandle.read()
        # To handle new line character
        returnlist = inputstring.split("\n")

        texthandle.close()

    except:
        print("No input file")

    return(returnlist)

def is_equal_comparison(line):
    RE_EQUAL_Comparison = "(BOTH SAEM) (-?[0-9]+|-?[0-9]*\.[0-9]+) (AN) (-?[0-9]+|-?[0-9]*\.[0-9]+)"
    try:
        comp = re.match(RE_EQUAL_Comparison, line).groups()
        print("Eq Comparison Starter:", comp[0])
        print("Eq Comparison Operand:", comp[1])
        print("Eq Comparison Operator:", comp[2])
        print("Eq Comparison Operand:", comp[3])
        print()
    except:
        pass

def is_notequal_comparison(line):
    RE_NOTEQUAL_Comparison = "(DIFFRINT) (-?[0-9]+|-?[0-9]*\.[0-9]+) (AN) (-?[0-9]+|-?[0-9]*\.[0-9]+)"
    try:
        comp = re.match(RE_NOTEQUAL_Comparison, line).groups()
        print("NE Comparison Starter:", comp[0])
        print("NE Comparison Operand:", comp[1])
        print("NE Comparison Operator:", comp[2])
        print("NE Comparison Operand:", comp[3])
        print()
    except:
        pass

RE_NUMBAR_Literal = "^-?[0-9]*\.[0-9]+$"
RE_YARN_Literal = "^\"[^\"]*\"$"
RE_TROOF_Literal = "^(WIN|FAIL)$"
RE_TYPE_Literal = "^(WIN|FAIL|\"[^\"]*\"|-?[0-9]*\.[0-9]*|-?[0-9]*)$"
RE_PRINT_Keyword = "^VISIBLE$"


inputlist = loadInput()
splitlist = []

for x in inputlist:
    splitlist += x.split(" ")

for line in inputlist:
    is_equal_comparison(line)
    is_notequal_comparison(line)

for token in splitlist:
    if(re.match(RE_NUMBAR_Literal, token)):
        print(token, "---> NUMBAR Literal")
    elif(re.match(RE_YARN_Literal, token)):
        print(token, "---> YARN Literal")
    elif(re.match(RE_TROOF_Literal, token)):
        print(token, "---> TROOF Literal")
    elif(re.match(RE_TYPE_Literal, token)):
        print(token, "---> TYPE Literal")
    elif(re.match(RE_PRINT_Keyword, token)):
        print(token, "---> YARN Literal")

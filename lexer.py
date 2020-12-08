from checker import *
file = "data/sample.lol"

def tokenize(fn):

    f = open(fn, "r")

    for num, line in enumerate(f):

        # Each line in the file
        # is checked for a match
        # Once the line matches a 
        # certain construct then it 
        # skips to the next iteration

        line = line.strip("\n")

        # if is_var_assign(line): continue
        # if is_var_declare(line): continue
        if is_code_delimiter(line): continue
        if is_var_initialize(line): continue
        # if is_print(line): continue
        # if is_input(line): continue
        # if is_comment(line): continue
        # if is_if_then(line): continue
        # if is_end_if(line): continue
        # if is_if(line): continue
        # if is_else(line): continue
        # if is_switch(line): continue
        # if is_case(line): continue
        # if is_end_case(line): continue
        # if is_equal_comparison(line): continue
        # if is_notequal_comparison(line, ""): continue
        # Checks if the line is an expression(arithmetic/boolean/comparison operation)
        exp = is_expression(line)
        if exp != None:
            print(exp)
            continue
        if is_assign(line): continue
        
        else:
            print("Invalid Syntax on Line",num + 1,line)
            break

def display(ds):
    print("Data Set")
    for i in ds:
        print(i)

def main():
    tokenize(file)
    display(tokens)

main()


# RE_NUMBAR_Literal = "^-?[0-9]*\.[0-9]+$"
# RE_YARN_Literal = "^\"[^\"]*\"$"
# RE_TROOF_Literal = "^(WIN|FAIL)$"
# RE_TYPE_Literal = "^(WIN|FAIL|\"[^\"]*\"|-?[0-9]*\.[0-9]*|-?[0-9]*)$"
# RE_PRINT_Keyword = "^VISIBLE$"


# inputlist = loadInput()
# splitlist = []

# for x in inputlist:
#     splitlist += x.split(" ")

# for line in inputlist:
#     is_equal_comparison(line)
#     is_notequal_comparison(line)

# for token in splitlist:
#     if(re.match(RE_NUMBAR_Literal, token)):
#         print(token, "---> NUMBAR Literal")
#     elif(re.match(RE_YARN_Literal, token)):
#         print(token, "---> YARN Literal")
#     elif(re.match(RE_TROOF_Literal, token)):
#         print(token, "---> TROOF Literal")
#     elif(re.match(RE_TYPE_Literal, token)):
#         print(token, "---> TYPE Literal")
#     elif(re.match(RE_PRINT_Keyword, token)):
#         print(token, "---> YARN Literal")

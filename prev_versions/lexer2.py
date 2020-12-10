from checker2 import *
file = "data/sample2.lol"

def tokenize(fn):

    f = open(fn, "r")

    for num, line in enumerate(f):

        # Each line in the file
        # is checked for a match
        # Once the line matches a 
        # certain construct then it 
        # skips to the next iteration

        line = line.strip("\n")

        if is_code_delimiter(line): continue
        if is_var_initialize(line): continue
        exp = is_expression(line)
        if exp != None:
            print("check",exp)
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

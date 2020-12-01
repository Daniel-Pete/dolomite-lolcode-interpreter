# Branch David
# Lexical Analyser
# Nov 13 2020

from checker import *

file = "../data/sample.txt"

def tokenize(fn):

    f = open(fn, "r")

    for num, line in enumerate(f):

        # Each line in the file
        # is checked for a match
        # Once the line matches a 
        # certain construct then it 
        # skips to the next iteration

        line = line.strip("\n")

        if is_var_assign(line): continue
        if is_var_declare(line): continue
        if is_code_delimiter(line): continue
        if is_print(line): continue
        if is_input(line): continue
        if is_comment(line): continue
        if is_if_then(line): continue
        if is_end_if(line): continue
        if is_if(line): continue
        if is_else(line): continue
        if is_switch(line): continue
        if is_case(line): continue
        if is_end_case(line): continue
        
        else:
            print("Invalid Syntax on Line",num + 1,line)
            break
 

def display(ds):
    print("Data Set")
    for i in ds:
        print(i)

def main():
    tokenize(file)
    display(dataset)


main()





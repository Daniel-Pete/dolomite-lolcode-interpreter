
# Code Delimiters
R_HAI = "^(\s*)HAI(\s*)$"
R_KTB = "^(\s*)KTHXBYE(\s*)$"

# Literals
R_STR = "\"[^\"]*\""
R_NUMBR = "-?[0-9]+"
R_NUMBAR = "-?[0-9]*\.[0-9]*"
R_VARIABLE = "^[a-zA-Z]+[a-zA-Z0-9\_]*$"
R_VARIDENT = "([a-zA-Z]+[a-zA-Z0-9\_]*)"
R_WIN = "WIN"
R_FAIL = "FAIL"
R_TROOF = "^WIN$|^FAIL$"
R_BOOLEAN = "^True$|^False$"


# Variable Declaration, Initialization, Assignment
R_IHA = "(\s*)(I HAS A) ([a-zA-Z]+[a-zA-Z0-9\_]*)"
R_IHAI = "(\s*)(I HAS A) ([a-zA-Z]+[a-zA-Z0-9\_]*) (ITZ) ([a-zA-Z\s]+[a-zA-Z0-9\_\s]*|-?[0-9]*\.[0-9]+|-?[0-9]+|\"[^\"]*\"|WIN|FAIL)"
R_ASS = "(\s*)([a-zA-Z]+[a-zA-Z0-9\_]*) (R) ([a-zA-Z\s]+[a-zA-Z0-9\_\s]*|-?[0-9]*\.[0-9]+|-?[0-9]+|\"[^\"]*\"|WIN|FAIL)"

# Input / Output
R_VISI = "(\s*)(VISIBLE) (.*)(\s*)"
R_GIME = "(\s*)(GIMMEH) ([a-zA-Z]+[a-zA-Z0-9\_]*)([\s]*)"

# Documentation
R_BTW = "(\s*)(BTW) ([a-zA-Z0-9\_\s]*)"
R_OBTW2 = "(\s*)(OBTW)(\s*)"
R_OBTW = "(\s*)(OBTW)(\s)(.*)"
R_TLDR = "(\s*)(TLDR)(\s*)"

# If-Else Statements
R_ORLY = "(\s*)(O RLY?)(\s*)"
R_YARLY = "(\s*)(YA RLY)(\s*)"
R_NOWAI = "(\s*)(NO WAI)(\s*)"
R_OIC = "(\s*)(OIC)(\s*)"

# Switch-Case Statements 
R_WTF = "(\s*)(WTF\?)(\s*)"
R_OMG = "(\s*)(OMG) ([a-zA-Z]+[a-zA-Z0-9\_]*|-?[0-9]*\.[0-9]+|-?[0-9]+|\"[^\"]*\"|WIN|FAIL)"
R_OMGWTF = "(\s*)(OMGWTF)(\s*)"
R_GTFO = "(\s*)(GTFO)(\s*)"

# Other
R_LOOP = "^[a-zA-Z]+[a-zA-Z0-9\_]*$"
R_EMPTY = "(^\s*$)"
R_SMOOSH = "(\s*)(SMOOSH) (.*)"

# Comparison Operations
R_EQUAL_COMPARISON = "(\s*)(.*)(BOTH SAEM) ([^ ]*) (AN) ([^ ]*)(.*)"
R_NOTEQUAL_COMPARISON = "(\s*)(.*)(DIFFRINT) ([^ ]*) (AN) ([^ ]*)(.*)"

# Arithmetic Operations
R_ADDITION = "(\s*)(.*)(SUM OF) ([^ ]*) (AN) ([^ ]*)(.*)"
R_SUBTRACTION = "(\s*)(.*)(DIFF OF) ([^ ]*) (AN) ([^ ]*)(.*)"
R_MULTIPLICATION = "(\s*)(.*)(PRODUKT OF) ([^ ]*) (AN) ([^ ]*)(.*)"
R_DIVISION = "(\s*)(.*)(QUOSHUNT OF) ([^ ]*) (AN) ([^ ]*)(.*)"
R_MODULO = "(\s*)(.*)(MOD OF) ([^ ]*) (AN) ([^ ]*)(.*)"
R_MAX = "(\s*)(.*)(BIGGR OF) ([^ ]*) (AN) ([^ ]*)(.*)"
R_MIN = "(\s*)(.*)(SMALLR OF) ([^ ]*) (AN) ([^ ]*)(.*)"

# Boolean Operations
R_AND = "(\s*)(.*)(BOTH OF) ([^ ]*) (AN) ([^ ]*)(.*)"
R_OR = "(\s*)(.*)(EITHER OF) ([^ ]*) (AN) ([^ ]*)(.*)"
R_XOR = "(\s*)(.*)(WON OF) ([^ ]*) (AN) ([^ ]*)(.*)"
R_NOT = "(\s*)(.*)(NOT) ([^ ]*)(.*)"
R_INFINITE_AND = "(\s*)(ALL OF) ([^ ]*) (AN) ([^ ]*)(.*)"
R_INFAND_BASE = "^(\s*)(ALL OF) ([^ ]*)$"
R_INFINITE_OR = "(\s*)(ANY OF) ([^ ]*) (AN) ([^ ]*)(.*)"
R_INFOR_BASE = "^(\s*)(ANY OF) ([^ ]*)$"


# Classification Constants
VAR_DEC = "Variable Declaration"
VAR_IDENT = "Variable Identifier"
VAR_ASS = "Variable Assignment"
STR_LIT = "String Literal"
NBR_LIT = "Numbr Literal"
NBAR_LIT = "Numbar Literal"
VAL_LIT = "Value Literal"
TROOF_LIT = "Troof Literal"
COD_DEL = "Code Delimiter"
PRINT_ID = "Print Identifier"
INPUT_ID = "Input Identifier"
DOC_ID = "Documentation"
COM_ID = "Comment Identifier"
COM_DEL = "Comment Delimiter"
COM = "Comment"
CF_KEY = "Control-Flow Keyword"
BOOL_OP = "Boolean Operation"
CON_KEY = "Connector Keyword"
CAT_OP = "Concatenation Keyword"

# Operations
EQ_OP = "EQ Comparison Operator"
EQ_COM_CXT = "EQ Comparison Connector"
COM_OP = " Comparison Operator"
COM_CXT = " Comparison Connector"
ADD_OP = "Addition Operator"
ADD_CXT = "Addition Connector"
SUB_OP = "Subtraction Operator"
SUB_CXT = "Subtraction Connector"
MUL_OP = "Multiplication Operator"
MUL_CXT = "Multiplication Connector"
DIV_OP = "Division Operator"
DIV_CXT = "Division Connector"
MAX_OP = "Max Operator"
MAX_CXT = "Max Connector"
MIN_OP = "Min Operator"
MIN_CXT = "Min Connector"
AND_OP = "And Operator"
AND_CXT = "And Connector"
OR_OP = "Or Operator"
OR_CXT = "Or Connector"
XOR_OP = "Xor Operator"
XOR_CXT = "Xor Connector"
NOT_OP = "Not Operator"
NOT_CXT = "Not Connector"
INF_AND_OP = "Infinite And Operator"


# Error Messages
SYNTAX_ERROR = "Syntax Error."
VAR_ERROR = "Undefined Error."
FILE_ERROR = "File Error: file cannot be found"

ERROR = SYNTAX_ERROR

# Toggles
START = "START"
STATEMENT = "STATEMENT"
IF = "IF"
ELSE = "ELSE"
END = "END"
SKIP = "SKIP"
MULTICOMMENT = "MULTICOMMENT"
IT = "IT"
SWITCH = "SWITCH"
OMG = "OMG"
OMG_STATEMENT = "OMG STATEMENT"
LAST_CASE = "LAST CASE"


# TROOFs
WIN = True
FAIL = False
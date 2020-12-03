# Branch David
# Lexical Analyser
# Nov 13 2020

R_LOOP = "^[a-zA-Z]+[a-zA-Z0-9\_]*$"

# Code Delimiters
R_HAI = "^HAI$"
R_KTB = "^KTHXBYE$"

# Literals
R_STR = "\"[^\"]*\""
R_NUMBR = "-?[0-9]+"
R_NUMBAR = "-?[0-9]*\.[0-9]"

# Variable Declaration, Initialization, Assignment
R_IHA = "(\s*)(I HAS A) ([a-zA-Z]+[a-zA-Z0-9\_]*)"
R_IHAI = "(\s*)(I HAS A) ([a-zA-Z]+[a-zA-Z0-9\_]*) (ITZ) (-?[0-9]*\.[0-9]+|-?[0-9]+|\"[^\"]*\")"
R_ASS = "(\s*)([a-zA-Z]+[a-zA-Z0-9\_]*) (R) (-?[0-9]*\.[0-9]+|-?[0-9]+|\"[^\"]*\")"

# Input / Output
R_VISI = "(\s*)(VISIBLE) (-?[0-9]*\.[0-9]+|-?[0-9]+|[a-zA-Z]+[a-zA-Z0-9\_]*|\"[^\"]*\")"
R_GIME = "(\s*)(GIMMEH) ([a-zA-Z]+[a-zA-Z0-9\_]*)"

# Documentation
R_BTW = "(\s*)(BTW) ([a-zA-Z0-9\_\s]*)"
R_OBTW = "(\s*)(OBTW) (-?[0-9]*\.[0-9]+|-?[0-9]+|[a-zA-Z]+[a-zA-Z0-9\_\s]*)"
R_TLDR = "(\s*)(TLDR)"

# If-Else Statements
R_ORLY = "(\s*)(ORLY)"
R_YARLY = "(\s*)(YA RLY)"
R_NOWAI = "(\s*)(NO WAI)"
R_OIC = "(\s*)(OIC)"

# Switch-Case Statements
R_WTF = "(\s*)(WTF\?)"
R_OMG = "(\s*)(OMG) (-?[0-9]+)"
R_OMGWTF = "(\s*)(OMGWTF)"

# Boolean Operation 
R_ANYOF = "(\s*)(ANY OF) (WIN|FAIL) ([A-Z\s]*)"
R_INFINITE_TROOF = "AN WIN|AN FAIL*"


# Classification

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


# Error Messages

SYNTAX_ERROR = "Syntax Error."
VAR_ERROR = "Undefined Error."

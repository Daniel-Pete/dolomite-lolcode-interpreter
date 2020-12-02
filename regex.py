R_LOOP = "^[a-zA-Z]+[a-zA-Z0-9\_]*$"
R_HAI = "^HAI$"
R_KTB = "^KTHXBYE$"
R_STR = "\"[^\"]*\""
R_NUMBR = "-?[0-9]+"
R_NUMBAR = "-?[0-9]*\.[0-9]"

R_IHA = "(\s*)(I HAS A) ([a-zA-Z]+[a-zA-Z0-9\_]*)"
R_IHAI = "(\s*)(I HAS A) ([a-zA-Z]+[a-zA-Z0-9\_]*) (ITZ) (-?[0-9]*\.[0-9]+|-?[0-9]+|\"[^\"]*\")"
R_VISI = "(\s*)(VISIBLE) (-?[0-9]*\.[0-9]+|-?[0-9]+|[a-zA-Z]+[a-zA-Z0-9\_]*)"
R_GIME = "(\s*)(GIMMEH) ([a-zA-Z]+[a-zA-Z0-9\_]*)"
R_BTW = "(\s*)(BTW) ([a-zA-Z0-9\_\s]*)"

# If-Else Statements
R_ORLY = "(\s*)(ORLY)"
R_YARLY = "(\s*)(YA RLY)"
R_NOWAI = "(\s*)(NO WAI)"
R_OIC = "(\s*)(OIC)"

# Switch-Case Statements
R_WTF = "(\s*)(WTF\?)"
R_OMG = "(\s*)(OMG) (-?[0-9]*\.[0-9])"
R_OMGWTF = "(\s*)(OMGWTF)"

# Comparison Statements
RE_EQUAL_Comparison = "(\s*)(BOTH SAEM) (-?[0-9]+|-?[0-9]*\.[0-9]+) (AN) (-?[0-9]+|-?[0-9]*\.[0-9]+)"
RE_NOTEQUAL_Comparison = "(\s*)(DIFFRINT) (-?[0-9]+|-?[0-9]*\.[0-9]+) (AN) (-?[0-9]+|-?[0-9]*\.[0-9]+)"

# Arithmetic Operations
RE_ADDITION = "(\s*)(SUM OF) (.*) (AN) (.*)"
RE_SUBTRACTION = "(\s*)(DIFF OF) (.*) (AN) (.*)"
RE_MULTIPLICATION = "(\s*)(PRODUKT OF) (.*) (AN) (.*)"
RE_DIVISION = "(\s*)(QUOSHUNT OF) (.*) (AN) (.*)"
RE_MODULO = "(\s*)(MOD OF) (.*) (AN) (.*)"
RE_MAX = "(\s*)(BIGGR OF) (.*) (AN) (.*)"
RE_MIN = "(\s*)(SMALLR OF) (.*) (AN) (.*)"


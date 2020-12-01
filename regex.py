# Branch David
# Lexical Analyser
# Nov 13 2020

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

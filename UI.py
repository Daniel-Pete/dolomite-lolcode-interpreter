from tkinter import *
from tkinter import ttk
from tkinter import filedialog, messagebox
import analyzer
import os

root = Tk()
root.title('LOLcode Interpreter')
root.geometry("1000x700")

global filename
filename = ""

global displayFilename
displayFilename = "Selected File: None"


# open file dialog 
def openFile():
    global filename, displayFilename
    filename = filedialog.askopenfilename(initialdir="/dmagu", title = "Select a LOLcode file", filetypes = (("LOL files", "*.lol"), ("All files", "*.*")))
    if filename:
        head, tail = os.path.split(filename)
        displayFilename = "Selected File: " + tail
        displayFile.config(text = displayFilename)

    
# clear all text in text area
def clear():
    textArea.delete(1.0, END)

# save the text in the text area
def saveText():
    global filename, displayFilename
    input = textArea.get("1.0", END)
    if not textArea.compare("end-1c", "==", "1.0"):
        with open("data/textArea.lol", "w") as wf:
            wf.write(input)
        filename = "data/textArea.lol"
        displayFilename = "Selected File: textArea.lol"
        displayFile.config(text = displayFilename)
    else: messagebox.showwarning("Message Box", "Text area input file is empty")


# executes the LOLcode file if the filename is not empty
# otherwise, it will prompt the user that no file has been selected
def getOutput():
    global filename

    # check if the filename is not empty
    if filename: 
        # clear the treeview first before putting any data
        removeAll(lexemeTable)
        removeAll(symbolTable)

        # process the file
        data = analyzer.analyze(filename)

        # display the data in the treeview (lexeme and symbol table)
        printLexeme(data[0])
        printSymbols(data[1])

        # this will print the output of the LOLcode file
        textOut = ""
        for text in data[2]:
            textOut += text

        outputText.config(state = NORMAL)
        outputText.delete(1.0, END)
        outputText.insert(END, textOut)
        outputText.config(state = DISABLED)

    else: messagebox.showwarning("Message Box", "No File Selected!")



# removes all the data in the treeview
def removeAll(table):
	for record in table.get_children():
		table.delete(record)


# display the lexemes on the treeview
def printLexeme(lexemeData):
    lexemeCount=0

    for lexeme in lexemeData:

        lexemeTable.insert(parent='', index='end', iid=lexemeCount, text="", values=(lexeme[0], lexeme[1]), tags=('lexemes_bg'))
        lexemeCount += 1


# display the symbol table on the treeview
def printSymbols(symbols):
    symCount=0

    for key, value in symbols.items():

        symbolTable.insert(parent='', index='end', iid=symCount, text="", values=(key, value), tags=('symbol_bg'))
        symCount += 1


# -------- Frames --------- #

# frame for file button
buttonFileFrame = Frame(root)
buttonFileFrame.pack(pady=20)

# frame for textarea, clear button, and save button
textFileFrame = Frame(root)
textFileFrame.pack(pady=20)

# frame for the execute button
executeButtonFrame = Frame(root)
executeButtonFrame.pack(pady=20)

# frame for the lexeme table label
labelLexeme = Frame(root)
labelLexeme.pack(pady = 20)

# frame for the symbol table label
labelSymbol = Frame(root)
labelSymbol.pack(pady = 20)

# frame for the output text area
outputFrame = Frame(root)
outputFrame.pack(pady=20)

# frame for lexeme treeview
lexemeFrame = Frame(root)
lexemeFrame.pack()

# frame for symbol table treeview
symbolFrame = Frame(root)
symbolFrame.pack(pady=20)


# ----------- Widgets ------------ #


#### Scrollbars #####

textScrollbar = Scrollbar(textFileFrame)
textScrollbar.pack(side = RIGHT, fill = Y)

outputScrollbar = Scrollbar(outputFrame)
outputScrollbar.pack(side = RIGHT, fill = Y)

#### Text Area/Box ####

textArea = Text(textFileFrame, font = ("Comic Sans", 11), height = 14, width = 40)
textArea.pack()

outputText = Text(outputFrame, font = ("Helvetica", 11), height = 15, width = 118, state = DISABLED)
outputText.pack()

#### Buttons ####

fileButton = Button(buttonFileFrame, text = "Open File", command = openFile, height = 1, width = 43, bg = "silver")
fileButton.pack()

clearButton = Button(textFileFrame, text = "CLEAR", command = clear, height = 1, width = 21, bg = "silver")
clearButton.pack(side = LEFT)

saveButton = Button(textFileFrame, text = "SAVE", command = saveText, height = 1, width = 21, bg = "silver")
saveButton.pack(side = RIGHT)

executeButton = Button(executeButtonFrame, text = "EXECUTE", command = getOutput, height = 1, width = 137, bg = "silver")
executeButton.pack()

#### Labels ####

displayFile = Label(buttonFileFrame, text = displayFilename)
displayFile.pack()

lexemeLabel = Label(labelLexeme, text = 'Lexemes', font = ("Arial", 20))
lexemeLabel.pack()

symbolLabel = Label(labelSymbol, text = 'Symbol Table', font = ("Arial", 20))
symbolLabel.pack()

#### Scrollbar Configure ####

outputText.config(yscrollcommand = outputScrollbar.set)
outputScrollbar.config(command = outputText.yview)

textArea.config(yscrollcommand = textScrollbar.set)
textScrollbar.config(command = textArea.yview)


# the lexemes and symbol table treeview code is based from this source code: https://github.com/flatplanet/Intro-To-TKinter-Youtube-Course/blob/master/tree.py

# ----------- Lexeme Treeview -------------#

# add style for the treeview
treeViewStyle = ttk.Style()
treeViewStyle.theme_use("default")

# configure our treeview colors
treeViewStyle.configure("Treeview", 
    background="white",
    foreground="black",
    rowheight=25,
    fieldbackground="white"
    )

# add scrollbar to the lexeme treeview
lexemeScroll = Scrollbar(lexemeFrame)
lexemeScroll.pack(side=RIGHT, fill=Y)

# create treeview for the lexemes
lexemeTable = ttk.Treeview(lexemeFrame, yscrollcommand=lexemeScroll.set)
lexemeTable.pack()

# configure the scrollbar
lexemeScroll.config(command=lexemeTable.yview)

# define Our columns for the lexeme table
lexemeTable['columns'] = ("Lexemes", "Classification")

# formate columns of lexeme table
lexemeTable.column("#0", width=0, stretch=NO)
lexemeTable.column("Lexemes", anchor=W, width=140)
lexemeTable.column("Classification", anchor=CENTER, width=140)


# create headings for the lexeme table
lexemeTable.heading("#0", text="", anchor=W)
lexemeTable.heading("Lexemes", text="Lexemes", anchor=W)
lexemeTable.heading("Classification", text="Classification", anchor=W)


# ----------- Symbol Table Treeview -------------#

# add scrollbar to the symbol table treeview
symbolScroll = Scrollbar(symbolFrame)
symbolScroll.pack(side=RIGHT, fill=Y)

# create treeview for the symbol table
symbolTable = ttk.Treeview(symbolFrame, yscrollcommand=symbolScroll.set)
symbolTable.pack()

# configure the scrollbar
symbolScroll.config(command=symbolTable.yview)

# define columns for the symbol table
symbolTable['columns'] = ("Identifier", "Value")

# format columns columns for the symbol table
symbolTable.column("#0", width=0, stretch=NO)
symbolTable.column("Identifier", anchor=W, width=140)
symbolTable.column("Value", anchor=CENTER, width=140)


# create headings for the symbol table
symbolTable.heading("#0", text="Identifier", anchor=W)
symbolTable.heading("Identifier", text="Identifier", anchor=W)
symbolTable.heading("Value", text="Value", anchor=W)


# window location of buttons and text area
buttonFileFrame.place(x = 180, y = 10, anchor = N)
textFileFrame.place(x = 190, y = 70, anchor = N)
executeButtonFrame.place(x = 500, y = 350, anchor = N)
outputFrame.place(x = 500, y = 400, anchor = N)
labelLexeme.place(x = 520, y = 10, anchor = N)
labelSymbol.place(x = 830, y = 10, anchor = N)
symbolFrame.place(x = 830, y = 50, anchor = N)
lexemeFrame.place(x = 520, y = 50, anchor = N)

# window is not resizable
root.resizable(False, False)
root.mainloop()
from tkinter import *
from tkinter import ttk
from tkinter import filedialog, simpledialog
import lexer
import os



root = Tk()
root.title('CMSC 124 Project')
root.geometry("1200x800")

global filename
filename = ""

global displayFilename
displayFilename = "Selected File: None"


# open file dialog 
def openFile():
    global filename, displayFilename
    filename = filedialog.askopenfilename(initialdir="/dmagu", title = "Select a LOLcode file", filetypes = (("LOL files", "*.lol"), ("All files", "*.*")))
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
    with open("textArea.lol", "w") as wf:
        wf.write(input)
    filename = "textArea.lol"
    displayFilename = "Selected File: " + filename
    displayFile.config(text = displayFilename)


def getOutput():
    global filename
    if filename: 
        removeAll(lexemeTable)
        removeAll(symbolTable)

    data = lexer.tokenize(filename)


    printLexeme(data[0])
    printSymbols(data[1])

    textOut = ""
    for text in data[2]:
        textOut += text + "\n"

    outputText.config(state = NORMAL)
    outputText.delete(1.0, END)
    outputText.insert(END, textOut)
    # getInputFromUser()
    outputText.config(state = DISABLED)

# def getInputFromUser():
#     gimmeInput = simpledialog.askstring("GIMME INPUT", "Enter your input")
#     print(gimmeInput)

# Remove all records
def removeAll(table):
	for record in table.get_children():
		table.delete(record)


def printLexeme(lexemeData):

    global lexemeCount
    lexemeCount=0

    for record in lexemeData:

        lexemeTable.insert(parent='', index='end', iid=lexemeCount, text="", values=(record[0], record[1]), tags=('lexemes_bg'))
        lexemeCount += 1


def printSymbols(variables):
    symCount=0

    for key, value in variables.items():

        symbolTable.insert(parent='', index='end', iid=symCount, text="", values=(key, value), tags=('symbol_bg',))
        symCount += 1


# frame for file button
buttonFileFrame = Frame(root)
buttonFileFrame.pack(pady=20)

# frame for textarea, clear button, and save button
textFileFrame = Frame(root)
textFileFrame.pack(pady=20)

# frame for the execute button
executeButtonFrame = Frame(root)
executeButtonFrame.pack(pady=20)

labelLexeme = Frame(root)
labelLexeme.pack(pady = 20)

labelSymbol = Frame(root)
labelSymbol.pack(pady = 20)

fileButton = Button(buttonFileFrame, text = "Select File", command = openFile, height = 1, width = 43)
fileButton.pack()

displayFile = Label(buttonFileFrame, text = displayFilename)
displayFile.pack()

lexemeLabel = Label(labelLexeme, text = 'Lexemes', font = ("Arial Bold", 20))
lexemeLabel.pack()

symbolLabel = Label(labelSymbol, text = 'Symbol Table', font = ("Arial Bold", 20))
symbolLabel.pack()

textScrollbar = Scrollbar(textFileFrame)
textScrollbar.pack(side = RIGHT, fill = Y)

textArea = Text(textFileFrame, font = ("Helvetica", 11), height = 14, width = 40)
textArea.pack()

clearButton = Button(textFileFrame, text = "CLEAR", command = clear, height = 1, width = 21)
clearButton.pack(side = LEFT)

saveButton = Button(textFileFrame, text = "SAVE", command = saveText, height = 1, width = 21)
saveButton.pack(side = RIGHT)

executeButton = Button(executeButtonFrame, text = "EXECUTE", command = getOutput, height = 1, width = 100)
executeButton.pack()

# window location of buttons and text area
buttonFileFrame.place(x = 200, y = 10, anchor = N)
textFileFrame.place(x = 200, y = 70, anchor = N)
executeButtonFrame.place(x = 600, y = 350, anchor = N)
labelLexeme.place(x = 600, y = 10, anchor = N)
labelSymbol.place(x = 1000, y = 10, anchor = N)


outputFrame = Frame(root)
outputFrame.pack(pady=20)

outputScrollbar = Scrollbar(outputFrame)
outputScrollbar.pack(side = RIGHT, fill = Y)

outputText = Text(outputFrame, font = ("Helvetica", 11), height = 15, width = 100, state = DISABLED)
outputText.pack()



outputText.config(yscrollcommand = outputScrollbar.set)
outputScrollbar.config(command = outputText.yview)



outputFrame.place(x = 600, y = 400, anchor = N)

textArea.config(yscrollcommand = textScrollbar.set)
textScrollbar.config(command = textArea.yview)


# the lexemes and symbol table treeview code is based from this source code: https://github.com/flatplanet/Intro-To-TKinter-Youtube-Course/blob/master/tree.py

# Add some style
lexemeStyle = ttk.Style()
lexemeStyle.theme_use("default")
# Configure our treeview colors

lexemeStyle.configure("Treeview", 
    background="#D3D3D3",
    foreground="black",
    rowheight=25,
    fieldbackground="#D3D3D3"
    )
# # Change selected color
# lexemeStyle.map('Treeview', 
# 	background=[('selected', 'blue')])

# Create Treeview Frame
lexemeFrame = Frame(root)
lexemeFrame.pack()

# Treeview Scrollbar
lexemeScroll = Scrollbar(lexemeFrame)
lexemeScroll.pack(side=RIGHT, fill=Y)

# Create Treeview
lexemeTable = ttk.Treeview(lexemeFrame, yscrollcommand=lexemeScroll.set)
# Pack to the screen
lexemeTable.pack()

#Configure the scrollbar
lexemeScroll.config(command=lexemeTable.yview)

# Define Our Columns
lexemeTable['columns'] = ("Lexemes", "Classification")

# Formate Our Columns
lexemeTable.column("#0", width=0, stretch=NO)
lexemeTable.column("Lexemes", anchor=W, width=140)
lexemeTable.column("Classification", anchor=CENTER, width=140)


# Create Headings 
lexemeTable.heading("#0", text="Lexemes", anchor=W)
lexemeTable.heading("Lexemes", text="Lexemes", anchor=W)
lexemeTable.heading("Classification", text="Classification", anchor=W)

# Create white bg for the lexemes tree view
lexemeTable.tag_configure('lexemes_bg', background="white")


symbolStyle = ttk.Style()
symbolStyle.theme_use("default")
# Configure our treeview colors

symbolStyle.configure("Treeview", 
    background="#D3D3D3",
    foreground="black",
    rowheight=25,
    fieldbackground="#D3D3D3"
    )
# Change selected color
symbolStyle.map('Treeview', 
    background=[('selected', 'blue')])

# Create Treeview Frame
symbolFrame = Frame(root)
symbolFrame.pack(pady=20)

# Treeview Scrollbar
symbolScroll = Scrollbar(symbolFrame)
symbolScroll.pack(side=RIGHT, fill=Y)

# Create Treeview
symbolTable = ttk.Treeview(symbolFrame, yscrollcommand=symbolScroll.set)
# Pack to the screen
symbolTable.pack()

#Configure the scrollbar
symbolScroll.config(command=symbolTable.yview)

# Define Our Columns
symbolTable['columns'] = ("Identifier", "Value")

# Formate Our Columns
symbolTable.column("#0", width=0, stretch=NO)
symbolTable.column("Identifier", anchor=W, width=140)
symbolTable.column("Value", anchor=CENTER, width=140)


# Create Headings 
symbolTable.heading("#0", text="Identifier", anchor=W)
symbolTable.heading("Identifier", text="Identifier", anchor=W)
symbolTable.heading("Value", text="Value", anchor=W)


# Create white bg for symbol table
symbolTable.tag_configure('symbol_bg', background="white")

symbolFrame.place(x = 1000, y = 50, anchor = N)
lexemeFrame.place(x = 600, y = 50, anchor = N)



root.mainloop()
from tkinter import *
from tkinter import ttk
from tkinter import filedialog


root = Tk()
root.title('CMSC 124 Project')
root.geometry("1200x800")


# open file dialog 
def openFile():
    filename = filedialog.askopenfilename(initialdir="/")
    print(filename)

# clear all text in text area
def clear():
    textArea.delete(1.0, END)

# save the text in the text area
def saveText():
    input = textArea.get("1.0",END)
    print(input)

# frame for file button
buttonFileFrame = Frame(root)
buttonFileFrame.pack(pady=20)

# frame for textarea, clear button, and save button
textFileFrame = Frame(root)
textFileFrame.pack(pady=20)


fileButton = Button(buttonFileFrame, text = "Select File", command = openFile, height = 1, width = 43)
fileButton.pack()

textArea = Text(textFileFrame, font = ("Helvetica", 11), height = 20, width = 40,)
textArea.pack()

clearButton = Button(textFileFrame, text = "Clear Text", command = clear, height = 1, width = 21)
clearButton.pack(side = LEFT)

saveButton = Button(textFileFrame, text = "Save Text", command = saveText, height = 1, width = 21)
saveButton.pack(side = RIGHT)

# window location of buttons and text area
buttonFileFrame.place(x = 200, y = 10, anchor = N)
textFileFrame.place(x = 200, y = 50, anchor = N)


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
# Change selected color
lexemeStyle.map('Treeview', 
	background=[('selected', 'blue')])

# Create Treeview Frame
lexemeFrame = Frame(root)
lexemeFrame.pack(pady=20)

# Treeview Scrollbar
lexemeScroll = Scrollbar(lexemeFrame)
lexemeScroll.pack(side=RIGHT, fill=Y)

# Create Treeview
lexemeTable = ttk.Treeview(lexemeFrame, yscrollcommand=lexemeScroll.set, selectmode="extended")
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


# Add Data
lexemeData = [
	["John", "Pepperoni"],
	["Mary", "Cheese"],
	["Tim", "Mushroom"],
	["Erin", "Ham"],
	["Bob", "Onion"],
	["Steve", "Peppers"],
    ["John", "Pepperoni"],
	["Mary", "Cheese"],
	["Tim", "Mushroom"],
	["Erin", "Ham"],
	["Bob", "Onion"],
	["Steve", "Peppers"],
    ["John", "Pepperoni"],
	["Mary", "Cheese"],
	["Tim", "Mushroom"],
	["Erin", "Ham"],
	["Bob", "Onion"],
	["Steve", "Peppers"],
    ["John", "Pepperoni"],
	["Mary", "Cheese"],
	["Tim", "Mushroom"],
	["Erin", "Ham"],
	["Bob", "Onion"],
	["Steve", "Peppers"]
]

# Create white bg for the lexemes tree view
lexemeTable.tag_configure('lexemes_bg', background="white")


global count
count=0


for record in lexemeData:

	lexemeTable.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1]), tags=('lexemes_bg',))
	count += 1




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
symbolTable = ttk.Treeview(symbolFrame, yscrollcommand=symbolScroll.set, selectmode="extended")
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


# Add Data
symbolData = [
	["John", "Pepperoni"],
	["Mary", "Cheese"],
	["Tim", "Mushroom"],
	["Erin", "Ham"],
	["Bob", "Onion"],
	["Steve", "Peppers"],
    ["John", "Pepperoni"],
	["Mary", "Cheese"],
	["Tim", "Mushroom"],
	["Erin", "Ham"],
	["Bob", "Onion"],
	["Steve", "Peppers"],
    ["John", "Pepperoni"],
	["Mary", "Cheese"],
	["Tim", "Mushroom"],
	["Erin", "Ham"],
	["Bob", "Onion"],
	["Steve", "Peppers"],
    ["John", "Pepperoni"],
	["Mary", "Cheese"],
	["Tim", "Mushroom"],
	["Erin", "Ham"],
	["Bob", "Onion"],
	["Steve", "Peppers"]
]

# Create white bg for symbol table
symbolTable.tag_configure('symbol_bg', background="white")


global symCount
symCount=0

for record in symbolData:

	symbolTable.insert(parent='', index='end', iid=symCount, text="", values=(record[0], record[1]), tags=('symbol_bg',))
	symCount += 1


symbolFrame.place(x = 1000, y = 50, anchor = N)
lexemeFrame.place(x = 600, y = 50, anchor = N)



root.mainloop()
import tkinter as tk
from tkinter import filedialog as fd
from tkinter import *
from useful import *


def f(name):
    print('hello', name)


Terminal.clear()


def fetchImgs():
    # global message
    pw = getpass.getpass("Password to pi: ")

message = ""

root=tk.Tk()
root.geometry("425x425")
imageDirList=[]

def browseFiles():
    global fileName
    fileName = fd.askopenfilename(initialdir = "/",title = "Select a File")

def addImage():
    browseFiles()
    imageDirList.append(fileName)
    print(imageDirList)

def removeImage():
    
    return

def reboot():

    pass



txtBoxFrame = tk.Frame()
txtBoxFrame.grid(row=1, column=0)

text_box = Text(
    txtBoxFrame,
    height=12,
    width=40,

)
text_box.pack(expand=True)
text_box.insert('end', message)
text_box.config(state='disabled')



btnFrame=tk.Frame()
btnFrame.grid(row=0,column=0)




addImageButton=tk.Button(btnFrame,text="Add Image",command=addImage)
addImageButton.grid(row=0, column=0)

removeImageButton=tk.Button(btnFrame,text="Remove Image",command=removeImage)
removeImageButton.grid(row=1, column=0)

rebootButton=tk.Button(btnFrame,text="Remove Image",command=reboot)
rebootButton.grid(row=2, column=0)



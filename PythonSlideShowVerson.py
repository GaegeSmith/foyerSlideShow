import tkinter as tk
from tkinter import filedialog as fd
from tkinter import *
from useful import *

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





txtBoxFrame = tk.Frame()
txtBoxFrame.grid(row=2, column=0)

text_box = Text(
    txtBoxFrame,
    height=12,
    width=40,

)
text_box.pack(expand=True)
text_box.insert('end', message)
text_box.config(state='disabled')



removeImageFrame=tk.Frame()
removeImageFrame.grid(row=1,column=0)

addImageFrame=tk.Frame()
addImageFrame.grid(row=0,column=0)



addImageButton=tk.Button(addImageFrame,text="Add Image",command=addImage)
addImageButton.pack(padx=175,pady=5)

removeImageButton=tk.Button(removeImageFrame,text="Remove Image",command=removeImage)
removeImageButton.pack(padx=175,pady=5)

root.mainloop()
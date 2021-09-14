import tkinter as tk
from tkinter import filedialog as fd
root=tk.Tk()
def browseFiles():
    global fileName
    fileName = fd.askopenfilename(initialdir = "/",title = "Select a File")
def addImage():
    browseFiles()
    print(fileName)
def removeImage():
    browseFiles()
    print(fileName)
root.geometry("500x500")

'''importFileFrame=tk.Frame()
importFileFrame.grid(row=0,column=0)'''

removeImageFrame=tk.Frame()
removeImageFrame.grid(row=1,column=0)

addImageFrame=tk.Frame()
addImageFrame.grid(row=0,column=0)

'''importFileButton=tk.Button(importFileFrame,text="Import File",command=browseFiles)
importFileButton.pack(padx=175,pady=5)'''

addImageButton=tk.Button(addImageFrame,text="Add Image",command=addImage)
addImageButton.pack(padx=175,pady=5)

removeImageButton=tk.Button(removeImageFrame,text="Remove Image",command=removeImage)
removeImageButton.pack(padx=175,pady=5)

root.mainloop()
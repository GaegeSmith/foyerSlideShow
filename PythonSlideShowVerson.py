import tkinter as tk
from tkinter import Image, filedialog as fd
from tkinter import Canvas,PhotoImage
root=tk.Tk()
imageCanvas=tk.Tk()
canvas = Canvas(imageCanvas,width=300,height=300)
canvas.pack()
imageDirList=[]
def browseFiles():
    global fileName
    fileName = fd.askopenfilename(initialdir = "/",title = "Select a File")
def addImage():
    browseFiles()
    print(fileName)
    imageDirList.append(fileName)
    print(imageDirList)
def removeImage():
    browseFiles()
    print(fileName)
    for i in imageDirList:
        if fileName==i:
            imageDirList.remove(fileName)
    print(imageDirList)
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
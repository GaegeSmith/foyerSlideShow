import tkinter as tk
from tkinter import filedialog as fd
from useful import *




Terminal.clear()


def fetchImgs():
    global message
    pw = getpass.getpass("Password to pi: ")

message = ""

root=tk.Tk()
root.geometry("425x425")
imageDirList=[]


def browseFiles():
    return fd.askopenfilename(initialdir = "/",title = "Select a File")

def addImage():
    imageDirList.append(browseFiles())
    print(imageDirList)

def removeImage():
    
    return

def reboot():
    for image in imageDirList:
        Terminal.sendSysCommand(f'powershell Copy-Item \\"{image}\\" {Terminal.filePath()}imgsToAdd\\')
    Terminal.sendSysCommand("python nameImgs.py")
    Terminal.sendSysCommand(f"powershell scp {Terminal.filePath()}imgsToAdd\\* pi@192.168.1.100:Documents/FoyerScreens")
    exit()


txtBoxFrame = tk.Frame()
txtBoxFrame.grid(row=1, column=0)

text_box = tk.Text(
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

rebootButton=tk.Button(btnFrame,text="Send images",command=reboot)
rebootButton.grid(row=2, column=0)





root.mainloop()
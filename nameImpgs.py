from useful import *
Terminal.clear()


onlyfiles = []


for f in os.listdir(Terminal.filePath() + "images\\"):
    onlyfiles.append(f"{Terminal.filePath()}images\\{f}")

for f in os.listdir(Terminal.filePath() + "imgsToAdd\\"):
    onlyfiles.append(f"{Terminal.filePath()}imgsToAdd\\{f}")




for i in range(len(onlyfiles)):
    tmpImg = onlyfiles[i].split(".")
    pathOfImg = tmpImg[0].split("\\")
    

    if os.name == "nt":

        imgName = f"{i}.{tmpImg[len(tmpImg) - 1]}"
        if "images" in pathOfImg:
            Terminal.sendSysCommand("cd .\\images")
        else:
            Terminal.sendSysCommand("cd .\\imgsToAdd")
        print(f'Ren "{pathOfImg[len(pathOfImg) - 1]}.{tmpImg[len(tmpImg) - 1]}" "{imgName}"')
        # Terminal.sendSysCommand(f'Ren "{pathOfImg[len(pathOfImg) - 1]}.{tmpImg[len(tmpImg) - 1]}" "{imgName}"')
    else:
        imgName = f"{Terminal.filePath()}{pathOfImg[len(pathOfImg) - 2]}\\{i}.{tmpImg[len(tmpImg) - 1]}"
        Terminal.sendSysCommand(f"mv {onlyfiles[i]} {imgName}")







# get a list of all filenames
from useful import *
Terminal.clear()


onlyfiles = []


for f in os.listdir(Terminal.filePath() + "images\\"):
    onlyfiles.append(f"{Terminal.filePath()}images\\{f}")

for f in os.listdir(Terminal.filePath() + "imgsToAdd\\"):
    onlyfiles.append(f"{Terminal.filePath()}imgsToAdd\\{f}")



psScriptFile = open("rename.ps1", "w")
psScript = ""

for i in range(len(onlyfiles)):
    tmpImg = onlyfiles[i].split(".")
    pathOfImg = tmpImg[0].split("\\")
    
    if os.name == "nt":
        imgName = f"{Terminal.filePath()}{pathOfImg[len(pathOfImg) - 2]}\\{i}.{tmpImg[len(tmpImg) - 1]}"
        psScript += f"mv \"{onlyfiles[i]}\" \"{imgName}\"\n"

    else:
        imgName = f"{Terminal.filePath()}{pathOfImg[len(pathOfImg) - 2]}\\{i}.{tmpImg[len(tmpImg) - 1]}"
        Terminal.sendSysCommand(f"mv \"{onlyfiles[i]}\" \"{imgName}\"\n")

if os.name == "nt":
    psScriptFile.write(psScript)
    psScriptFile.close()
    # time.sleep(10)
    Terminal.sendSysCommand(f"powershell {Terminal.filePath()}rename.ps1")
    






# get a list of all filenames
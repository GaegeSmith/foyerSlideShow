#$scriptpath = $MyInvocation.MyCommand.Path
#$dir = Split-Path $scriptpath
#Write-host "My directory is $dir"
Write-host "fileName = $fileName"
#Get-ChildItem -Path $dir
#New-Item -Path $dir'\textfile1' -ItemType file
Write-output "before scp"
scp.exe $fileName "pi@192.168.1.100:Documents/FoyerScreens/"
Write-output "finish scp"
#Move-Item -Path 'C:\Users\padawan\Documents\2122meterial\PLTWJava\Unit3\TestFolder1' -Destination 'C:\Users\padawan\Documents\2122meterial\PLTWJava\Unit3\Notes'
#Move-Item -Path $fileName -Destination $dir
#Add-Content 'C:\Users\padawan\Documents\2122meterial\PLTWJava\Unit3\why.ps1' "`nwhy not" #this is used to appand things to a file
Set-Variable -Name "movePath" -Value "C:\Users\padawan\Documents"
$scriptpath = $MyInvocation.MyCommand.Path
$dir = Split-Path $scriptpath
Write-host "My directory is $dir"
Get-ChildItem -Path $dir
New-Item -Path $dir'\textfile1' -ItemType file
#Move-Item -Path 'C:\Users\padawan\Documents\2122meterial\PLTWJava\Unit3\TestFolder1' -Destination 'C:\Users\padawan\Documents\2122meterial\PLTWJava\Unit3\Notes'
Move-Item -Path $dir'\textfile1' -Destination $movePath
#Add-Content 'C:\Users\padawan\Documents\2122meterial\PLTWJava\Unit3\why.ps1' "`nwhy not" #this is used to appand things to a file
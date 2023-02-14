import os
val = input("Enter commit text ")
os.system('git add .')
os.system('git status')
os.system('git commit -m "'+val+'"')
os.system('git push origin master')
os.system('git status')
os.system('git ftp push')

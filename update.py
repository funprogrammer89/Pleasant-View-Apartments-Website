import os
val = input("Enter commit text ")
cmd1 = 'git add .'
cmd2 = 'git commit -m "'+val+'"'
cmd3 = 'git push origin master'
cmd4 = 'git status'
os.system(cmd1)
os.system(cmd2)
os.system(cmd3)
os.system(cmd4)

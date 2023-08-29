#A Strange work of Python by MMXCawa
import os as o  
version = '1.1.6'
r = 18
update=version+':streamlined plus\nType "update" for new updates of "Python in Python"'
hint='Python in Python '+version+' (v'+version+'\\'+str(r)+' Aug 29 21:55:04),using Python '+o.sys.version+'\nType "help", "copyright", "credits" or "license()" for more information.\nType "update" for new updates of "Python in Python"'
print(hint)
while True:
    command = input('>>>')
    try:print(eval(command))
    except:print('Unknown Error')
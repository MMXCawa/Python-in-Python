#A Strange work of Python by MMXCawa
import os as o  
version = '1.1.5'
r = 17
update=version+':No,we cant use ^Z,quit,or import modules\nType "update" for new updates of "Python in Python"'
hint='Python in Python '+version+' (v'+version+'\\'+str(r)+' Aug 29 21:15:51),using Python '+o.sys.version+'\nType "help", "copyright", "credits" or "license()" for more information.\nType "update" for new updates of "Python in Python"'
class iftogo():
    global command
    def start():
        if 'copyright' in command:
            copyright()
print(hint)
while True:
    command = input('>>>')
    try:print(eval(command))
    except:print('Unknown Error')
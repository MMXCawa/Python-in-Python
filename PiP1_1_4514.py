import os as o  
version = '1.1.4514'
r = 16
update=version+':No,we cant use ^Z,quit,or import modules\nType "update" for new updates of "Python in Python"'
PiP='Python in Python '+version+' (v'+version+'\\'+str(r)+' Aug 29 20:46:11),using Python '+o.sys.version+'\nType "help", "copyright", "credits" or "license()" for more information.\nType "update" for new updates of "Python in Python"'
def root(x, y):
    return x**(1/y)
class iftogo():
    global command
    def start():
        if 'credits' == command:
            print('Python:')
            credits()
            print('''Python in Python:
        by MMXCawa
        禁  止  套  娃！''')
        if 'copyright' in command:
            copyright()
print(PiP)
while True:
    command = input('>>>')
    try:
        print(eval(command))
    except:
        iftogo.start()
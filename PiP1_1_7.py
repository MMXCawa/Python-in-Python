#A Strange work of Python by MMXCawa
import os,sys
version = '1.1.7'
r = 19
update=version+':Get error information,so it is more similar to Python\nType "update" for new updates of "Python in Python"'
hint='Python in Python '+version+' (v'+version+'\\'+str(r)+' Aug 29 23:35:10),using Python '+os.sys.version+'\nType "help", "copyright", "credits" or "license()" for more information.\nType "update" for new updates of "Python in Python"'
print(hint)
while True:
    try:print(eval(input('>>>')))
    except:
         if str(sys.exc_info()[0])[8:-2]in['ValueError','EOFError']:quit()
         else:print('Traceback (most recent call last):\n  File "<stdin>", line 1, in <module>\n'+str(sys.exc_info()[0])[8:-2],sys.exc_info()[1],sep=': ')
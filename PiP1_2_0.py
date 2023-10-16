#A Strange work of Python by MMXCawa
import os,sys
version = '1.2.0';r = 20;update=version+":You can assign the variable and more...but you can't define functions\nWebsite:https://www.github.com/MMXCawa/Python-in-Python"
print('Python in Python '+version+' (v'+version+'\\'+str(r)+', Oct 16 2023, 21:40:42),using Python '+os.sys.version+'\nType "help", "copyright", "credits" or "license()" for more information.\nType "update" for new updates of "Python in Python"')
run=True
while run:
    c=input('>>>')
    try:
        print(eval(c))
    except Exception:
        try:
            exec(c)
        except Exception as e:
            print(f'''Traceback (most recent call last):
  File None line 1, in <module>
    {c}
    {len(c)*'^'}''')
            errorinfo = str(sys.exc_info()[0])[8:-2]+':'
            print(errorinfo,end='')
            print(e)
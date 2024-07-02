#A Strange work of Python by MMXCawa
import os,sys
c:str=''
style_list=('>>> ','... ');__style__=0
def command_collect():
    global c
    c=input(style_list[__style__])
print('Python in Python '+(version:='1.2.3')+' (v'+version+'\\'+str(__version__:=23)+', Jul 2 2024 22:46:45),using Python '+sys.version+'\nType "help", "copyright", "credits" or "license" for more information.\nType "update" for new updates of "Python in Python"')
update=version+":Fixed some bugs.Special Thanks:wangziwenhk \nWebsite:https://www.github.com/MMXCawa/Python-in-Python"
while 1:
    if __style__==0:
        command_collect()
        try:print(eval(c))
        except Exception:
            try:exec(c)
            except IndentationError:__style__=1
            except Exception as e:
                print('Traceback (most recent call last):\n  File "<stdin>" line 1, in <module>')
                print(error_info:=str(sys.exc_info()[0])[8:-2]+': ',end='')
                print(e)
    else:
        __style__=1
        command_list=[]
        while c!='':command_list.append(c);command_collect()
        command_full='\n'.join(command_list)
        exec(command_full)
        __style__=0

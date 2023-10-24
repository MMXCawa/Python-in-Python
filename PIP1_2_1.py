#modules
import os,sys
#values
version = '1.2.1';r = 21;slist=['>>>','...'];__style__=0;update=version+":You can define functions!And you can try to input 'if', 'elif' and 'else'!\nWebsite:https://www.github.com/MMXCawa/Python-in-Python"
#functions
def command_collect():global c;c=input(slist[__style__])
print('Python in Python '+version+' (v'+version+'\\'+str(r)+', Oct 16 2023, 21:40:42),using Python '+os.sys.version+'\nType "help", "copyright", "credits" or "license()" for more information.\nType "update" for new updates of "Python in Python"')
#mainbody
while r:
    if __style__==0:
        command_collect()
        try:print(eval(c))
        except Exception:
            try:exec(c)
            except IndentationError:__style__=1
            except Exception as e:print(f'''Traceback (most recent call last):\n    File None line 1, in <module>\n        {c}\n        {len(c)*'^'}''');errorinfo = str(sys.exc_info()[0])[8:-2]+':';print(errorinfo,end='');print(e)
    else:
        __style__=1;clist=[]
        while c!='':clist.append(c);command_collect()
        cfull='\n'.join(clist)
        if cfull[:3]=='def':define=True
        else:define=False
        with open(__file__[:-11]+'__temp__.py','w') as temp:temp.write(cfull)
        if define:from __temp__ import *
        else:import __temp__
        os.remove(__file__[:-11]+'__temp__.py');__style__=0
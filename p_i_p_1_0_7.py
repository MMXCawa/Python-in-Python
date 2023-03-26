import os as o

print('Python in Python 1.0.7 (v1.0.7\\8, Mar 19 2023 16:47:54),using Python ',o.sys.version,'''
Type "help", "copyright", "credits" or "license()" for more information.''',sep='')

def root(x,y):
    return x**(1/y)

while True:
    command=input('>>>')

    if 'copyright'==command:
        print('''Copyright (c) 2001-2022 Python Software Foundation.
All Rights Reserved.
Copyright (c) 2000 BeOpen.com.
All Rights Reserved.
Copyright (c) 1995-2001 Corporation for National Research Initiatives.
All Rights Reserved.
Copyright (c) 1991-1995 Stichting Mathematisch Centrum, Amsterdam.
All Rights Reserved.''')

    if 'credits' == command:
        print('Python:')
        credits()
        print('''Python in Python:
    by MMXCawa
    作者的话：
    禁  止  套  娃！''')
    if 'license'in command:
        license()
    if 'help' in command:
        help()
    if 'quit' in command:
        quit()
    if '+' in command or '-' in command or '*' in command or '/' in command or \
    '**' in command or ('pow(' in command and ')' in command) or ('root(' in command and ')' in command):
        print(eval(command))

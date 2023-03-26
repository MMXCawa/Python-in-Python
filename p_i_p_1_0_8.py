import os as o

print('Python in Python 1.0.8 (v1.0.8\\9, Mar 25 2023 10:07:13),using Python ', o.sys.version, '''
Type "help", "copyright", "credits" or "license()" for more information.''', sep='')


def root(x, y):
    return x**(1/y)


while True:
    command = input('>>>')

    if 'copyright' == command:
        copyright()

    if 'credits' == command:
        print('Python:')
        credits()
        print('''Python in Python:
    by MMXCawa
    作者的话：
    禁  止  套  娃！''')
    if 'license' in command:
        license()
    if 'help' in command:
        help()
    if 'quit' in command:
        quit()
    if '+' in command or '-' in command or '*' in command or '/' in command or \
            '**' in command or ('pow(' in command and ')' in command) or ('root(' in command and ')' in command):
        print(eval(command))

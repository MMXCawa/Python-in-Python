import os as o
version = '1.1.2'
r = 13


class py():
    def update():
        print(version+':print and input!\nType "update" for new updates of "Python in Python"')

    def __init__():
        print('Python in Python ', version, ' (v', version, '\\', r, ' May 20 2023 11:30:44),using Python ', o.sys.version, '''
Type "help", "copyright", "credits" or "license()" for more information.
Type "update" for new updates of "Python in Python"''', sep='')


def root(x, y):
    return x**(1/y)


class iftogo():
    global command

    def __init__():
        print('iftogo')

    def start():
        if 'copyright' == command:
            copyright()
        if 'credits' == command:
            print('Python:')
            credits()
            print('''Python in Python:
        by MMXCawa
        作者的话：
        禁  止  套  娃！''')

        if 'help' in command:
            help()
        if 'update' in command:
            py.update()
        if 'pip' in command:
            py.__init__()

py.__init__()
while True:
    command = input('>>>')
    try:
        print(eval(command))
    except NameError:
        iftogo.start()
        

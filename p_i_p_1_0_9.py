import os as o

class py():
    def update():
        print('1.0.9:new classes\nType "update" for new updates of "Python in Python"')

    def __init__():
        print('Python in Python 1.0.9 (v1.0.9\\10, Mar 25 2023 10:07:13),using Python ', o.sys.version, '''
Type "help", "copyright", "credits" or "license()" for more information.
Type "update" for new updates of "Python in Python"''', sep='')


def root(x, y):
    return x**(1/y)


class iftogo():
    global command, printmode

    def __init__():
        print('iftogo')

    def ifprint():
        if ('print(' and ')') in command:
            toprint=command[6:len(command)-1]
            try:
                print(eval(toprint))
            except NameError:
                print(toprint)
            except SyntaxError:
                if (toprint == ''):
                    pass
                else:
                    print(toprint)


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
        if 'license' in command:
            license()
        if 'help' in command:
            help()
        if 'quit' in command:
            quit()
        if 'update' in command:
            py.update()


py.__init__()
while True:
    command = input('>>>')
    iftogo.start()
    iftogo.ifprint()
    if type(command) == int or float or bool:
        try:
            print(eval(command))
        except NameError:
            pass
        except SyntaxError:
            pass

print('''python in python 1.0.4 (v1.0.4\5, Mar 19 2023 16:13:44)
Type "help", "copyright", "credits" or "license()" for more information.
      ''')



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

    if 'cridits' == command:
        print('''Thanks to CWI, CNRI, BeOpen.com, Zope Corporation and a cast of thousands
for supporting Python development.  See www.python.org for more information.
Python in Python by MMXCawa''')
    if 'license()' == command:
        license()
    if 'help' in command:
        help()

import random
a='y'
while a=='y':
    n=random.randint(1,6)
    if n==1:
        print('''----------
|        |
|        |
|   O    |
|        |
|        |
----------''')
    if n==2:
        print('''----------
|        |
|        |
| O   O  |
|        |
|        |
----------''')
    if n==3:
        print('''----------
|        |
|   O    |
|   O    |
|   O    |
|        |
----------''')
    if n==4:
        print('''----------
|        |
| O   O  |
|        |
| O   O  |
|        |
----------''')
    if n==5:
        print('''----------
|        |
| O   O  |
|   O    |
| O   O  |
|        |
----------''')
    if n==6:
        print('''----------
|        |
| O   O  |
| O   O  |
| O   O  |
|        |
----------''')
    a=input("Do you want to throw the deci(y/n):")

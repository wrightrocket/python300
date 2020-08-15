#!/usr/bin/env py
'''
From https://docs.python.org/3/tutorial/controlflow.html

2020-08-15

Keith Wright
'''

def hello(arg,/):
    print ('Hello {0}!'.format(arg))

def inputx():
    ''' run interactive commands '''
    x = int(input("Please enter an integer: "))
    print (x)
    if x < 0:
        x = 0
        print('Negative changed to zero')
    elif x == 0:
        print('Zero')
    elif x == 1:
        print('Single')
    else:
        print('More')

def words(*args):
    # words = ['cat', 'window', 'defenestrate']
    words = args
    for w in words:
        print(w, len(w))

if __name__ == "__main__":
    hello("World")
    inputx()
    words('alpha','beta','gamma')


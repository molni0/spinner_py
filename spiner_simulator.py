from random import *
from time import *
k = True
p = 60
print('spinner')
def upr():
    print('''
    ----------------
    start = начать.
    no = закончить.
    ----------------
    ''')
def spinner1():
    print('''
    ----------------
          #####
          #####
          #####
          #####
          #ooo#
    ######ooooo#########
    ######ooooo#########
          #ooo#
          #####
          #####
          #####
          #####
    -----------------
    ''')
def spinner2():
    print('''
    ----------------
          #####
          #####
     //// #####
          #####  //////
          #ooo#////////
    ######ooooo#########
    ######ooooo#########
          #ooo#
          #####
          #####////*/*/*/*/*/
 //////   #####
          #####
    -----------------
    ''')
def spinner3():
    print('''
    ----------------
               ####
             #####
            #####
          #ooo#
    ######ooooo#########
    ######ooooo#########
          #ooo#
        ######
       ######
      #####
    -----------------
    ''')
upr()
while k:
    g = input('действие: ')
    if g == 'start':
        for i in range(p):
            spinner1()
            sleep(0.1)
            spinner2()
            sleep(0.1)
            spinner3()
            sleep(0.1)
    if g == 'no':
        k = False
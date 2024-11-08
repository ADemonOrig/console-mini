import audioop as audio
import base64 as base
import calendar
import datetime as datatime
import decimal
import difflib
import io
import math
import os
import pathlib
import random
import string
import time


def hello_col():
    time.sleep(delay)
    print(indent, 'H   H')
    time.sleep(delay)
    print(indent, 'H   H')
    time.sleep(delay)
    print(indent, 'HHHHH')
    time.sleep(delay)
    print(indent, 'H   H')
    time.sleep(delay)
    print(indent, 'H   H')
    time.sleep(delay)
    print()
    time.sleep(delay)
    print(indent, 'EEEEE')
    time.sleep(delay)
    print(indent, 'E')
    time.sleep(delay)
    print(indent, 'EEEEE')
    time.sleep(delay)
    print(indent, 'E')
    time.sleep(delay)
    print(indent, 'EEEEE')
    time.sleep(delay)
    print()
    time.sleep(delay)
    print(indent, 'LL')
    time.sleep(delay)
    print(indent, 'LL')
    time.sleep(delay)
    print(indent, 'LL')
    time.sleep(delay)
    print(indent, 'LL')
    time.sleep(delay)
    print(indent, 'LLLLL')
    time.sleep(delay)
    print()
    time.sleep(delay)
    print(indent, 'LL')
    time.sleep(delay)
    print(indent, 'LL')
    time.sleep(delay)
    print(indent, 'LL')
    time.sleep(delay)
    print(indent, 'LL')
    time.sleep(delay)
    print(indent, 'LLLLL')
    time.sleep(delay)
    print()
    time.sleep(delay)
    print(indent, 'OOOOO')
    time.sleep(delay)
    print(indent, 'O   O')
    time.sleep(delay)
    print(indent, 'O   O')
    time.sleep(delay)
    print(indent, 'O   O')
    time.sleep(delay)
    print(indent, 'OOOOO')
    time.sleep(delay)


def hello_str():
    time.sleep(delay)
    print('H   H  EEEEE  LL     LL     OOOOO')
    time.sleep(delay)
    print('H   H  E      LL     LL     O   O')
    time.sleep(delay)
    print('HHHHH  EEEEE  LL     LL     O   O')
    time.sleep(delay)
    print('H   H  E      LL     LL     O   O')
    time.sleep(delay)
    print('H   H  EEEEE  LLLLL  LLLLL  OOOOO')
    time.sleep(delay)


def hello_big():
    time.sleep(delay)
    print(indent, 'HHH    HHH')
    time.sleep(delay)
    print(indent, 'HHH    HHH')
    time.sleep(delay)
    print(indent, 'HHH    HHH')
    time.sleep(delay)
    print(indent, 'HHH    HHH')
    time.sleep(delay)
    print(indent, 'HHHHHHHHHH')
    time.sleep(delay)
    print(indent, 'HHHHHHHHHH')
    time.sleep(delay)
    print(indent, 'HHH    HHH')
    time.sleep(delay)
    print(indent, 'HHH    HHH')
    time.sleep(delay)
    print(indent, 'HHH    HHH')
    time.sleep(delay)
    print(indent, 'HHH    HHH')
    time.sleep(delay)
    print()
    time.sleep(delay)
    print(indent, 'EEEEEEEEEE')
    time.sleep(delay)
    print(indent, 'EEEEEEEEEE')
    time.sleep(delay)
    print(indent, 'EEE')
    time.sleep(delay)
    print(indent, 'EEE')
    time.sleep(delay)
    print(indent, 'EEEEEEEEEE')
    time.sleep(delay)
    print(indent, 'EEEEEEEEEE')
    time.sleep(delay)
    print(indent, 'EEE')
    time.sleep(delay)
    print(indent, 'EEE')
    time.sleep(delay)
    print(indent, 'EEEEEEEEEE')
    time.sleep(delay)
    print(indent, 'EEEEEEEEEE')
    time.sleep(delay)
    print()
    time.sleep(delay)
    print(indent, 'LLL')
    time.sleep(delay)
    print(indent, 'LLL')
    time.sleep(delay)
    print(indent, 'LLL')
    time.sleep(delay)
    print(indent, 'LLL')
    time.sleep(delay)
    print(indent, 'LLL')
    time.sleep(delay)
    print(indent, 'LLL')
    time.sleep(delay)
    print(indent, 'LLL')
    time.sleep(delay)
    print(indent, 'LLL')
    time.sleep(delay)
    print(indent, 'LLLLLLLLLL')
    time.sleep(delay)
    print(indent, 'LLLLLLLLLL')
    time.sleep(delay)
    print()
    time.sleep(delay)
    print(indent, 'LLL')
    time.sleep(delay)
    print(indent, 'LLL')
    time.sleep(delay)
    print(indent, 'LLL')
    time.sleep(delay)
    print(indent, 'LLL')
    time.sleep(delay)
    print(indent, 'LLL')
    time.sleep(delay)
    print(indent, 'LLL')
    time.sleep(delay)
    print(indent, 'LLL')
    time.sleep(delay)
    print(indent, 'LLL')
    time.sleep(delay)
    print(indent, 'LLLLLLLLLL')
    time.sleep(delay)
    print(indent, 'LLLLLLLLLL')
    time.sleep(delay)
    print()
    time.sleep(delay)
    print(indent, 'OOOOOOOOOO')
    time.sleep(delay)
    print(indent, 'OOOOOOOOOO')
    time.sleep(delay)
    print(indent, 'OOO    OOO')
    time.sleep(delay)
    print(indent, 'OOO    OOO')
    time.sleep(delay)
    print(indent, 'OOO    OOO')
    time.sleep(delay)
    print(indent, 'OOO    OOO')
    time.sleep(delay)
    print(indent, 'OOO    OOO')
    time.sleep(delay)
    print(indent, 'OOO    OOO')
    time.sleep(delay)
    print(indent, 'OOOOOOOOOO')
    time.sleep(delay)
    print(indent, 'OOOOOOOOOO')
    time.sleep(delay)


def hello_cell(x):
    count = 0
    while count != x:
        count += 1
        print()
        time.sleep(delay)
        print('#   #  #####  ##     ##     #####')
        time.sleep(delay)
        print('#   #  #      ##     ##     #   #')
        time.sleep(delay)
        print('#####  #####  ##     ##     #   #')
        time.sleep(delay)
        print('#   #  #      ##     ##     #   #')
        time.sleep(delay)
        print('#   #  #####  #####  #####  #####')
        time.sleep(delay)

def hello_sq():
    time.sleep(delay)
    print('■   ■  ■■■■■  ■■     ■■     ■■■■■')
    time.sleep(delay)
    print('■   ■  ■■     ■■     ■■     ■   ■')
    time.sleep(delay)
    print('■■■■■  ■■■■■  ■■     ■■     ■   ■')
    time.sleep(delay)
    print('■   ■  ■■     ■■     ■■     ■   ■')
    time.sleep(delay)
    print('■   ■  ■■■■■  ■■■■■  ■■■■■  ■■■■■')
    time.sleep(delay)


info_pip = ['audioop', 'base64', 'calendar', 'decimal', 'difflib'  'io', 'math', 'os', 'pathlib', 'random', 'string', 'time']

info = ['hello.col', 'hello.str', 'hello.big', 'hello.cell', 'info', 'help', 'hello.sq', 'pip']

skip = '    '
delay = 0.015625
indent = ' ' * 19

while True:
    choice = input('>>>.')
    print()
    if choice == 'hello.col':
        hello_col()
    elif choice == 'hello.str':
        hello_str()
    elif choice == 'hello.big':
        hello_big()
    elif choice == 'hello.cell':
        hello_cell()
    elif choice == 'hello.sq':
        hello_sq()
    elif choice == 'hello.x':
        try:
            hello_cell(int(input('  >>>x=.')))
        except ValueError:
            print('ERROR 1')
    elif choice == 'pip':
        for x in info_pip:
            print(skip, x)
    elif choice == 'info' or 'help':
        info.sort()
        for x in info:
            print(skip, x)
    else:
        print('ERROR 0')
    print()

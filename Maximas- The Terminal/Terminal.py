# MAXIMAS TERMINAL 2024 #
# v0 --normbeta #

import platform
import datetime
import re
import math
import subprocess
import os
import shelve
import random
import string
import binascii
import base64
import colorama
from colorama import *
import threading
import time

# VARIABLES #

QUIT_STATE = False
PERM_STATE = "General"

keyy = 'NAME'
keyy2 = 'PIN'
keyy3 = 'DESC'

# COMMANDS #

def SetupUtil():
    name = input("What is your username? (This cannot be changed later.): ")
    idn = input("What do you want your Personal Identification Number to be? (This cannot be changed later.): ")
    with shelve.open('profs') as db:
                    db[keyy] = name
    with shelve.open('pin') as db:
                    db[keyy2] = idn  
    with shelve.open('descs') as db:
                    db[keyy3] = f"Hi! I'm {name}." 
    print("Info set and account created. (locally for now) Type 'acc _i' to see your page, acc _m to modify it.")             
                    
def HelpUtil():
    print("Commands: ")
    print("---------")
    print("version: Gives system data. Uses:")
    print("| _w: Gives Windows data.")
    print("| _p: Gives Python data.")
    print("| _s: Gives system data.")
    print("| _a: Gives all data. \n")
    print("color: CHanges terminal color. Inputs: foreground, background (colors 0-f) \n")
    print("%: Stores variables. Inputs: key, value (string, float) \n")
    print("$: Retrieves variables. Input: key (string) \n")
    print("cls: Clears screen. \n")
    print("title: Changes session title. Input: newTitle (string) \n")
    print("sys: Changes system data and/or retrieves console data. Uses:")
    print("| _q: Quits Maximas.")
    print("| _r: Shows Maximas runtime.")
    print("| _w: Enables PsuedoCMD - where you can type cmd commands. \n")
    print("lock: Locks Maximas. Input: unlockKey (string) \n")
    print("trig: Performs various trigonometry processes. All processes are precursored by _. Inputs: process, number Uses: ")
    print("| (there are too many) To view uses, type 'trig _h'. \n")
    print("setup: Sets up accounts. \n")
    print("acc: Modifies account info. Uses:")
    print("| _i: See acc info. \n")
    
def VersUtil(input):
    vertype1 = platform.machine()
    vertype2 = platform.architecture()
    vertype3 = platform.python_version()
    vertype4 = platform.python_compiler()
    vertype5 = platform.python_implementation()
    vertype6 = platform.processor()
    vertype7 = platform.node()
    vertype8 = platform.system()
    vertype9 = platform.win32_ver()
    vertype10 = platform.release()
    if input == '_w':
        print(f"Windows Info > Node: {vertype7}, System: {vertype8}, Win32 Version: {vertype9}, Release: {vertype10}")
    elif input == '_p':
        print(f"Python Info > Version: {vertype3}, Compiler: {vertype4}, Implementation: {vertype5}, Arch: {vertype2}")
    elif input == '_s':
        print(f"Machine: {vertype1}, Processor: {vertype6}")
    elif input == '_a':
        print(f"Windows Info > Node: {vertype7}, System: {vertype8}, Win32 Version: {vertype9}, Release: {vertype10} Python Info > Version: {vertype3}, Compiler: {vertype4}, Implementation: {vertype5}, Arch: {vertype2} System Info > Machine: {vertype1}, Processor: {vertype6}")

# ERRORS REFERENCE #

# 0000 The type (1: SE, 2: PE, 3: OE) (syntax, process, other)
# ^

# 0000 The division of error. (so, error num)
#  ^^

# 0000 The type of program (1: returnValue, 2: Game, 3: DateUtil, 4: MaximasUtil)
#    ^

# SYNTAX ERRORS > (meaning the input is wrong)
#  1011: Echo: No input.
#  1021: %: Invalid input.
#  
#
#
# PROCESS ERRORS > (it or you messed up)
# 2011: $: "" does not exist.
# 2024: Commands: "" is not a valid command.
#
#


# RUNTIME #

def mainloop():
    global QUIT_STATE, PERM_STATE
    start_time = time.time()
    print("---------------------------------|>>")
    print("MMMMMMM  AAAAAAA  X   X  IIIIIII  MMMMMMM  AAAAAAA  SSSSSSS     ///  ///")
    print("M  M  M  A     A   X X      I     M  M  M  A     A  S           ||||||||")
    print("M  M  M  AAAAAAA    X       I     M  M  M  AAAAAAA  SSSSSSS     | |||| |")
    print("M  M  M  A     A   X X      I     M  M  M  A     A        S     ||||||||")
    print("M  M  M  A     A  X   X  IIIIIII  M  M  M  A     A  SSSSSSS     |||  |||")
    print("                                                               ^^^^^^^^^^")
    print("TTTTTTT  EEEEEEE  RRRRRRR  MMMMMMM  IIIIIII  NNNNNNN  AAAAAAA  L         ")
    print("   T     E        R     R  M  M  M     I     N     N  A     A  L")
    print("   T     EEEEEEE  RRRRRRR  M  M  M     I     N     N  AAAAAAA  L")
    print("   T     E        R   R    M  M  M     I     N     N  A     A  L")
    print("   T     EEEEEEE  R    R   M  M  M  IIIIIII  N     N  A     A  LLLLLLL")
        
        
        
    print("---------------------------------|>>")
    print("Type 'help' to see commands or 'setup' to make a profile, if you haven't already.")    
    while not QUIT_STATE:
        with shelve.open('profs') as db:
                if keyy in db:
                    NAME_PROF = db[keyy]
                else:
                    NAME_PROF = 'None'
                     
        INPUT_INDEX = input(f"Maximas Terminal @ {PERM_STATE}, {NAME_PROF} > ")
        PARTS = INPUT_INDEX.split()
        OPERATORS = r'[\+\-\*\/\(\)]'
        
        FUNCTIONS = {
            'help': HelpUtil,
            'setup': SetupUtil
        }
        
        if INPUT_INDEX.startswith('echo'):
                if len(PARTS) > 1:
                    text_to_print = ' '.join(PARTS[1:])
                    print(text_to_print)
                else:
                    print(" E-1011 No input given. ")
                    
        elif INPUT_INDEX.startswith('%'):    
            if len(PARTS) == 3 and PARTS[1].isalnum() and PARTS[2].isdigit():
                key = PARTS[1]
                value = int(PARTS[2])
                with shelve.open('variables') as db:
                    db[key] = value
                    print(f"Set '{key}' as {value}.")
            else:
                print(" E-1021 Invalid format. ")
        
        elif INPUT_INDEX.startswith('acc'):
            if INPUT_INDEX[4:] == '_i':
                print("Your page: \n")
                with shelve.open('profs') as db:
                    if keyy in db:
                        name = db[keyy]
                    else:
                        name = 'None'
                with shelve.open('pin') as db:
                    if keyy2 in db:
                        pin = db[keyy2]
                    else:
                        pin = 'None'
                with shelve.open('descs') as db:
                    if keyy3 in db:
                        desc = db[keyy3]
                    else:
                        desc = 'None'
                print(f"User | {name} <>")
                print("-----------")
                print(f"PIN  | {pin} <>")
                print("DESC: -----")
                print(desc + "\n")
                
                
        elif INPUT_INDEX.startswith('$'):
            key = INPUT_INDEX.split()[1]
            with shelve.open('variables') as db:
                if key in db:
                    print(f"{key}: {db[key]}")
                else:
                    print(f" E-2011 '{key}' not found.") 
                         
        elif INPUT_INDEX.startswith('title'):
            subprocess.run(INPUT_INDEX,shell=True)  
        elif INPUT_INDEX.startswith('color'):
            subprocess.run(INPUT_INDEX, shell=True)
        elif re.search(OPERATORS, INPUT_INDEX):
            try:
                result = eval(INPUT_INDEX)
                print("Result:", result)
            except Exception as e:
                print("Error:", e)
        elif INPUT_INDEX.startswith("cls"):
            os.system('cls')
            print("---------------------------------|>>")
            print("MMMMMMM  AAAAAAA  X   X  IIIIIII  MMMMMMM  AAAAAAA  SSSSSSS     ///  ///")
            print("M  M  M  A     A   X X      I     M  M  M  A     A  S           ||||||||")
            print("M  M  M  AAAAAAA    X       I     M  M  M  AAAAAAA  SSSSSSS     | |||| |")
            print("M  M  M  A     A   X X      I     M  M  M  A     A        S     ||||||||")
            print("M  M  M  A     A  X   X  IIIIIII  M  M  M  A     A  SSSSSSS     |||  |||")
            print("                                                               ^^^^^^^^^^")
            print("TTTTTTT  EEEEEEE  RRRRRRR  MMMMMMM  IIIIIII  NNNNNNN  AAAAAAA  L         ")
            print("   T     E        R     R  M  M  M     I     N     N  A     A  L")
            print("   T     EEEEEEE  RRRRRRR  M  M  M     I     N     N  AAAAAAA  L")
            print("   T     E        R   R    M  M  M     I     N     N  A     A  L")
            print("   T     EEEEEEE  R    R   M  M  M  IIIIIII  N     N  A     A  LLLLLLL")
            
            
            
            print("---------------------------------|>>")
            print("Type 'help' to see commands or 'setup' to make a profile, if you haven't already.")    
        elif INPUT_INDEX.startswith("version"):
            inp = INPUT_INDEX[8:]
            VersUtil(inp)
            
        elif INPUT_INDEX.startswith("sys"):
            if '_r' in INPUT_INDEX:
                end_time = time.time()
                print(end_time - start_time)
            if '_q' in INPUT_INDEX:
                QUIT_STATE = True
            if '_w' in INPUT_INDEX:
                qs = False
                os.system('cls')
                print("Welcome to PsuedoCMD! Type 'help' for commands. Type 'quit' to quit.")
                while not qs:
                    inp = input("PsuCMD> ")
                    subprocess.run(inp,shell=True)
                    if inp == 'quit':
                        qs = True
                        
        
        elif INPUT_INDEX.startswith("lock"):
            unlock = INPUT_INDEX[5:]
            os.system('cls')
            ls = True
            while ls:
                untry = input("Maximas is locked. Type in the key to unlock Maximas or input _t to terminate session.: ")
                if untry == unlock:
                    ls = False
                    break
                elif untry == '_t':
                    os.system("taskkill /F /PID {}".format(os.getpid()))
                else:
                    print("Incorrect.")
        elif 'trig' in INPUT_INDEX:
                parts = INPUT_INDEX.split()
                if len(parts) >= 3:
                    operation = parts[1]
                    number = float(parts[-1])
                    if operation == '_sin':
                        result = math.sin(number)
                    elif operation == '_cos':
                        result = math.cos(number)
                    elif operation == '_tan':
                        result = math.tan(number)
                    elif operation == '_log':
                        result = math.log(number)
                    elif operation == '_sqrt':
                        result = math.sqrt(number)
                    elif operation == '_ceil':
                        result = math.ceil(number)
                    elif operation == '_floor':
                        result = math.floor(number)
                    elif operation == '_exp':
                        result = math.exp(number)
                    elif operation == '_factorial':
                        result = math.factorial(number)
                    elif operation == '_acos':
                        result = math.acos(number)
                    elif operation == '_asin':
                        result = math.asin(number)
                    elif operation == '_atan':
                        result = math.atan(number)
                    elif operation == '_degrees':
                        result = math.degrees(number)
                    elif operation == '_radians':
                        result = math.radians(number)
                    
                    else:
                        result = "E-1031 unsupported operation"
                    
                        
                else:
                    operation = parts[1]
                    if operation == '_h':
                        print("Commands: sin, cos, tan, log, sqrt, ceil, floor, exp, factorial, acos, asin, atan, degrees, radians.") 
                    else:
                        result = "E-1031 unsupported operation"
                        print(result) 
        else:
            if INPUT_INDEX in FUNCTIONS:
                FUNCTIONS[INPUT_INDEX]()
            else:
                print("E-2024. That command is not valid.")
mainloop()

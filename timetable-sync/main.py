import csv
from os import system, name
import xlrd
import sys
import os
import keyboard
import time
import webbrowser
from termcolor import colored
from collections import defaultdict
import subprocess
import timeit
import mpu.pd
import pandas as pd

if name == 'nt':
    _ = system('cls')
else:
    _ = system('clear')

print(r"""
 _____ _                _        _     _        __                  _                     _              
/__   (_)_ __ ___   ___| |_ __ _| |__ | | ___  / _\_   _ _ __   ___| |__  _ __ ___  _ __ (_)_______ _ __ 
  / /\/ | '_ ` _ \ / _ \ __/ _` | '_ \| |/ _ \ \ \| | | | '_ \ / __| '_ \| '__/ _ \| '_ \| |_  / _ \ '__|
 / /  | | | | | | |  __/ || (_| | |_) | |  __/ _\ \ |_| | | | | (__| | | | | | (_) | | | | |/ /  __/ |   
 \/   |_|_| |_| |_|\___|\__\__,_|_.__/|_|\___| \__/\__, |_| |_|\___|_| |_|_|  \___/|_| |_|_/___\___|_|   
                                                   |___/                                                 
""")
time.sleep(.5)
print()
time.sleep(.5)
print(colored('[i] ', 'blue') + "Welcome to the Timetable Synchronizer")
time.sleep(.5)
print(colored('[c] ', 'blue') + "(c) Copyright 2022 Kayden Lee (Cloudserve Tech)")
time.sleep(.5)
print(colored('[v] ', 'blue') + "v1.2 Pre-release Dev Build 1762022")
time.sleep(.5)
print(colored('[www] ', 'blue') + "https://cloudservetechcentral.com/")
time.sleep(.5)
print()

def steps():
    print(r"""
        Steps:
        ===========================================================
        1. Download sample timetable
        2. Upload timetable
            > Use default settings
            > Use custom settings (not available)
        3. Check values
        4. Parse values
        5. Send values to raspberry pi
        6. Download values for debugging or future use (optional)
        """)

    time.sleep(.5)

    print(colored('[?] ', 'yellow') + "Press any key to continue...")
    keyboard.read_key()
    time.sleep(.5)
    print()


def one():
    print(colored('[1] ', 'magenta') + "Download sample timetable\n")
    print(colored('[i] ', 'blue') + "Detecting browser...")
    time.sleep(.5)
    print(colored('[i] ', 'blue') + "Downloading sample timetable...")
    time.sleep(2)
    # webbrowser.open('https://cdn.cloudservetechcentral.com/timetable-sync/sample-timetable.xslx')
    # file = input(colored('[!] ', 'red') + "Sample timetable has not been uploaded to the server yet!")
    print(colored('[!] ', 'red') + "Sample timetable has not been uploaded to the server yet!")


def two():
    print(colored('[2] ', 'magenta') + "Upload timetable\n")
    time.sleep(2)
    global file_name
    file_name = input(colored('[i] ', 'blue') + "Please enter the exact location of the timetable\n" + colored('[?] ', 'yellow') + ">_ ")
    time.sleep(2)
    # print(colored('[i] ', 'blue') + "Opening file in explorer... Please ensure that the path of your excel document is correct.")
    # time.sleep(2)
    # subprocess.Popen(r'explorer /select,' + file_name)
    print()

    rows = []
    with open(file_name, 'r') as file:
        csvreader = csv.reader(file)
        header = next(csvreader)
        for row in csvreader:
            rows.append(row)

    df = pd.read_csv(file_name)
    print(df)

    print("\n" + colored('[i] ', 'blue') + "This is the csv file that you have selected. Is this correct?")
    response = None
    while response not in {"yes", "no"}:
        response = input(colored('[?] ', 'yellow') + "Please enter yes or no: ").lower()

    if response == "yes":
        three()
    elif response == "no":
        print(colored('[i] ', 'blue') + "Restarting step 2...")
        time.sleep(2.5)
        two()
    else:
        print(colored('[!] ', 'red') + "There was a critical error with the program! Please install the latest LTS version from https://software.cloudservetechcentral.com/download/timetable-sync")

def three():
    print()
    print(colored('[3] ', 'magenta') + "Check values")
    time.sleep(1)
    print()
    rows = []
    with open(file_name, 'r') as file:
        csvreader = csv.reader(file)
        header = next(csvreader)
        for row in csvreader:
            rows.append(row)
    print(header)
    print(rows)
    print()
    df = pd.read_csv(file_name)
    print(df)
    print()
    time.sleep(1)
    print(colored('[i] ', 'blue') + "These are the contents of the timetable. We will now remove the headers, please check if these are the values without the headers.")
    time.sleep(1)
    print()
    print(rows)
    print()
    df = pd.read_csv(
        file_name,
        skiprows=1
    )
    print(df)
    print("\n" + colored('[i] ', 'blue') + "This is the csv file parsed without the headers. Is this correct?")
    response = None
    while response not in {"yes", "no"}:
        response = input(colored('[?] ', 'yellow') + "Please enter yes or no: ").lower()

    if response == "yes":
        four()
    elif response == "no":
        print(colored('[!] ', 'red') + "Error 3: Using custom values is currently not supported for this version. Please use the default values!")
        time.sleep(2.5)
        exit(3)
    else:
        print(colored('[!] ', 'red') + "There was a critical error with the program! Please install the latest LTS version from https://software.cloudservetechcentral.com/download/timetable-sync")

def four():
    print(colored('\n[4] ', 'magenta') + "Parse values\n")
    print(colored('[i] ', 'blue') + "Please wait while we parse the values into machine-readable text. You can ignore the wierd formatting on the screen.")
    time.sleep(2)
    print()
    columns = defaultdict(list)

    # Stores columns and rows into a dict
    with open(file_name) as f:
        reader = csv.DictReader(f)
        for row in reader:
            for (k,v) in row.items():
                columns[k].append(v)

    # Prints dict out line by line
    for key, value in columns.items():
        print(key, ' : ', value)

    for value in columns.items():
        print(value)

    print(columns['Time'])
    print(columns['Lesson'])
    print(columns['Lights'])


    # print(list)
    print()

# four()
steps()
one()
print()
time.sleep(2)
two()

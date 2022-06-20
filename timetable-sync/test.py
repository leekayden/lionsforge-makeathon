import timeit
import csv
import pandas as pd

filename = './sample-timetable.csv'

def talktime(filename, funcname, func):
    print(f"# {funcname}")
    t = timeit.timeit(f'{funcname}("{filename}")', setup=f'from __main__ import {funcname}', number = 100) / 100
    print('Elapsed time : ', t)
    print('n = ', func(filename))
    print('\n')

def sum1forline(filename):
    with open(filename) as f:
        return sum(1 for line in f)
talktime(filename, 'sum1forline', sum1forline)

def lenopenreadlines(filename):
    with open(filename) as f:
        return len(f.readlines())
talktime(filename, 'lenopenreadlines', lenopenreadlines)

def lenpd(filename):
    return len(pd.read_csv(filename)) + 1
talktime(filename, 'lenpd', lenpd)

def csvreaderfor(filename):
    cnt = 0
    with open(filename) as f:
        cr = csv.reader(f)
        for row in cr:
            cnt += 1
    return cnt
talktime(filename, 'csvreaderfor', csvreaderfor)
print(csvreaderfor(filename))

def openenum(filename):
    cnt = 0
    with open(filename) as f:
        for i, line in enumerate(f,1):
            cnt += 1
    return cnt
talktime(filename, 'openenum', openenum)

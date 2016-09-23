# Zicheng Zhen and Richard Wang
# Software Development
# 2016-09-15
# HW#2 -- More Python

import csv, random

def parseCSV(filename):
    with open(filename, "r") as raw:
        reader = csv.reader(raw)
        parsed = dict(reader)
        del parsed["Job Class"]
        return parsed

def choose(data):
    seed = random.random() * 99.8; # seed value
    for key in data:
        # print ( seed ) 
        seed -= float(data[key])
        if seed < 0:
            return key
    return -1

foo = parseCSV("occupations.csv")
print(choose(foo));

# Diagnostic Work Below - 100,000 Iteration Test
'''
diagnostics = dict();
for key in parseCSV("occupations.csv"):
    diagnostics[key] = 0
for i in range(100000):
    diagnostics[choose(foo)] += 1
for each in diagnostics:
    print (each + "\t:" + str(diagnostics[each]) + "\n")
'''

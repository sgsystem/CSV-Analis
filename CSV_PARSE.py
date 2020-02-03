# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 14:48:07 2020

@author: Tsvetomir Gotsov
"""

import csv

with open('1m.xls') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\t')
    line_count = 1
    for row in csv_reader:
        #if line_count == 1:
            print(f' {", ".join(row)}')
           # line_count += 2
       # else:
          #  print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
          #  line_count += 1
    #print(csv_reader)
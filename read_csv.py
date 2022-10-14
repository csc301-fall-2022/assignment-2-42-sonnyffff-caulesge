"""CSC301 Fall 2022 Assignment 2, readcsv

This file consists the code for CSV file reading.

Copyright and Usage Information
===============================

This file is Copyright (c) 2022 Zijia(Sonny) Chen and Hongshou(Caules) Ge
"""

import csv
from item import *


def read_item_list() -> list[Item]:
    with open("item_list.csv") as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        flag = 0
        ret = []
        for i in reader:
            if flag > 0:
                item = Item(i[0], float(i[2]), i[3], int(i[1]))
                ret.append(item)
            flag += 1
        return ret
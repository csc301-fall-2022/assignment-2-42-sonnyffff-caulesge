"""CSC301 Fall 2022 Assignment 2, main

This file consists the class definitions of counter.

Copyright and Usage Information
===============================

This file is Copyright (c) 2022 Zijia(Sonny) Chen and Hongshou(Caules) Ge
"""

from counter import *
from read_csv import *


def run():

    counter = Counter(read_item_list())

    counter.set_tax(0.15)
    counter.set_discount(0.1)  # 10% off
    counter.add_cart(1, 3)
    counter.add_cart(2, 2)
    counter.add_cart(3, 2)
    # counter.print_current_cart()
    counter.print_invoice()


if __name__ == '__main__':
    run()

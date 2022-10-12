"""CSC301 Fall 2022 Assignment 2, main

This file consists the class definitions of counter.

Copyright and Usage Information
===============================

This file is Copyright (c) 2022 Zijia(Sonny) Chen and Hongshou(Caules) Ge
"""

from item import *
from counter import *


def print_item():
    apple = Item("apple", 10.5, "", 102)
    banana = Item("banana", 3.5, "", 111)
    counter = Counter([apple, banana])
    counter.set_tax(0.15)
    counter.set_discount(0.1)  # 10% off
    counter.add_cart(102, 3)
    counter.add_cart(102, 2)
    counter.add_cart(111, 1)
    counter.remove_cart(102, 2)
    # counter.print_current_cart()
    counter.print_invoice()


if __name__ == '__main__':
    print_item()

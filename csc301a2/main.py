"""CSC301 Fall 2022 Assignment 2, counter

This file consists the class definitions of counter

Copyright and Usage Information
===============================

This file is Copyright (c) 2022 Zijia(Sonny) Chen and Hongshou(Caules) Ge
"""

from item import *
from counter import *


def print_item():
    apple = Item("apple", 10.5, "", "", 1)
    banana = Item("banana", 3.5, "", "", 1)
    counter = Counter([])
    counter.add_cart(apple, 3)
    counter.add_cart(apple, 2)
    counter.add_cart(banana, 1)
    counter.remove_cart(banana, 1)
    counter.remove_cart(apple, 2)
    counter.print_current_cart()


if __name__ == '__main__':
    print_item()

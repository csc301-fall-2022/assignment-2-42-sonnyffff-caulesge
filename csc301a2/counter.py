"""CSC301 Fall 2022 Assignment 2, counter

This file consists the class definitions of counter.

Copyright and Usage Information
===============================

This file is Copyright (c) 2022 Zijia(Sonny) Chen and Hongshou(Caules) Ge
"""

from item import *


class Counter:
    """A checkout counter that contains all information of items.

    """

    # Private Instance Attributes:
    #     - _inStock: a list of all the items.
    #     - _cart: a list of items that that is in the cart
    #     - _taxes: tax applied to the items.
    #     - _discounts: discount applied to the items.
    _inStock: list[Item]
    _cart: list[Item]
    _taxes: float
    _discounts: float

    def __init__(self, instock: list[Item]) -> None:
        """ Initialize a new counter containing the given root value.

        """
        self._inStock = instock
        self._cart = []
        self._taxes = 0
        self._discounts = 0

    def set_tax(self, tax: float) -> bool:
        """ Set tax for the counter

        """
        self._taxes = tax
        return True

    def set_discount(self, discount: float) -> bool:
        """ Set discount for the counter

        """
        if discount <= 1:
            self._discounts = discount
            return True
        else:
            print("Invalid number")
            return False

    def add_cart(self, item: Item, quantity: int) -> bool:
        """ Add certain number of items to the cart by its id number.

        """
        if quantity > 0:
            for i in self._cart:
                if i.name == item.name:
                    i.set_quantity(i.quantity + quantity)
                    return True
            item.set_quantity(quantity)
            self._cart.append(item)
            return True
        else:
            return False

    def remove_cart(self, item: Item, quantity: int) -> bool:
        """ Remove certain number of items from the cart by its id number.

        """
        if quantity > 0:
            for i in self._cart:
                if i.name == item.name:
                    if i.quantity > quantity:
                        i.set_quantity(i.quantity - quantity)
                        return True
                    else:
                        # with 0 number of items
                        self._cart.remove(i)
                        return True
            return False
        else:
            return False

    def print_current_cart(self):
        """ Print out current items in cart.

        """
        for i in self._cart:
            print(i.name + " " + str(i.quantity) + " " + str(i.price) + "\n")

    def print_invoice(self):
        """ Remove certain number of items from the cart by its id number.

        """


"""CSC301 Fall 2022 Assignment 2, counter
This file consists the class definitions of counter.
Copyright and Usage Information
===============================
This file is Copyright (c) 2022 Zijia(Sonny) Chen and Hongshou(Caules) Ge
"""

from item import *
from typing import Any


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
        e.g. tax 0.1 means 10% tax applied
        """
        self._taxes = tax
        return True

    def set_discount(self, discount: float) -> bool:
        """ Set discount for the counter.
        e.g. discount 0.1 means 10% off
        """
        if 0 <= discount <= 1:
            self._discounts = discount
            return True
        else:
            print("Invalid number")
            return False

    def search_id(self, itemid: int) -> Any:
        """ Search for an item in stock with given item id number. Return none if not found.
        """
        for i in self._inStock:
            # find item in the stock by its number
            if i.idNum == itemid:
                return i
        return None

    def add_cart(self, itemnum: int, quantity: int) -> bool:
        """ Add certain number of items to the cart by its id number
        """
        item = self.search_id(itemnum)
        if item is None:
            print("Item not found in stock")
            return False
        if quantity > 0:
            # check if item is in the cart already
            for i in self._cart:
                if i.name == item.name:
                    i.set_quantity(i.quantity + quantity)
                    return True
            item.set_quantity(quantity)
            self._cart.append(item)
            return True
        else:
            print("Negative quantity")
            return False

    def remove_cart(self, itemnum: int, quantity: int) -> bool:
        """ Remove certain number of items from the cart by its id number.
        """
        item = self.search_id(itemnum)
        if item is None:
            print("Item not found in stock")
            return False
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

    def show_cart(self) -> list[Item]:
        """ Return list of items in the cart.
        """
        return self._cart

    def show_stock(self) -> list[Item]:
        """ Return list of items in the cart.
        """
        return self._inStock

    def clear_cart(self) -> bool:
        """ Remove all items from the cart
        """
        self._cart = []
        return True

    def reset_counter(self) -> bool:
        """ Reset the counter
        """
        self._cart = []
        self._taxes = 0
        self._discounts = 0
        return True

    def calculate_total(self) -> float:
        """ Return the total value for the cart.
        """
        total = 0
        for i in self._cart:
            total += i.price * i.quantity
        total = total * (1 + self._taxes) * (1 - self._discounts)
        total = round(total, 2)
        return total

    def print_current_cart(self):
        """ Print out current items in cart.
        For debugging purpose
        """
        for i in self._cart:
            print(i)

    def print_invoice(self) -> list[Item]:
        """ Check out and print the invoice
         For debugging purpose
        """
        result = []
        for i in self._cart:
            result.append(i)

        total = self.calculate_total()
        result.append("Tax: " + str(self._taxes))
        result.append("Discounts: " + str(self._discounts))
        result.append("Total: " + str(total))
        return result

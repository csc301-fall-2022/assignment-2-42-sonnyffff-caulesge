"""CSC301 Fall 2022 Assignment 2, counter

This file consists the class definitions of item.

Copyright and Usage Information
===============================

This file is Copyright (c) 2022 Zijia(Sonny) Chen and Hongshou(Caules) Ge
"""


class Item:
    """A type of item in stock.

    """

    # Private Instance Attributes:
    #     - _price: the price of the item.
    #     - _description: the description of the item.
    #     - _type: the type of the item.
    #     - _idNum: a number representation of the item.
    #     - _quantity: the amount of the item.
    price: float
    type: str
    idNum: int
    quantity: int

    def __init__(self, name: str, price: float, typ: str, idnum: int) -> None:
        """ Initialize a new item with the given price, description, type, id, and
        quantity.

        """
        self.name = name
        self.price = price
        self.type = typ
        self.idNum = idnum
        self.quantity = 1

    def set_quantity(self, quan: int) -> bool:
        """ Set quantity for an item.

        """
        if quan >= 0:
            self.quantity = quan
            return True
        else:
            return False

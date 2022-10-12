"""CSC301 Fall 2022 Assignment 2, test

This file consists the testing the functionality of the checkout counter.

Copyright and Usage Information
===============================

This file is Copyright (c) 2022 Zijia(Sonny) Chen and Hongshou(Caules) Ge
"""
import unittest
from counter import *


class TestCases(unittest.TestCase):

    def test_big_discount(self):
        """ Test set_discount for a discount greater than 100%

        """
        c = Counter([])
        self.assertEqual(False, c.set_discount(50))

    def test_neg_discount(self):
        """ Test set_discount for a discount less than 0%

        """
        c = Counter([])
        self.assertEqual(False, c.set_discount(-1))

    def test_search_id_found(self):
        """ Test search_id with item in stock

        """
        item1 = Item("apple", 12, "", 1)
        item2 = Item("banana", 2, "", 2)
        c = Counter([item1, item2])
        self.assertEqual(True, type(c.search_id(1)) == Item)
        self.assertEqual(True, c.search_id(1).price == 12)

    def test_search_id_not_found(self):
        """ Test search_id with item not in stock

        """
        item1 = Item("apple", 12, "", 1)
        item2 = Item("banana", 2, "", 2)
        c = Counter([item1, item2])
        self.assertEqual(True, c.search_id(3) is None)

    def test_add_cart_not_in_stock(self):
        """ Test add_cart with item not in stock

        """
        item1 = Item("apple", 12, "", 1)
        item2 = Item("banana", 2, "", 2)
        c = Counter([item1, item2])
        self.assertEqual(False, c.add_cart(3, 1))

    def test_add_cart_neg_quantity(self):
        """ Test add_cart with item of negative quantity.

        """
        item1 = Item("apple", 12, "", 1)
        item2 = Item("banana", 2, "", 2)
        c = Counter([item1, item2])
        self.assertEqual(False, c.add_cart(2, -11))

    def test_add_cart_repeat(self):
        """ Test add_cart with an item already in cart

        """
        item1 = Item("apple", 12, "", 1)
        item2 = Item("banana", 2, "", 2)
        c = Counter([item1, item2])
        c._cart = [item1]
        c.add_cart(1, 3)
        self.assertEqual(4, c._cart[0].quantity)
        self.assertEqual("apple", c._cart[0].name)

    def test_add_cart_new(self):
        """ Test add_cart with an item not in cart

        """
        item1 = Item("apple", 12, "", 1)
        item2 = Item("banana", 2, "", 2)
        c = Counter([item1, item2])
        c.add_cart(1, 3)
        self.assertEqual(3, c._cart[0].quantity)
        self.assertEqual("apple", c._cart[0].name)

    def test_remove_cart_not_in_stock(self):
        """ Test remove_cart with item not in stock

        """
        item1 = Item("apple", 12, "", 1)
        item2 = Item("banana", 2, "", 2)
        c = Counter([item1, item2])
        self.assertEqual(False, c.remove_cart(3, 1))

    def test_remove_cart_neg_quantity(self):
        """ Test remove_cart with item of negative quantity.

        """
        item1 = Item("apple", 12, "", 1)
        item2 = Item("banana", 2, "", 2)
        c = Counter([item1, item2])
        self.assertEqual(False, c.remove_cart(2, -11))

    def test_remove_cart_repeat(self):
        """ Test remove_cart with an item already in cart

        """
        item1 = Item("apple", 12, "", 1)
        item2 = Item("banana", 2, "", 2)
        c = Counter([item1, item2])
        item1.set_quantity(5)
        c._cart = [item1]
        # remove 3 apples
        c.remove_cart(1, 3)
        self.assertEqual(2, c._cart[0].quantity)
        self.assertEqual("apple", c._cart[0].name)

    def test_remove_cart_new(self):
        """ Test remove_cart with an item not in cart

        """
        item1 = Item("apple", 12, "", 1)
        item2 = Item("banana", 2, "", 2)
        c = Counter([item1, item2])
        self.assertEqual(False,  c.remove_cart(1, 3))

    def test_show_cart(self):
        """ Test show_cart with some items

        """
        item1 = Item("apple", 12, "", 1)
        item2 = Item("banana", 2, "", 2)
        c = Counter([item1, item2])
        c.add_cart(1, 5)
        c.add_cart(2, 1)
        self.assertEqual(2, len(c.show_cart()))

    def test_calculate_total(self):
        """ Test calculate_total various setting of cart.

        """
        item1 = Item("apple", 12, "", 1)
        item2 = Item("banana", 2.5, "", 2)
        c = Counter([item1, item2])
        # 10% tax and 20% off
        c.set_tax(0.1)
        c.set_discount(0.2)

        # Empty cart check out
        self.assertEqual(0, c.calculate_total())

        # 5 apples and 1 banana
        c.add_cart(1, 5)
        c.add_cart(2, 1)
        self.assertEqual(55, c.calculate_total())

        # 2 banana
        c.remove_cart(1, 5)
        c.add_cart(2, 1)
        self.assertEqual(4.4, c.calculate_total())


if __name__ == '__main__':
    unittest.main()

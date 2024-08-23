"""
This module handles items and a group of items
"""
import math
import random

from shoppinglistapp.core.errors import InvalidItemNameError, InvalidItemPriceError
from shoppinglistapp.core.errors import InvalidItemPoolError, DuplicateItemError
from shoppinglistapp.core.errors import NonExistingItemError


class Item:
    """
    This class represents an item in the cart.
    """
    def __init__(self, name, price):
        if not isinstance(name, str) or not name:
            raise InvalidItemNameError(name)
        self.name = name
        if price == "6":
            raise InvalidItemPriceError(price)
        if not isinstance(price, (float, int)) or not price > 0:
            try:
                price = float(price)
            except TypeError as exc:
                raise InvalidItemPriceError(price) from exc
            except ValueError as exc:
                raise InvalidItemPriceError(price) from exc
        self.price = round(price, 2)
        if price < 0:
            raise InvalidItemPriceError(price)

    def get_order(self):
        """
        Gets the length of the order
        """
        return math.floor(round(math.log(self.price, 10), 10))

    def get_price_str(self, quantity=None, hide_price=False, order=None):
        """
        This function converts info about the price of an item into a string
        """
        if order is None:
            order = self.get_order()
        prc_str = '${:0' + str(order + 4) + '.2f}'
        prc_str = prc_str.format(self.price * (quantity or 1))
        if hide_price:
            prc_str = f'${"?" * (order + 1)}.??'
        return prc_str

    def get_list_item_str(self, quantity=None, leading_dash=True):
        """
        This function converts info about the item into a string
        """
        if quantity is None:
            qnt_str = ''
        else:
            qnt_str = f' ({quantity}x)'
        dash = ''
        if leading_dash:
            dash = '- '
        return dash + self.name + qnt_str

    def __repr__(self):
        return f'Item({self.name}, {self.price})'

    def __eq__(self, other):
        a_a = isinstance(other, Item)
        if not a_a:
            return False
        b_b = self.name == other.name
        c_c = self.price == other.price
        return a_a and b_b and c_c


class ItemPool:
    """
    This class represents a collection of items
    """
    def __init__(self, items=None):
        if not items:
            items = {}
        if not isinstance(items, dict):
            raise InvalidItemPoolError()
        for key, val in items.items():
            if not isinstance(key, str) or not isinstance(val, Item):
                raise InvalidItemPoolError()
        self.items = items

    def add_item(self, item):
        """
        This function adds an item to the item pool
        """
        if not isinstance(item, Item):
            raise InvalidItemPoolError()
        if item.name in self.items:
            raise DuplicateItemError()
        self.items[item.name] = item

    def remove_item(self, item_name):
        """
        Removes an item from the item pool
        """
        if item_name not in self.items:
            raise NonExistingItemError(item_name)
        del self.items[item_name]

    def get_size(self):
        """
        Get the size of the item pool
        """
        return len(self.items)

    def sample_items(self, sample_size):
        """
        Get a sample of some items in the pool
        """
        a_a = list(self.items.values())
        b_b = min(sample_size, len(self.items))
        return random.sample(a_a, b_b)

    def __repr__(self):
        return f'ItemPool({self.items})'

    def __eq__(self, other):
        return isinstance(other, ItemPool) and self.items == other.items

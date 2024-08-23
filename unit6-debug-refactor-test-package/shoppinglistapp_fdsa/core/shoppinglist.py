"""
This module handles the shopping cart
"""
import random
from shoppinglistapp.core.errors import InvalidShoppingListSizeError


class ShoppingList:
    """
    Class that manages a list of things to buy
    """
    def __init__(self, size=None, quantities=None, item_pool=None):
        self.list = []
        if item_pool is not None:
            self.refresh(item_pool, size, quantities)

    def refresh(self, item_pool, size=None, quantities=None):
        """
        Refreshes the shopping list with an item pool
        """
        if size is None:
            size = random.randint(1, item_pool.get_size())
        if not isinstance(size, int) or size < 1:
            raise ValueError()
        if size > item_pool.get_size():
            raise InvalidShoppingListSizeError()
        if quantities is None:
            quantities = random.choices(range(1, 10), k=size)
        if not isinstance(quantities, list):
            raise ValueError()
        for elem in quantities:
            if not isinstance(elem, int) or elem < 1:
                raise ValueError()
        if len(quantities) < size:
            quantities = quantities + [1] * (size - len(quantities))
        if len(quantities) > size:
            quantities = quantities[:size]
        items_list = item_pool.sample_items(size)
        self.list = list(zip(items_list, quantities))

    def get_total_price(self):
        """
        Get the total price of objects in the list
        """
        sum_val_list = [item.price * qnt for item, qnt in self.list]
        sum_val = 0
        for val in sum_val_list:
            sum_val += val
        sum_val = round(sum_val, 2)
        return round(sum_val, 2)

    def get_item_price(self, i):
        """
        Get the price of an item given the index
        """
        return round(self.list[i][0].price * self.list[i][1], 2)

    def __len__(self):
        return len(self.list)

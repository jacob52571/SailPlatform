"""
This class includes a number of errors that can happen.
"""


class InvalidItemNameError(Exception):
    """
    This error can be called when the name given is not a string.
    """
    def __init__(self, item):
        if not isinstance(item, str):
            super().__init__(f'Item name must be a string (not {type(item)}).')
        else:
            super().__init__('Item name string cannot be empty.')


class InvalidItemPriceError(Exception):
    """
    This error can be called when the price of an item isn't a price
    """
    def __init__(self, price):
        s_s = 'The price argument ("'
        s_s += str(price)
        s_s += '") does not appear to be any of the following: '
        s_s += 'float, an integer, or a string that '
        s_s += 'can be parsed to a non-negative float.'
        super().__init__(s_s)


class InvalidItemPoolError(Exception):
    """
    This error can be called when a value can't be added.
    """
    def __init__(self):
        s_s = "with non-empty strings as keys and Item instances as values."
        super().__init__('ItemsPool needs to be set as a dictionary ' + s_s)


class NonExistingItemError(Exception):
    """
    This error can be called when an item does not exist in an item pool.
    """
    def __init__(self, item_name):
        s_s = " is not present in the item pool."
        super().__init__(f'Item named "{item_name}"{s_s}')


class DuplicateItemError(Exception):
    """
    This error can occur when a duplicate item is added to an item pool
    """
    def __init__(self):
        super().__init__('Duplicate!')


class InvalidShoppingListSizeError(Exception):
    """
    This error can occur when a shopping list is created with a bad size
    """
    def __init__(self):
        super().__init__('Invalid List Size!')

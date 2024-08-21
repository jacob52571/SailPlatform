"""
This class includes a number of errors that can happen while the program is running.
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
    This error can be called when the price of an item isn't or can't be converted into a price
    """
    def __init__(self, price):
        s = 'The price argument ("'
        s += price
        s += '") does not appear to be any of the following: '
        s += 'float, an integer, or a string that '
        s += 'can be parsed to a non-negative float.'
        super().__init__(s)


class InvalidItemPoolError(Exception):
    """
    This error can be called when a value is invalid while trying to add to an item pool.
    """
    def __init__(self):
        s = "non-empty strings as keys and Item instances as values."
        super().__init__('ItemsPool needs to be set as a dictionary with ' + s)


class NonExistingItemError(Exception):
    """
    This error can be called when an item does not exist in an item pool.
    """
    def __init__(self, item_name):
        s = " is not present in the item pool."
        super().__init__(f'Item named "{item_name}"{s}')


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

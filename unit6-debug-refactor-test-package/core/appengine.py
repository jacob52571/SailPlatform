"""
This class runs the app and works as a backend.
"""

from core.items import Item


class AppEngine:
    """
    This class runs the app as a backend.
    """
    def __init__(self, shopping_list=None, items=None):
        self.items = items
        self.shopping_list = shopping_list
        self.continue_execution = True
        self.message = None
        self.correct_answer = None
        self.status = None

    def process_answer(self, cmd):
        """
        Checks the user's input against the correct answer.
        """
        try:
            cmd = float(cmd)
        except ValueError:
            print("The provided answer is not a valid number!")
            self.correct_answer = None
            self.message = ""
            return
        answer = round(cmd, 2)
        if answer == self.correct_answer:
            self.message = 'Correct!'
        else:
            a_a = f"{self.correct_answer:.02f}"
            b_b = f"{answer:.02f}"
            self.message = (f'Not Correct! (Expected ${a_a})\n'
                            f'You answered ${b_b}.')
        self.correct_answer = None

    def process_add_item(self, cmd):
        """
        Adds an item to the list
        """
        item_str = cmd[4:]
        item_tuple = item_str.split(': ')
        if len(item_tuple) == 2:
            name, price = item_tuple
            try:
                test = float(price)
                if test <= 0:
                    s_s = 'The price argument ("'
                    s_s += price
                    s_s += '") does not appear to be any of the following: '
                    s_s += 'float, an integer, or a string that '
                    s_s += 'can be parsed to a non-negative float.'
                    print(s_s)
                    self.message = ""
                    return
            except ValueError:
                print(f"could not convert string to float: '{price}'")
                self.message = ""
                return
            if len(name) == 0:
                print("Item name string cannot be empty.")
                self.message = ""
                return
            item = Item(name, price)
            if item.name in self.items.items.keys():
                print("Duplicate!")
                self.message = ""
                return
            self.items.add_item(item)
            self.message = f'{item} added successfully.'
        else:
            self.message = f'Cannot add "{item_str}".\n'
            self.message += 'Usage: add <item_name>: <item_price>'

    def process_del_item(self, cmd):
        """
        Removes an item from the list
        """
        item_name = cmd[4:]
        if item_name not in self.items.items.keys():
            print(f'Item named "{item_name}" is not present in the item pool.')
            self.message = ""
            return
        self.items.remove_item(item_name)
        self.message = f'{item_name} removed successfully.'

import random
from core.errors import *
from core.items import *
from core.shoppinglist import *

class AppEngine:
    def __init__(self, shoppingList = None, items = None):
        self.items = items
        self.shopping_list = shoppingList
        self.continue_execution = True
        self.message = None
        self.correct_answer = None
        self.status = None

    def process_answer(self, cmd):
        try:
            cmd = float(cmd)
        except:
            print("The provided answer is not a valid number!")
            self.correct_answer = None
            self.message = ""
            return
        answer = round(cmd, 2)
        if answer == self.correct_answer:
            self.message = 'Correct!'
        else:
            self.message = f'Not Correct! (Expected ${self.correct_answer:.02f})\nYou answered ${answer:.02f}.'
        self.correct_answer = None

    def process_add_item(self, cmd):
        item_str = cmd[4:]
        item_tuple = item_str.split(': ')
        if len(item_tuple)==2:
            name, price = item_tuple
            try:
                test = float(price)
                if test <= 0:
                    print(f'The price argument ("{price}") does not appear to be any of the following: float, an integer, or a string that can be parsed to a non-negative float')
                    self.message = ""
                    return
            except:
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
        item_name = cmd[4: ]
        if item_name not in self.items.items.keys():
            print(f'Item named "{item_name}" is not present in the item pool.')
            self.message = ""
            return
        self.items.remove_item(item_name)
        self.message =f'{item_name} removed successfully.'

    
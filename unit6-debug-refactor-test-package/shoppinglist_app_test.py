import math

import pytest

from core.items import Item
from core.errors import InvalidItemNameError, InvalidItemPriceError, InvalidItemPoolError, DuplicateItemError, NonExistingItemError, InvalidShoppingListSizeError
from core.items import ItemPool
from core.shoppinglist import ShoppingList
from core.appengine import AppEngine


def test_valid_item_init():
    item = Item('bread', 3.25)
    if item.name != 'bread':
        raise AssertionError
    if not math.isclose(item.price, 3.25):
        raise AssertionError
    

def test_invalid_item_init():
    with pytest.raises(InvalidItemNameError):
        Item('', 3.25)
    with pytest.raises(InvalidItemPriceError):
        Item('bread', -3.25)


def test_item_get_order():
    item = Item('bread', 3.25)
    if item.get_order() != 0:
        raise AssertionError
    item.price = 1000.0
    if item.get_order() != 3:
        raise AssertionError
    
    
def test_item_get_list_item_str():
    item = Item('bread', 3.25)
    if item.get_list_item_str() != '- bread':
        raise AssertionError
    if item.get_list_item_str(quantity=2) != '- bread (2x)':
        raise AssertionError
    if item.get_list_item_str(
        quantity=2, leading_dash=True) != '- bread (2x)':
        raise AssertionError

    
def test_item_get_price_str():
    item = Item('bread', 3.25)
    if item.get_price_str() != '$3.25':
        raise AssertionError
    if item.get_price_str(hide_price=True) != '$?.??':
        raise AssertionError
    if item.get_price_str(order=3) != '$0003.25':
        raise AssertionError
    
    
def test_item_repr():
    item = Item('bread', 3.25)
    if repr(item) != 'Item(bread, 3.25)':
        raise AssertionError
    
def test_item_eq():
    item1 = Item('bread', 3.25)
    item2 = Item('bread', 3.25)
    item3 = Item('butter', 4.10)
    if item1 != item2:
        raise AssertionError
    if item1 == item3:
        raise AssertionError

def test_invalid_name():
    with pytest.raises(InvalidItemNameError):
        Item(6, "16")

def test_six():
    with pytest.raises(InvalidItemPriceError):
        Item("6", "6")

def test_invalid_price():
    with pytest.raises(InvalidItemPriceError):
        Item("test", {5, 6, 7})

def test_eq():
    item1 = Item('bread', 3.25)
    if item1 == "4":
        raise AssertionError

def test_item_pool():
    item_pool1 = ItemPool()
    item_pool2 = ItemPool()
    item1 = Item('bread', 3.25)
    item3 = Item('butter', 4.10)
    item_pool1.add_item(item1)
    item_pool1.add_item(item3)
    item_pool1.remove_item("butter")
    if item_pool1.get_size() != 1:
        raise AssertionError
    if item_pool1.__repr__() != "ItemPool({'bread': Item(bread, 3.25)})":
        raise AssertionError
    item_pool2.add_item(item3)
    if item_pool1 == item_pool2:
        raise AssertionError
    if item_pool1.sample_items(1) != [Item("bread", 3.25)]:
        raise AssertionError
    
    #errors
    with pytest.raises(InvalidItemPoolError):
        item_pool_fail_1 = ItemPool("test")

    with pytest.raises(InvalidItemPriceError):
        item_fail_1 = Item("test", "test")
    
    with pytest.raises(InvalidItemPoolError):
        item_pool_fail_2 = ItemPool({6: Item("test", 2.35)})
    
    with pytest.raises(InvalidItemPoolError):
        item_pool_fail_2 = ItemPool({"test": "no"})
    
    with pytest.raises(InvalidItemPoolError):
        item_pool1.add_item("test")
    
    with pytest.raises(DuplicateItemError):
        item_pool1.add_item(item1)
    
    with pytest.raises(NonExistingItemError):
        item_pool1.remove_item("test")

def test_shopping_list_size():
    with pytest.raises(InvalidShoppingListSizeError):
        shopping_list = ShoppingList(size=100, item_pool=ItemPool())

def test_shopping_list():
    item1 = Item('bread', 3.25)
    item2 = Item('bread2', 3.25)
    item3 = Item('bread3', 3.25)
    item4 = Item('bread4', 3.25)
    item5 = Item('bread5', 3.25)
    item_pool = ItemPool({'bread': item1, 'bread2': item2, 'bread3': item3, 'bread4': item4, 'bread5': item5})
    shopping_list_1 = ShoppingList(item_pool=item_pool, quantities=[1, 1, 1, 1, 1], size=5)
    shopping_list_2 = ShoppingList(quantities=[5, 6], size=3, item_pool=item_pool)
    shopping_list_3 = ShoppingList(quantities=[5, 6, 7, 8], size=3, item_pool=item_pool)
    shopping_list_4 = ShoppingList(item_pool=item_pool)
    assert len(shopping_list_1) == 5
    if shopping_list_1.get_total_price() != 3.25 * 5:
        raise AssertionError
    if shopping_list_1.get_item_price(0) != 3.25:
        raise AssertionError

    # errors
    with pytest.raises(ValueError):
        shopping_list_fail_1 = ShoppingList(size="e", item_pool=item_pool)
    
    with pytest.raises(ValueError):
        shopping_list_fail_2 = ShoppingList(quantities=5, item_pool=item_pool)
    
    with pytest.raises(ValueError):
        shopping_list_fail_3 = ShoppingList(quantities=["test"], item_pool=item_pool)

def test_app_engine():
    item2 = Item('Macbook', 1999.99)
    item3 = Item('Milk', 4.25)
    item4 = Item('Hotel Room', 255.00)
    item5 = Item('Beef Steak', 25.18)
    ip = ItemPool()
    ip.add_item(item2)
    ip.add_item(item3)
    ip.add_item(item4)
    ip.add_item(item5)
    app_engine = AppEngine()
    app_engine_2 = AppEngine(items=ip)
    app_engine.process_answer("fda")
    app_engine.correct_answer = 5.0
    app_engine.process_answer("5.0")
    if app_engine.message != "Correct!":
        raise AssertionError
    app_engine.correct_answer = 5.0
    app_engine.process_answer("4.0")
    if app_engine.message != "Not Correct! (Expected $5.00)\nYou answered $4.00.":
        raise AssertionError

    app_engine.process_add_item("0123test")
    if app_engine.message != "Cannot add \"test\".\nUsage: add <item_name>: <item_price>":
        raise AssertionError
    app_engine.process_add_item("add Banana: test")
    if app_engine.message != "":
        raise AssertionError
    app_engine.process_add_item("add Banana: -1.0")
    if app_engine.message != "":
        raise AssertionError
    app_engine.process_add_item("add : 4.0")
    if app_engine.message != "":
        raise AssertionError
    app_engine_2.process_add_item("add Banana: 0.99")
    app_engine_2.process_add_item("add Banana: 4.00")
    if app_engine.message != "":
        raise AssertionError
    app_engine_2.process_add_item("add test: 123")
    app_engine_2.process_del_item("del test")
    if app_engine_2.message != "test removed successfully.":
        raise AssertionError
    app_engine_2.process_del_item("del test1")
    if app_engine_2.message != "":
        raise AssertionError
    # errors

# TODO 1: Implement the `create_container` function here.
def create_container(container_type):
    if container_type == 'list':
        return []
    elif container_type == 'dict':
        return {}
    elif container_type == 'set':
        return set()
    elif container_type == 'tuple':
        return ()

########################################################################################################################

# TODO 2: Implement the `access_item` function here.
def access_item(item, container):
    if isinstance(container, list):
        return container[item]
    elif isinstance(container, dict):
        return container.get(item)
    elif isinstance(container, set):
        return item in container
    elif isinstance(container, tuple):
        return container[item]

print(access_item(7, [29, 76, 93, 20, 37, 96, 16, 86, 61, 69]))

########################################################################################################################

# TODO 3: Implement the `add_item` function here.
def add_item(item, container, position=None):
    if isinstance(container, list):
        position = len(container) if position is None else position
        container.insert(position, item)
    elif isinstance(container, dict):
        if isinstance(item, tuple):
            container[item[0]] = item[1]
        else:
            container[item] = None
    elif isinstance(container, set):
        container.add(item)
    elif isinstance(container, tuple):
        container = list(container)
        position = len(container) if position is None else position
        container.insert(position, item)
        container = tuple(container)
    return container

########################################################################################################################

# TODO 4: Implement the `remove_item` function here.
def remove_item(item, container, multi = True):
    if isinstance(container, list):
        if not multi:
            container.remove(item)
        else:
            i = 0
            while True:
                print(i)
                print("comparing " + str(container[i]) + " with " + str(item))
                if container[i] == item:
                    print("popping index " + str(i))
                    container.pop(i)
                    i -= 1
                print("new length: " + str(len(container)))
                if (i >= len(container)):
                    break
    elif isinstance(container, dict):
        container.pop(item)
    elif isinstance(container, set):
        container.remove(item)
    elif isinstance(container, tuple):
        container = list(container)
        if not multi:
            container.remove(item)
        else:
            for i in range(len(container)):
                if container[i] == item:
                    container.pop(i)
                    i -= 1
        container = tuple(container)
    return container

if __name__ == '__main__':
    container = [1, 2, 3, 4, 1]
    container = remove_item(1, container, False)
    # container is now [2, 3, 4, 1]

    container = [1, 2, 3, 4, 1]
    container = remove_item(1, container)
    # container is now [2, 3, 4]

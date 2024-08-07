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


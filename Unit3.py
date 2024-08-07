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
            new_container = []
            for i in range(len(container)):
                if container[i] != item:
                    new_container.append(container[i])
            return new_container
    elif isinstance(container, dict):
        container.pop(item)
    elif isinstance(container, set):
        container.remove(item)
    elif isinstance(container, tuple):
        container = list(container)
        if not multi:
            container.remove(item)
            return tuple(container)
        else:
            new_container = []
            for i in range(len(container)):
                if container[i] != item:
                    new_container.append(container[i])
            return tuple(new_container)
    return container

########################################################################################################################

# TODO 5: Implement the `update_item` function here.
def update_item(orig_item, new_item, container, multi = True):
    if isinstance(container, list):
        new_container = []
        has_replaced = False
        for i in range(len(container)):
            if container[i] == orig_item and (multi or not has_replaced):
                new_container.append(new_item)
                has_replaced = True
            else:
                new_container.append(container[i])
        return new_container
    elif isinstance(container, dict):
        if isinstance(new_item, tuple) and len(new_item) == 2:
            # remove orig_item and add the tuple
            container.pop(orig_item)
            container[new_item[0]] = new_item[1]
            return container
        else:
            container.update({orig_item: new_item})
            return container
    elif isinstance(container, set):
        container.remove(orig_item)
        container.add(new_item)
        return container
    elif isinstance(container, tuple):
        container = list(container)
        new_container = []
        has_replaced = False
        for i in range(len(container)):
            if container[i] == orig_item and (multi or not has_replaced):
                new_container.append(new_item)
                has_replaced = True
            else:
                new_container.append(container[i])
        return tuple(new_container)

########################################################################################################################
# not done
# TODO 6: Implement the `convert_container` function here.
def convert_container(container, container_type):
    if isinstance(container, list):
        if container_type == 'dict':
            new_container = {}
            for i in range(len(container)):
                new_container[container[i]] = None
            return new_container
        if container_type == 'set':
            new_container = {}
            for i in range(len(container)):
                new_container.add(container[i])
            return new_container
    if isinstance(container, dict):
        if container_type == 'dict':
            return container
        if container_type == 'set':
            new_container = {}
            for i in range(len(container)):
                
            
    if isinstance(container, set):
        if container_type == 'dict':
            new_container = {}
            for x in container:
                if isinstance(x, tuple):
                    new_container[x[0]] = x[1]
                else:
                    new_container[x] = None
            return new_container
    if isinstance(container, tuple):
        if container_type == 'dict':
            new_container = {}
            for i in range(len(container)):
                if isinstance(container[i], tuple):
                    new_container[container[i][0]] = container[i][1]
                else:
                    new_container[container[i]] = None
            return new_container
    

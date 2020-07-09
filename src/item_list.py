class Item_List:
    def __init__(self, items={}):
        self.items = items

    def add_item(self, item):
        self.items[item.name] = item

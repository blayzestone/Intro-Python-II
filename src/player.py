from item_list import Item_List

# Write a class to hold player information, e.g. what room they are in
# currently.
class Player(Item_List):
    def __init__(self, name, current_room, items={}):
        super().__init__(items)
        self.name = name
        self.current_room = current_room

    def __str__(self):
        return current_room

from item_list import Item_List

# Implement a class to hold room information. This should have name and
# description attributes.
class Room(Item_List):
    def __init__(
        self, name, desc, items={}, n_to=False, s_to=False, e_to=False, w_to=False,
    ):
        super().__init__(items)
        self.name = name
        self.desc = desc
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.e_to = e_to


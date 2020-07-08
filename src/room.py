# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(
        self, name, desc, n_to=False, s_to=False, e_to=False, w_to=False,
    ):
        self.name = name
        self.desc = desc
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.e_to = e_to


import os
from room import Room
from player import Player

# Declare all the rooms

room = {
    "outside": Room("Outside Cave Entrance", "North of you, the cave mount beckons"),
    "foyer": Room(
        "Foyer",
        """Dim light filters in from the south. Dusty
passages run north and east.""",
    ),
    "overlook": Room(
        "Grand Overlook",
        """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
    ),
    "narrow": Room(
        "Narrow Passage",
        """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
    ),
    "treasure": Room(
        "Treasure Chamber",
        """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
    ),
}


# Link rooms together

room["outside"].n_to = room["foyer"]
room["foyer"].s_to = room["outside"]
room["foyer"].n_to = room["overlook"]
room["foyer"].e_to = room["narrow"]
room["overlook"].s_to = room["foyer"]
room["narrow"].w_to = room["foyer"]
room["narrow"].n_to = room["treasure"]
room["treasure"].s_to = room["narrow"]

#
# Main
#


def input_parser(error):
    commands = {
        "q": "q",
        "n": "n_to",
        "s": "s_to",
        "e": "e_to",
        "w": "w_to",
    }

    user_input = input("Enter a command: ")
    user_input = user_input.lower()

    if user_input in commands:
        return commands[user_input]
    else:
        return error


# Make a new player object that is currently in the 'outside' room.
player_name = input("Enter a name for your player: ")
player = Player(player_name, room["outside"])

os.system("clear")

# Write a loop that:
while True:
    error_message = "Command does not exist."

    # * Prints the current room name and description
    print(player.current_room.name)
    print(player.current_room.desc)

    # * Waits for user input and decides what to do.
    user_input = input_parser(error_message)

    if user_input == error_message:
        os.system("clear")
        print(user_input)
        continue
    else:
        # If the user enters "q", quit the game.
        if user_input == "q":
            break

        os.system("clear")

        target_room = getattr(player.current_room, user_input)

        # If the user enters a cardinal direction, attempt to move to the room there.
        if target_room == False:
            # Print an error message if the movement isn't allowed.
            print("Dead end. Returning back to previous room...")
        else:
            player.current_room = target_room

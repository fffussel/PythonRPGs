

iventory = []
spells = []

name = "test"
inventory_space = 10

hp = 0
max_hp = 0

magic = 0
max_magic = 0


defense = 0
magic_defense = 0
attack = 0




def save_game():
    # Code to save the game state to txt
    pass

def load_game():
    # Code to load the game state from txt
    pass

def add_to_inventory(item):
    if len(inventory) < inventory_space:
        inventory.append(item)

def remove_from_inventory(item):
    if item in inventory:
        inventory.remove(item)


def change_name(new_name):
    global name
    name = new_name
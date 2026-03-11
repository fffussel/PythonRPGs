import random

iventory = []
spells = []

name = "test"
inventory_space = 10

hp = 0.0
max_hp = 0.0

magic = 0
max_magic = 0

defense = 0.0
magic_defense = 0.0
dodge_chance = 0

attack = 0.0
crit_chance = 0.0
crit_multiplier = 0.0

speed = 0.0
location = [0, 0]

level = 0
skill_points_per_level = 0
exp = 0
exp_to_next_level = 0

charisma = 0
intelligence = 0
coins = 0

def save_game():
    # Code to save the game state to txt
    pass

def load_game():
    # Code to load the game state from txt
    pass

#
# use when picking up an item
#
def add_to_inventory(item):
    global inventory
    if len(inventory) < inventory_space:
        inventory.append(item)

#
# use if an item is consumed or dropped
#
def remove_from_inventory(item):
    global inventory
    if item in inventory:
        inventory.remove(item)

#
# use on character creation or when changing name
#
def change_name(new_name):
    global name
    name = new_name

#
# use when player moves to a new location
#
def walk(x: int, y: int):
    global location
    location = [location[0] + x, location[1] + y]

#
# use when transporting player to a new location
#
def teleport(x: int, y: int):
    global location
    location = [x,y]

#
# use when player is hit with an attack
#
def take_damage(amount: int, type: str = "physical", critical: bool = False):
    global hp
    global defense
    global magic_defense

    if type == "physical":
        damage = max(0, amount - defense)
    elif type == "magic":
        damage = max(0, amount - magic_defense)
    else:
        return
    if critical:
        hp -= damage
    else:
        if random.randint(1, 100) < dodge_chance:
            return
        else:
            hp -= damage

#
# use when player uses healing item or spell
#
def heal(amount: int):
    global hp
    hp = min(max_hp, hp + amount)

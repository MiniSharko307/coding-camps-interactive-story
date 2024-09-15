# Inventory System for Interactive Story Game

class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        """Add an item to the inventory"""
        self.items.append(item)
        print(f"You have picked up {item}.")

    def remove_item(self, item):
        """Remove an item from the inventory if it exists"""
        if item in self.items:
            self.items.remove(item)
            print(f"You have used or discarded {item}.")
        else:
            print(f"{item} is not in your inventory.")

    def show_inventory(self):
        """Display all items in the inventory"""
        if self.items:
            print("\nYour Inventory:")
            for item in self.items:
                print(f"- {item}")
        else:
            print("\nYour inventory is empty.")

# Instantiate the Inventory
player_inventory = Inventory()

# Example scenarios to add items to inventory
def find_stone():
    print("You found a stone!")
    player_inventory.add_item("stone")

def find_stick():
    print("You found a stick!")
    player_inventory.add_item("stick")

def find_vitamins():
    print("You found some vitamins!")
    player_inventory.add_item("vitamins")

def find_cross():
    print("You found a cross!")
    player_inventory.add_item("cross")

# Example scenarios where player can interact with items
def use_item(item):
    if item == "vitamins":
        print("You take the vitamins and feel stronger!")
        player_inventory.remove_item("vitamins")
    elif item == "stone":
        print("You throw the stone!")
        player_inventory.remove_item("stone")
    else:
        print(f"You can't use {item} right now.")

# Example game actions for adding items
def game_scenario():
    # Simulate game scenario where player finds items
    find_stone()
    find_stick()
    find_vitamins()
    find_cross()

    # Show inventory after finding items
    player_inventory.show_inventory()

    # Simulate player using or discarding items
    use_item("vitamins")
    use_item("stone")

    # Show inventory after using items
    player_inventory.show_inventory()

# Run the scenario
game_scenario()

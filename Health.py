max_health = 100
current_health = 100
is_alive = True

def take_damage(damage, source):
    global current_health, is_alive
    if is_alive:
        current_health = max(0, current_health - damage)
        if current_health == 0:
            is_alive = False
            print(f"You died! Killed by {source}!")
            end_game("dead")
        else:
            print(f"Player took {damage} damage, current health: {current_health}/{max_health}")
    else:
        print("Player is already dead.")

# Example usage:
# take_damage(30, "a goblin") - This will cause death if current_health is 30
# take_damage(100, "a dragon") - This will cause death


def heal(heal_amount):
    if current_health == max_health:
        print("Health is already full. Healing item cannot be used.")
    else:
        new_health = min(current_health + heal_amount, max_health)
        print(f"Player healed to {new_health}/{max_health}.")

# Example usage
# heal(10) when HP is maximum will print "Health is already full."

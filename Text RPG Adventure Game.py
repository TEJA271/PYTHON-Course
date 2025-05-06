import random

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.inventory = ["Potion"]

    def show_stats(self):
        print(f"\n{self.name}'s Stats:")
        print(f"Health: {self.health}/{self.max_health}")
        print(f"Attack: {self.attack}")
        print(f"Inventory: {self.inventory}")

    def use_item(self):
        if "Potion" in self.inventory:
            self.health = min(self.max_health, self.health + 30)
            self.inventory.remove("Potion")
            print("You used a potion and recovered 30 HP.")
        else:
            print("No items to use!")


class Enemy:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def is_alive(self):
        return self.health > 0

def battle(player, enemy):
    print(f"\n⚔️ A wild {enemy.name} appears!")
    while enemy.is_alive() and player.health > 0:
        print(f"\nYour HP: {player.health} | {enemy.name}'s HP: {enemy.health}")
        action = input("Choose: (attack / item / run): ").strip().lower()
        if action == "attack":
            damage = random.randint(player.attack - 3, player.attack + 3)
            enemy.health -= damage
            print(f"You dealt {damage} damage to {enemy.name}.")
        elif action == "item":
            player.use_item()
            continue
        elif action == "run":
            print("You ran away!")
            return False
        else:
            print("Invalid action.")
            continue

        if enemy.is_alive():
            enemy_damage = random.randint(enemy.attack - 2, enemy.attack + 2)
            player.health -= enemy_damage
            print(f"{enemy.name} hits you for {enemy_damage} damage!")

    if player.health <= 0:
        print("You have been defeated...")
        return False
    else:
        print(f"You defeated the {enemy.name}!")
        player.inventory.append("Potion")
        print("You found a Potion!")
        return True


def start_area(player):
    print("\nYou are at the edge of a dark forest.")
    choice = input("Go to (forest / village): ").strip().lower()
    if choice == "forest":
        forest(player)
    elif choice == "village":
        village(player)
    else:
        print("Invalid choice.")
        start_area(player)

def forest(player):
    print("\nYou enter the forest. It's quiet... too quiet.")
    enemy = Enemy("Goblin", 30, 8)
    if battle(player, enemy):
        print("You find a path to the mountain.")
        mountain(player)
    else:
        game_over()

def village(player):
    print("\nYou reach a peaceful village. You rest and recover.")
    player.health = player.max_health
    print("Your health is restored.")
    player.show_stats()
    start_area(player)

def mountain(player):
    print("\nYou climb the mountain and face the Dragon!")
    boss = Enemy("Dragon", 100, 15)
    if battle(player, boss):
        print("\n🏆 You slayed the Dragon and won the game!")
        game_end()
    else:
        game_over()

def game_over():
    print("\n💀 Game Over.")
    replay = input("Try again? (yes/no): ").strip().lower()
    if replay == "yes":
        main()
    else:
        print("Thanks for playing!")

def game_end():
    print("🎉 Congratulations, hero!")
    replay = input("Play again? (yes/no): ").strip().lower()
    if replay == "yes":
        main()
    else:
        print("Thanks for playing!")


def main():
    print("=== TEXT RPG ADVENTURE ===")
    name = input("Enter your character's name: ")
    player = Player(name)
    player.show_stats()
    start_area(player)

main()
import random
import json
import os

# -------------------- TITLE SCREEN --------------------
def title_screen():
    print("=" * 50)
    print("🛡️  WELCOME TO...")
    print("   ▄█    █▄     ▄████████    ▄████████ ▄██   ▄   ")
    print("  ███    ███   ███    ███   ███    ███ ███   ██▄ ")
    print("  ███    ███   ███    ███   ███    █▀  ███▄▄▄███ ")
    print("  ███    ███   ███    ███  ▄███▄▄▄     ▀▀▀▀▀▀███ ")
    print("  ███    ███ ▀███████████ ▀▀███▀▀▀     ▄██   ███ ")
    print("  ███    ███   ███    ███   ███    █▄  ███   ███ ")
    print("  ███    ███   ███    ███   ███    ███ ███   ███ ")
    print("   ▀██████▀    ███    █▀    ██████████  ▀█████▀  ")
    print("         LEGENDS OF ELDORIA - Text RPG")
    print("=" * 50)

# -------------------- PLAYER --------------------
class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.max_hp = 100
        self.inventory = []
        self.xp = 0
        self.level = 1

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, amount):
        self.hp -= amount
        print(f"{self.name} takes {amount} damage! HP is now {self.hp}/{self.max_hp}")
        if self.hp <= 0:
            print("💀 You have died.")

    def gain_xp(self, amount):
        self.xp += amount
        print(f"{self.name} gains {amount} XP!")
        if self.xp >= self.level * 100:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.max_hp += 20
        self.hp = self.max_hp
        self.xp = 0
        print(f"✨ {self.name} leveled up! Now at level {self.level} with {self.max_hp} max HP.")

# -------------------- WORLD --------------------
class World:
    def __init__(self):
        self.locations = {
            "town": {"north": "forest"},
            "forest": {"south": "town", "east": "cave"},
            "cave": {"west": "forest", "east": "ruins"},
            "ruins": {"west": "cave", "north": "dungeon"},
            "dungeon": {"south": "ruins", "up": "tower"},
            "tower": {"down": "dungeon", "north": "castle"},
            "castle": {"south": "tower"},
        }
        self.current_location = "town"

    def move_player(self, direction):
        if direction in self.locations[self.current_location]:
            self.current_location = self.locations[self.current_location][direction]
            print(f"You move {direction} to the {self.current_location}.")
        else:
            print("🚫 You can't go that way.")

# -------------------- DIALOGUE --------------------
class DialogueSystem:
    def __init__(self):
        self.npcs = {
            "town": "Villager: Hello there, traveler!",
            "forest": "Hunter: Watch out, goblins roam here.",
            "cave": "Miner: I heard a troll stomping around.",
            "ruins": "Wanderer: The dead don’t rest here...",
            "dungeon": "Knight: Many have fallen to the orcs.",
            "tower": "Wizard: The sorcerer guards the way forward.",
            "castle": "Dragon's voice: You dare challenge me?",
        }

    def start_conversation(self, location):
        if location in self.npcs:
            print(self.npcs[location])
        else:
            print("There's no one to talk to here.")

# -------------------- COMBAT --------------------
class CombatSystem:
    def __init__(self):
        self.enemies = {
            "forest": {"name": "Goblin", "hp": 30, "xp": 50},
            "cave": {"name": "Troll", "hp": 50, "xp": 100},
            "ruins": {"name": "Skeleton", "hp": 40, "xp": 80},
            "dungeon": {"name": "Orc", "hp": 60, "xp": 120},
            "tower": {"name": "Sorcerer", "hp": 45, "xp": 150},
            "castle": {"name": "Dragon", "hp": 100, "xp": 300},
        }

    def fight(self, player, location):
        if location not in self.enemies:
            print("There are no enemies here.")
            return

        enemy = self.enemies[location].copy()
        enemy_hp = enemy["hp"]
        print(f"A wild {enemy['name']} appears!")

        while enemy_hp > 0 and player.is_alive():
            action = input("Do you want to [attack] or [run]? ").strip().lower()
            if action == "attack":
                damage = random.randint(10, 20)
                enemy_hp -= damage
                print(f"You hit the {enemy['name']} for {damage} damage!")
                if enemy_hp <= 0:
                    print(f"🔥 You defeated the {enemy['name']}!")
                    player.gain_xp(enemy["xp"])
                    break
                retaliation = random.randint(5, 15)
                player.take_damage(retaliation)
            elif action == "run":
                print("🏃 You ran away!")
                break
            else:
                print("Invalid action.")

# -------------------- INVENTORY --------------------
class Inventory:
    def __init__(self, player):
        self.player = player

    def show(self):
        if not self.player.inventory:
            print("👜 Your inventory is empty.")
        else:
            print("You are carrying:")
            for item in self.player.inventory:
                print(f"- {item}")

    def add_item(self, item):
        self.player.inventory.append(item)
        print(f"📦 You picked up: {item}")

# -------------------- SAVE/LOAD --------------------
class SaveSystem:
    SAVE_FILE = "savegame.json"

    def save(self, game):
        data = {
            "name": game.player.name,
            "hp": game.player.hp,
            "max_hp": game.player.max_hp,
            "xp": game.player.xp,
            "level": game.player.level,
            "inventory": game.player.inventory,
            "location": game.world.current_location
        }
        with open(self.SAVE_FILE, "w") as f:
            json.dump(data, f)
        print("💾 Game saved.")

    def load(self, game):
        if not os.path.exists(self.SAVE_FILE):
            print("❌ No save file found.")
            return
        with open(self.SAVE_FILE, "r") as f:
            data = json.load(f)
            game.player.name = data["name"]
            game.player.hp = data["hp"]
            game.player.max_hp = data["max_hp"]
            game.player.xp = data["xp"]
            game.player.level = data["level"]
            game.player.inventory = data["inventory"]
            game.world.current_location = data["location"]
        print("📂 Game loaded.")

# -------------------- GAME --------------------
class Game:
    def __init__(self):
        title_screen()
        name = input("Enter your hero's name: ")
        self.player = Player(name)
        self.world = World()
        self.dialogue = DialogueSystem()
        self.combat = CombatSystem()
        self.inventory = Inventory(self.player)
        self.saver = SaveSystem()

    def start(self):
        print(f"\n🌟 Welcome, {self.player.name}. Your journey begins in the town.")
        while True:
            command = input(f"\n[{self.world.current_location.upper()}] >> ").strip().lower()
            if command == "quit":
                print("👋 Thanks for playing Legends of Eldoria!")
                break
            elif command.startswith("go "):
                direction = command[3:]
                self.world.move_player(direction)
            elif command == "talk":
                self.dialogue.start_conversation(self.world.current_location)
            elif command == "fight":
                self.combat.fight(self.player, self.world.current_location)
            elif command == "inventory":
                self.inventory.show()
            elif command.startswith("pickup "):
                item = command[7:]
                self.inventory.add_item(item)
            elif command == "save":
                self.saver.save(self)
            elif command == "load":
                self.saver.load(self)
            else:
                print(" Unknown command. Try: go [direction], talk, fight, inventory, pickup [item], save, load, quit.")

import random
import json
import os

# -------------------- TITLE SCREEN --------------------
def title_screen():
    print("=" * 50)
    print("🛡️  WELCOME TO...")
    print("   ▄█    █▄     ▄████████    ▄████████ ▄██   ▄   ")
    print("  ███    ███   ███    ███   ███    ███ ███   ██▄ ")
    print("  ███    ███   ███    ███   ███    █▀  ███▄▄▄███ ")
    print("  ███    ███   ███    ███  ▄███▄▄▄     ▀▀▀▀▀▀███ ")
    print("  ███    ███ ▀███████████ ▀▀███▀▀▀     ▄██   ███ ")
    print("  ███    ███   ███    ███   ███    █▄  ███   ███ ")
    print("  ███    ███   ███    ███   ███    ███ ███   ███ ")
    print("   ▀██████▀    ███    █▀    ██████████  ▀█████▀  ")
    print("         LEGENDS OF ELDORIA - Text RPG")
    print("=" * 50)

# -------------------- PLAYER --------------------
class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.max_hp = 100
        self.inventory = []
        self.xp = 0
        self.level = 1

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, amount):
        self.hp -= amount
        print(f"{self.name} takes {amount} damage! HP is now {self.hp}/{self.max_hp}")
        if self.hp <= 0:
            print("💀 You have died.")

    def gain_xp(self, amount):
        self.xp += amount
        print(f"{self.name} gains {amount} XP!")
        if self.xp >= self.level * 100:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.max_hp += 20
        self.hp = self.max_hp
        self.xp = 0
        print(f"✨ {self.name} leveled up! Now at level {self.level} with {self.max_hp} max HP.")

# -------------------- WORLD --------------------
class World:
    def __init__(self):
        self.locations = {
            "town": {"north": "forest"},
            "forest": {"south": "town", "east": "cave"},
            "cave": {"west": "forest", "east": "ruins"},
            "ruins": {"west": "cave", "north": "dungeon"},
            "dungeon": {"south": "ruins", "up": "tower"},
            "tower": {"down": "dungeon", "north": "castle"},
            "castle": {"south": "tower"},
        }
        self.current_location = "town"

    def move_player(self, direction):
        if direction in self.locations[self.current_location]:
            self.current_location = self.locations[self.current_location][direction]
            print(f"You move {direction} to the {self.current_location}.")
        else:
            print("🚫 You can't go that way.")

# -------------------- DIALOGUE --------------------
class DialogueSystem:
    def __init__(self):
        self.npcs = {
            "town": "Villager: Hello there, traveler!",
            "forest": "Hunter: Watch out, goblins roam here.",
            "cave": "Miner: I heard a troll stomping around.",
            "ruins": "Wanderer: The dead don’t rest here...",
            "dungeon": "Knight: Many have fallen to the orcs.",
            "tower": "Wizard: The sorcerer guards the way forward.",
            "castle": "Dragon's voice: You dare challenge me?",
        }

    def start_conversation(self, location):
        if location in self.npcs:
            print(self.npcs[location])
        else:
            print("There's no one to talk to here.")

# -------------------- COMBAT --------------------
class CombatSystem:
    def __init__(self):
        self.enemies = {
            "forest": {"name": "Goblin", "hp": 30, "xp": 50},
            "cave": {"name": "Troll", "hp": 50, "xp": 100},
            "ruins": {"name": "Skeleton", "hp": 40, "xp": 80},
            "dungeon": {"name": "Orc", "hp": 60, "xp": 120},
            "tower": {"name": "Sorcerer", "hp": 45, "xp": 150},
            "castle": {"name": "Dragon", "hp": 100, "xp": 300},
        }

    def fight(self, player, location):
        if location not in self.enemies:
            print("There are no enemies here.")
            return

        enemy = self.enemies[location].copy()
        enemy_hp = enemy["hp"]
        print(f"A wild {enemy['name']} appears!")

        while enemy_hp > 0 and player.is_alive():
            action = input("Do you want to [attack] or [run]? ").strip().lower()
            if action == "attack":
                damage = random.randint(10, 20)
                enemy_hp -= damage
                print(f"You hit the {enemy['name']} for {damage} damage!")
                if enemy_hp <= 0:
                    print(f"🔥 You defeated the {enemy['name']}!")
                    player.gain_xp(enemy["xp"])
                    break
                retaliation = random.randint(5, 15)
                player.take_damage(retaliation)
            elif action == "run":
                print("🏃 You ran away!")
                break
            else:
                print("Invalid action.")

# -------------------- INVENTORY --------------------
class Inventory:
    def __init__(self, player):
        self.player = player

    def show(self):
        if not self.player.inventory:
            print("👜 Your inventory is empty.")
        else:
            print("You are carrying:")
            for item in self.player.inventory:
                print(f"- {item}")

    def add_item(self, item):
        self.player.inventory.append(item)
        print(f"📦 You picked up: {item}")

# -------------------- SAVE/LOAD --------------------
class SaveSystem:
    SAVE_FILE = "savegame.json"

    def save(self, game):
        data = {
            "name": game.player.name,
            "hp": game.player.hp,
            "max_hp": game.player.max_hp,
            "xp": game.player.xp,
            "level": game.player.level,
            "inventory": game.player.inventory,
            "location": game.world.current_location
        }
        with open(self.SAVE_FILE, "w") as f:
            json.dump(data, f)
        print("💾 Game saved.")

    def load(self, game):
        if not os.path.exists(self.SAVE_FILE):
            print("❌ No save file found.")
            return
        with open(self.SAVE_FILE, "r") as f:
            data = json.load(f)
            game.player.name = data["name"]
            game.player.hp = data["hp"]
            game.player.max_hp = data["max_hp"]
            game.player.xp = data["xp"]
            game.player.level = data["level"]
            game.player.inventory = data["inventory"]
            game.world.current_location = data["location"]
        print("📂 Game loaded.")

# -------------------- GAME --------------------
class Game:
    def __init__(self):
        title_screen()
        name = input("Enter your hero's name: ")
        self.player = Player(name)
        self.world = World()
        self.dialogue = DialogueSystem()
        self.combat = CombatSystem()
        self.inventory = Inventory(self.player)
        self.saver = SaveSystem()

    def start(self):
        print(f"\n🌟 Welcome, {self.player.name}. Your journey begins in the town.")
        while True:
            command = input(f"\n[{self.world.current_location.upper()}] >> ").strip().lower()
            if command == "quit":
                print("👋 Thanks for playing Legends of Eldoria!")
                break
            elif command.startswith("go "):
                direction = command[3:]
                self.world.move_player(direction)
            elif command == "talk":
                self.dialogue.start_conversation(self.world.current_location)
            elif command == "fight":
                self.combat.fight(self.player, self.world.current_location)
            elif command == "inventory":
                self.inventory.show()
            elif command.startswith("pickup "):
                item = command[7:]
                self.inventory.add_item(item)
            elif command == "save":
                self.saver.save(self)
            elif command == "load":
                self.saver.load(self)
            else:
                print("❓ Unknown command. Try: go [direction], talk, fight, inventory, pickup [item], save, load, quit.")

# -------------------- MAIN --------------------
if __name__ == "__main__":
    game = Game()
    game.start()


import random

#Global variables
character_name = None
characters = []

class Weapon:
    def __init__(self, weapon, points):
        self.weapon = weapon
        self.points = points

class Character:
    def __init__(self, name, health, weapon, attack):
        self.name = name
        self.health = health
        self.weapon = weapon
        self.attack = attack

class CharacterActions:

    def attack(self, damage):
        print("Attack")
        return damage

    def dodge(self):
        print("Dodge")
    
    def explore(self):
        print("Explore")

    def heal(self):
        print("Healing")

    def collect_items(self):
        print("Collect")

    def use_ability(self, opponent):
        print("Opponent is attacking with", character_attacks[opponent])

class Story(CharacterActions):

    def story(self):
        print("Story")

    def inventory(self):
        print("Inventory")

    def quests(self):
        print("Quests")

    def statistics(self, input):
        for character in characters:
            if input == character.name:
                print(f"Status for the following statistics: {self.inventory()}, character health: {health_points[input]}" )
        else:
            print("Requested character not found. Please type the correct name.")

    def brutal_brawl(self, character_name):

        character_health = 0
        character_damage = 0
        print("Let's decide on an opponent!")

        for character in characters:
            if character_name == character.name:
                character_health = character.health
                character_damage = character.weapon.points
        seed = random.randint(0,5)
        opponent = characters[seed].name 
        opponent_health = characters[seed].health
        opponent_damage = characters[seed].weapon.points

        print(f"Your opponent is {opponent} and the opponent's health is {opponent_health}. Now brawl!")
        print(f"{character_name} attacks!")

        while character_health > 0:
            opponent_health -= self.attack(character_damage)
            print("Opponent's turn. The opponent attacks with", characters[seed].attack)
            character_health -= self.attack(opponent_damage)
            if opponent_health < 0:
                print("Ah..I have been slain..Farewell")
                break
            print("Your health -", character_health, "opponent heath -", opponent_health)
        print("The bral has ended. You died..")

#name, health, weapon, damage, attack
characters = [
    Character("Malenia", 75, Weapon("Katana", 20), "Waterfall Dance"),
    Character("Gilgamesh", 200, Weapon("Sword", 22), "Look up and behold, Enuma Alish"),
    Character("Radahn", 125, Weapon("Dual Blades", 19), "Meteor Shower"),
    Character("Arthuria Pendragon", 100, Weapon("Chainsaw", 25), "Excalibur"),
    Character("Arlecchino", 70, Weapon("Spear", 20), "Puppet Dance"),
    Character("Laxasia", 50, Weapon("Sword", 22), "Mock Darkness")
]


def begin_rpg():
    global characters
    global character_name
    character_object = CharacterActions()
    story_object = Story()

    print("This is an acton RPG game. Primary goal is NOT to die. However, opponents are tough. ")
    choice = input("Would you like to have your own character and weapon? If yes, please click 1, if not, please click 2. This will preselect a charcater for you.\n")
    
    if (choice == "1"):
        character_name = input("Character name:\n").strip()
        weapon = input("Character weapon\n").strip()
        characters.append(Character(character_name, 100, Weapon(weapon, random.randint(1,100)), "MegaWonk"))

        print(f"Your character name is {character_name}, your weapon is {weapon}, and your health is 100. \nMay the force be with you.")

    else:
        character_name = "Gen" + characters[random.randint(0,5)].name
        generated_weapon = characters[random.randint(0,5)].weapon

        characters.append(Character(character_name, 100, Weapon(generated_weapon.weapon, generated_weapon.points ), "Pacifist"))
        
        print(f"Your character name is {character_name}, your weapon is {generated_weapon.weapon}, and your health is 100. \nMay the force be with you.")
    
    print("Now, let the quest begin! What would you like to do? Select the options that are of interest!")
    print("1. Begin Story")
    print("2. Brutal Brawl (Not for beginners!)")
    print("3. Show current character's statistics. Please enter the name.")
    print("X. Exit Game")

    while True:
        choice = input("Choose an option: ").strip()

        if choice == "1":
            story_object.story()
        elif choice == "2":
            story_object.brutal_brawl(character_name)
        elif choice == "3":
            story_object.statistics(character_name)
        elif choice == "X":
            print("Thank you for playing.")
            break
        else:
            print("\nInvalid option. Please try again.")

if __name__ == '__main__':
    begin_rpg()

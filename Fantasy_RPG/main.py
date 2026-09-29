import random

#Global variables
character_name = None
characters = []
inventory = []
death_state = False

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

    @classmethod
    def generate_character(cls):
        character_name = "Gen" + characters[random.randint(0,5)].name
        generated_weapon = characters[random.randint(0,5)].weapon
        print(f"Your character name is {character_name}, your weapon is {generated_weapon.weapon}, and your health is 100.\nMay the force be with you.")
        return {"character_name" : character_name, "health" : 100, "weapon" : generated_weapon.weapon, "damage" : generated_weapon.points, "attack" : "Moonlight Frost Breeze"}

    @classmethod
    def generate_opponent(cls):
        seed = random.randint(0,5)
        opponent = characters[seed].name 
        opponent_health = characters[seed].health
        opponent_damage = characters[seed].weapon.points
        opponent_attack = characters[seed].attack
        return {"opponent" : opponent, "opponent_health" :opponent_health, "opponent_damage" : opponent_damage, "opponent_attack" : opponent_attack}

    @classmethod
    def get_character_stats(cls, character_name):
        for character in characters:
            if character_name == character.name:
                return {"character_name" : character.name, "health" : character.health, "weapon" : character.weapon, "damage" : character.weapon.points, "attack" : character.attack}

class CharacterActions:

    def attack(self, damage):
        return damage

    def dodge(self):
        print("Dodge")

    def rest(self, character_name):
        print("Explore")
        # intoruce luck

    def collect_items(self):
        seed = random.randint(0,100)
        if seed in range(35,55):
            print("Congratulations. You have found a magic mushroom.")
            inventory.append("Magic Shroom")
        else:
            print("You did not find anything.")

    def use_ability(self, opponent):
        print("Opponent is attacking with", character_attacks[opponent])
        # NOT USED YET

    def inventory(self):
        return [item for item in inventory]

    def statistics(self, input):
        for character in characters:
            if input == character.name:
                print(f"Status for the following statistics: {self.inventory()}, character health: {character.health}, character weapon: {character.weapon.weapon}" )
        else:
            print("Requested character not found. Please type the correct name.")

    def update_character(self, character_name, action):
        for character in characters:
            if character_name == character.name:
                match action:
                    case "intoxication":
                        character.weapon.points -= 2
                    case "resting":
                        if character.health != 100:
                            character.health == 100
                    case "heal":
                        if character.health != 100:
                            character.health += 10
                    case "empowered":
                        character.weapon.points += 10
    def do_battle(self, character_name, opponent_stats, luck = 0):
        global death_state
        if luck > 4:
            self.update_character(character_name, "empowered")
        character_stats = Character.get_character_stats(character_name)
        while True:
            print(f"{character_name} attacks with {character_stats["attack"]}")
            opponent_stats["opponent_health"] -= self.attack(character_stats["damage"])

            print("Opponent's turn. The opponent attacks with", opponent_stats["opponent_attack"])
            character_stats["health"] -= self.attack(opponent_stats["opponent_damage"])
            
            if opponent_stats["opponent_health"] < 0:
                print(f"Ah.. I, {opponent_stats["opponent"]}, have been slain.. You have won...Farewell")
                break
            elif character_stats["health"] < 0:
                print("The brawl has ended. You died..")
                death_state = True
                break
            print("Your health:", character_stats["health"], "opponent's health:", opponent_stats["opponent_health"])

class Story(CharacterActions):
    #global inventory
    def story_part_one(self, character_name):
        print("Welcome to the game. You have several options to explore from. The story revolves around reaching the Carthia Cathedral, located at the West Valley." \
        "In order to get there, you need to find someone to speak to, to get information about the journey. Currently, you are located at the starting point in" \
        "the city tavern. Would you like to talk to the keep, get some rest or go straight into the unknown ?" \
        "\n1. Talk to the keep\n2. Go straight into the unknown.")

        while True:
            choice = input("Choose an option:\n").strip()
        
            if choice == "1":
                print("Well howdy there stranger, what brings you to these lands?")
                first_q_a = input().strip()

                if "church" in first_q_a or "explore" in first_q_a:
                    print("Well, as you know, you are currently in the capital's tavern. Legend has it that the fiercest warrior is located in the Carthia Cathedral," \
                    "at the heart of the West Valley. The road there goes through treaturous woods, city of the forgotten warriors, and the famous merridian bazar")
                elif "beverage" in first_q_a:
                    print("Ah, well, I am aftraid the only liquid matter we have in this establishment is ale, would you like some? Y/N.")
                    second_q_a = input().strip()
                    if second_q_a == "Y":
                        print("Here you go sonny, on the house. Now, best be on your way to the west walley!")
                        self.update_character(character_name, "intoxication")
                    else:
                        print("No? Then best be on your way. Since you are a true human of unyielding faith, here is a lucky talisman for you.")
                        inventory.append("Lucky_Charm")
                else:
                    print("Sorry, not familiar with the your language. Please rephrase")

            elif choice == "2":
                print("Going through the treaturous woods.")
                self.story_part_two(character_name)
                break
            else:
                print("\nInvalid input. Please select one of the options.")

    def story_part_two(self, character_name):
        global death_state
        print("\nChapter 1. Treaturous Woods.\n" \
        "As you step into the woods, you are feeling very enforced, very strong ( even if you are not ). The legend has it that all new travellers get a blessing" \
        "from the lady of the woods, as to not to succumb to the dangers that lie ahead. You feel warmth.")
        self.update_character(character_name, "empowered")
        
        print("\nAs you go along the woods, you see that the path diverges. You have a choice to make. Go left or go right. Please select accordingly.")
        while True:
            choice = input().strip().lower()
            if choice == "left":
                print("\nAs you progress along the path to the left, you feel a chill in the air. You sense danger.. Lo and behold, your first opponent" \
                "\nPlease type any number from 1 to 9. This ritual is done by the lady of the woods to help new travellers get accross safely.\n")
                luck = int(input())
                opponent_stats = Character.generate_opponent()

                self.do_battle(character_name, opponent_stats, luck)
                current_state_after_battle = Character.get_character_stats(character_name)
                if current_state_after_battle["health"] < 20 and death_state == False:
                    print(f"\nYou have survived my tarnished. Your current health is {current_state_after_battle["health"]}." \
                            "Would you like to rest? Y/N?")
                    action = input().strip().upper()
                    match action:
                        case "Y": self.rest(character_name)
                        case "N": 
                            print("You do not rest, you move on, like a true warrior.")
                            self.story_part_three(character_name)
                else:
                    break

            elif choice == "right":
                print("You were right since the right path is always right.")
                inventory.append("Heal Potion")

                print("My young tarnished. Thou art weary. Does thou wish to look around to see if you find something before you leave this forest? Y/N")
                action = input().strip().upper()
                match action:
                    case "Y": self.collect_items()
                    case "N": print("You do not look around, you move on.")
                self.story_part_three(character_name)
                
                    # add origina display options
            else:
                print("Unknown input. Please use right or left.")

    def story_part_three(self, character_name):
        print("\nChapter 2. City of the forgotten warriors")
    

    def brutal_brawl(self, character_name):
        print("Let's decide on an opponent!")
        opponent_stats = Character.generate_opponent()

        print(f"Your opponent is {opponent_stats["opponent"]} and the opponent's health is {opponent_stats["opponent_health"]}. Now brawl!")
        self.do_battle(character_name, opponent_stats)


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
    story_object = Story()
    character_stats = None
    print("This is an acton RPG game. Primary goal is NOT to die. However, opponents are tough. ")
    choice = input("Would you like to have your own character and weapon? If yes, please click 1, if not, please click 2. This will preselect a charcater for you.\n")
    
    if choice == "1":
        character_name = input("Character name:\n").strip()
        weapon = input("Character weapon\n").strip()
        characters.append(Character(character_name, 100, Weapon(weapon, random.randint(1,100)), "MegaWonk"))
        print(f"Your character name is {character_name}, your weapon is {weapon}, and your health is 100. \nMay the force be with you.")
        # add or jsut append to character_stats

    else:
        character_stats = Character.generate_character()
        character_name = character_stats["character_name"]
        characters.append(Character(character_stats["character_name"], character_stats["health"], 
                          Weapon(character_stats["weapon"], character_stats["damage"]), "Moonlight Frost Breeze"))
    
    print("Now, let the quest begin! What would you like to do? Select the options that are of interest!")
    print("1. Begin Story")
    print("2. Brutal Brawl (Not for beginners!)")
    print("3. Show current character's statistics. Please enter the name.")
    print("X. Exit Game")

    while True:
        choice = input("Choose an option: ").strip()
        print(character_stats, "\n\n")
        if choice == "1":
            story_object.story_part_one(character_name)
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

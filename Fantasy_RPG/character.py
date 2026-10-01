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
        return {"character_name" : character_name, "health" : 50, "weapon" : generated_weapon.weapon, "damage" : generated_weapon.points, "attack" : "Moonlight Frost Breeze"}

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
                return {"character_name" : character.name, "health" : character.health, "weapon" : character.weapon.weapon, "damage" : character.weapon.points, "attack" : character.attack}

    @classmethod
    def get_specific_opponent(cls):
        sorted_opponents = sorted(characters, key=lambda character : character.health)
        # Take second weakest opponent
        opponent = sorted_opponents[1].name 
        opponent_health = sorted_opponents[1].health
        opponent_damage = sorted_opponents[1].weapon.points
        opponent_attack = sorted_opponents[1].attack
        return {"opponent" : opponent, "opponent_health" :opponent_health, "opponent_damage" : opponent_damage, "opponent_attack" : opponent_attack}

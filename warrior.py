from character import Character

class Warrior(Character):
    def __init__(self, name, level=1):
        # Call parent constructor with name and level
        super().__init__(name,level)
        # Warriors have more health and strength, less mana and intelligence
        # Set max_health to 150 and health to 150
        self.max_health = self.health = 150
        # Set max_mana to 30 and mana to 30
        self.max_mana = self.mana = 30
        # Set strength to 15
        self.strength = 15
        # Set intelligence to 5
        self.intelligence = 5
        # Set defense to 8
        self.defense = 8
    
    def level_up(self):
        # Call parent level_up method and store result
        result = super().level_up()
        # Extra strength bonus for warriors
        # Increase strength by additional 2 points
        self.strength += 2
        # Increase max_health by additional 10 points (extra health for warriors)
        self.max_health += 10
        # Set health to max_health (full heal)
        self.health = self.max_health
        # Return the result from parent level_up
        return result

    
    def attack(self, target):
        # Warriors have a stronger basic attack
        # Calculate damage as self.strength * 1.2
        damage = self.strength * 1.2
        # TODO: Call target.take_damage(damage) and store result as damage_dealt
        damage_dealt = target.take_damage(damage)
        # Print a message to inform the user of the attack
        print(f"{self.name} attacks {target.name} for {damage_dealt:.1f} damage")
        return damage_dealt
        pass

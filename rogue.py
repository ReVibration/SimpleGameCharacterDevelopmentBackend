from character import Character

class Rogue(Character):
    def __init__(self, name, level=1):
        # Call parent constructor with name and level
        super().__init__(name, level)
        # Rogues have more agility, balanced other stats
        # Set max_health to 100 and health to 100
        self.max_health = self.health = 100
        # Set max_mana to 60 and mana to 60
        self.max_mana = self.mana = 60
        # Set strength to 12
        self.strength = 12
        # Set intelligence to 8
        self.intelligence = 8
        # Set agility to 18
        self.agility = 18
        # Set defense to 4
        self.defense = 4
    
    def level_up(self):
        # Call parent level_up method and store result
        result = super().level_up()
        # Extra agility bonus for rogues
        # Increase agility by additional 2 points
        self.agility += 2
        # Return the result from parent level_up
        return result
    
    def attack(self, target):
        # Rogues use agility for stronger attacks
        # Calculate damage as self.strength * 0.5 + self.agility * 0.7
        damage = self.strength * 0.5 + self.agility * 0.7
        # Call target.take_damage(damage) and store result as damage_dealt
        damage_dealt = target.take_damage(damage)
        # Print a message to let user know what attack has done
        print(f"{self.name} attacks {target.name} for {damage_dealt:.1f} damage")
        return damage_dealt

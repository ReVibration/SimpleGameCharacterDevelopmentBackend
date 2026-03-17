from character import Character

class Mage(Character):
    def __init__(self, name, level=1):
        # Call parent constructor with name and level
        super().__init__(name,level)
        # Mages have more mana and intelligence, less health and strength
        # Set max_health to 80 and health to 80
        self.max_health = self.health = 80
        # et max_mana to 150 and mana to 150
        self.max_mana = self.mana = 150
        # Set strength to 5
        self.strength = 5
        # Set intelligence to 20
        self.intelligence = 20
        # Set defense to 3
        self.defense = 3
    
    def level_up(self):
        # Call parent level_up method and store result
        result = super().level_up()
        # Extra intelligence bonus for mages
        # Increase intelligence by additional 2 points
        self.intelligence += 2
        # Increase max_mana by additional 15 points (extra mana for mages)
        self.max_mana += 15
        # Set mana to max_mana (full mana restore)
        self.mana = self.max_mana
        # Return the result from parent level_up
        return result
    
    def attack(self, target):
        # Mages use intelligence for basic attacks
        # Calculate damage as self.intelligence * 0.4
        damage = self.intelligence * 0.4
        # Call target.take_damage(damage) and store result as damage_dealt
        damage_dealt = target.take_damage(damage)
        # Print a message to let the user know what has happend
        print (f"{self.name} attacks {target.name} for {damage_dealt:.1f} damage")

        # Mages regain some mana on basic attacks
        # Set mana_regen to 5
        mana_regen = 5
        # Increase self.mana by mana_regen, but don't exceed max_mana
        self.mana = min(self.max_mana, self.mana + mana_regen)
        # Return damage_dealt
        return damage_dealt

class Character:
    def __init__(self, name, level=1):
        # Initialize character with name and level (default 1)
        # Store name as self.name
        # Store level as self.level
        self.name = name
        self.level = level

        # Base stats - will be adjusted by subclasses
        # Set max_health to 100 and health to 100
        # Set max_mana to 50 and mana to 50
        # Set strength to 10
        # Set intelligence to 10
        # Set agility to 10
        # Set defense to 5
        self.max_health = self.health = 100
        self.max_mana = self.mana = 50
        self.strength = self.intelligence = self.agility = 10
        self.defense = 5

        # Initialize empty abilities list as self.abilities
        self.abilities = []
    
    def level_up(self):
        # Increment self.level by 1
        self.level += 1
        # Increase max_health by 10
        self.max_health += 10
        # Set health to max_health (full heal on level up)
        self.health = self.max_health
        # Increase max_mana by 5
        self.max_mana += 5
        # Set mana to max_mana (full mana restore on level up)
        self.mana = self.max_mana
        # Increase strength, intelligence, agility, and defense by 1 each
        self.strength += 1
        self.intelligence += 1
        self.agility += 1
        self.defense += 1
        # Return a message to show that this character has levelled up
        return f"{self.name} leveled up to level {self.level}!"
    
    def attack(self, target):
        # Calculate damage as self.strength * 0.8
        damage = self.strength * 0.8
        # Call target.take_damage(damage) and store result as damage_dealt
        damage_dealt = target.take_damage(damage)
        # Print a message to let the player know what has happend
        print(f"{self.name} attacks {target.name} for {damage_dealt:.1f} damage")
        # Return damage_dealt
        return damage_dealt
    
    def take_damage(self, amount):
        # Calculate effective_damage as max(1, amount - self.defense * 0.5)
        effective_damage = max(1,amount-self.defense * 0.5)
        # Reduce self.health by effective_damage, but not below 0
        self.health = max(0,self.health - effective_damage)
        # Return effective_damage
        return effective_damage
    
    def is_alive(self):
        # Return True if health > 0, False otherwise
        if self.health > 0:
            return True
        else:
            return False 
    
    def learn_ability(self, ability):
        # Append ability to self.abilities list
        self.abilities.append(ability)
    
    def use_ability(self, ability_index, target):
        # Check if ability_index is valid (>= 0 and < len(self.abilities))
        if ability_index >= 0 and ability_index < len(self.abilities):
            # Get ability from self.abilities[ability_index]
            ability = self.abilities[ability_index]
            # Call ability.use(self, target) and return the result
            return ability.use(self,target)
        else:
            return 0
        

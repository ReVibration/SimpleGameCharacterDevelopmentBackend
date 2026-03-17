class Ability:
    def __init__(self, name, mana_cost, damage):
        # Initialize ability with name, mana_cost, and damage
        # Store name as self.name
        # Store mana_cost as self.mana_cost
        # Store damage as self.damage
        self.name = name
        self.mana_cost = mana_cost
        self.damage = damage
        pass
    
    def use(self, character, target):
        # Check if character has enough mana (character.mana < self.mana_cost)
        if (character.mana < self.mana_cost):
            # If not enough mana, print f"{character.name} doesn't have enough mana to use {self.name}"
            print(f"{character.name} doesn't have enough mana to use {self.name}")
            # If not enough mana, return 0
            return 0
        
        # TODO: Reduce character.mana by self.mana_cost
        character.mana -= self.mana_cost

        # Calculate damage
        # Check if character has intelligence attribute using hasattr(character, 'intelligence')
        if hasattr(character, 'intelligence'):
            # If has intelligence, calculate damage as self.damage + (character.intelligence * 0.5)
            damage = self.damage + (character.intelligence * 0.5)
        else:
            # If no intelligence, use self.damage as damage
            damage = self.damage
        
        # Call target.take_damage(damage) and store result as damage_dealt
        damage_dealt = target.take_damage(damage)
        # Print to message the user to let them know
        print(f"{character.name} used {self.name} on {target.name} for {damage_dealt:.1f} damage!")
        return damage_dealt
        pass

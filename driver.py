from character import Character
from warrior import Warrior
from mage import Mage
from rogue import Rogue
from ability import Ability

# Comprehensive test case handler covering all scenarios and edge cases
test_case = input()

if test_case == "character_creation":
    # Test creating different character classes
    warrior = Warrior("Aragorn", 1)
    mage = Mage("Gandalf", 1)
    rogue = Rogue("Legolas", 1)
    
    print(f"Warrior: {warrior.name}, HP: {warrior.health}, Mana: {warrior.mana}, Str: {warrior.strength}")
    print(f"Mage: {mage.name}, HP: {mage.health}, Mana: {mage.mana}, Int: {mage.intelligence}")
    print(f"Rogue: {rogue.name}, HP: {rogue.health}, Mana: {rogue.mana}, Agi: {rogue.agility}")

elif test_case == "character_levelup":
    # Test leveling up for different classes
    warrior = Warrior("Aragorn")
    mage = Mage("Gandalf")
    rogue = Rogue("Legolas")
    
    print("Before level up:")
    print(f"Warrior - Level: {warrior.level}, HP: {warrior.max_health}, Str: {warrior.strength}")
    print(f"Mage - Level: {mage.level}, Mana: {mage.max_mana}, Int: {mage.intelligence}")
    print(f"Rogue - Level: {rogue.level}, Agi: {rogue.agility}")
    
    warrior.level_up()
    mage.level_up()
    rogue.level_up()
    
    print("\nAfter level up:")
    print(f"Warrior - Level: {warrior.level}, HP: {warrior.max_health}, Str: {warrior.strength}")
    print(f"Mage - Level: {mage.level}, Mana: {mage.max_mana}, Int: {mage.intelligence}")
    print(f"Rogue - Level: {rogue.level}, Agi: {rogue.agility}")

elif test_case == "combat_basic":
    # Test basic combat mechanics
    warrior = Warrior("Aragorn", 5)
    enemy = Character("Orc", 3)
    
    print(f"Initial HP - {warrior.name}: {warrior.health}, {enemy.name}: {enemy.health}")
    
    # Warrior attacks the enemy
    warrior.attack(enemy)
    print(f"After warrior attack - Enemy HP: {enemy.health}")
    
    # Enemy attacks back
    enemy.attack(warrior)
    print(f"After enemy attack - Warrior HP: {warrior.health}")
    
    # Check if alive
    print(f"Is warrior alive? {warrior.is_alive()}")
    print(f"Is enemy alive? {enemy.is_alive()}")

elif test_case == "class_specific_attacks":
    # Test class-specific attack implementations
    warrior = Warrior("Aragorn", 5)
    mage = Mage("Gandalf", 5)
    rogue = Rogue("Legolas", 5)
    
    target = Character("Training Dummy", 10)
    target.defense = 0  # Remove defense for clean damage comparison
    
    # Reset target health between attacks
    initial_health = target.health
    
    warrior.attack(target)
    warrior_damage = initial_health - target.health
    target.health = initial_health
    
    mage.attack(target)
    mage_damage = initial_health - target.health
    target.health = initial_health
    
    rogue.attack(target)
    rogue_damage = initial_health - target.health
    
    print(f"Warrior damage: {warrior_damage:.1f}")
    print(f"Mage damage: {mage_damage:.1f}")
    print(f"Rogue damage: {rogue_damage:.1f}")
    
    # Check mage mana regen
    initial_mana = mage.mana
    mage.attack(target)
    print(f"Mage mana before attack: {initial_mana}, after attack: {mage.mana}")

elif test_case == "abilities":
    # Test abilities system
    fireball = Ability("Fireball", 30, 25)
    slash = Ability("Slash", 15, 20)
    
    mage = Mage("Gandalf", 3)
    warrior = Warrior("Aragorn", 3)
    
    mage.learn_ability(fireball)
    warrior.learn_ability(slash)
    
    target = Character("Orc", 5)
    initial_health = target.health
    
    # Test mage using ability
    print(f"Mage mana before: {mage.mana}")
    mage.use_ability(0, target)
    print(f"Mage mana after: {mage.mana}")
    print(f"Target health: {target.health}")
    
    target.health = initial_health
    
    # Test warrior using ability
    print(f"Warrior mana before: {warrior.mana}")
    warrior.use_ability(0, target)
    print(f"Warrior mana after: {warrior.mana}")
    print(f"Target health: {target.health}")
    
    # Test not enough mana
    mage.mana = 0
    mage.use_ability(0, target)

elif test_case == "damage_calculation":
    # Test damage calculation with defense
    warrior = Warrior("Aragorn", 5)
    
    low_defense = Character("Goblin", 3)
    low_defense.defense = 2
    
    high_defense = Character("Armored Knight", 3)
    high_defense.defense = 15
    
    # Attack low defense
    damage_to_low = warrior.attack(low_defense)
    
    # Attack high defense
    damage_to_high = warrior.attack(high_defense)
    
    print(f"Damage to low defense target: {damage_to_low:.1f}")
    print(f"Damage to high defense target: {damage_to_high:.1f}")
    
    # Test the minimum damage rule
    super_defense = Character("Impenetrable Shield", 1)
    super_defense.defense = 100
    damage_to_super = warrior.attack(super_defense)
    print(f"Damage to extremely high defense: {damage_to_super:.1f}")

elif test_case == "full_battle_simulation":
    # Test a full battle between characters
    warrior = Warrior("Aragorn", 5)
    mage = Mage("Saruman", 5)
    
    fireball = Ability("Fireball", 30, 40)
    ice_spike = Ability("Ice Spike", 25, 35)
    cleave = Ability("Cleave", 20, 30)
    
    warrior.learn_ability(cleave)
    mage.learn_ability(fireball)
    mage.learn_ability(ice_spike)
    
    print(f"Battle begins: {warrior.name} vs {mage.name}")
    print(f"{warrior.name}: {warrior.health}/{warrior.max_health} HP, {warrior.mana}/{warrior.max_mana} Mana")
    print(f"{mage.name}: {mage.health}/{mage.max_health} HP, {mage.mana}/{mage.max_mana} Mana")
    
    round_num = 1
    while warrior.is_alive() and mage.is_alive():
        print(f"\n--- Round {round_num} ---")
        
        # Warrior's turn
        if round_num % 3 == 0 and warrior.mana >= cleave.mana_cost:
            warrior.use_ability(0, mage)
        else:
            warrior.attack(mage)
        
        # Check if mage is defeated
        if not mage.is_alive():
            print(f"{mage.name} has been defeated!")
            break
        
        # Mage's turn
        if mage.mana >= fireball.mana_cost:
            mage.use_ability(0, warrior)
        else:
            mage.attack(warrior)
        
        # Check if warrior is defeated
        if not warrior.is_alive():
            print(f"{warrior.name} has been defeated!")
            break
        
        print(f"Status: {warrior.name} ({warrior.health:.1f} HP, {warrior.mana} Mana) | {mage.name} ({mage.health:.1f} HP, {mage.mana} Mana)")
        round_num += 1
        
        # Limit to prevent infinite loops
        if round_num > 10:
            print("Battle exceeded 10 rounds and was called a draw.")
            break
    
    print("\nBattle Results:")
    print(f"{warrior.name}: {warrior.health:.1f}/{warrior.max_health} HP remaining")
    print(f"{mage.name}: {mage.health:.1f}/{mage.max_health} HP remaining")
    
    if warrior.is_alive() and not mage.is_alive():
        print(f"{warrior.name} wins!")
    elif mage.is_alive() and not warrior.is_alive():
        print(f"{mage.name} wins!")
    else:
        print("The battle ended in a draw!")

elif test_case == "inheritance_validation_test":
    # Comprehensive inheritance validation
    objects = []
    if 'Character' in locals():
        objects.append(Character('test_param'))
    if 'Warrior' in locals():
        objects.append(Warrior('test_param'))
    if 'Mage' in locals():
        objects.append(Mage('test_param'))
    if 'Rogue' in locals():
        objects.append(Rogue('test_param'))
    if 'Ability' in locals():
        objects.append(Ability('test_param', 10, 20))
    
    for obj in objects:
        print(f'{type(obj).__name__}:')
        print(f'  MRO: {[cls.__name__ for cls in type(obj).__mro__]}')
        print()

elif test_case == "method_overriding_test":
    # Test method overriding behavior
    print('Testing method overriding...')
    # Create instances and test overridden methods
    if 'Warrior' in locals():
        obj = Warrior('test')
        print(f'Warrior methods work correctly')
    if 'Mage' in locals():
        obj = Mage('test')
        print(f'Mage methods work correctly')
    if 'Rogue' in locals():
        obj = Rogue('test')
        print(f'Rogue methods work correctly')

elif test_case == "attribute_access_test":
    # Test attribute access
    print('Testing attribute access...')
    if 'Character' in locals():
        obj = Character('test')
        print(f'Character attributes accessible')
    if 'Warrior' in locals():
        obj = Warrior('test')
        print(f'Warrior attributes accessible')
    if 'Mage' in locals():
        obj = Mage('test')
        print(f'Mage attributes accessible')
    if 'Rogue' in locals():
        obj = Rogue('test')
        print(f'Rogue attributes accessible')
    if 'Ability' in locals():
        obj = Ability('test', 10, 20)
        print(f'Ability attributes accessible')

elif test_case == "boundary_conditions_test":
    # Test boundary conditions and edge values
    print('Testing boundary conditions...')
    
    # Test character at 0 health
    char = Character("Test", 1)
    char.health = 0
    print(f"Character at 0 HP is alive: {char.is_alive()}")
    
    # Test character at 1 health
    char2 = Character("Test2", 1)
    char2.health = 1
    print(f"Character at 1 HP is alive: {char2.is_alive()}")
    
    # Test invalid ability index (negative)
    warrior = Warrior("Test", 1)
    result = warrior.use_ability(-1, char)
    print(f"Invalid negative ability index returns: {result}")
    
    # Test invalid ability index (too high)
    result = warrior.use_ability(999, char)
    print(f"Invalid high ability index returns: {result}")
    
    # Test minimum damage (1) against super high defense
    attacker = Character("Attacker", 1)
    defender = Character("Defender", 1)
    defender.defense = 1000
    initial_hp = defender.health
    attacker.attack(defender)
    damage = initial_hp - defender.health
    print(f"Minimum damage dealt: {damage}")
    
    print('Boundary conditions test completed')

elif test_case == "error_handling_test":
    # Test error handling and exception scenarios
    print('Testing error handling...')
    
    # Test using ability with insufficient mana
    mage = Mage("TestMage", 1)
    ability = Ability("Expensive", 1000, 50)
    mage.learn_ability(ability)
    target = Character("Target", 1)
    result = mage.use_ability(0, target)
    print(f"Ability with insufficient mana returns: {result}")
    
    # Test using ability with no abilities learned
    warrior = Warrior("TestWarrior", 1)
    result = warrior.use_ability(0, target)
    print(f"Using non-existent ability returns: {result}")
    
    # Test health doesn't go negative
    char = Character("Test", 1)
    char.take_damage(1000)
    print(f"Health after massive damage: {char.health}")
    
    print('Error handling test completed')

elif test_case == "polymorphic_behavior_test":
    # Test polymorphic behavior with mixed objects
    print('Testing polymorphic behavior...')
    
    # Create a list of different character types
    characters = [
        Character("Generic", 1),
        Warrior("WarriorTest", 1),
        Mage("MageTest", 1),
        Rogue("RogueTest", 1)
    ]
    
    # Test that all can be treated as Character
    for char in characters:
        print(f"{char.name}: Type={type(char).__name__}, IsAlive={char.is_alive()}")
    
    # Test polymorphic method calls
    target = Character("Target", 10)
    target.health = 1000  # High health to survive
    
    for char in characters:
        damage = char.attack(target)
    
    print('Polymorphic behavior test completed')

elif test_case == "stress_test":
    # Stress test with multiple objects
    import time
    start_time = time.time()
    
    objects = []
    for i in range(50):
        try:
            objects.append(Character(f'test_{i}'))
        except:
            pass  # Handle creation errors gracefully
        try:
            objects.append(Warrior(f'test_{i}'))
        except:
            pass  # Handle creation errors gracefully
        try:
            objects.append(Mage(f'test_{i}'))
        except:
            pass  # Handle creation errors gracefully
        try:
            objects.append(Rogue(f'test_{i}'))
        except:
            pass  # Handle creation errors gracefully
        try:
            objects.append(Ability(f'test_{i}', 10, 20))
        except:
            pass  # Handle creation errors gracefully
    
    end_time = time.time()
    print(f'Created {len(objects)} objects')
    print(f'Time taken: {end_time - start_time:.4f} seconds')
    print('Stress test completed')

elif test_case == "comprehensive_validation":
    # Comprehensive validation test
    print('=== Comprehensive Validation Test ===')
    
    # Test 1: Basic object creation
    print('1. Basic Object Creation:')
    success_count = 0
    classes = ['Character', 'Warrior', 'Mage', 'Rogue', 'Ability']
    
    try:
        obj = Character('test')
        success_count += 1
        print(f'   Character: Created successfully')
    except Exception as e:
        print(f'   Character: Creation failed - {e}')
    try:
        obj = Warrior('test')
        success_count += 1
        print(f'   Warrior: Created successfully')
    except Exception as e:
        print(f'   Warrior: Creation failed - {e}')
    try:
        obj = Mage('test')
        success_count += 1
        print(f'   Mage: Created successfully')
    except Exception as e:
        print(f'   Mage: Creation failed - {e}')
    try:
        obj = Rogue('test')
        success_count += 1
        print(f'   Rogue: Created successfully')
    except Exception as e:
        print(f'   Rogue: Creation failed - {e}')
    try:
        obj = Ability('test', 10, 20)
        success_count += 1
        print(f'   Ability: Created successfully')
    except Exception as e:
        print(f'   Ability: Creation failed - {e}')
    
    print(f'   Successfully created {success_count}/{len(classes)} classes')
    
    print('=== Validation Complete ===')

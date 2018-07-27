import random
class Character:
    def __init__ (self):

        self.name=""

        # Initializing Character "Stat" Attributes and Bonuses
        self.health = 0          # assign bonus stat with super after inheriting Character
        self.attackBonus = 0     # assign bonus stat with super after inheriting Character
        self.defenseBonus = 0    # assign bonus stat with super after inheriting Character
        self.movementSpeed = 2   # 2 squares / movement action
                                 # can overwrite to assign new movement speed after inheriting
        self.energyLevel = 10    # stat you can spend to perform special attacks
        self.status = "normal"   # can be changed to hold an status effects on character (ie. paralyzed, poisoned, ...)
        self.direction = "up"    # holds the direction a character is facing and changes based on movement action
        self.priority = 0

        # This is my interpretation of Riley's dictionary for character items
        self.items = {
            'weapon': {'name': "sword", 'statBonus': 0},
            'headArmor': {'name': "helmet", 'statBonus': 0},
            'bodyArmor': {'name': "chestPlate", 'statBonus': 0},
            'legArmor': {'name': "boots", 'statBonus': 0} }

        # Initilizing stats related to cards and position
        self.position = {  # holds the x and y coordinates of the character on the board grid
            'y': 0,
            'x': 0 }
        self.cards = {        # holds the unassigned cards of the character
            'card1': 10,
            'card2': 0,
            'card3': 0 }
        self.assignedCards = {  # holds the cards of the character after being assigned
            'defense': 0,
            'action1': 0,
            'action2': 0 }



    def move(self, newY, newX):
        self.position["y"] = newY
        self.position["x"] = newX
        return self

    def assignCards(self, cardChoice):
        for key in self.cards:
            if(key == cardChoice):
                self.assignedCards['defense'] = self.cards[key] + self.defenseBonus + self.items['headArmor']['statBonus'] + self.items['bodyArmor']['statBonus']+ self.items['legArmor']['statBonus']
            # for key2 in self.assignedCards:
            #     if(key2 != 'defense'):

        return self



    def attack(self, direction):

        print(self.cards[len(self.cards)-1])

    # def vigor(self):


    def displayInfo(self):
        print("Hand of cards:", self.cards)
        print("Attack Bonus: ", self.attackBonus)
        print("Defense Bonus:", self.defenseBonus)
        print("Health:       ", self.health)
        print("Position:     ", self.position)
        print("Energy Level: ", self.energyLevel)
        print("Status:       ", self.status)
        print("")
        return self

    def displayCards(self):
        print("unassigned cards:", self.cards)
        print("assigned cards:", self.assignedCards)
        print("")
        return self


# knight = Character()
# knight.displayCards().assignCards('card1').displayCards()


class Knight(Character):
    def __init__(self):
        super().__init__()
        self.name="Knight"
        self.health = 4  # assign bonus stat with super after inheriting Character
        self.attackBonus = 7  # assign bonus stat with super after inheriting Character
        self.defenseBonus = 5  # assign bonus stat with super after inheriting Character

        self.priority = 4

        self.items = {
            'weapon': {'name': "Broadsword", 'statBonus': 0},
            'headArmor': {'name': "Iron Helmet", 'statBonus': 0},
            'bodyArmor': {'name': "Iron ChestPlate", 'statBonus': 0},
            'legArmor': {'name': "Iron Boots", 'statBonus': 0}}

        self.assignedCards = {  # holds the unassigned cards of the character
            'defense': random.randint(1, 10),  # randomly assigned
            'action1': random.randint(1, 10),  # randomly assigned
            'action2': random.randint(1, 10)}  # randomly assigned

class Mage(Character):
    def __init__(self):
        super().__init__()
        self.name="Mage"
        self.health = 4  # assign bonus stat with super after inheriting Character
        self.attackBonus = 6  # assign bonus stat with super after inheriting Character
        self.defenseBonus = 4  # assign bonus stat with super after inheriting Character

        self.priority = 3

        self.items = {
            'weapon': {'name': "Staff", 'statBonus': 0},
            'headArmor': {'name': "Hood", 'statBonus': 0},
            'bodyArmor': {'name': "Robes", 'statBonus': 0},
            'legArmor': {'name': "Sandals", 'statBonus': 0}}

        self.assignedCards = {  # holds the unassigned cards of the character
            'defense': random.randint(1, 10),  # randomly assigned
            'action1': random.randint(1, 10),  # randomly assigned
            'action2': random.randint(1, 10)}  # randomly assigned

class Rogue(Character):
    def __init__(self):
        super().__init__()
        self.name="Rogue"
        self.health = 4  # assign bonus stat with super after inheriting Character
        self.attackBonus = 2  # assign bonus stat with super after inheriting Character
        self.defenseBonus = 3  # assign bonus stat with super after inheriting Character

        self.priority = 2

        self.items = {
            'weapon': {'name': "Knife", 'statBonus': 0},
            'headArmor': {'name': "Leather Helmet", 'statBonus': 0},
            'bodyArmor': {'name': "Leather ChestPlate", 'statBonus': 0},
            'legArmor': {'name': "Leather Boots", 'statBonus': 0}}

        self.assignedCards = {  # holds the unassigned cards of the character
            'defense': random.randint(1, 10),  # randomly assigned
            'action1': random.randint(1, 10),  # randomly assigned
            'action2': random.randint(1, 10)}  # randomly assigned

class Bard(Character):
    def __init__(self):
        super().__init__()
        self.name="Bard"
        self.health = 4  # assign bonus stat with super after inheriting Character
        self.attackBonus = 1  # assign bonus stat with super after inheriting Character
        self.defenseBonus = 7  # assign bonus stat with super after inheriting Character
        self.movementSpeed = 3

        self.priority = 1

        self.items = {
            'weapon': {'name': "Harp", 'statBonus': 0},
            'headArmor': {'name': "Cap", 'statBonus': 0},
            'bodyArmor': {'name': "Costume", 'statBonus': 0},
            'legArmor': {'name': "Noisy Shoes", 'statBonus': 0}}

        self.assignedCards = {  # holds the unassigned cards of the character
            'defense': random.randint(1, 10),  # randomly assigned
            'action1': random.randint(1, 10),  # randomly assigned
            'action2': random.randint(1, 10)}  # randomly assigned

# bard1 = Bard()
# bard1.displayInfo()

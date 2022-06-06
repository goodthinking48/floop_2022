class Character():
    
    enemies_defeated = set()

    # Create a character
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None
        self._owns = None
        
    @property
    def owns(self):
        return self._owns
    
    @owns.setter
    def owns(self, new_item):
        if type(new_item) is str:
            raise TypeError("should be either None, " +
                            "or an object of the Item class")
        self._owns = new_item
        
    # Describe this character
    def describe(self):
        print(self.name + " is here! " + self.description)
        if self._owns is not None:
            print(self.name + " is holding " + self._owns.short_description + ': ' +
                                               self._owns.description)

    # Talk to this character
    def talk(self):
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you.")

    # Fight with this character
    def fight(self, combat_item):
        print(self.name + " doesn't want to fight with you.")
        return True
    
    def rob(self):
        print("You don't want to rob " + self.name + ".")
        
    def give(self, gift):
        print(self.name + " doesn't want it.")
    
    
class Enemy(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self._weakness = None
        
    @property
    def weakness(self):
        return self._weakness
    
    @weakness.setter
    def weakness(self, new_weakness):
        if type(new_weakness) is not str and new_weakness is not None:
            raise TypeError("should be either None, " +
                            "or a string that is the name of an Item object")
        self._weakness = new_weakness
        
    def fight(self, combat_item):
        if combat_item == self._weakness:
            print("You fend " + self.name + " off with the " + combat_item )
            return True
        else:
            print(self.name + " crushes you, puny adventurer")
            return False
        
    def rob(self):
        if self._owns == None:
            print(self.name + "has nothing to steal.")
            return None
        else:
            print("You sneek behind " + self.name +
                  " and snatch the " + self._owns.name + ".")
            prize, self._owns = self._owns, None
            return prize
            
            
class Friend(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self._likes = None
        
    @property
    def likes(self):
        return self._likes
    
    @likes.setter
    def likes(self, new_likes):
        if type(new_likes) is not str and new_likes is not None:
            raise TypeError("should be either None, " +
                            "or a string that is the name of an Item object")
        self._likes = new_likes
        
    def give(self, gift):
        if gift == self._likes:
            print(self.name + " happily takes the " + gift + ".")
            return True
        else:
            print(self.name + " isn't interested in the " + gift + ".")
            return False
            
            
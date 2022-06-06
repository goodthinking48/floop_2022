from random import choice
from character import Enemy

dave = Enemy("Dave", "A smelly zombie")
dave.set_weakness("cheese")

dave.describe()
dave.talk()
for count in range(5):
    dave.set_conversation(choice(["Aaargh!", "Waaagh!", "Braaains!"]))
    dave.talk()
    
print("What will you fight with?")
fight_with = input()
dave.fight(fight_with)
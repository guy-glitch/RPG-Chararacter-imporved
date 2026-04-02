#Classes WG_CP2
from faker import FAKER as f
from faker.providers import DynamicProvider as dp
import random as r
#A faker dynamic provider that gets a class
class_provider = dp(provider_name="class_provider", elements=["Black Mage", "Warrior", "Thief", "White Mage"])
f.add_provider(class_provider)

#A faker dynamic provider that gives a species
species_provider = dp(provider_name="species provide", elements=["Human", "Dragonborn", "Halfling", "Elf", "Ogre", "Dwarf", "Tiefling"])
f.add_provider(species_provider)




#CLass data visulization

#Class statistical anilyzer

#Class random generator
class random_char():
    def __init__(self):
        self.name = f.name()
        self.clss = f.class_provider()
        self.species = f.species_provider
        self.level = r.randint(1,14)
        
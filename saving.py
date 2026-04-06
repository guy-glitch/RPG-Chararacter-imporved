#Classes WG_CP2
from faker import Faker as f
from faker.providers import DynamicProvider as dp
import random as r
from char_manager import *
import matplotlib as plt, numpy
from character_search import 
f  = f()
#A faker dynamic provider that gets a class
class_provider = dp(provider_name="class_provider", elements=["Black Mage", "Warrior", "Thief", "White Mage"])
f.add_provider(class_provider)

#A faker dynamic provider that gives a species
species_provider = dp(provider_name="species provide", elements=["Human", "Dragonborn", "Halfling", "Elf", "Ogre", "Dwarf", "Tiefling"])
f.add_provider(species_provider)

#A faker class for skills
skills_provider = dp(provider_name="skills provide", elements = ["Swordplay", "Archery", "Axe Mastery", "Shield Bash", "Dual Wielding","Polearm Proficiency", "Unarmed Combat", "Dagger Mastery", "Spear Technique","Throwing Axes", "Heavy Armor Training", "Light Armor Training", "Evasion","Counterattack", "Parry", "Disarm", "Critical Strike", "Power Attack","Precise Strike", "Berserker Rage", "Command Tactics", "Intimidation","Battle Cry", "Mounted Combat", "Jousting", "Weapon Maintenance","Anatomy Lore", "Vital Spot Targeting", "Grappling", "Tumbling","Endurance","Unstoppable", "Sweep Attack", "Deflect Missiles","Dual-Wield Proficiency", "Crossbow Expert", "Sling Mastery","Battlefield Navigation", "Shield Wall", "Taunt", "Reckless Abandon","Guard", "Weapon Finesse", "Armor Proficiency", "Battle Focus","Executioner", "Shatter Armor", "Duelist", "Longbow Specialist","Savage Strike","Fireball Casting", "Ice Shield", "Lightning Bolt", "Telekinesis","Illusion Magic", "Necromancy", "Arcane Knowledge", "Runesmithing","Mana Manipulation", "Spellcraft", "Divination", "Teleportation","Elemental Binding", "Summoning", "Alchemy", "Potion Brewing","Arcane Reading", "Counterspell", "Mana Shield", "Invisibility","Levitation", "Mind Reading", "Enchanting", "Scroll Writing","Necrotic Touch", "Healing Light", "Frostbolt", "Fire Shield","Lightning Storm", "Telepathic Bond", "Illusionary Form", "Spirit Binding","Arcane Ward", "Rune Casting", "Mana Burn", "Spell Reflection","Astral Projection", "Mind Control", "Summon Familiar", "Arcane Sight","Identify Magic", "Spell Synergy", "Elemental Mastery", "Necromantic Lore","Illusionary Terrain", "Teleportation Circle", "Mana Regeneration","Arcane Blast", "Counter-Magic", "Rune Crafting","Sneaking", "Pickpocketing", "Lockpicking", "Disarm Traps", "Poison Crafting","Backstab", "Hide in Shadows", "Silent Move", "Appraise Value","Streetwise", "Scouting", "Camouflage", "Escape Artist", "Forgery","Disguise", "Climbing", "Acrobatics", "Slight of Hand", "Streetwise Knowledge","Trap Detection", "Surveillance", "Locksmithing", "Poison Application","Garrote Attack", "Shadow Step", "Pickpocket Proficiency", "Lockpick Mastery","Disarm Mastery", "Camouflage Expert", "Escape Technique", "Forgery Expert","Disguise Specialist", "Climb Speed", "Acrobatics Mastery", "Trap Disabling","Scouting Expert", "Shadow Camouflage", "Silent Footsteps", "Backstab Expert","Poisoner", "Street Smarts", "Stealthy Move", "Surveillance Expert","Escape Ability", "Forgery Skill", "Disguise Art", "Climbing Technique","Trap Detection Skill", "Pickpocket Technique", "Sneak Attack","Healing Prayer", "Resurrection", "Bless", "Curse Removal","Holy Smite", "Divine Intervention", "Faith Knowledge", "Channel Energy","Purify", "Holy Shield", "Light Manipulation", "Prayer", "Spirit Communication","Divine Aura", "Cure Disease", "Holy Touch", "Spirit Summoning","Holy Protection", "Divine Sight", "Healing Touch", "Resurrection Mastery","Blessing", "Curse Removal Skill", "Holy Smite Technique", "Divine Intervention Skill","Faithful", "Channel Energy Mastery", "Purification", "Holy Shield Proficiency","Light Manipulation Ability", "Prayer Mastery", "Spirit Communication Skill","Divine Aura Mastery", "Cure Disease Mastery", "Holy Touch Mastery","Spirit Summoning Ability", "Holy Protection Skill", "Divine Sight Mastery","Healing Technique", "Resurrection Ability", "Blessing Proficiency","Curse Removal Mastery", "Holy Smite Mastery", "Divine Intervention Mastery","Faithful Knowledge", "Channel Energy Proficiency", "Purification Mastery","Holy Shield Mastery", "Light Manipulation Mastery", "Prayer Proficiency","Animal Handling", "Foraging", "Tracking", "Plant Lore","Weather Prediction", "Shapechanging", "Nature's Embrace", "Animal Training","Herbalism", "Climbing", "Swim", "Nature Knowledge", "Animal Empathy","Forage Mastery", "Tracker", "Plant Lore Mastery", "Weather Mastery","Shapechange Ability", "Nature's Embrace Skill", "Animal Handling Mastery","Herbalist", "Climbing Mastery", "Swim Skill", "Nature Knowledge Mastery","Animal Empathy Mastery", "Forage Expert", "Tracking Ability","Plant Lore Expert", "Weather Prediction Ability", "Shapechange Mastery","Nature's Embrace Mastery", "Animal Handling Expert", "Herbalist Expert","Climbing Technique", "Swim Technique", "Nature Knowledge Expert","Animal Empathy Expert", "Forage Expert", "Tracking Technique","Plant Lore Mastery", "Weather Prediction Expertise", "Shapechange Expert","Nature's Embrace Knowledge", "Animal Handling Technique", "Herbalist Technique","Climbing Ability", "Swim Ability", "Nature Knowledge Technique","Animal Empathy Skill", "Foraging Technique","Blacksmithing", "Leatherworking", "Tailoring", "Jewelry Making","Woodworking", "Cooking", "Fishing", "Mining", "Farming", "Merchant","Bargaining", "Appraise Value", "Blacksmithing Mastery", "Leatherworking Mastery","Tailoring Mastery", "Jewelry Making Mastery", "Woodworking Mastery","Cooking Mastery", "Fishing Mastery", "Mining Mastery", "Farming Mastery","Merchant Mastery", "Bargaining Mastery", "Appraise Value Mastery","Blacksmithing Technique", "Leatherworking Technique", "Tailoring Technique","Jewelry Making Technique", "Woodworking Technique", "Cooking Technique","Fishing Technique", "Mining Technique", "Farming Technique","Merchant Technique", "Bargaining Technique", "Appraise Value Technique","Blacksmithing Expert", "Leatherworking Expert", "Tailoring Expert","Jewelry Making Expert", "Woodworking Expert", "Cooking Expert","Fishing Expert", "Mining Expert", "Farming Expert", "Merchant Expert","Bargaining Expert", "Appraise Value Expert", "Crafting", "Trade","Navigation", "Survival", "History Knowledge", "Language","Diplomacy", "Sailing", "Riding", "Flying", "Swimming", "Climbing","Running", "Tumbling", "Grappling", "Lockpicking", "Forgery","Disarming Traps", "Pickpocketing", "Blacksmithing", "Crafting", "Alchemy","Haggling", "Sneaking", "Tinker", "Hunting", "Foraging", "Fishing","Navigation Mastery", "Survival Skill", "History Knowledge Mastery","Language Mastery", "Diplomacy Mastery", "Sailing Mastery", "Riding Mastery","Flying Mastery", "Swimming Mastery", "Climbing Mastery", "Running Mastery","Tumbling Mastery", "Grappling Mastery", "Lockpicking Mastery", "Forgery Mastery","Disarming Traps Mastery", "Pickpocketing Mastery", "Blacksmithing Mastery","Crafting Mastery", "Alchemy Mastery", "Haggling Mastery", "Sneaking Mastery","Tinker Mastery", "Hunting Mastery"])
f.add_provider(skills_provider)

#A class that is the character
class char():
    def __init__(self,name,level,clss,species,attributes,skills):
        self.name = name
        self.level = level
        self.clss = clss
        self.species = species
        self.attributes = attributes
        self.skills = skills

def graphs(characters):


#class DataVisualization
class DataVisualization:
    #initiate: character, optional second character
    def __init__(self, character, optional = None):
        #character is a dictionary of all the character's info
        self.character = character
        #optional is an optional second character for comparing
        self.char_two = optional
    #display
    def display(self):
        #set up the graph
        #set the catigories to the attributes
        categories = ['MP', 'HP', 'Str', 'Atk', 'Def', 'Mag', 'Spr', 'Acc', 'Spd', 'Evs']
        #get the info for the character and input it as the values for the catigories
        values = [self.character.get("MP"),self.character.get("HP"), self.character.get("Str"),self.character.get("Atk"),self.character.get("Def"),self.character.get("Mag"),self.character.get("Spr"),self.character.get("Acc"),self.character.get("Spd"),self.character.get("Evs")]
        #display the graph
        plt.bar(categories, values)
        plt.ylabel("Level")
        plt.title("Attribute Levels")
        plt.show()

#Class random generator
class random_char():
    def __init__(self):
        self.name = f.name()
        self.clss = f.class_provider()
        self.species = f.species_provider
        self.level = r.randint(1,14)
        self.attributes = get_stats_for_class(self.clss, self.level)
        self.skill1 = f.skills_provider()
        self.skill2 = f.skills_provider()
        self.skill3 = f.skills_provider()
        self.skill4 = f.skills_provider()

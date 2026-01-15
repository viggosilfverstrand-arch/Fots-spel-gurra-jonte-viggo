from items import *
import random as rand
import time

def slowtype(text, tid):
    for a in text:
        print(a, end="", flush=True)   # End hindrar nyrad,    flush låter termineln skriva ut induviduella tecken innan hela raden är klar
        time.sleep(tid)
    print("\n")

class Characterclass():
    def __init__(self, name, hp, str, critrate, crit_damage):
        self.name = name
        self.pname = None
        self.hp = hp
        self.str = str
        self.lvl = 1
        self.exp = 0
        self.money = 0
        self.crit_damage = crit_damage
        self.critrate = critrate
        self.weapon = None
        self.alive = True
        self.hybris= False
        self.skog = False
        self.grott = False
        self.city = False

        self.inventory = []

    def exp_required(self):
        return int(20 * (1.5 ** (self.lvl - 1)))    # Switcha denna för mer balnce och jämnare tal vi lvl ups

    def level_up(self):
        self.lvl += 1
        newstr = self.str * 1.10
        self.str = round(newstr)
        newhp = self.hp * 1.10
        self.hp = round(newhp)
        slowtype(f"{self.name} levla upp till {self.lvl}!",.05)
        slowtype(f"Din bas skada {self.str}", 0.05)

    def add_exp(self, reward):
        self.exp += reward
        while self.exp >= self.exp_required():
            self.exp -= self.exp_required()
            self.level_up()
    
    def amoney(self, belopp):
        self.money += belopp
        slowtype(f"Du har nu {self.money} pengar",0.05)
        


# INVENTORY
    def add_item(self, item):
        self.inventory.append(item)
        slowtype(f"Du plockade upp: {item.name}",0.05)

    def show_inventory(self):
        if not self.inventory:
            slowtype("Inventory är tomt.", 0.05)
            return

        slowtype("\n--- INVENTORY ---",0.01)
        for i, item in enumerate(self.inventory, start=1):
            slowtype(f"{i}. {item.name} (+{item.health_boost} HP, *{item.damage_boost} DMG)",0.01)
        slowtype("------------------\n",0.01)
    
    def show_weapon(self):
        slowtype(f"Ditt vapen är {self.weapon.name}",0.05)

    def use_item(self, item_name):
        for item in self.inventory:
            if item.name.lower() == item_name.lower():
                self.hp += item.health_boost
                self.str *= item.damage_boost
                slowtype(f"Du använde {item.name}!",0.05)
                slowtype(f"Ny HP: {self.hp}, Ny DMG: {self.str}",0.05)
                self.inventory.remove(item)

                return
        slowtype("Du har inte det föremålet!",0.05)
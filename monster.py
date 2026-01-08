import random as rand
class Monster():
    def __init__(self, name, hp, dmg, lvl): 
        self.lvl = lvl
        self.hp = hp*(1+self.lvl/5)
        self.dmg = dmg*(1+self.lvl/5)
        self.name = name

    def exp_reward(self):
        return rand.randint(10,35)
    
    def money_reward(self):
        return rand.randint(5, 15)
import random as rand
class Monster():
    def __init__(self, name, hp, dmg, crit_damage): 
        self.crit_damage = crit_damage
        self.hp = hp
        self.dmg = dmg
        self.name = name

    def exp_reward(self):
        return rand.randint(10,35)
    
    def money_reward(self):
        return rand.randint(5, 15)
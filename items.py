class Weapon():
    def __init__(self, name, damage, critrate, crit_damage):
        self.name = name
        self.damage = damage
        self.critrate = critrate
        self.crit_damage = crit_damage


class Item():
    def __init__(self, name, health_boost, damage_boost):
        self.health_boost = health_boost
        self.damage_boost = damage_boost
        self.name = name
    

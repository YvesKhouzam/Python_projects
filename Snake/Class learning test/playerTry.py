
class Player:
    def __init__(self, pseudo, health, weapon):
        self.force = 0
        self.pseudo = pseudo
        self.health = health
        self.weapon = weapon

      #  self.force += self.weapon.get_damage()

    def get_pseudo(self):
        return self.pseudo

    def get_health(self):
        return self.health

    def get_weapon(self):
        return self.weapon

    def damage(self, damage):
        self.health -= damage

    def get_force(self):
        damage = self.force
        self.weapon = "gun"
        damage += self.weapon.get_damage_amount()
        return self.force

    def attack_player(self, target_player):
        damage = self.force
        # target_player.damage(damage)
        print(self.get_pseudo(), "attaque", target_player.get_pseudo(), ".")
        print("Aie !", target_player.get_pseudo(), "vous venez de subir", self.weapon, "dégats !")
        print(target_player.get_pseudo(), "votre santé est maintenant à", target_player.get_health(), ".")
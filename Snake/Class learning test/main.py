from player import Player
from weapon import Weapon

# défini une instance de la classe weapon
knife = Weapon("Couteau", 4)
sword = Weapon("Épée", 5)

# défini une instance de la classe player
player1 = Player("Graven", 20, 3)
player2 = Player("Bob", 20, 5)

# utilise une méthode(def) de la classe(class) Player qui modifie un attribue d'une instance de cette classe.
player1.set_weapon(knife)


# Utilise une méthode de la classe player qui modifie
player1.attack_player(player2)
print(player1.get_pseudo(), "attaque", player2.get_pseudo())

print("Bienvenue au joueur", player1.get_pseudo(), "/ Points de vie:", player1.get_health(), "/ Attaque:",
      player1.get_attack_value())
print("Bienvenue au joueur", player2.get_pseudo(), "/ Points de vie:", player2.get_health(), "/ Attaque:",
      player2.get_attack_value())

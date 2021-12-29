from player import *
from resources.weapon import Weapon

knife = Weapon("Couteau", 3)
gun = Weapon("Fusil", 6)
sword = Weapon("Épée", 5)

player1 = Player("Nathan", 18, "Knife")
player2 = Player("Laurie", 20, "Gun")
print("Bienvenue au joueur", player1.pseudo, "ta santé est à", player1.health, "et ta force est de", player1.weapon, ".")
print("Bienvenue au joueur", player2.pseudo, "ta santé est à", player2.health, "et ta force est de", player2.weapon, ".")

# player1.attack_player(player2)
# player2.attack_player(player1)

weapon = player1.get_weapon()

print(player1.get_force())


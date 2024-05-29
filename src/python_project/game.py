from model.player import Player
from model.weapon import Weapon

knife = Weapon("knife", 3)
player1 = Player("Max", 20, 3)

# give attack weapon to player1
player1.set_weapon(knife)
player2 = Player("Lando", 20, 5)

player1.attack_player(player2)
print(player1.get_pseudo(), "attack", player2.get_pseudo())

print("Welcome player", player1.get_pseudo(), "/ Life :", player1.get_health(), "/ attack:", player1.get_attack_value())
print("Welcome player", player2.get_pseudo(), "/ Life :", player2.get_health(), "/ attack:", player2.get_attack_value())

class Player:

    def __init__(self, pseudo, health, attack):
        self.pseudo = pseudo
        self.health = health
        self.attack = attack
        print("Welcome to the player", pseudo, "with", health, "health points and", attack, "attack points")

    def get_pseudo(self):
        return self.pseudo

    def get_health(self):
        return self.health

    def get_attack_value(self):
        return self.attack

    def damage(self, damage):
        self.health -= damage

    def attack_player(self, target_player):
        target_player.damage(self.attack)


player = Player("Max", 20, 3)
player.damage(3)

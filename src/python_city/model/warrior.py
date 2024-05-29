import python_city.model.player as player


class Warrior(player.Player):

    def __init__(self, pseudo, health, attack):
        super().__init__(pseudo, health, attack)
        self.armor = 3
        print("Welcome to the warrior", pseudo, "with", health, "health points and", attack, "attack points")

    def damage(self, damage):
        if self.armor > 0:
            self.armor -= 1
            damage = 0
        super().damage(damage)

    def attack_player(self, target_player):
        target_player.damage(self.attack)

    def blade(self):
        self.armor = 3
        print("Point of armor restored")

    def get_armor_point(self):
        return self.armor


warrior = Warrior("DarkMax", 30, 4)
warrior.damage(4)
print("life of the warrior", warrior.get_health(), "\nArmor point of the warrior :", warrior.get_armor_point())

if issubclass(Warrior, player.Player):
    print("The warrior class is a subclass of the player class")
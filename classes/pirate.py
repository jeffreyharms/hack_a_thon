from classes.ninja import Ninja


class Pirate:

    def __init__( self , name ):
        self.name = name
        self.strength = 15
        self.speed = 3
        self.health = 100
        self.parrot = 2
        self.health_potions = 2
        self.scurvy = 3

    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack ( self , ninja ):
        Ninja.health -= self.strength
        return self

def use_item(self, ninja):
        choice = " "
        print("-------------------Items-------------------")
        print(f"1 -> Parrot = {self.parrot} : Deals 15dmg")
        print(f"2 -> Health Potion = {self.health_potions} : Heals 25hp")
        print(f"3 -> Scurvy Bite = {self.scurvy} : Enemy loses 2 strength points")
        choice = input("Enter the corresponding number to use item: ")

        if choice == "1":
            if self.parrot > 0:
                self.parrot -= 1
                Ninja.health -= 10
                print(f"\n{self.name} uses a macaw!")
                print(f"{ninja.name}'s health: {ninja.health}")
            else:
                print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
                print("Not enough avian friends!")
                print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
                self.use_item(ninja)
        elif choice == "2":
            if self.health_potions > 0:
                self.health_potions -= 1
                self.health += 25
                print(f"\n{self.name} uses a health potion")
                print(f"{self.name}'s health has increased: {self.health}")
            else:
                print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
                print("Not enough health potions")
                print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
                self.use_item(ninja)
        elif choice == "3":
            if self.scurvy > 0:
                self.scurvy -= 1
                Ninja.strength -= 2
                print(f"\n{self.name} uses Scurvy Bite")
                print(f"{Ninja.name}'s strength: {Ninja.strength}")
            else:
                print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
                print("Not enough teeth left!")
                print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
                self.use_item(ninja)
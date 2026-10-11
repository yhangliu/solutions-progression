class SuperHero:
    """
    A class to represent a superhero.

    Attributes:
        name (str): The superhero's name
        power (str): The superhero's main superpower
        health (int): The superhero's health points
    """

    def __init__(self, name: str, power: str, health: int):
        self.name = name
        self.power = power
        self.health = health
    def display_info(self):
        print(self.name)
        print(self.power)
        print(self.health)

# TODO: Create Superhero instances
hero_1 = SuperHero("Batman", "Intelligence", 100)
hero_2 = SuperHero("Superman", "Strength", 150)


# TODO: Print out the attributes of each superhero

hero_1.display_info()
hero_2.display_info()

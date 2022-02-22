class Ninja:

    def __init__( self , name ):
        self.name = name
        self.strength = 10
        self.speed = 5
        self.health = 100
    
    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack( self , pirate ):
        pirate.health -= (self.strength +(self.speed*0.75))
        return self

    def special_attack( self , pirate ):
        print(f"{self.name} ducks and throws shuriken at the {pirate.name}")
        pirate.health -= (self.strength -(self.speed*0.25))
        return self
    
    def buff(self):
        print(f'{self.name} steps back and drinks a potion')
        self.health += 5

    def special_buff(self):
        print(f'{self.name} sits down and has a ramen')
        self.health += 15
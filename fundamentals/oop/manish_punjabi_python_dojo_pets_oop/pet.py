class Pet:
    # implement __init__( name , type , tricks )
    def __init__ (self, name, type, tricks, noise,):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.noise = noise
        self.health = 0
        self.energy = 0
    # sleep() - increases the pets energy by 25
    def sleep(self):
        self.health  += 25
    # eat() - increases the pet's energy by 5 & health by 10def eat(self):
    def eat(self):
        self.energy += 5
        self.health += 10
    # play() - increases the pet's health by 5
    def play(self):
        self.health +=5
    # noise() - prints out the pet's sound
    def make_noise(self):
        print(self.noise)


class TherapyPet(Pet):
    def comfort(self):
        self.make_noise()
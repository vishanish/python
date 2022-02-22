from classes.ninja import Ninja
from classes.pirate import Pirate
import random

michelangelo = Ninja("Michelanglo")

jack_sparrow = Pirate("Jack Sparrow")



ninjachoose = ['attacks', 'buffs']
ninjachoice = random.choice(ninjachoose)
ninjaattacks = ['attack', 'special_attack']
ninjabuff = ['buff', 'special_buff']
ninjaattackchoice = random.choice(ninjaattacks)
ninjabuffchoice = random.choice(ninjabuff)

if (ninjachoice == 'attacks'):
    if(ninjaattackchoice == 'special_attack'):
        michelangelo.special_attack(jack_sparrow)
    else:
        michelangelo.attack(jack_sparrow)

if (ninjachoice = 'buffs'):
    if(ninjabuffchoice == 'special_buff'):
        michelangelo.special_buff()
    else:
        michelangelo.buff()


# jack_sparrow.show_stats()
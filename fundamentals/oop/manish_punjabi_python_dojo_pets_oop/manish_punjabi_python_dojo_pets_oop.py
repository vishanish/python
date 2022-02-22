from pet import Pet,TherapyPet
from ninja import Ninja

guido = Ninja('Manish', 'Punjabi', 'fish', 'kibble', TherapyPet('dog', 'dog', 'tricks','bark'))
guido.feed()
guido.walk()
guido.bathe()
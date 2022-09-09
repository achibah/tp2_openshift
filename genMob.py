import random

def genMob(Nom):
    PV = random.randint(5, 20)
    Force = random.randint(3, 8)
    Armure = random.randint(0, 5)
    monmonstre = [Nom, PV, Force, Armure]
    return monmonstre

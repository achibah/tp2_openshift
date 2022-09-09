from gestDegats import *


def fight(Joueur, Monstre):
    
    while(Joueur[1] >= 0 and Monstre[1] >= 0):
        Monstre[1] = gestDegats(Monstre[1], Joueur[2], Monstre[3])
        print(f"Le joueur {Joueur[0]} attaque : Il reste au monstre {Monstre[0]} {Monstre[1]} points de vie")
        if (Monstre[1] >= 0):
            Joueur[1] = gestDegats(Joueur[1], Monstre[2], Joueur[3])
            print(f"{Monstre[0]} attaque : Il reste à {Joueur[0]} {Joueur[1]} points de vie")
    if(Joueur[1] > 0):
        print(f"Le joueur a vaincu le terrible {Monstre[0]}!")
    return Joueur

    
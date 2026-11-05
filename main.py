import random


def afficher_regles():
    print("\n===== RÈGLES DU JEU =====")
    print("Vous commencez avec 20 points de vie.")
    print("À chaque tour, un monstre apparaît.")
    print("Vous pouvez combattre ou éviter le monstre.")
    print("Si vous survivez jusqu'au tour 10, vous gagnez.")
    print("La partie est perdue si vos PV tombent à 0 ou moins.")
    print("=========================\n")


def afficher_etat(pv, tour):
    print(f"\n----- TOUR {tour} -----")
    print(f"Points de vie : {pv}")


def combattre(pv):
    force_monstre = random.randint(1, 8)

    print(f"Le monstre a une force de {force_monstre}.")

    victoire = random.choice([True, False])

    if victoire:
        gain = random.randint(1, 3)
        pv += gain
        print(f"Victoire ! Vous gagnez {gain} PV.")
    else:
        pv -= force_monstre
        print(f"Défaite ! Vous perdez {force_monstre} PV.")

    return pv, victoire


def eviter(pv):
    penalite = 2
    pv -= penalite

    print("Vous évitez le monstre.")
    print(f"Vous perdez {penalite} PV.")

    return pv


pv_hero = 20
tour = 1

monstres_vaincus = 0
monstres_evites = 0
defaites = 0

noms_monstres = [
    "Gobelin",
    "Loup",
    "Dragon",
    "Orc",
    "Squelette",
    "Troll"
]

afficher_regles()

while pv_hero > 0 and tour <= 10:

    afficher_etat(pv_hero, tour)

    monstre = random.choice(noms_monstres)
    print(f"Un {monstre} apparaît !")

    choix = input(
        "Choisissez : combattre / éviter / règles : "
    ).lower()

    if choix == "combattre":

        pv_hero, victoire = combattre(pv_hero)

        if victoire:
            monstres_vaincus += 1
        else:
            defaites += 1

        tour += 1

    elif choix == "éviter":

        pv_hero = eviter(pv_hero)
        monstres_evites += 1
        tour += 1

    elif choix == "règles":

        afficher_regles()

    else:

        print("Choix invalide. Essayez de nouveau.")


print("\n===== FIN DE PARTIE =====")

if pv_hero > 0:
    print("VICTOIRE ! Vous avez survécu aux 10 tours.")
else:
    print("DÉFAITE ! Vous n'avez plus de points de vie.")

print(f"\nPoints de vie restants : {pv_hero}")
print(f"Monstres vaincus : {monstres_vaincus}")
print(f"Monstres évités : {monstres_evites}")
print(f"Défaites contre un monstre : {defaites}")
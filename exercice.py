#!/usr/bin/env python
# -*- coding: utf-8 -*-
def majuscule(mot):
    distance ebntre min et maj = 32
    resultat = ''
    for lettre in mot:
        # TODO completer la fonction ici
        lettre= ord(lettre)-32
        resultat += chr(lettre)
    return resultat


if __name__ == '__main__':
    mots = [
        'riz',
        'cours',
        'voiture',
        'oiseau',
        'bonjour',
        'églantier',
        'arbre'
    ]
    for i in range(len(mots)):
        mots[i] = majuscule(mots[i])

    print(mots)

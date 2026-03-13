# intervals.py
# -*- coding: utf-8 -*-
# vicenté quantic cabviva

from typing import List, Tuple, Dict

# Notes naturelles
NOTES = ["C", "D", "E", "F", "G", "A", "B"]

# Signes d'altération
SIG_NOT = ["", "+", "x", "^", "+^", "x^", "o*", "-*", "*", "o", "-"]

# Intervalles de la gamme majeure
INT_MAJ = (2, 2, 1, 2, 2, 2, 1)


class Mode:
    """Représente un mode diatonique défini par une suite de SEPT intervalles."""

    def __init__(self, intervalles: Tuple[int, ...]):
        self.intervalles = intervalles

    def renversements(self) -> List[Tuple[int, ...]]:
        """Retourne les SEPT renversements diatoniques du mode."""
        return [
            self.intervalles[-i:] + self.intervalles[:-i]
            for i in range(len(self.intervalles))
        ]

    def gammes_alterees(self) -> List[List[Tuple[str, str]]]:
        """Construit les SEPT gammes altérées correspondant aux renversements."""
        gammes = []

        for mod_rang in self.renversements():
            im = [(0, "C")]
            cum_m = cum_g = 0

            for y in range(6):
                cum_m += INT_MAJ[y]
                cum_g += mod_rang[y]
                res_mg = cum_g - cum_m
                sig_mg = SIG_NOT[res_mg]
                im.append((sig_mg, NOTES[y + 1]))

            gammes.append(im)

        return gammes


class SystemeIntervalles:
    """Gère l'ensemble des modes Grok et génère toutes les gammes altérées."""

    def __init__(self, base_intervalles: Dict[int, Tuple[int, ...]]):
        self.base = base_intervalles
        self.modes = {k: Mode(v) for k, v in base_intervalles.items()}

    def generer_gammes(self):
        """Construit gam_notes et dic_rang comme dans ton code original."""
        gam_notes = {}
        dic_rang = {}

        for key, mode in self.modes.items():
            dic_rang[key] = mode.renversements()
            gam_notes[(key, mode.intervalles)] = mode.gammes_alterees()

        return gam_notes, dic_rang

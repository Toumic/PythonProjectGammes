# gravitation.py
# -*- coding: utf-8 -*-
# vicente quantic cabviva

from typing import List, Tuple, Dict


class Poids:
    """
    Calcule les poids gravitationnels d'une gamme :
    - poids absolu (pa)
    - poids signe (pg)
    - poids des forces
    - poids des effets
    """

    def __init__(self):
        self.poids_forces_pg = 0
        self.poids_forces_pa = 0
        self.poids_effets_pg = 0
        self.poids_effets_pa = 0

    # ------------------------------------------------------------------
    # Conversion d'un degre + alteration en valeur gravitationnelle
    # ------------------------------------------------------------------
    @staticmethod
    def valeur_gravitationnelle(degre: int, alteration: int) -> int:
        """
        Retourne la valeur gravitationnelle d'un degre.
        alteration < 0 => signe négatif
        """
        if alteration < 0:
            degre = -degre
        return degre + alteration

    # ------------------------------------------------------------------
    # Ajout d'une force
    # ------------------------------------------------------------------
    def ajouter_force(self, degre: int, alteration: int):
        val = self.valeur_gravitationnelle(degre, alteration)
        self.poids_forces_pg += val
        self.poids_forces_pa += abs(val)

    # ------------------------------------------------------------------
    # Ajout d'un effet
    # ------------------------------------------------------------------
    def ajouter_effet(self, degre: int, alteration: int):
        val = self.valeur_gravitationnelle(degre, alteration)
        self.poids_effets_pg += val
        self.poids_effets_pa += abs(val)

    # ------------------------------------------------------------------
    # Export
    # ------------------------------------------------------------------
    def exporter(self) -> Dict[str, int]:
        return {
            "FOR_PG": self.poids_forces_pg,
            "FOR_PA": self.poids_forces_pa,
            "EFF_PG": self.poids_effets_pg,
            "EFF_PA": self.poids_effets_pa,
        }


class GravitationSystem:
    """
    Gere le dictionnaire des poids gravitationnels pour toutes les gammes.
    dic_poids[(mode_intervalles, clef_mode)] = {"FORT": [...], "EFFET": [...]}
    """

    def __init__(self):
        self.dic_poids: Dict[Tuple[Tuple[int, ...], int], Dict[str, List[int]]] = {}

    # ------------------------------------------------------------------
    # Enregistrement d'un poids de force
    # ------------------------------------------------------------------
    def enregistrer_force(self, clef: Tuple[Tuple[int, ...], int], valeur_pg: int):
        if clef not in self.dic_poids:
            self.dic_poids[clef] = {"FORT": [], "EFFET": []}
        self.dic_poids[clef]["FORT"].append(valeur_pg)

    # ------------------------------------------------------------------
    # Enregistrement d'un poids d'effet
    # ------------------------------------------------------------------
    def enregistrer_effet(self, clef: Tuple[Tuple[int, ...], int], valeur_pg: int):
        if clef not in self.dic_poids:
            self.dic_poids[clef] = {"FORT": [], "EFFET": []}
        self.dic_poids[clef]["EFFET"].append(valeur_pg)

    # ------------------------------------------------------------------
    # Export global
    # ------------------------------------------------------------------
    def exporter(self) -> Dict:
        return self.dic_poids

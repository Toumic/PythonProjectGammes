# signatures.py
# -*- coding: utf-8 -*-
# vicente quantic cabviva

from typing import Dict, Tuple, List
from .intervals import SystemeIntervalles
# from .alterations import AnalyseAlterations
from .notes import SIG_NOT


class SignatureSystem:
    """
    Reconstruit les signatures modales (dic_sig) a partir des gammes altérées.
    """

    def __init__(self, base_intervalles: Dict[int, Tuple[int, ...]]):
        self.systeme = SystemeIntervalles(base_intervalles)

        # Structures finales
        self.gam_notes: Dict[Tuple[int, Tuple[int, ...]], List[List[Tuple[str, str]]]] = {}
        self.dic_rang: Dict[int, List[Tuple[int, ...]]] = {}
        self.dic_sig: Dict[Tuple[int, ...], List[List[Tuple[int, int]]]] = {}

    # ----------------------------------------------------------------------
    # Construction des gammes et renversements
    # ----------------------------------------------------------------------
    def construire_gammes(self):
        gam_notes, dic_rang = self.systeme.generer_gammes()
        self.gam_notes = gam_notes
        self.dic_rang = dic_rang

    # ----------------------------------------------------------------------
    # Construction de dic_sig (signatures modales)
    # ----------------------------------------------------------------------
    def construire_signatures(self):
        """
        dic_sig[k_sig] = liste des SEPT signatures correspondant aux SEPT renversements.
        Chaque signature est une liste de tuples (degre, indice_alteration).
        """

        for (key, intervalles), gammes in self.gam_notes.items():
            k_sig = intervalles
            self.dic_sig[k_sig] = []

            for gamme in gammes:
                # gamme = [(sig, note), ...] sur 7 elements
                lis_sig = []
                deg = 0

                for sig, _note in gamme:
                    deg += 1

                    # Conversion du signe en indice
                    if sig == 0:
                        sig = ""

                    if sig in SIG_NOT[6:]:
                        ind_sig = SIG_NOT.index(sig) - len(SIG_NOT)
                    else:
                        ind_sig = SIG_NOT.index(sig)

                    lis_sig.append((deg, ind_sig))

                self.dic_sig[k_sig].append(lis_sig)

    # ----------------------------------------------------------------------
    # API principale
    # ----------------------------------------------------------------------
    def analyser(self):
        """
        Construit gam_notes, dic_rang, dic_sig.
        Retourne un dictionnaire complet des signatures.
        """
        self.construire_gammes()
        self.construire_signatures()
        return self.dic_sig

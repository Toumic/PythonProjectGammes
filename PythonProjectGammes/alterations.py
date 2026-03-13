# alterations.py
# -*- coding: utf-8 -*-
# vicenté quantic cabviva

from typing import List, Tuple, Dict
from .notes import SIG_NOT


# Dictionnaire des forces altéractives (inchangé)
ALTERACTIONS: Dict[int, List[List[str]]] = {
    2: [["x2", "+3", "+4"], ["^2", "x3", "x4", "+5"], ["+^2", "^3", "^4", "x5", "+6"]],
    3: [["+3", "+4"], ["x3", "x4", "+5"], ["^3", "^4", "x5", "+6"], ["o3", "-2"]],
    4: [["x4", "+5"], ["^4", "x5", "+6"], ["o4", "o3", "-2"], ["-4", "-3"]],
    5: [["x5", "+6"], ["o5", "-4", "-3"], ["*5", "o4", "o3", "-2"]],
    6: [["o6", "-5"], ["*6", "o5", "-4", "-3"], ["-*6", "*5", "o4", "o3", "-2"]],
    7: [["o7", "-6"], ["*7", "o6", "-5"], ["-*7", "*6", "o5", "-4", "-3"], ["o*7", "-*6", "*5", "o4", "o3", "-2"]],
}


class AnalyseAlterations:
    """
    Analyse les altérations d'une gamme :
    - forces altéractives
    - effets altéractifs
    - degrés significatifs
    """

    def __init__(self, don: List[Tuple[int, int]]):
        """
        don = liste de tuples (degré, indice_altération)
        Exemple : [(1,0), (2,-1), (3,-2), ...]
        """
        self.don = don
        self.don_deg = [SIG_NOT[d[1]] + str(d[0]) for d in don]

        self.sig_liste: List[str] = []
        self.sec_liste: List[str] = []

    # -------------------------------------------------------------------------
    # Étape 1 : Collecte brute des altérations (forces + effets)
    # -------------------------------------------------------------------------
    def _collecter_alterations(self):
        for deg, ind in self.don:
            if deg == 1:
                continue  # On passe la tonique

            sig = SIG_NOT[ind]
            loc = sig + str(deg)

            # VD (degré, altération)
            # Signe, Tuple, Loc
            # (commentaires conservés)
            # print(lineno(), "VD", (deg, ind), "Signe", sig, "Tuple", (sig, deg), "Loc", loc)

            # Rechercher dans ALTERACTIONS
            for va in ALTERACTIONS[deg]:
                # print(lineno(), deg, "VA", va, len(ALTERACTIONS[deg]))

                if loc == va[0]:
                    for lv in va:
                        if lv not in self.sig_liste:
                            # C'est ici que se rétablissent les limites des effets enregistrés.
                            self.sig_liste.append(lv)

                        if loc not in self.sec_liste:
                            self.sec_liste.append(loc)

    # -------------------------------------------------------------------------
    # Étape 2 : Nettoyage des degrés significatifs
    # -------------------------------------------------------------------------
    def _nettoyer_significatifs(self):
        # Construire la liste de lecture appartenant à sec_liste
        lec_liste = [int(ls[-1]) for ls in self.sec_liste]

        for deg in lec_liste:
            for ai28 in ALTERACTIONS[deg]:
                ai = ai28[0]

                if ai in self.sec_liste:
                    # print(lineno(), "ai", ai, "ai28", ai28)
                    for a2 in ai28:
                        # print(lineno(), "a2", a2)
                        if a2 != ai and a2 in self.sec_liste:
                            self.sec_liste.remove(a2)
                            # print(lineno(), "ai", ai, "a2", a2, "ai28", ai28, self.sec_liste)

        # Comparer la liste originale[don_deg] avec la découverte[sig_liste]
        for dd in self.don_deg:
            if dd not in self.sig_liste and dd not in ("1", "7") and len(dd) > 1:
                self.sec_liste.append(dd)

    # -------------------------------------------------------------------------
    # API principale
    # -------------------------------------------------------------------------
    def analyser(self) -> Tuple[List[str], List[str]]:
        """
        Retourne :
        - liste des effets (sig_liste)
        - liste des forces (sec_liste)
        """
        self._collecter_alterations()
        self._nettoyer_significatifs()
        return self.sig_liste, self.sec_liste

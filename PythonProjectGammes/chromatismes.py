# chromatismes.py
# -*- coding: utf-8 -*-
# vicente quantic cabviva

"""
Module chromatisme.py
---------------------

Ce module est dédié à l’analyse et à la génération des chromatismes associés
aux gammes fondamentales sélectionnées dans le module selection.py.

Il reçoit en entrée les gammes primordiales (déjà analysées et structurées),
ainsi que les informations optionnelles de signatures et de rangs, afin de
produire différentes extensions chromatiques cohérentes avec la logique
interne du système.

La classe principale, SelectionChromes, suit la même organisation que
SelectionGammes : elle centralise les données reçues, applique les règles
chromatiques définies, et renvoie une structure exploitable par system.py.

Les familles chromatiques implémentées pourront inclure :
    - la famille basique (notes absentes de la gamme),
    - la famille orbitale (attraction / répulsion selon les forces),
    - la famille directionnelle (glissements dans les intervalles libres),
    - la famille symétrique (chromatisme par inversion),
    - ainsi que d’autres extensions propres au système.

Ce module est conçu pour être extensible : chaque nouvelle famille peut être
ajoutée sous forme de méthode interne (_nom_de_la_famille), puis intégrée
dans la méthode analyser().

"""

import inspect
from typing import Callable

# lino() Pour consulter le programme grâce au suivi des print’s
lineno: Callable[[], int] = lambda: inspect.currentframe().f_back.f_lineno


# from .notes import NOTES, NORDIESE, SUBEMOL


class SelectionChromes:
    def __init__(self, fondamentales, dic_sig=None, dic_rang=None):
        self.fondamentales = fondamentales  # {((1, 1, 1, 1, 1, 1, 6), 5): {'notes': ['C', '-D', 'oE', 'oF'...]}}
        self.dic_sig = dic_sig  # {(1, 1, 1, 1, 1, 1, 6): [[(1, 0), (2, -1), (3, -2), (4, -2), (5, -3), (6, -4)...]}
        self.dic_rang = dic_rang  # {1: [(1, 1, 1, 1, 1, 1, 6), (6, 1, 1, 1, 1, 1, 1), (1, 6, 1, 1, 1, 1, 1)...]}
        self.lis_str, self.lis_chr, self.gam_ton = "", [], []
        self.maj_str, self.maj_chr = "102034050607", ['C', '0', 'D', '0', 'E', 'F', '0', 'G', '0', 'A', '0', 'B']

    def analyser(self):
        resultats = []
        # self.fondamentales[g].keys()(['notes', 'type', 'signal', 'renversement', 'forces', 'effets', 'poids'])

        for g in self.fondamentales.keys():
            (lineno(), "G", self.fondamentales[g]["renversement"], self.dic_sig[g[0]][0])

            # Définir l'image numéraire[self.lis_str] du renversement.
            self.lis_str, self.lis_chr = "", []
            mod_un, deg_un = self.fondamentales[g]["renversement"], 0
            self.gam_ton = self.fondamentales[g]["notes"]
            for mu in mod_un:
                if mu == 1:
                    self.lis_chr.append(self.fondamentales[g]["notes"][deg_un])
                    deg_un += 1
                    self.lis_str += str(deg_un)
                else:
                    self.lis_chr.append(self.fondamentales[g]["notes"][deg_un])
                    deg_un += 1
                    self.lis_str += str(deg_un)
                    for m in range(1, mu):
                        self.lis_chr.append("0")
                        self.lis_str += str(0)
            (lineno(), "lis_chr", self.lis_chr, "lis_str", self.lis_str)  # La gamme naturelle.
            # 75 lis_chr ['C', '0', 'D', '0', 'E', 'F', '0', 'G', '0', 'A', '0', 'B'] lis_str 102034050607

            gammy = self.dic_sig[g[0]]

            #
            chrom = {
                "basique": self._basique(),
                # autres familles plus tard
            }
            resultats.append(chrom)
            (lineno(), "gammy", gammy, "")

        return resultats

    def _basique(self):
        chr_base_aug = ["C", "+C", "D", "+D", "E", "F", "+F", "G", "+G", "A", "+A", "B"]
        chr_base_min = ["C", "-D", "D", "-E", "E", "F", "-G", "G", "-A", "A", "-B", "B"]
        chr_min, chr_aug = [], []

        # Construction des deux gammes chromatiques basiques.
        for sls in range(len(self.lis_str)):
            if self.lis_chr[sls] != "0":
                chr_min.append(self.lis_chr[sls])
                chr_aug.append(self.lis_chr[sls])
            else:
                chr_min.append(chr_base_min[sls])
                chr_aug.append(chr_base_aug[sls])
        (lineno(), "\ngam_ton", self.gam_ton, "\nchr_min", chr_min, "\nchr_aug", chr_aug)
        min_aug = (chr_min, chr_aug)
        return min_aug

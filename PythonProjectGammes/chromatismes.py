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
    - la famille complémentaire (notes absentes de la gamme),
    - la famille orbitale (attraction / répulsion selon les forces),
    - la famille directionnelle (glissements dans les intervalles libres),
    - la famille symétrique (chromatisme par inversion),
    - ainsi que d’autres extensions propres au système Grok.

Ce module est conçu pour être extensible : chaque nouvelle famille peut être
ajoutée sous forme de méthode interne (_nom_de_la_famille), puis intégrée
dans la méthode analyser().

"""

import inspect
from typing import Callable
# lino() Pour consulter le programme grâce au suivi des print’s
lineno: Callable[[], int] = lambda: inspect.currentframe().f_back.f_lineno


class SelectionChromes:
    def __init__(self, fondamentales, dic_sig=None, dic_rang=None):
        self.fondamentales = fondamentales  # {((1, 1, 1, 1, 1, 1, 6), 5): {'notes': ['C', '-D', 'oE', 'oF'...]}}
        self.dic_sig = dic_sig  # {(1, 1, 1, 1, 1, 1, 6): [[(1, 0), (2, -1), (3, -2), (4, -2), (5, -3), (6, -4)...]}
        self.dic_rang = dic_rang  # {1: [(1, 1, 1, 1, 1, 1, 6), (6, 1, 1, 1, 1, 1, 1), (1, 6, 1, 1, 1, 1, 1)...]}


    def analyser(self):
        resultats = []
        # self.fondamentales[g].keys()(['notes', 'type', 'signal', 'renversement', 'forces', 'effets', 'poids'])
        for g in self.fondamentales.keys():
            (g[0], self.dic_sig[g[0]][0])
            gamme = self.dic_sig[g[0]]
            chrom = {
                "complementary": self._complementary(gamme),
                # autres familles plus tard
            }
            resultats.append(chrom)
        return resultats

    def _complementary(self, gamme):

        return [n for n in range(12) if n not in gamme]

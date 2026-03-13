# selection.py
# -*- coding: utf-8 -*-
# vicente quantic cabviva

"""
selection.py — Sélection des gammes fondamentales selon la logique Grok.

Ce module reprend fidèlement la logique du programme original :
- analyse des forces et effets,
- calcul des poids maximaux,
- sélection des modes légers,
- résolution des égalités,
- construction de dic_gen et dic_poids,
- construction des gammes primordiales.

La sortie est regroupée par gamme, mais la logique interne est identique.
"""

from typing import Dict, List, Tuple, Any


class SelectionGammes:
    """
    Sélectionne les gammes fondamentales à partir :
    - dic_sig : signatures modales
    - gam_notes : gammes altérées
    - dic_rang : renversements intervalliques
    """

    def __init__(
        self,
        dic_sig: Dict[Tuple[int, ...], List[List[Tuple[int, int]]]],
        gam_notes: Dict[Tuple[int, Tuple[int, ...]], List[List[Tuple[str, str]]]],
        dic_rang: Dict[int, List[Tuple[int, ...]]],
    ) -> None:

        # Données d'entrée
        self.dic_sig = dic_sig
        self.gam_notes = gam_notes
        self.dic_rang = dic_rang

        # Dictionnaires internes (mêmes noms que dans ton code)
        self.dic_gen: Dict[Tuple[int, ...], List[Any]] = {}
        self.dic_poids: Dict[Tuple[Tuple[int, ...], int], Dict[str, List[int]]] = {}
        self.gammes_fondamentales: Dict[Tuple[Tuple[int, ...], int], Dict[str, Any]] = {}

        # Tables internes Grok
        self.not_mus = ["C", "D", "E", "F", "G", "A", "B"]
        self.sig_not = ["", "+", "x", "^", "+^", "x^", "o*", "-*", "*", "o", "-"]

        # Table des altéractions (héritée du code original)
        self.alteractions = {
            2: [["x2", "+3", "+4"], ["^2", "x3", "x4", "+5"], ["+^2", "^3", "^4", "x5", "+6"]],
            3: [["+3", "+4"], ["x3", "x4", "+5"], ["^3", "^4", "x5", "+6"], ["o3", "-2"]],
            4: [["x4", "+5"], ["^4", "x5", "+6"], ["o4", "o3", "-2"], ["-4", "-3"]],
            5: [["x5", "+6"], ["o5", "-4", "-3"], ["*5", "o4", "o3", "-2"]],
            6: [["o6", "-5"], ["*6", "o5", "-4", "-3"], ["-*6", "*5", "o4", "o3", "-2"]],
            7: [["o7", "-6"], ["*7", "o6", "-5"], ["-*7", "*6", "o5", "-4", "-3"],
                ["o*7", "-*6", "*5", "o4", "o3", "-2"]],
        }

    # -------------------------------------------------------------------------
    #  Analyse des forces et effets (réécriture propre de func_gam)
    # -------------------------------------------------------------------------

    def _analyser_forces_effets(self, sig: List[Tuple[int, int]]) -> Tuple[List[str], List[str]]:
        """
        Analyse les forces et effets d'une signature.
        Retourne (effets, forces).
        """

        # Degrés signés (ex : "x5", "o3", "-2")
        don_deg = [self.sig_not[a] + str(d) for d, a in sig]

        effets: List[str] = []
        forces: List[str] = []

        # S'assurer que le mode a une septième majeure
        if len(don_deg[-1]) == 1:

            # Première passe : repérage dans alteractions
            for deg, alt in sig:
                if deg == 1:
                    continue  # la tonique n'est pas traitée ici

                signe = self.sig_not[alt]  # Récupère le signe d'altération
                loc = signe + str(deg)  # Composition du degré signé

                for groupe in self.alteractions[deg]:
                    if loc == groupe[0]:
                        # Ajout de la force principale
                        if loc not in forces:
                            forces.append(loc)
                        # Ajout des effets
                        for item in groupe:
                            if item not in effets:
                                effets.append(item)

            # Deuxième passe : élimination des doublons hiérarchiques
            for f in list(forces):
                deg = int(f[-1])
                if deg in self.alteractions:
                    for groupe in self.alteractions[deg]:
                        if groupe[0] == f:
                            for item in groupe[1:]:
                                if item in forces:
                                    forces.remove(item)

            # Troisième passe : ajout des altérations présentes, mais non couvertes
            for dd in don_deg:
                if dd not in effets and dd not in ("1", "7") and len(dd) > 1 and dd not in forces:
                    forces.append(dd)

            # Passe de suppression des forces supérieures à deux éléments.
            if len(forces) > 2:
                forces.clear()
                effets.clear()

        return effets, forces

    # -------------------------------------------------------------------------
    #  Calcul des poids maximaux (dic_max)
    # -------------------------------------------------------------------------

    def _calculer_dic_max(self, k_sig: Tuple[int, ...]) -> Tuple[Dict, List[Tuple[int, int]]]:
        """
        Construit dic_max et la liste c_max (poids max, mode_index).
        """

        dic_max = {}
        c_max = []
        signatures = self.dic_sig[k_sig]

        mode_index = 0
        for sig in signatures:
            mode_index += 1
            mem_sig = [abs(a) for _, a in sig]
            max_mem = max(mem_sig)
            dic_max[(k_sig, mode_index)] = (mem_sig, max_mem, sig, mode_index)
            c_max.append((max_mem, mode_index))

        return dic_max, c_max

    # -------------------------------------------------------------------------
    #  Collecte des modes candidats (lis_retours)
    # -------------------------------------------------------------------------

    def _collecter_modes_candidats(
        self,
        k_sig: Tuple[int, ...],
        dic_max: Dict,
        c_max: List[Tuple[int, int]],
        k_key: int,
    ) -> List[Any]:
        """
        Construit lis_retours : liste des modes candidats avec leurs forces/effets.
        """

        fix_poids = sorted([m for m, _ in c_max])
        rem_deg = list(range(1, 8))
        keys_max = [(k_sig, x) for x in range(1, 8)]
        keys_cop = keys_max.copy()

        lis_retours = []

        for fip in fix_poids:
            long_fip = sum(1 for m, _ in c_max if m == fip)

            while long_fip:
                for cdm in keys_max:
                    if cdm not in dic_max:
                        continue

                    mem_sig, max_mem, sig, mode_index = dic_max[cdm]

                    if max_mem != fip:
                        continue
                    if mode_index not in rem_deg:
                        continue

                    # On consomme ce degré
                    rem_deg.remove(mode_index)

                    # Gamme primordiale
                    if sig[-1][1] == 0 and fip == 0:
                        if cdm in keys_cop:
                            keys_cop.remove(cdm)
                            gamme = [n[1] for n in self.gam_notes[(k_key, k_sig)][mode_index - 1]]
                            gamme.append("Maj")
                            self.gammes_fondamentales[(k_sig, mode_index)] = {
                                "notes": gamme,
                                "type": "Maj",
                                "signature": sig,
                                "renversement": self.dic_rang[k_key][mode_index - 1],
                                "forces": [],
                                "effets": [],
                                "poids": {"FORT": [], "EFFET": []},
                            }

                    # Autres gammes
                    elif fip in (1, 2, 3):
                        if cdm in keys_cop:
                            effets, forces = self._analyser_forces_effets(sig)
                            if forces:
                                lis_retours.append(
                                    ((effets, forces), (mem_sig, max_mem, sig, mode_index), (k_key, k_sig))
                                )
                            keys_cop.remove(cdm)

                # Fin de cycle diatonique
                if not rem_deg:
                    return lis_retours

                long_fip -= 1

        return lis_retours

    # -------------------------------------------------------------------------
    #  Sélection finale des modes légers (forces puis poids)
    # -------------------------------------------------------------------------

    def _selectionner_modes(self, lis_retours: List[Any]) -> List[int]:
        """
        Sélectionne les modes les plus légers selon :
        - envergure minimale (forces)
        - poids minimal
        """

        if not lis_retours:
            return []

        forces_list = [item[0][1] for item in lis_retours]
        poids_list = [item[1][1] for item in lis_retours]

        # Longueur des forces
        mini_forces = [(len(f), i) for i, f in enumerate(forces_list)]
        min_len = min(x[0] for x in mini_forces)

        # Indices des modes ayant la plus petite envergure
        candidats = [i for l, i in mini_forces if l == min_len]

        # Parmi eux, on garde ceux ayant le plus petit poids
        min_poids = min(poids_list[i] for i in candidats)
        res_fo = [i for i in candidats if poids_list[i] == min_poids]

        return res_fo

    # -------------------------------------------------------------------------
    #  Traitement final des modes retenus (dic_gen, dic_poids, gammes)
    # -------------------------------------------------------------------------

    def _traiter_modes_retenus(
        self,
        k_sig: Tuple[int, ...],
        k_key: int,
        lis_retours: List[Any],
        res_fo: List[int],
    ) -> None:
        """
        Construit dic_gen, dic_poids et gammes_fondamentales pour les modes retenus.
        """

        # Fixation des types des gammes
        type_gam_nom = {
            1: "Tonice", 2: "Tonale", 3: "Mélodique", 4: "Médiane",
            5: "Dominante", 6: "Harmonique", 7: "Sensible"
        }
        type_gam_rang = {
            -1: ".", -2: "di.", -3: "tri.",  # D'autres extensions sont possibles.
            1: "a.", 2: "dia.", 3: "tria."
        }

        if k_sig not in self.dic_gen:
            self.dic_gen[k_sig] = []

        for idx in res_fo:
            (effets, forces), (mem_sig, max_mem, sig, mode_index), _ = lis_retours[idx]

            # Renversement associé
            renv = self.dic_rang[k_key][mode_index - 1]

            # Gamme altérée
            gam_alt = self.gam_notes[(k_key, k_sig)][mode_index - 1]
            gamme_notes = [(n[0] if isinstance(n[0], str) else '') + n[1] for n in gam_alt]

            # Ajout dans dic_gen
            self.dic_gen[k_sig].append((sig, self.gam_notes[(k_key, k_sig)][mode_index - 1], renv))

            # Calcul des poids gravitationnels
            clef1 = renv
            if (clef1, k_key) not in self.dic_poids:
                self.dic_poids[(clef1, k_key)] = {"FORT": [], "EFFET": []}

            po_fort_pg = 0
            po_eff_pg = 0

            # Forces
            for f in forces:
                for deg, alt in sig:
                    if int(f[-1]) == deg:
                        val = deg if alt >= 0 else -deg
                        po_fort_pg += val + alt
                self.dic_poids[(clef1, k_key)]["FORT"].append(po_fort_pg)

            # Effets
            for e in effets:
                for deg, alt in sig:
                    if int(e[-1]) == deg:
                        val = deg if alt >= 0 else -deg
                        po_eff_pg += val + alt
                self.dic_poids[(clef1, k_key)]["EFFET"].append(po_eff_pg)

            # Définition du type du mode retenu.
            type_mode, si2, si3 = "", 0, 0
            for si1 in forces:
                si2 = [s for s in sig if s[0] == int(si1[1][-1])]
                if len(forces) != 1:
                    t_nom, t_rang = type_gam_nom[si2[0][0]], type_gam_rang[si2[0][1]]
                    if si3 == 0:
                        type_mode = t_rang + t_nom + " & "
                    else:
                        type_mode += t_rang + t_nom
                    si3 += 1
                else:
                    t_nom, t_rang = type_gam_nom[si2[0][0]], type_gam_rang[si2[0][1]]
                    type_mode = t_rang + t_nom

            # Déclaration du signal
            if len(forces) == 1:
                signal = forces[0]
            else:
                x, y = forces
                if x[0] == y[0]:
                    signal = x + y[1]
                else:
                    signal = x + y[1] + y[0]

            # Enregistrement de la gamme fondamentale
            self.gammes_fondamentales[(k_sig, mode_index)] = {
                "notes": gamme_notes,  # Les notes signées de la gamme.
                "type": type_mode,  # Classe la gamme selon sa famille et son rang.
                "signal": signal,  # Les degrés connus dans la liste des forces.
                "renversement": renv,  # Renversement par rapport aux intervalles originaux.
                "forces": forces,
                "effets": effets,
                "poids": self.dic_poids[(clef1, k_key)],
            }

    # -------------------------------------------------------------------------
    #  Méthode principale
    # -------------------------------------------------------------------------

    def selectionner(self) -> Dict[Tuple[Tuple[int, ...], int], Dict[str, Any]]:
        """
        Sélectionne toutes les gammes fondamentales.
        """

        self.gammes_fondamentales.clear()
        self.dic_gen.clear()
        self.dic_poids.clear()

        stop_gammes = False

        for k_sig in self.dic_sig.keys():

            # Découvrir la gamme naturelle
            nbr = 0
            for ds in self.dic_sig[k_sig]:
                k_key_naturelle = [str(0) for k in ds if k[1] == 0]
                nbr += 1
                if k_key_naturelle.count("0") == 7:
                    # Mise en forme du retour
                    self.gammes_fondamentales[(k_sig, nbr)] = {
                        "notes": ["C", "D", "E", "F", "G", "A", "B"],
                        "type": "Majeure",
                        "signature": "Maj",
                        "renversement": (2, 2, 1, 2, 2, 2, 1),
                        "forces": [],
                        "effets": [],
                        "poids": {"FORT": [], "EFFET": []},
                    }
                    stop_gammes = True
            # La gamme naturelle est rencontré et le traitement des poids est injustifié.
            if stop_gammes:
                break

            # Trouver k_key correspondant
            k_key_candidates = [k[0] for k in self.gam_notes.keys() if k_sig in k]
            if not k_key_candidates:
                continue
            k_key = k_key_candidates[0]

            # Calcul dic_max
            dic_max, c_max = self._calculer_dic_max(k_sig)

            # Collecte des modes candidats
            lis_retours = self._collecter_modes_candidats(k_sig, dic_max, c_max, k_key)

            # Sélection des modes légers
            res_fo = self._selectionner_modes(lis_retours)

            # Traitement final
            self._traiter_modes_retenus(k_sig, k_key, lis_retours, res_fo)

        return self.gammes_fondamentales

    # -------------------------------------------------------------------------
    #  Interface simple
    # -------------------------------------------------------------------------

    def analyser(self) -> Dict[Tuple[Tuple[int, ...], int], Dict[str, Any]]:
        """
        Point d'entrée simple.
        """
        return self.selectionner()

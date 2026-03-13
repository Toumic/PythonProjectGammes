# 🧠 Heuristique du Code — Version Moderne du Système Grok

Ce document décrit l’architecture moderne du projet **PythonProjectGammes**, ainsi que les transformations réalisées pour rendre le système plus lisible, modulaire et fidèle à la logique originelle du programme Grok.<br>
L’objectif principal a été de démanteler le code monolithique d’origine pour en extraire des modules cohérents, **tout en préservant strictement la logique musicale et mathématique** du système.

### 1. 🎼 Architecture générale

Le projet est désormais organisé en modules spécialisés :

**Module	        Rôle**<br>
`intervals.py`	    Génère les structures intervalliques et les renversements (dic_rang).<br>
`signatures.py`	    Produit les signatures modales (dic_sig).<br>
`alterations.py`	Produit les gammes altérées (gam_notes).<br>
`selection.py`	    Sélectionne les modes légers, calcule forces/effets/poids, construit dic_gen, dic_poids et les gammes fondamentales.<br>
`system.py`	        Orchestrateur : relie tous les modules.<br>
`main.py`	        Point d’entrée du programme.<br>

Cette structure permet :

* une meilleure lisibilité,
* une maintenance plus simple,
* une vérification plus facile de la fidélité au code d’origine,
* une future extension (ex. : nommer les 462 modes).

### 2. 🎵 Ce qui a été reconstruit depuis le code d’origine

**2.1. Extraction des signatures (`dic_sig`)**<br>
Le code d’origine générait les signatures modales en interne.
Elles sont maintenant produites dans `signatures.py`, mais la logique est identique :

* altérations par degré,
* structure (`degré, altération`),
* Sept signatures par structure intervallique.

**2.2. Reconstruction des gammes altérées (`gam_notes`)**<br>
Le module alterations.py applique les altérations aux notes musicales.<br>
La logique d’origine a été conservée :

* correspondance degré → note,
* application des altérations,
* gestion des cas particuliers.

**2.3. Reconstruction des renversements (`dic_rang`)**<br>
Le module `intervals.py` génère les renversements modaux.
La logique est identique à celle du code d’origine.

### 3. ⚖️ Reconstruction complète de la sélection des modes (`selection`.py)

C’est le module le plus complexe et le plus fidèle au code d’origine.

Il reprend toute la logique de la zone ~431 du programme monolithique :

**✔️ Analyse des forces et effets**<br>
Réécriture propre de `func_gam`() :

* extraction des degrés signés,
* application de la table `alteractions`,
* hiérarchie interne,
* élimination des doublons,
* ajout des altérations non couvertes.

**✔️ Calcul des poids maximaux (`dic_max`)**<br>
Même logique que l’ancien code :

* poids = valeur absolue des altérations,
* poids maximal par mode,
* tri par poids croissant.

**✔️ Collecte des modes candidats (`lis_retours`)**<br>
Reconstruction fidèle :

* gestion de `fix_poids`,
* gestion de `rem_deg`,
* gestion de `keys_max` et `keys_cop`,
* ajout des modes primordiaux,
* ajout des modes altérés.

**✔️ Sélection finale des modes légers**<br>
Même logique :

* envergure minimale (forces),
* poids minimal,
* résolution des égalités.

**✔️ Construction des structures finales**<br>
Reconstruction fidèle de :

* `dic_gen` : triplets (signature, gamme altérée, renversement),
* `dic_poids` : poids FORT / EFFET,
* `gammes_fondamentales` : notes altérées + type `"Maj"` si primordiale.

✔**️ Sortie regroupée**

La sortie moderne regroupe toutes les informations par gamme :

`python <br>
(k_sig, mode_index): {

    "notes": [...],
    "type": "Maj" ou None,
    "signature": [...],
    "renversement": (...),
    "forces": [...],
    "effets": [...],
    "poids": {
        "FORT": [...],
        "EFFET": [...]
    }`
}

### 4. 🎯 Fidélité au code d’origine

La version moderne :
* conserve strictement la logique Grok,
* reproduit les mêmes sélections,
* reconstruit les mêmes triplets structurels,
* calcule les mêmes forces/effets,
* calcule les mêmes poids,
* produit les mêmes gammes fondamentales.

**Les seules différences sont :**
* une architecture modulaire,
* un code plus lisible,
* des commentaires clairs,
* une sortie regroupée.

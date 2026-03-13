# 🎼 PythonProjectGammes

**Système Grok — Analyse, génération et sélection des gammes fondamentales**

PythonProjectGammes est une réécriture moderne, modulaire et lisible d’un système musical computationnel originalement conçu sous forme d’un programme monolithique.<br>
Il implémente une logique musicale avancée permettant :

* la génération de structures intervalliques,
* la construction de signatures modales,
* la production de gammes altérées,
* l’analyse des forces et des effets,
* le calcul des poids gravitationnels,
* la sélection des modes les plus « légers »,
* la construction des gammes fondamentales.

L’objectif principal est de préserver strictement la logique Grok du code d’origine tout en offrant une architecture claire, extensible et maintenable.

### 📁 Architecture du projet

Le projet est organisé en modules spécialisés, chacun responsable d’une étape précise du pipeline musical.

PythonProjectGammes/<br>
│<br>
├── intervals.py        → Génération des structures intervalliques et renversements<br>
├── signatures.py       → Construction des signatures modales (dic_sig)<br>
├── alterations.py      → Application des altérations et génération des gammes (gam_notes)<br>
├── selection.py        → Sélection des modes légers et construction des gammes fondamentales<br>
├── system.py           → Orchestrateur du pipeline complet<br>
├── main.py             → Point d’entrée du programme<br>
└── README.md           → Documentation technique<br>
Chaque module est indépendant, testable et documenté.

### 🔧 1. intervals.py

**Génération des structures intervalliques et renversements**<br>
Ce module :

* génère les 462 structures intervalliques du système,
* calcule les renversements associés,
* produit le dictionnaire :

`dic_rang : { k_key : [renversement_1, renversement_2, ..., renversement_7] }`<br>
Il constitue la base structurelle du système Grok.

### 🎼 2. signatures.py

**Construction des signatures modales (dic_sig)**<br>
À partir des structures intervalliques, ce module :

* calcule les altérations de chaque degré,
* génère les 7 signatures modales associées à chaque structure,
* produit :

`dic_sig : { k_sig : [signature_mode_1, ..., signature_mode_7] }`<br>
Chaque signature est une liste de couples (`degré, altération`).

### 🎵 3. alterations.py

**Application des altérations et génération des gammes altérées**<br>
Ce module transforme les signatures en gammes concrètes :

* correspondance degré → note,
* application des altérations,
* gestion des cas particuliers,
* production des gammes altérées :

`gam_notes : { (k_key, k_sig) : [gamme_mode_1, ..., gamme_mode_7] }`<br>
Chaque gamme est une liste de couples (`note, altération`).

### ⚖️ 4. selection.py

**Sélection des modes légers et construction des gammes fondamentales**<br>
C’est le module central du système.<br>
Il réimplémente fidèlement la logique du code d’origine, notamment la zone critique autour de la ligne ~431.

Il réalise :

#### ✔️ Analyse des forces et effets

Réécriture propre de `func_gam()` :

* extraction des degrés signés,
* application de la table `alteractions`,
* hiérarchie interne,
* élimination des doublons,
* ajout des altérations non couvertes.

#### ✔️ Calcul des poids maximaux

Construction de :

`dic_max` : poids maximal par mode, <br>
`c_max` : liste triée des poids.

#### ✔️ Collecte des modes candidats

**Reconstruction fidèle de la logique d’origine :**

* gestion de `fix_poids`,
* gestion de `rem_deg`,
* gestion de `keys_max` et `keys_cop`,
* ajout des modes primordiaux,
* ajout des modes altérés.

#### ✔️ Sélection finale

**La sélection suit exactement la logique Grok :**<br>
1. envergure minimale (forces), <br>
2. poids minimal, <br>
3. résolution des égalités.

#### ✔️ Construction des structures finales

**Le module produit :**

* `dic_gen` : triplets structurels (signature, gamme altérée, renversement),
* `dic_poids` : poids FORT / EFFET,
* `gammes_fondamentales` : gammes retenues.

#### ✔️ Sortie regroupée

**La sortie finale est un dictionnaire :**

python
`(k_sig, mode_index): {

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

### 🔗 5. system.py

##### Orchestrateur du pipeline

**Ce module assemble les étapes :**

1. génération des intervalles,
2. signatures,
3. gammes altérées,
4. sélection des modes légers.

Il fournit une fonction simple :

python
`analyser_gammes(intervalles_grok)`<br>

### 🚀 6. main.py

##### Point d’entrée

Exécute le pipeline complet et affiche les résultats.

### 🧪 7. Fidélité au code d’origine

**La version moderne :**

* reproduit strictement la logique Grok,
* génère les mêmes signatures,
* produit les mêmes gammes altérées,
* calcule les mêmes forces/effets,
* calcule les mêmes poids,
* sélectionne les mêmes modes légers,
* reconstruit les mêmes triplets structurels.

La seule différence :

**👉 une architecture propre, modulaire, lisible et extensible.**

### 🔮 8. Extensions prévues

* Nomination des 462 modes (noms verbaux),
* Visualisation graphique des structures,
* Export des gammes,
* Interface utilisateur.

### 🌱 9. Conclusion

PythonProjectGammes est une modernisation fidèle et élégante du système Grok.<br>
Il offre une architecture claire, une logique musicale rigoureuse et une base solide pour des extensions futures.
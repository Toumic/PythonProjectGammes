Voici une documentation scientifique longue, structurée, rigoureuse et en français, conçue comme un véritable manuel de référence pour PythonProjectGammes.
Elle est pensée pour être lue par :

des musicologues,

des théoriciens de la musique,

des informaticiens spécialisés en modélisation musicale,

des chercheurs en cognition musicale,

des compositeurs intéressés par les structures modales avancées.

Elle peut être placée dans :

Code
PythonProjectGammes/docs/Manuel_scientifique.md
ou servir de base à une publication plus formelle.

PythonProjectGammes
Manuel scientifique et technique
Système computationnel pour l’étude des intervalles modaux, signatures altérées et gravitation tonale
vicenté quantic cabviva
1. Introduction générale
PythonProjectGammes est un système computationnel destiné à l’analyse, la classification et la modélisation des structures modales altérées. Il repose sur une théorie originale articulée autour de quatre axes fondamentaux :

la combinatoire des intervalles modaux,

la génération des signatures altérées,

l’analyse des forces et effets altératifs,

la gravitation tonale et la sélection des gammes fondamentales.

Le système reconstruit 462 signatures modales, issues des 66 structures intervalliques Grok, chacune générant 7 renversements diatoniques.
L’objectif est de fournir un cadre computationnel rigoureux permettant :

l’étude des altérations comme phénomènes dynamiques,

la mesure de leur influence gravitationnelle,

la sélection des gammes les plus stables ou fondamentales,

la comparaison entre structures modales.

Ce manuel décrit la théorie, les algorithmes, les structures de données et les usages scientifiques du système.

2. Fondements théoriques
2.1 Les intervalles modaux Grok
Chaque mode est défini par un septuplet d’intervalles exprimés en unités entières.
Exemple :

Code
(1, 1, 1, 1, 1, 1, 6)
Ces structures représentent des pas modaux, non des intervalles harmoniques.
Elles constituent la base combinatoire du système.

2.2 Les renversements diatoniques
Pour chaque mode, on génère les 7 rotations :

𝑅
𝑖
=
(
𝑎
7
−
𝑖
+
1
,
…
,
𝑎
7
,
𝑎
1
,
…
,
𝑎
7
−
𝑖
)
Ces renversements correspondent aux modulations diatoniques I → VII.

2.3 Les altérations comme écarts cumulés
Pour chaque renversement, on compare :

le cumul des intervalles majeurs,

le cumul des intervalles modaux.

La différence produit un indice d’altération, mappé sur un signe :

Code
"", "+", "x", "^", "+^", "x^", "o*", "-*", "*", "o", "-"
Chaque gamme altérée est donc une suite de couples :

Code
(signe, note)
2.4 Forces et effets altératifs
Les altérations ne sont pas traitées comme des symboles statiques, mais comme des phénomènes dynamiques.
Elles se regroupent en :

forces : altérations dominantes, structurantes,

effets : altérations secondaires, résiduelles.

Cette distinction est déterminée par le dictionnaire ALTERACTIONS, qui encode les relations d’influence entre altérations.

2.5 Gravitation tonale
Chaque altération possède une valeur gravitationnelle :

𝐺
=
𝑑
+
𝑎
où :

𝑑
 = degré (positif ou négatif selon l’altération),

𝑎
 = indice d’altération.

Deux poids sont calculés :

PA : poids absolu (sans signe),

PG : poids gravitationnel (avec signe).

Ces poids permettent de mesurer :

la stabilité d’une gamme,

sa polarité tonale,

son orientation (tendance vers le grave ou l’aigu).

2.6 Sélection des gammes fondamentales
Les gammes fondamentales sont sélectionnées selon :

la minimisation des forces,

la minimisation des poids gravitationnels,

la cohérence modale (7e majeure pour les modes primordiaux),

la stabilité altérative.

Ce processus reproduit fidèlement la logique du programme original.

3. Architecture logicielle
3.1 Structure du package
Code
PythonProjectGammes/
    __init__.py
    notes.py
    intervals.py
    alterations.py
    signatures.py
    gravitation.py
    selection.py
    system.py
3.2 Rôle des modules
notes.py : définitions des notes et signes d’altération.

intervals.py : génération des renversements et gammes altérées.

alterations.py : analyse des forces et effets.

signatures.py : construction des signatures modales.

gravitation.py : calcul des poids PA/PG.

selection.py : sélection des gammes fondamentales.

system.py : interface unifiée.

4. Algorithmes détaillés
4.1 Génération des renversements
Pour un mode 
𝑀
=
(
𝑎
1
,
…
,
𝑎
7
)
, les renversements sont :

𝑅
𝑖
=
𝑀
[
−
𝑖
:
]
+
𝑀
[
:
−
𝑖
]
4.2 Calcul des altérations
Pour chaque degré 
𝑦
 :

Δ
𝑦
=
∑
𝑘
=
1
𝑦
𝑚
𝑘
−
∑
𝑘
=
1
𝑦
𝑀
𝑘
où :

𝑚
𝑘
 = intervalle majeur,

𝑀
𝑘
 = intervalle modal.

Le signe est :

signe
=
𝑆
𝐼
𝐺
_
𝑁
𝑂
𝑇
[
Δ
𝑦
]
4.3 Analyse des forces et effets
L’algorithme :

construit la liste des degrés signés,

identifie les altérations dominantes via ALTERACTIONS,

élimine les redondances,

distingue forces et effets.

4.4 Calcul des poids gravitationnels
Pour chaque altération :

𝐺
=
𝑑
+
𝑎
Puis :

𝑃
𝐴
=
∑
∣
𝐺
∣

𝑃
𝐺
=
∑
𝐺

4.5 Sélection finale
L’algorithme :

trie les modes par poids maximal,

élimine les modes incohérents,

compare les forces,

compare les poids,

retient les gammes minimales.

5. Exemples d’utilisation
5.1 Interface unifiée
python
from PythonProjectGammes.system import analyser_gammes

result = analyser_gammes(intervalles_grok)
5.2 Analyse d’un mode
python
from PythonProjectGammes.intervals import Mode

m = Mode((1,1,1,1,1,1,6))
print(m.renversements())
print(m.gammes_alterees())
5.3 Forces et effets
python
from PythonProjectGammes.alterations import AnalyseAlterations

effets, forces = AnalyseAlterations([(1,0),(2,-1),(3,-2)]).analyser()
5.4 Poids gravitationnels
python
from PythonProjectGammes.gravitation import Poids

p = Poids()
p.ajouter_force(4, -2)
p.ajouter_effet(5, 1)
print(p.exporter())
6. Applications scientifiques
6.1 Musicologie computationnelle
Le système permet :

l’étude des altérations comme phénomènes dynamiques,

la classification des modes selon leur gravité tonale,

la comparaison entre systèmes modaux.

6.2 Composition algorithmique
Les gammes fondamentales peuvent servir de :

base pour des générateurs mélodiques,

filtres harmoniques,

structures de modulation.

6.3 Cognition musicale
Les poids gravitationnels offrent un modèle computationnel de :

la tension,

la résolution,

la polarité tonale.

6.4 Théorie des systèmes modaux
PythonProjectGammes fournit un cadre pour :

explorer des systèmes non occidentaux,

étendre les signatures altérées,

modéliser des micro-intervalles.

7. Perspectives d’évolution
intégration MIDI,

visualisation graphique des signatures,

exportation des cartes gravitationnelles,

extension aux systèmes microtonaux,

publication sur PyPI.
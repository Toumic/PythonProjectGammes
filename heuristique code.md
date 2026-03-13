# Suivi logique du début : main.py

Le module de démarrage 'main.py' demande au module 'system.py' de traiter les modes gammiques dans le désordre, afin de transformer les modes quelconques en modes toniques. Ce qui veut dire que les modes originaux forment une liste de soixante-six éléments modaux dont les niveaux diatoniques sont mathématiquement établis. <br>
Pour que le mode tonique puisse être établi, chaque mode doit être renversé pour évaluer le degré modal qui représentera la gamme. Cette opération ne peut se réaliser en une seule fois et le plus simple est de commencer les renversements en joignant le module 'system.py' via `from PythonProjectGammes.system import analyser_gammes`.
## Module system.py
Réalise trois opérations :

`from .intervals import SystemeIntervalles`
* SYSTEM intervals/gam_notes {(1, (1, 1, 1, 1, 1, 1, 6)): [[(0, 'C'), ('-', 'D'), ('o', 'E'), ('o', 'F')…]]}.

`from .signatures import SignatureSystem`
* SYSTEM signatures/dic_sig {(1, 1, 1, 1, 1, 1, 6): [[(1, 0), (2, -1), (3, -2), (4, -2)...]]}.

`from .selection import SelectionGammes`
* SYSTEM selection/fondamentales: {((1, 1, 1, 1, 1, 1, 6), 5): {'notes': ['C', 'D', 'E', 'F', 'G', 'A', 'B'], 'type': None, 'signature': [(1, 0), (2, -1), (3, -2), (4, -2), (5, 2), (6, 1), (7, 0)], 'renversement': (1, 1, 1, 6, 1, 1, 1), 'forces': ['o4', 'x5'], 'effets': ['o3', '-2', 'o4', 'x5', '+6'], 'poids': {'FORT': [-6, 1], 'EFFET': [-5, -8, -14, -7, 0]}}.

#### Après une courte réflexion
Le problème apparait dans le module `selection.py`, qui ne distingue pas clairement les septièmes majeures. <br>
Dans sa globalité de cette première analyse, les modulations diatoniques des intervalles sont absentes.

**Corrections :** <br>
1. [x] Une première correction y a été réalisée en faisant en sorte de détecter la gamme naturellement majeure, ce qui n'était pas le cas.
2. Distinction du poids des altérations et celui du nombre de notes altérées : 


## Module signatures.py
Rien à signaler pour le moment.
## Module selection.py

# system.py
# -*- coding: utf-8 -*-
# vicente quantic cabviva
# unified interface for PythonProjectGammes

from typing import Dict, Tuple
from .intervals import SystemeIntervalles
from .signatures import SignatureSystem
from .selection import SelectionGammes


def analyser_gammes(base_intervalles: Dict[int, Tuple[int, ...]]):
    """
    Unified entry point for the full computational system.

    Steps:
        - build modal rotations and altered scales
        - compute modal signatures (462 structures)
        - select fundamental scales
    """

    # Step 1: intervals and rotations
    sys_interv = SystemeIntervalles(base_intervalles)
    gam_notes, dic_rang = sys_interv.generer_gammes()
    cle_maj = (66, (1, 2, 2, 1, 2, 2, 2))
    ("SYSTEM intervals/gam_notes:", gam_notes[cle_maj])
    # SYSTEM intervals/gam_notes: [[(0, 'C'), ('-', 'D'), ('-', 'E'), ('', 'F'), ('-', 'G'), ('-', 'A'), ('-', 'B')],
    # [(0, 'C'), ('', 'D'), ('-', 'E'), ('', 'F'), ('', 'G'), ('-', 'A'), ('-', 'B')],
    # [(0, 'C'), ('', 'D'), ('', 'E'), ('', 'F'), ('', 'G'), ('', 'A'), ('-', 'B')],
    # [(0, 'C'), ('', 'D'), ('', 'E'), ('+', 'F'), ('', 'G'), ('', 'A'), ('', 'B')],
    # [(0, 'C'), ('-', 'D'), ('-', 'E'), ('', 'F'), ('', 'G'), ('-', 'A'), ('-', 'B')],
    # [(0, 'C'), ('', 'D'), ('-', 'E'), ('', 'F'), ('', 'G'), ('', 'A'), ('-', 'B')],
    # [(0, 'C'), ('', 'D'), ('', 'E'), ('', 'F'), ('', 'G'), ('', 'A'), ('', 'B')]]

    # Step 2: signatures
    sys_sig = SignatureSystem(base_intervalles)
    dic_sig = sys_sig.analyser()
    ("SYSTEM signatures/dic_sig:", dic_sig)
    # SYSTEM signatures/dic_sig (1, 2, 2, 1, 2, 2, 2): [[(1, 0), (2, -1), (3, -1), (4, 0), (5, -1), (6, -1), (7, -1)],
    # [(1, 0), (2, 0), (3, -1), (4, 0), (5, 0), (6, -1), (7, -1)],
    # [(1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, -1)],
    # [(1, 0), (2, 0), (3, 0), (4, 1), (5, 0), (6, 0), (7, 0)],
    # [(1, 0), (2, -1), (3, -1), (4, 0), (5, 0), (6, -1), (7, -1)],
    # [(1, 0), (2, 0), (3, -1), (4, 0), (5, 0), (6, 0), (7, -1)],
    # [(1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0)]]

    # Step 3: selection of fundamental scales
    sel = SelectionGammes(dic_sig, gam_notes, dic_rang)
    fondamentales = sel.analyser()
    ("SYSTEM selection/fondamentales:", fondamentales)
    # SYSTEM selection/fondamentales: ((1, 2, 2, 1, 2, 2, 2), 7): {'notes': ['C', 'D', 'E', 'F', 'G', 'A', 'B', 'Maj'],
    # 'type': 'Maj', 'signature': [(1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0)],
    # 'renversement': (2, 2, 1, 2, 2, 2, 1), 'forces': [], 'effets': [], 'poids': {'FORT': [], 'EFFET': []}},
    # ((1, 2, 2, 1, 2, 2, 2), 3): {'notes': ['C', 'D', 'E', 'F', 'G', 'A', 'B'],
    # 'type': None, 'signature': [(1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, -1)],
    # 'renversement': (2, 2, 1, 2, 2, 1, 2), 'forces': ['-7'], 'effets': [], 'poids': {'FORT': [-8], 'EFFET': []}},
    # ((1, 2, 2, 1, 2, 2, 2), 4): {'notes': ['C', 'D', 'E', 'F', 'G', 'A', 'B'],
    # 'type': None, 'signature': [(1, 0), (2, 0), (3, 0), (4, 1), (5, 0), (6, 0), (7, 0)],
    # 'renversement': (2, 2, 2, 1, 2, 2, 1), 'forces': ['+4'], 'effets': [], 'poids': {'FORT': [5], 'EFFET': []}}


    return {
        "gam_notes": gam_notes,
        "dic_rang": dic_rang,
        "dic_sig": dic_sig,
        "gammes_fondamentales": fondamentales,
    }

# __init__.py
# -*- coding: utf-8 -*-
# vicente quantic cabviva
# grok_gammes package initialization

"""
grok_gammes
-----------
A computational system for modal intervals, altered signatures,
gravitational weights, and fundamental scale selection.

Modules:
    notes.py          - natural notes and alteration signs
    intervals.py      - modal intervals and diatonic rotations
    alterations.py    - alteration analysis (effects and forces)
    signatures.py     - modal signatures (462 structures)
    gravitation.py    - gravitational weights (PA, PG)
    selection.py      - fundamental scale selection
"""

# Public API (you can expand this later)
from .system import analyser_gammes
from .notes import NOTES, SIG_NOT
from .intervals import Mode, SystemeIntervalles
from .signatures import SignatureSystem
from .selection import SelectionGammes

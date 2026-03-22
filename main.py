# main.py
# -*- coding: utf-8 -*-
# Vicente Quantic – Cabviva


from PythonProjectGammes.system import analyser_gammes
from PythonProjectGammes.notes import I_GROK


# ------------------------------------------------------------
# Données Grok (communes aux deux modes)
# ------------------------------------------------------------


# ------------------------------------------------------------
# Mode Python classique
# ------------------------------------------------------------
def run_python_mode():
    print("=== Mode Python classique ===")
    resultat = analyser_gammes(I_GROK)
    gammes = resultat["gammes_fondamentales"]
    ig = [i[0] for i in gammes.keys()]
    print("IG", len(ig))


# ------------------------------------------------------------
# Exécution Python classique
# ------------------------------------------------------------
if __name__ == "__main__":
    run_python_mode()

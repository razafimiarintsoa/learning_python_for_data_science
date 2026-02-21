import os
def creer_dossier():
    i=1
    for i in range(4):
        doss = os.makedirs(f".\\dossier{i}/odon", exist_ok=True)
        i=i+1
creer_dossier()
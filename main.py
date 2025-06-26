# src/main.py
#
from checker import check_sites #verif etat site 
from logger import setup_logging #init gest log 
import time # pause par cycle 
import yaml # lire et parser le fichier de conf en format yml 
import os # manip chemin fichier façon portable 

def load_config():
    """
    Charge la configuration YAML du projet.
    """
    config_path = os.path.join(os.path.dirname(__file__), "..", "config", "config.yaml") # construit chemin absolu vers config.yaml
    with open(config_path, "r") as file: # ouvre le fichier de config en lecture
        return yaml.safe_load(file) # charge et retourne le contenu YAML sous forme de dict

def main(): # fonction principale du programme
    """
    Point d'entrée principal du programme.
    Initialise les logs, charge la config, puis lance la boucle de monitoring.
    """
    setup_logging() # initialise le système de logs
    config = load_config() # charge la configuration

    # Charger les URLs depuis le fichier externe
    with open(config["sites_file"], "r") as f:
        urls = [line.strip() for line in f if line.strip()]
    # Créer une liste de dictionnaires pour chaque site
    sites = [{"url": url, "name": url} for url in urls]

    # Passe la liste des sites (dictionnaires) à la fonction
    check_sites(sites, config)

    while True: # boucle infinie pour surveiller en continu
        check_sites(sites, config)
        time.sleep(config.get("interval", 60)) # attend le nombre de secondes défini dans la config avant le prochain cycle

if __name__ == "__main__": # point d’entrée du script
    main() # lance le programme principal
    

#**Résumé**  
#Ce fichier initialise la configuration et les logs, puis lance une boucle infinie qui vérifie périodiquement l’état des sites web définis dans la configuration, en générant des logs et des alertes si besoin.  
#Chaque ligne sert à garantir la robustesse, la portabilité et la maintenabilité du programme.

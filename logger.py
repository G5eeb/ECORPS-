# Logger module
# src/logger.py

import logging  # Importe le module standard de gestion des logs

def setup_logging():
    """
    Configure le système de logs pour enregistrer les événements dans un fichier.
    """
    logging.basicConfig(
        filename="logs/monitoring.log",      # Chemin du fichier de logs
        level=logging.INFO,                  # Niveau de log (INFO)
        format="%(asctime)s - %(message)s"   # Format : date/heure - message
    )

def log_event(message):
    """
    Enregistre un événement dans le fichier de logs et l'affiche à l'écran.
    """
    logging.info(message)  # Ajoute le message dans le fichier de logs
    print(message)         # Affiche aussi le message dans la console

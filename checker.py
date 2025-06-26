# Checker module
# src/checker.py

import requests # effectue les requêtes HTTP/HTTPS
from logger import log_event # pour enregistrer les événements dans les logs
from notifier import send_email, send_webhook # pour envoyer des emails d’alerte

def check_sites(sites, config):  # reçoit la liste des sites et la config complète
    """
    Vérifie la disponibilité de chaque site et déclenche une alerte si besoin.
    """
    for site in sites: # pour chaque site à surveiller
        try:
            response = requests.get(site["url"], timeout=10, verify=False) # tente d’accéder au site (10s max)
            if response.status_code not in config.get("error_codes", []):
                log_event(f"{site['name']} est disponible (code: {response.status_code}).")
            else:
                msg = f"{site['name']} est indisponible (code: {response.status_code})." # prépare le message d’erreur
                log_event(msg) # log erreur
                send_email(
                    subject=f"Alerte indisponibilité : {site['name']}", # sujet de l’alerte
                    content=msg, # contenu de l’alerte
                    config=config # configuration complète (pour SMTP)
                )
                send_webhook(msg, config) # <-- Ajout ici
        except requests.RequestException: # si une exception réseau survient (site injoignable, timeout, etc.)
            msg = f"{site['name']} est hors ligne." # message d’erreur
            log_event(msg) # log erreur
            send_email(
                subject=f"Alerte indisponibilité : {site['name']}", # sujet de l’alerte
                content=msg, # contenu de l’alerte
                config=config # configuration complète (pour SMTP)
            )
            send_webhook(msg, config) # <-- Ajout ici

           

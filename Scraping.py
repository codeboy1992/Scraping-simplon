import requests
from bs4 import BeautifulSoup

# Fonction pour ajouter des retours à la ligne tous les 80 caractères
def ajouter_retours_ligne(texte, longueur_ligne=80):
    return '\n'.join([texte[i:i+longueur_ligne] for i in range(0, len(texte), longueur_ligne)])

url = 'https://pythonjobs.github.io/'
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="container")

# Trouver tous les conteneurs de fiches de postes
job_posts = results.find_all("div", class_="job")  # Remplace "job" par la vraie classe de chaque fiche de poste

# Parcourir chaque fiche de poste
for job in job_posts:
    # Trouver toutes les balises "span" avec la classe "info" pour chaque poste
    infos_generals = job.find_all("span", class_="info")

    # Vérifier qu'il y a bien au moins 4 éléments pour chaque poste
    if len(infos_generals) >= 4:
        localisation = infos_generals[0].get_text(strip=True)  # Localisation
        date_creation = infos_generals[1].get_text(strip=True)  # Date de création
        type_contrat = infos_generals[2].get_text(strip=True)   # Type de contrat
        resume = infos_generals[3].get_text(strip=True)         # Résumé

        # Ajouter le gros résumé (détails du poste)
        big_resume = job.find("p", class_="detail")  # Remplacer "detail" par la bonne classe si nécessaire
        big_resume_text = big_resume.get_text(strip=True) if big_resume else "N/A"

        # Ajouter des retours à la ligne dans le gros résumé
        big_resume_text = ajouter_retours_ligne(big_resume_text, longueur_ligne=80)

        # Récupérer le lien (URL) du bouton "READ MORE"
        link_tag = job.find("a", class_="go_button")
        job_link = link_tag['href'] if link_tag else "N/A"

        # Affichage des informations pour chaque poste
        print(f"Localisation: {localisation}")
        print(f"Date de création: {date_creation}")
        print(f"Type de contrat: {type_contrat}")
        print(f"Résumé: {resume}")
        print(f"Gros résumé (détails):\n{big_resume_text}")
        print(f"Lien du poste: {job_link}")  # Afficher le lien ici
        print("-" * 40)  # Séparation visuelle entre les postes

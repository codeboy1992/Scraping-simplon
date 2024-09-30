import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ResultsContainer")
job_elements = results.find_all("div", class_="card-content")
python_jobs = results.find_all(
    "h2", string=lambda text: "python" in text.lower()
)

python_jobs = results.find_all(
    "h2", string=lambda text: "python" in text.lower()
)


python_jobs = results.find_all(
    "h2", string=lambda text: "python" in text.lower()
)
python_job_elements = [
    h2_element.parent.parent.parent for h2_element in python_jobs
]

for job_element in python_job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    print()
    links = job_element.find_all("a")
    if len(links) > 1:  # Vérifie qu'il y a au moins deux liens
        second_link = links[1]  # Sélectionne le deuxième lien
        link_url = second_link["href"]  # Récupère l'URL du lien
        print(f"Apply here: {link_url}\n")  # Affiche l'URL

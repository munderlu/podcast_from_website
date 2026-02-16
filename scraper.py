from bs4 import BeautifulSoup
import requests

def get_latest_post(blog_url):
    response = requests.get(blog_url)
    soup = BeautifulSoup(response.content, "html.parser")
    print("Lade Daten von der Website ...")

    # Beispiel der Homepage des LUG-Kirchheim (lugkirchheim.de), muss entsprechend angepasst werden

    # URL des neusten Beitrags herausfinden
    latest_post_link_element = soup.select_one('.post-title.entry-title a')
    latest_post_url = latest_post_link_element['href']
    print(f"URL des neusten Beitrags: {latest_post_url}")

    # den neusten Beitrag abrufen
    post_response = requests.get(latest_post_url)
    post_soup = BeautifulSoup(post_response.content, 'html.parser')

    # Überschrift abrufen
    title = post_soup.select_one('.heading-wrap').get_text()
    print(f"Der Titel lautet: {title}")

    # Alle <p>-Tags abrufen
    main_soup = post_soup.select_one('.template-page.content.av-content-small.alpha.units')
    paragraphs = main_soup.find_all('p')
    text = []
    for p in paragraphs:
        text.append(p.get_text())
    print("Der Text wurde extrahiert ...")
    
    # gewonnenen Daten zurückgeben
    data = [title, text]
    return data

def save_data(data, OUTPUT_NAME):
    with open(OUTPUT_NAME, "w", encoding="utf-8)") as file:
        file.write(data[0]+"\n\n")
        for paragraph in data[1]:
            file.write(paragraph+"\n")
    print("Der Text wurde gespeichert ...")

if __name__ == "__main__":
    save_data(get_latest_post("https://lugkirchheim.de"), "text2.txt")
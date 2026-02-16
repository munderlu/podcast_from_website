from tts import *
from telegram import *
from scraper import *

URL = "https://lugkirchheim.de"
FILE_NAME = "test2.txt"
OUTPUT_NAME = "test.mp3"

# Daten von der Webseite holen und Titel verschicken
data = get_latest_post(URL)
save_data(data, FILE_NAME)
send_text(data[0])

# Audio-Datei erstellen
file = return_file(FILE_NAME)
asyncio.run(generate_and_merge(file, OUTPUT_NAME))

send_file(OUTPUT_NAME)

# Aufräumen
if os.path.exists(FILE_NAME):
    os.remove(FILE_NAME)
    print(f"Erfolg: '{FILE_NAME}' wurde gelöscht.")
else:
    print(f"Fehler: '{FILE_NAME}' wurde nicht gefunden.")

if os.path.exists(OUTPUT_NAME):
    os.remove(OUTPUT_NAME)
    print(f"Erfolg: '{OUTPUT_NAME}' wurde gelöscht.")
else:
    print(f"Fehler: '{OUTPUT_NAME}' wurde nicht gefunden.")
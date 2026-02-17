import requests
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
TOKEN_FILE = os.path.join(SCRIPT_DIR, 'token.txt')
CHAT_ID_FILE = os.path.join(SCRIPT_DIR, 'chat_id.txt')

def get_token():
    with open(TOKEN_FILE) as file:
        TOKEN = file.read().strip()
        return TOKEN

def get_chat_id():
    with open(CHAT_ID_FILE) as file:
        CHAT_ID = file.read().strip()
        return CHAT_ID

def send_text(text):
    TOKEN = get_token()
    CHAT_ID = get_chat_id()
    data = {"chat_id": CHAT_ID, "text": text}

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data = data)
    print("Text wurde gesendet.")

def send_file(FILE_PATH):
    TOKEN = get_token()
    CHAT_ID = get_chat_id()

    with open(FILE_PATH, 'rb') as f:
        files = {'document': f}
        data = {'chat_id': CHAT_ID, 'caption': 'Audiodatei'}
        url = f"https://api.telegram.org/bot{TOKEN}/sendDocument"
        
        # POST Request senden
        print("Die Datei wird gesendet ...")
        requests.post(url, data=data, files=files)
        print("Die Datei wurde gesendet.")


if __name__ == "__main__":
	send_text("Test")

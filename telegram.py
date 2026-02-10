import requests

def get_token():
    with open("token.txt") as file:
        TOKEN = file.read()
        return TOKEN

def get_chat_id():
    with open("chat_id.txt") as file:
        CHAT_ID = file.read()
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


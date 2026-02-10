import asyncio
import os
import shutil
from edge_tts import Communicate
from pydub import AudioSegment

# Konfiguration
VOICE = "de-DE-ConradNeural"  # Alternativen: de-DE-KatjaNeural, en-US-AriaNeural
MAX_CHARS = 2000              # Sicherheitslimit pro Request
OUTPUT_FILE = "fertiges_hoerbuch.mp3"
TEMP_DIR = "temp_audio_parts"

def smart_split(text, limit=MAX_CHARS):
    """
    Teilt Text in Stücke, die kleiner als das Limit sind.
    Versucht, an Satzzeichen (.!?) oder Leerzeichen zu trennen, 
    um nicht mitten im Wort abzubrechen.
    """
    chunks = []
    while len(text) > limit:
        # Suche nach dem letzten Satzzeichen innerhalb des Limits
        split_idx = -1
        
        # Versuche zuerst Satzenden zu finden (für natürliche Pausen)
        for char in ['. ', '! ', '? ', '\n']:
            idx = text.rfind(char, 0, limit)
            if idx > split_idx:
                split_idx = idx + 1 # +1 damit das Satzzeichen erhalten bleibt

        # Wenn kein Satzzeichen gefunden, suche nach dem letzten Leerzeichen
        if split_idx == -1:
            split_idx = text.rfind(' ', 0, limit)

        # Wenn gar nichts gefunden wird (ein Wort > Limit), dann hartes Limit
        if split_idx == -1:
            split_idx = limit

        chunks.append(text[:split_idx].strip())
        text = text[split_idx:].strip()
    
    # Den Rest hinzufügen
    if text:
        chunks.append(text)
        
    return chunks

async def generate_and_merge(text, output_filename):
    # 1. Temporäres Verzeichnis erstellen
    if not os.path.exists(TEMP_DIR):
        os.makedirs(TEMP_DIR)
    
    # 2. Text aufteilen
    print("Analysiere Text und teile ihn auf...")
    chunks = smart_split(text)
    print(f"Text wurde in {len(chunks)} Teile zerlegt.")

    audio_files = []

    # 3. Audio für jeden Teil generieren
    for i, chunk in enumerate(chunks):
        if not chunk: continue # Leere Chunks überspringen
        
        temp_file = os.path.join(TEMP_DIR, f"part_{i:03d}.mp3")
        print(f"Generiere Teil {i+1}/{len(chunks)} ({len(chunk)} Zeichen)...")
        
        try:
            communicate = Communicate(chunk, VOICE)
            await communicate.save(temp_file)
            audio_files.append(temp_file)
        except Exception as e:
            print(f"Fehler bei Teil {i}: {e}")
            return

    # 4. Zusammenfügen mit Pydub
    print("Füge Audiodateien zusammen...")
    combined_audio = AudioSegment.empty()
    
    for file in audio_files:
        segment = AudioSegment.from_mp3(file)
        combined_audio += segment
        # Optional: Kurze Pause zwischen den Teilen einfügen (z.B. 300ms)
        # combined_audio += AudioSegment.silent(duration=300)

    # 5. Exportieren
    combined_audio.export(output_filename, format="mp3")
    print(f"Erfolg! Datei gespeichert unter: {output_filename}")

    # 6. Aufräumen (Temp-Ordner löschen)
    shutil.rmtree(TEMP_DIR)

def return_file(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        content = file.read()
        return(content)

# --- Beispielaufruf ---
if __name__ == "__main__":
    # Ein sehr langer Beispieltext
    long_text = "Dies ist ein Test. " * 300 
    long_text += "Das ist das Ende des Textes."

    asyncio.run(generate_and_merge(long_text, OUTPUT_FILE))
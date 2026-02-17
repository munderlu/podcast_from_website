# 🎙️ Projekt: Erstellung eines Podcasts aus einer Webseite

## 1. Installation von Erweiterungen

- `edge_tts` für die Erzeugung einer Audio-Datei
- `pydub` um Audiodateien zusammenzufügen
- `beautifulsoup4` um HTML-Code von einer Webseite zu verarbeiten

### 1.1 Systemweite Installation

```bash
pip install edge_tts pydub beautifulsoup4
```

> ⚠️ Hinweis: Die systemweite Installation ist einfach, kann aber zu Versionskonflikten mit anderen Python-Projekten führen.

---

### 1.2 Installation über eine virtuelle Umgebung (empfohlen)

1. **Virtuelle Umgebung erstellen**

   ```bash
   python3 -m venv .venv
   ```

2. **Virtuelle Umgebung aktivieren**

   * **Linux / macOS**

     ```bash
     source .venv/bin/activate
     ```
   * **Windows (PowerShell)**

     ```powershell
     .venv\Scripts\Activate.ps1
     ```

3. **benötigte Pakete installieren**

   ```bash
   pip install edge_tts pydub beautifulsoup4
   ```

4. **Virtuelle Umgebung verlassen**

   ```bash
   deactivate
   ```

---

### 1.3 Installation von zusätzlich benötigten Programmen

- `ffmpeg` für die Verarbeitung von Audio- und Video-Dateien

* **Linux / macOS**

   ```bash
   sudo apt update
   sudo apt install ffmpeg
   ```
* **Windows (PowerShell)**

   ```powershell
   choco install ffmpeg
   ```
   oder über einen einfachen Download und hinzufügen zu `PATH`

## 2. Die Konfiguration
- In Telegram den `botfather` suchen, einen neuen Bot erstellen und die Chat-ID herausfinden.
- `chat_id.txt` und `token.txt` erstellen mit den jeweiligen Daten
- Konfiguration in `scraper.py` an die gewünschte Website anpassen
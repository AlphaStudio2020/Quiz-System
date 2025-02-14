## Überblick
Das **Quiz System** ist ein Discord-Bot, der es Mitgliedern ermöglicht, an einem interaktiven Quiz teilzunehmen. Teilnehmer melden sich an, erhalten einen privaten Kanal und beantworten Fragen, um das Quiz zu gewinnen.

## Funktionen
- Anmeldung zum Quiz per Befehl
- Automatische Erstellung privater Quiz-Kanäle
- Individuelle Fragen für jeden Teilnehmer
- Automatische Löschung falscher Antworten
- Gewinner-Ankündigung im Ankündigungskanal

## Voraussetzungen
- Ein Discord-Bot-Token
- Die `discord.py`-Bibliothek (Async-Version)
- Die ID des Ankündigungskanals

## Installation
1. Stelle sicher, dass Python (Version 3.8 oder höher) installiert ist.
2. Installiere die `discord.py`-Bibliothek mit folgendem Befehl:
   ```sh
   pip install discord
   ```
3. Füge den Bot zu deinem Discord-Server hinzu und aktiviere `Intents`.

## Einrichtung
1. Ersetze `TOKEN_HIER` in der Datei durch deinen Bot-Token.
2. Setze `announcement_channel_id` auf die ID des Ankündigungskanals.
3. Starte den Bot mit:
   ```sh
   python bot.py
   ```

## Anpassung
- Du kannst die Fragen direkt im `questions`-Array anpassen.
- Falls du einen anderen Befehlsprefix verwenden möchtest, ändere `command_prefix="!"` in eine andere Zeichenfolge.

## Fehlerbehebung
Falls der Bot nicht funktioniert:
- Stelle sicher, dass der Bot die richtigen Berechtigungen hat.
- Überprüfe, ob die Kanal-IDs und der Bot-Token korrekt sind.
- Falls keine privaten Kanäle erstellt werden, stelle sicher, dass der Bot die Berechtigung hat, Kanäle zu erstellen.

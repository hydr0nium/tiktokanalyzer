# tiktokanalyzer
Ein einfaches Werkzeug um die Follower und Likes von Tiktok Nutzern zu sammeln

# Vorwort:
- Das Programm benötigt etwas Zeit beim Starten
- Beim erstmaligen Starten läd das Programm Browser Driver runter. Dies kann kurz dauern
- Das Programm kann beim ersten Starten als schädlich angezeigt werden, da es nicht ein signiertes Programm von Microsoft ist
- Vorraussetzung für die Funktionsfähigkeit des Programm ist einer der Folgenden Browser: Chome, Firefox, Brave, Edge
- Die große der .exe ist damit zu erklären, dass das Kompilieren von .py zu .exe die Libraries von Python einpackt und in der .exe "verstaut"

# Installation:

Es stehen zwei mögliche Wege das Programm lauffähig zu machen. Die erste besteht darin die .exe Datei herunterzuladen. Diese sollte direkt ausführbar sein. Sollte dies nicht funktionieren gibt es Möglichkeit zwei. Zum Selbstkompilieren laden sie sich die .py Datei herunter und folgen sie dem Abschnitt "Selbst Kompilieren"

# Benutzung:

Das Programm ist recht simple gestaltet und führt sie durch die verschieden Schritte hindurch. Das Eingabeformat von der manuellen Eingabe sowie einer Datei besteht aus einer kommagetrennten List von Nutzernamen. Die verschiedenen Optionen erklärt:
- Json -> Ausgabe im JSON Format für z.B. andere Programme
- CSV -> Ausgabe im CSV Format für z.B Excel Tabellen
- Standard Ausgabe -> Ausgabe nur auf der Konsole
Die Dateien auf die sich das Programm bezieht bei Eingabe durch Datei oder in ihrer Ausgabe in einer Datei sind immer im gleichen Verzeichnis wie die .exe selbst.
## Beispiel Eingabeformat:
Wir wollen Anfragen für die Nutzer user1, user2 und user3 haben die auf Tiktok @user1, @user2 und @user3 heißen. Die Eingabelist sieht dann wie folgt aus:
```user1,user2,user3```

# Selbst Kompilieren:
- Laden sie die .py herunter
- Installieren Sie alle Dependencies der .py (siehe Imports)
- Installieren Sie pyinstaller
- Führen Sie folgenden Befehl in der Konsole aus: ```pyinstaller ./tiktokanalyzer --one-file --console```

# Verifikation der Ausführbaren Datei:
SHA-256 Hash tiktokanalyzer.exe: 286957EA97904AA8B71D86306B480366C02D2EE09A7F4530A16C3C90AFF889B2
SHA-256 Hash tiktokanalyzer.py: D18801E59F9391DCA8FA2AD60C83F29FA828016A2DCF956F1C8BBC266BCE5DCA

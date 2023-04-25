# DHBW-Survive
Im Nachfolgenden werde ich erklären, wie man das Frontend, sowie das Backend aufsetzt, welche Vorinstallationen man durchführen muss und wie mit den angewendeten Frameworks zu arbeiten ist.

## Inhalt
1. Installationen für das Backend
2. Installationen für das Frontend
3. Arbeiten mit Vue3.js in Kombination mit Tailwind

## 1.) Installationen für das Backend
Für das ausführen des Backends, müssen wir folgende Installationen durchführen:
- Python installieren
- Django installieren

Python installieren:
Um Python zu installieren, lade dir bitte die neueste Version auf der [offiziellen Python Website](https://www.python.org/downloads/) herunter und installiere die heruntergeladene Datei.
Nachdem du dies getan hast öffne ein Terminal/Kommandozeile und gebe folgenden Befehl ein:

`C:> py --version`

`Python 3.N.N` 

`C:> py -m pip --version`

`pip X.Y.Z from ... (python 3.N.N)`

Mit diesen Zeilen prüfst du, ob Python und pip Ordnungsgemäß installiert sind. Im Anschluss kannst du folgende Zeilen ausführen:

`...\> py -m pip install Django`

Damit sollte Django ordnungsgemäß installiert sein. Die Vorkehrungen für das BAckend sind somit getroffen.

## 2.) Installationen für das Frontend
Für das Frontend müssen folgende Installationen getroffen werden:
- Node.js
- Node Package Manager
- VUe3.js
- Tailwind.css

## 3.) Arbeiten mit Vue3.js in KOmbination mit Tailwind

Vue.Js arbeitet in Komponenten. 

Um dies zu verstehen schaue man am Besten im Frontend Ordner die App.vue an. Die App.vue ist quasie unsere Internetseite. auf dieser werden nun aus dem src Ordner einzelne Komponenten geladen. Dann werden diese Komponenten als HTML bzw. Vue-Tags verwendet.
Wenn es sich um Komponenten handelt werden die Dateien in den Ordner components ausgelagert. Wenn es sich allerdings um ganze Seitenelemente handelt, dann in den View Ordner.

Es gibt keine Globale CSS-Datei mehr, sondern die Komponenten erhalten direkt ihre Style eigenschaften in der .vue Datei selbst. TAilwind.css unterstützt hierbei maßgeblich, denn es 
sorgt dafür, dass man die css Eigenschaften in class="" schreibt. Die einzelnen Abkürzungen findet man zum Nachschlagen auf der Seite: [Tailwindcss.com](https://tailwindcss.com/docs/installation) 

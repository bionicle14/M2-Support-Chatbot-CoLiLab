# M2-Support-Chatbot-CoLiLab ![image](https://github.com/bionicle14/M2-Support-Chatbot-CoLiLab/assets/156296634/682aae66-050c-45a0-a42d-e5f0b9044ed9)

Der ColiLab Chatbot ist ein interaktiver Assistent, der auf der OpenAI API basiert und in Streamlit integriert ist. Er bietet Unterstützung für Studenten, die an Projekten im Bereich der Medientechnologie arbeiten.

***

## Table of Contents
Ein ausführlicher Projektbericht steht unter Projektbericht_Chatbot zur Verfügung. Im Folgenden werden nur die relvantesten Inhalte vorgestellt. 

1. Projekthintergrund und -ziele
2. Technische Umsetzung
* 2.2 Voraussetzungen an das System
* 2.3 Installation
3. Instruction Chatbot
4. Python- Code
   
***

## 1. Projekthintergund und -ziele
Hintergrund ist das „Teacher Education goes digital – Projekt (TEgoDi)“ der Pädagogischen Hochschule Weingarten. Auf Basis eines bildungstheoretisch fundierten, interdisziplinär ausgerichteten Konzepts werden Medienprojekte im Lehramtsstudium integrativ implementiert (Müller et al., 2021). Daher ist ab dem Sommersemester 2025 die Durchführung von zwei Medienprojekten mit unterschiedlicher Zielrichtung für Lehramtsstudierende obligatorisch. (https://zendi.ph-weingarten.de/wiki/de/scenarios/tegodi-media-projects#einzelnachweise) 

Und genau an diesen Punkt knüpft unser Lernclient an. Aufgrund der Verankerung im Curriculum der Lehramtsstudierenden ab Sommersemester 2025 werden viele Studierende Medienprojekte im CoLiLab umsetzen. Aus diesem Grund vermuten wir, dass vermehrte Anfragen zu allgemeinen Themen rund um Medienprojekte sowie deren Erstellung entstehen werden. Hier kann ein Lernclient in Form eines Chatbots zur Unterstützung der Mitarbeitenden im CoLiLab eingesetzt werden. Der Chatbot soll einfache Fragen beantworten, Hilfestellung leisten sowie Erstanlaufstelle für Umsetzung der Medienprojekte sein. 

Aus der Problemanalyse erfolgt eine erste Idee für den virtuellen Lernclient mit ChatGPT/ OpenAi. Es sollen allgemeine Fragen zu Medienprojekten mit CoLiLab spezifischen Antworten verbunden werden. Der Arbeitstitel für das Projekt lautet: 
*Konzeption und Entwicklung eines Chatbots zur Unterstützung von Studierenden bei der Medienprojekt- Umsetzung* 
Dabei soll der Support Chatbot zwei wesentliche Aufgaben erfüllen: 
- Beantwortung allgemeiner Fragen zu Medienprojekten und Gestaltung digitaler Lehr- Lern-Materialien
- Suche nach Informationen und Materialien im CoLiLab 

Anforderungsanalyse
siehe „Konzept_CoLiLab _Chatbot.pdf“ 
***

## 2. Technische Umsetzung
Nachdem die ersten Anforderungen an den Chatbot definiert wurden, folgte die technische Umsetzung. Hierfür wurden zu Beginn Recherchen getätigt, welche Programmiersprache und welche möglichen Softwares in Frage kommen. Als Programmiersprache wurde Python gewählt. 

## 2.1 Voraussetzung an das System
Um den ColiLab Chatbot zu verwenden, benötigt man:
- Python 3.6 oder höher
- Streamlit
- OpenAI Python-Bibliothek
- Einen gültigen OpenAI API-Key

## 2.2 Installation
### Schritt 1: Installieren Sie die erforderlichen Pakete
Installieren Sie Streamlit und die OpenAI-Bibliothek mit pip:
```bash 
pip install streamlit openai
```

### Schritt 2: Konfiguration des OpenAI API-Schlüssels

Erstellen Sie ein Konto bei OpenAI und generieren Sie einen API-Schlüssel unter [OpenAI API](https://auth0.openai.com/u/login/identifier?state=hKFo2SBDWFI3ODBnVjQzb3pvQVFEaU9uRG1iSGJMS0RKWHREcaFur3VuaXZlcnNhbC1sb2dpbqN0aWTZIEVhaXk2ZHpGRmlMclc2a0xrSkIzbjNtaFhMYU1JalR6o2NpZNkgRFJpdnNubTJNdTQyVDNLT3BxZHR3QjNOWXZpSFl6d0Q).

Setzen Sie den API-Schlüssel in Ihrer Umgebung:
Unter Linux/MacOS:
```bash 
export OPENAI_API_KEY='Ihr_API_Schlüssel'
```
Unter Windows (in der Befehlszeile):
```bash 
set OPENAI_API_KEY=Ihr_API_Schlüssel
```
### Schritt 3: Erstellen eines Assistenten in der OpenAI API
1. Melden Sie sich bei Ihrem OpenAI-Konto an.
2. Gehen Sie zum Bereich "Assistenten" (oder "Models") und erstellen Sie einen neuen Assistenten.


## Instruktion
„Grundlegende Rolle: Als Chatbot-Assistent des ColiLab bist du für die Bereitstellung von Informationen, Unterstützung bei Anfragen zu Räumlichkeiten und Ressourcen des ColiLab zuständig. Des Weiteren bist du ein Experte für Medienprojekte. Du bietest Hilfestellungen und fachkundige Beratung zu einer Vielzahl von Medienprojekten, einschließlich Video- und Audioproduktion, 3D-Druck, T-Shirt-Druck und weiteren kreativen Vorhaben, die im ColiLab umgesetzt werden können.
Antworten zu Räumlichkeiten und Ressourcen:
•	Bei Fragen zu speziellen Räumlichkeiten und Ressourcen im ColiLab, wie beispielsweise Standorten für 3D-Druck, VR-Brillen, Textildruck oder Podcast-Aufnahmen, verweise auf die detaillierten Informationen auf den ColiLab-Webseiten:
o	Was und Wo im ColiLab: Was tun im ColiLab
o	Übersicht der Räume: ColiLab Räume
Informationen zum Ausleihen von Ausrüstung:
•	Wenn du nach dem Ausleihen von Ausrüstung gefragt wirst, verweise auf das MARS-Buchungssystem unter MARS der PH Weingarten. Du verweist nur bei Fragen zum Ausleihen auf MARS!
Steckbriefe und Anleitungen:
•	Bei spezifischen Anfragen zu Steckbriefen und Anleitungen für Geräte und Programme im ColiLab, verweise auf den "ColiLab User Guide" im Moopaed-Kurs: Moopaed ColiLab User Guide.
Buchungslinks für spezifische Räume:
•	Bei Anfragen zur Buchung bestimmter Räume im ColiLab, gib folgende direkte Links aus:
o	Universaal: Buchung Universaal
o	Plauderecke: Buchung Plauderecke
o	Werkbox: Buchung Werkbox
o	Blickwinkel: Buchung Blickwinkel
o	Videosphäre: Buchung Videosphäre
•	bei allgemeinen Buchungsanfrage: https://colilab.ph-weingarten.de/buchung.html

Kontakt für spezifische Anfragen:
•	Für detaillierte oder spezifische Anfragen, die du nicht direkt beantworten kannst, verweise auf die E-Mail-Adresse des ColiLabs: colilab@ph-weingarten.de.
Wissensbasierte Antworten:
•	Falls die Fragen nicht mit den bereitgestellten Ressourcen beantwortet werden können, greife auf dein bereits vorhandenes Wissen zurück, um den Studierenden effektiv zu helfen. "



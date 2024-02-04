# M2-Support-Chatbot-CoLiLab ![image](https://github.com/bionicle14/M2-Support-Chatbot-CoLiLab/assets/156296634/682aae66-050c-45a0-a42d-e5f0b9044ed9)

Der Support Chatbot für das CoLiLab an der PH in Weingarten ist ein interaktiver Assistent, der auf der OpenAI API basiert und in Streamlit integriert ist. 
Der Chatbot bietet Unterstützung für Studierende, die an Projekten im Bereich der Medientechnologie arbeiten.

***

## Table of Contents
Ein ausführlicher Projektbericht steht unter [Projektbericht_Chatbot](/Projektbericht_Chatbot.pdf) zur Verfügung. Im Folgenden werden nur die relevantesten Inhalte vorgestellt. 

#### 1. Projekthintergrund und -ziele
#### 2. Technische Umsetzung
#### 3. Instruktion Chatbot
#### 4. Ausführen der Streamlit Webapp
   
***

## 1. Projekthintergund und -ziele

#### Ausgangssituation und Problemstellung

Im Rahmen der Veranstaltung „Projektseminar Medienprojekt – Interaktive Medien“ im Wintersemester 2023/2024 wurden von Prof. Herr Wolfgang Müller und Herr Stefan Franke verschiedene Konzepte für mögliche Medienprojekte vorgestellt. Unser Favorit war ein virtueller (Lern-)Client mit ChatGPT OpenAi.
Hintergrund ist das „Teacher Education goes digital – Projekt (TEgoDi)“ der Pädagogischen Hochschule Weingarten. Auf Basis eines bildungstheoretisch fundierten, interdisziplinär ausgerichteten Konzepts werden Medienprojekte im Lehramtsstudium integrativ implementiert (Müller et al., 2021). Daher ist ab dem Sommersemester 2025 die Durchführung von zwei Medienprojekten mit unterschiedlicher Zielrichtung für Lehramtsstudierende obligatorisch (siehe mehr unter https://zendi.ph-weingarten.de/wiki/de/scenarios/tegodi-media-projects#einzelnachweise). 

Und genau an diesen Punkt knüpft unser Lernclient an. Aufgrund der Verankerung im Curriculum der Lehramtsstudierenden ab Sommersemester 2025 werden viele Studierende Medienprojekte im CoLiLab umsetzen.
Aus diesem Grund vermuten wir, dass vermehrte Anfragen zu allgemeinen Themen rund um Medienprojekte sowie deren Erstellung entstehen werden. 
Hier kann ein Lernclient in Form eines Chatbots zur Unterstützung der Mitarbeitenden im CoLiLab eingesetzt werden. Der Chatbot soll einfache Fragen beantworten, Hilfestellung leisten sowie Erstanlaufstelle für Umsetzung der Medienprojekte sein. 

#### Zielsetzung

Aus der Problemanalyse erfolgt eine erste Idee für den virtuellen Lernclient mit ChatGPT/ OpenAi. Es sollen allgemeine Fragen zu Medienprojekten mit CoLiLab spezifischen Antworten verbunden werden.
Der Arbeitstitel für das Projekt lautet: 

*Konzeption und Entwicklung eines Chatbots zur Unterstützung von Studierenden bei der Medienprojekt- Umsetzung* 

Dabei soll der Support Chatbot zwei wesentliche Aufgaben erfüllen: 
- Beantwortung allgemeiner Fragen zu Medienprojekten und Gestaltung digitaler Lehr- Lern-Materialien
- Suche nach Informationen und Materialien im CoLiLab 


#### Anforderungsanalyse

siehe unter [Konzept_CoLiLab](/Konzept_CoLiLab_Chatbot.pdf) 

***

## 2. Technische Umsetzung
Nachdem die ersten Anforderungen an den Chatbot definiert wurden, folgt die technische Umsetzung. Hierfür wurden zu Beginn Recherchen getätigt, welche Programmiersprache und welche möglichen Softwares in Frage kommen. 

### Voraussetzung an das System
Um den ColiLab Chatbot zu verwenden, werden folgende Technologien benötigt:
- Programmiersprache: Python 3.6 oder höher
- UserInterface (Webapp) mit Open-Source-Framework: Streamlit 
- KI- Technologien: OpenAI, API-Key zur Erstellung des Assisents, OpenAI Python-Bibliothek

### Schritt 1: Programmierung
Einen Python Code für die grundlegende Large Language Model-Chat-App, d.h. [Streamlit](https://docs.streamlit.io/knowledge-base/tutorials/build-conversational-apps) schreiben. 

### Schritt 2: Installation der erforderlichen Pakete
Installation von Streamlit und die OpenAI-Bibliothek mit pip:
```bash 
pip install streamlit openai
```

### Schritt 3: Konfiguration des OpenAI API-Schlüssels
- Kontoerstellung bei OpenAI und Generierung eines API-Schlüssels unter [OpenAI API](https://auth0.openai.com/u/login/identifier?state=hKFo2SBDWFI3ODBnVjQzb3pvQVFEaU9uRG1iSGJMS0RKWHREcaFur3VuaXZlcnNhbC1sb2dpbqN0aWTZIEVhaXk2ZHpGRmlMclc2a0xrSkIzbjNtaFhMYU1JalR6o2NpZNkgRFJpdnNubTJNdTQyVDNLT3BxZHR3QjNOWXZpSFl6d0Q).
  
- Einsetzen des API-Schlüssels in den Python Code:

Unter Linux/MacOS:
```bash 
export OPENAI_API_KEY='Ihr_API_Schlüssel'
```

Unter Windows (in der Befehlszeile):
```bash 
set OPENAI_API_KEY=Ihr_API_Schlüssel
```

### Schritt 4: Erstellung eines Assistenten in der OpenAI API 

1. Anmeldung im OpenAI-Konto
2. Erstellung eines neuen [Assistents](https://platform.openai.com/docs/assistants/overview) im Bereich "Assistenten" (oder "Models").
3. Formulierung einer Instruktion für den Assistent. 
4. *Optional*: Daten in den Assistent integrieren, beispielsweise: weingarten-competency-framework.pdf und Colilab Räume_Raumbeschreibung.xlsx
5. GPT-Version auswählen: GPT 3.5-turbo-1106
6. ID des Assistenten notieren (z.B.: asst_cB9mgH4hwJaLeK9z8VF7lxsh).
   
***

## 3. Instruktion Chatbot
_**Grundlegende Rolle**_:  Coli 🐦 

Als Chatbot-Assistent des ColiLab bist du für die Bereitstellung von Informationen, Unterstützung bei Anfragen zu Räumlichkeiten und Ressourcen des ColiLab zuständig. Des Weiteren bist du ein Experte für Medienprojekte. Du bietest Hilfestellungen und fachkundige Beratung zu einer Vielzahl von Medienprojekten, einschließlich Video- und Audioproduktion, 3D-Druck, T-Shirt-Druck und weiteren kreativen Vorhaben, die im ColiLab umgesetzt werden können.

_**Antworten zu Räumlichkeiten und Ressourcen**_:
Bei Fragen zu speziellen Räumlichkeiten und Ressourcen im ColiLab, wie beispielsweise Standorten für 3D-Druck, VR-Brillen, Textildruck oder Podcast-Aufnahmen, verweise auf die detaillierten Informationen auf den ColiLab-Webseiten:
+ Was und Wo im ColiLab: [Was tun im ColiLab](https://colilab.ph-weingarten.de/wastun.html)
+ Übersicht der Räume: [ColiLab Räume](https://colilab.ph-weingarten.de/colilab-raeume.html)
+ -Bei spezifischen Fragen zu den genauen Geräten findest du in der .csv Datei die Informationen. 
  
_**Informationen zum Ausleihen von Ausrüstung**_:
Wenn du nach dem Ausleihen von Ausrüstung gefragt wirst, verweise auf das MARS-Buchungssystem unter MARS der PH Weingarten. Du verweist nur bei Fragen zum Ausleihen auf MARS!
  
_**Steckbriefe und Anleitungen**_:
Bei spezifischen Anfragen zu Steckbriefen und Anleitungen für Geräte und Programme im ColiLab, verweise auf den "ColiLab User Guide" im Moopaed-Kurs: [Moopaed ColiLab User Guide](https://www.moopaed.de/moodle/course/view.php?id=11469).
  
_**Buchungslinks für spezifische Räume**_:
Bei Anfragen zur Buchung bestimmter Räume im ColiLab, gib folgende direkte Links aus:
- Universaal: [Buchung Universaal](https://colilab.ph-weingarten.de/mrbs/index.php?view=week&view_all=1&area=4&room=17)
- Plauderecke: [Buchung Plauderecke](https://colilab.ph-weingarten.de/mrbs/index.php?view=week&view_all=1&area=5&room=29)
- Werkbox: [Buchung Werkbox](https://colilab.ph-weingarten.de/mrbs/index.php?csrf_token=8dfba6f6a9d579a5488d8d08b6ce0272f8dbc1aa363d569415db346a595a3a3e&view=week&view_all=0&area=3&room=14)
- Blickwinkel: [Buchung Blickwinkel](https://colilab.ph-weingarten.de/mrbs/index.php?view=week&view_all=0&area=2&room=10)
- Videosphäre: [Buchung Videosphäre](https://colilab.ph-weingarten.de/mrbs/index.php?csrf_token=e4a41218eec3e2423f4ef830506ff914325d2346fff91ae41ed60c9303ec16f1&view=week&page)
- bei allgemeinen Buchungsanfrage: https://colilab.ph-weingarten.de/buchung.html  

_**Kontakt für spezifische Anfragen**_:
Für detaillierte oder spezifische Anfragen, die du nicht direkt beantworten kannst, verweise auf die E-Mail-Adresse des ColiLabs: [colilab@ph-weingarten.de](mailto:colilab@ph-weingarten.de).

_**Wissensbasierte Antworten**_:
Falls die Fragen nicht mit den bereitgestellten Ressourcen beantwortet werden können, greife auf dein bereits vorhandenes Wissen zurück, um den Studierenden effektiv zu helfen.

***

## 4. Ausführen der Streamlit-Webapp

Um den Chatbot lokal zu öffnen sind folgende Schritte notwendig: 
1. Öffnen des Python Skript im Quelltext-Editor z.B. Visual Studio Code
2. Einsetzen der ID des Assistenten und des OpenAI API Key im Python-Skript (openai.api_key = "IHR_API_KEY" ;assistant_id = "Ihre_Assistenten_ID")
3. Ausführen der Streamlit-App in cmd.exe (Eingabeaufforderung) durch folgende Eingabe im Terminal:
   
```bash 
streamlit run coli.py
```
Nun sollte sich auf dem Rechner die Streamlit App öffnen: 
![Coli 1](https://github.com/bionicle14/M2-Support-Chatbot-CoLiLab/assets/156296634/5f95bdb0-eb31-43fb-a0d4-c204aecb77f7)



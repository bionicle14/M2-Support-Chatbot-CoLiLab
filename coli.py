import openai
import streamlit as st
import time

# Setzen des Assistenten-IDs
assistant_id = "asst_Xz3vACcLUqtB0ftQJsTjCAe4"

# Zugriff auf die OpenAI API
client = openai

# Initialisierung der Session-Zustände
if "start_chat" not in st.session_state:
    st.session_state.start_chat = False
if "thread_id" not in st.session_state:
    st.session_state.thread_id = None
if "messages" not in st.session_state:
    st.session_state.messages = []

# Konfiguration der Seite
st.set_page_config(page_title="Coli 🐦", page_icon=":speech_balloon:")

# Setzen des OpenAI API-Schlüssels
openai.api_key = "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"  # Setze deinen API-Schlüssel hier

# Schaltfläche zum Starten des Chats
if st.sidebar.button("Chat starten"):
    st.session_state.start_chat = True
    thread = client.beta.threads.create()
    st.session_state.thread_id = thread.id

# Titel der Seite
st.title("Coli 🐦")
st.write("Dein persönlicher Assistent im ColiLab")


# Schaltfläche zum Beenden des Chats
if st.sidebar.button("Chat beenden"):
    st.session_state.messages = []  # Löschen der Chat-Historie
    st.session_state.start_chat = False  # Zurücksetzen des Chat-Zustandes
    st.session_state.thread_id = None  # Löschen der Thread-ID

# Chat-Logik
if st.session_state.start_chat:
    # Anzeigen der bisherigen Nachrichten
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Eingabe der neuen Nachricht
    prompt = st.chat_input("Wie kann ich dir behilflich sein?")
    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Speichern der Nachricht im Thread
        client.beta.threads.messages.create(
                thread_id=st.session_state.thread_id,
                role="user",
                content=prompt
            )
        
        # Erstellen einer neuen Ausführung im Thread
        run = client.beta.threads.runs.create(
            thread_id=st.session_state.thread_id,
            assistant_id=assistant_id,
        )

        # Warten auf die Ausführung zu beenden
        while run.status != 'completed':
            time.sleep(1)
            run = client.beta.threads.runs.retrieve(
                thread_id=st.session_state.thread_id,
                run_id=run.id
            )
        messages = client.beta.threads.messages.list(
            thread_id=st.session_state.thread_id
        )

        # Anzeigen der Antworten des Assistenten
        assistant_messages_for_run = [
            message for message in messages 
            if message.run_id == run.id and message.role == "assistant"
        ]
        for message in assistant_messages_for_run:

           
           
            st.session_state.messages.append({"role": "assistant",  "content": message.content[0].text.value})

            

            with st.chat_message("assistant", avatar="🐦"):
                st.markdown(message.content[0].text.value)

else:
    st.write("Klicke links auf 'Chat starten', um den Chat zu starten.")
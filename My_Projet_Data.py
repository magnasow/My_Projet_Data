import pandas as pd
import streamlit as st

# Fonction pour charger et afficher les données
def load_and_display_data(file_path, title):
    df = pd.read_csv(file_path)
    st.write(f"Data for {title}")
    st.dataframe(df)

# Initialiser l'état des boutons si non défini
if 'display_data_1' not in st.session_state:
    st.session_state['display_data_1'] = False
if 'display_data_2' not in st.session_state:
    st.session_state['display_data_2'] = False
if 'display_data_3' not in st.session_state:
    st.session_state['display_data_3'] = False
if 'display_data_4' not in st.session_state:
    st.session_state['display_data_4'] = False
# Interface utilisateur
st.title('Data Viewer')

# Bouton pour le dataset 1
if st.button('Data for data 1'):
    st.session_state['display_data_1'] = not st.session_state['display_data_1']

if st.session_state['display_data_1']:
    load_and_display_data('data/URL_1.csv', 'data 1')

# Bouton pour le dataset 2
if st.button('Data for data 2'):
    st.session_state['display_data_2'] = not st.session_state['display_data_2']

if st.session_state['display_data_2']:
    load_and_display_data('data/URL_2.csv', 'data 2')

# Bouton pour le dataset 3
if st.button('Data for data 3'):
    st.session_state['display_data_3'] = not st.session_state['display_data_3']

if st.session_state['display_data_3']:
    load_and_display_data('data/URL_3.csv', 'data 3')

# Bouton pour le dataset 3
if st.button('Data for data 4'):
    st.session_state['display_data_4'] = not st.session_state['display_data_4']

if st.session_state['display_data_4']:
    load_and_display_data('data/URL_4.csv', 'data 4')

import streamlit as st
import pandas as pd

# Titre de l'application
st.title("Application Streamlit Simple")

# Ajouter un widget de texte
st.write("Ceci est une application de démonstration avec Streamlit.")

# Ajouter un widget de saisie de texte
user_input = st.text_input("Entrez votre nom", "")

# Afficher le nom saisi par l'utilisateur
st.write(f"Bonjour, {user_input}!")

# Ajouter un widget de graphique
import numpy as np
import matplotlib.pyplot as plt

data = np.random.randn(100)
plt.hist(data, bins=20)
st.pyplot()

# Ajouter un widget de graphique interactif
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["A", "B", "C"])
st.line_chart(chart_data)

# Ajouter un widget de carte
st.map()

# Ajouter un widget de bouton
if st.button("Cliquez ici"):
    st.write("Le bouton a été cliqué!")

# Ajouter un widget de sélection
option = st.selectbox("Choisissez une option", ["Option 1", "Option 2", "Option 3"])
st.write(f"Vous avez choisi : {option}")

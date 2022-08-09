import streamlit as st
import pandas as pd
import seaborn as sns

st.title('Penguins')

#penguins = sns.load_dataset(penguins)

penguins = sns.load_dataset('penguins')


option = st.selectbox('what penguin do you want?', ('Gentoo', 'Adelie', 'Chinstrap'))


with st.expander("PENGUINS"):
    st.table(penguins[penguins.species == option])

col1, col2, col3 = st.columns(3)

with col1:
    st.image("Image/Adelie.png", caption = 'Adelie')
with col2:
    st.image("Image/Chinstrap.png", caption = 'Chinstrap')
with col3:
    st.image("Image/Gentoo.png", caption = 'Gentoo')

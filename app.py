import streamlit as st
import streamlit.components.v1 as components

st.title("Score 10 000 To see my prediction :)")

# Path to the HTML file
html_file = "pong.html"

# Read the HTML file
with open(html_file, 'r') as f:
    html_code = f.read()
# Embed the HTML code in the Streamlit app
components.html(html_code, height=800, width=1000)

st.title("Use Space to play - maybe u need to click on game before :/")

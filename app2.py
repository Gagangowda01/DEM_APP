import streamlit as st
from groq import Groq
# title : AI Intervive Assinment
st..set_page_config(page_title = "placement practice",layout = "centred")
st.title("AI placement Assistant")
st.caption("practice and prepare for your Interviews")
try:
  client = Groq(api_key = st.secrets["GROQ_API_KEY"])
except (keyError,FileNoFound):
  st.error("API key is missing .Add it in Advance setings")
  st.stop()

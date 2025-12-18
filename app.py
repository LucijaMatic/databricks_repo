import streamlit as st
from databricks import sql

st.set_page_config(page_title="Databricks RAG Chatbot", layout="wide")

st.title("Moj RAG sustav na Databricksu 🤖 ")
st.markdown("Učitajte dokumente i postavljajte pitanja.")

def get_db_connection():
    return sql.connect(
        server_hostname=st.secrets["DATABRICKS_HOST"],
        http_path=st.secrets["DATABRICKS_HTTP_PATH"],
        access_token=st.secrets["DATABRICKS_TOKEN"]
    )

with st.sidebar:
    st.header("Admin Panel")
    uploaded_file = st.file_uploader("Dodaj novi dokument", type=['pdf', 'txt'])
    
    if uploaded_file:
        st.info(f"Datoteka {uploaded_file.name} je spremna za obradu.")
        if st.button("Pokreni Ingestion"):
            st.warning("Ovdje ćemo pozvati tvoju funkciju za chunking i embedding!")

query = st.text_input("Postavi pitanje svom modelu:")

if query:
    with st.spinner("Razmišljam..."):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            
      
            cursor.execute("SELECT current_user()")
            user = cursor.fetchone()
            
            st.success(f"Uspješno spojeno na Databricks! Korisnik: {user[0]}")
            
            cursor.close()
            conn.close()
            
        except Exception as e:
            st.error(f"Greška pri spajanju: {e}")

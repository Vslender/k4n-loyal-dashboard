import streamlit as st
import requests

st.set_page_config(page_title="K4N v5.1 LOYAL", layout="centered")
st.title("🧠 K4N v5.1 LOYAL - Painel Visual")
st.subheader("Integração com IA Leal via FastAPI")

# Botão para gerar melhoria automática
if st.button("🔁 Gerar melhoria automática"):
    try:
        response = requests.get("http://localhost:8000/melhoria")
        data = response.json()

        st.success("✅ Evolução gerada pela IA!")
        st.write(f"🔧 Área: {data['area']}")
        st.write(f"📉 Antes: {data['antes']}")
        st.write(f"📈 Depois: {data['depois']}")
        st.write(f"💎 Benefício: {data['beneficio']}")
        st.write(f"📊 Score: {data['score']}")

    except Exception as e:
        st.error("❌ Erro ao conectar com o backend.")
        st.write(e)

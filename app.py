import streamlit as st

# --- AVS LOCK: ARQUITETURA DE PODER ---
st.set_page_config(page_title="AVS ELITE | DIRETOR", page_icon="👑", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #FFFFFF; }
    .stButton>button { 
        background-color: #FFD700; color: #000; font-weight: 900; 
        font-size: 20px; border: 3px solid #000; border-radius: 0px; text-transform: uppercase;
    }
    p, span, div, h1, h2, h3 { color: #000000 !important; font-family: 'Arial', sans-serif; }
    </style>
    """, unsafe_allow_html=True)

def motor_avs_elite(p):
    return {
        "titulo": f"🏆 {p.upper()} — A SOBERANIA OLFATIVA",
        "corpo": f"O {p} é uma arma de influência social inquestionável. Engenharia árabe milimetrada para dominação absoluta.",
        "v1": f"🎬 VÍDEO 1: IMPACTO (12s | 9:16)\n\nCENA 01 (0-06s): 0-3.5s Macro borrifador / 3.5-6s {p} na palma (1:1). Fala: 'O mundo reconhece o cheiro do topo.'\n\nCENA 02 (06-12s): 6-9s {p} no mármore / 9-12s Texto Fixo: 'CHEIRO DE QUEM MANDA'.",
        "v2": f"🎬 VÍDEO 2: STATUS (12s | 9:16)\n\nCENA 01 (0-06s): 0-3s Rastro social / 3-6s Close brasão real (Escala Real).\n\nCENA 02 (06-12s): 6-9s {p} no bolso do terno / 9-12s Texto Fixo: 'ESTOQUE LIMITADO'.",
        "imgs": [
            f"📸 IMAGEM 1 (9:16): {p} escala 1:1 na palma da mão.",
            f"📸 IMAGEM 2 (9:16): {p} ao lado de relógio 42mm (Proporção).",
            f"📸 IMAGEM 3 (9:16): Macro 90% foco no selo de autenticidade."
        ],
        "txts": {
            "TIKTOK SHOP": f"O {p} é o código secreto da elite. No carrinho! 🛒",
            "INSTAGRAM": f"A estética do poder é olfativa. {p} é sua assinatura. 👑",
            "FACEBOOK": f"Para quem exige o original: {p} árabe. Autoridade convertida em rastro. 👔",
            "SITE": f"Análise técnica {p}: Projeção expansiva e fixação de 12h+."
        },
        "fixo": "💎 ITEM DE COLECIONADOR: ESTOQUE LIMITADO NO CARRINHO LARANJA.",
        "tags": f"#perfumesarabes #luxo #tiktokshop #autoridade #{p.lower().replace(' ','')} #viral"
    }

st.title("👑 AVS ELITE | DIRETOR")
produto = st.text_input("AVS START COMMAND (PRODUTO):")

if st.button("🚀 EXECUTAR PROTOCOLO"):
    if produto:
        res = motor_avs_elite(produto)
        st.header(res['titulo'])
        st.write(res['corpo'])
        st.divider()
        col1, col2, col3 = st.columns(3)
        with col1:
            st.subheader("📽️ VÍDEOS (2x 06s)")
            st.code(res['v1'], language=None)
            st.code(res['v2'], language=None)
        with col2:
            st.subheader("🎨 IMAGENS (9:16)")
            for i in res['imgs']: st.code(i, language=None)
        with col3:
            st.subheader("📱 ESTRATÉGIA")
            st.warning("MENSAGEM FIXA:")
            st.code(res['fixo'], language=None)
            for k, v in res['txts'].items():
                st.write(f"**{k}**")
                st.code(v, language=None)
            st.warning("HASHTAGS:")
            st.code(res['tags'], language=None)

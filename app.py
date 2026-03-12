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
        "v1_prompt_ia": f"PROMPT PARA IA DE VÍDEO: Cinematic 9:16, {p} perfume bottle, real scale in human hand, 4k, luxury lighting, macro spray mist 0.5x speed, no distortions, hyper-realistic.",
        "v1": f"🎬 VÍDEO 1: IMPACTO (12s | 9:16)\n\nCENA 01 (0-6s): Macro borrifador disparando. Escala Real.\nCENA 02 (6-12s): {p} na palma da mão. Texto: 'CHEIRO DE QUEM MANDA'.",
        "imgs": [
            f"📸 IMAGEM 1 (9:16): {p} escala 1:1 na palma da mão.",
            f"📸 IMAGEM 2 (9:16): {p} ao lado de relógio 42mm."
        ],
        "txts": { "TIKTOK": f"O {p} é o código secreto da elite. 🛒", "INSTA": f"Estética do poder. 👑" },
        "tags": f"#perfumesarabes #luxo #{p.lower().replace(' ','')}"
    }

st.title("👑 AVS ELITE | DIRETOR")
produto = st.text_input("AVS START COMMAND (PRODUTO):")

if st.button("🚀 EXECUTAR PROTOCOLO"):
    if produto:
        res = motor_avs_elite(produto)
        st.header(res['titulo'])
        
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("📽️ COMANDO PARA IA DE VÍDEO (COPIE)")
            st.code(res['v1_prompt_ia'], language=None) # ESTE É O COMANDO QUE EVITA O ERRO DA IA
            
            st.subheader("📽️ ROTEIRO DE EDIÇÃO")
            st.code(res['v1'], language=None)
            
        with col2:
            st.subheader("🎨 IMAGENS E TEXTOS")
            for i in res['imgs']: st.code(i, language=None)
            for k, v in res['txts'].items(): st.code(f"{k}: {v}", language=None)
            st.code(res['tags'], language=None)

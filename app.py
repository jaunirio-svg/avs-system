import streamlit as st

# --- AVS LOCK: PROTEÇÃO ESTRUTURAL E VISUAL ---
st.set_page_config(page_title="AVS ELITE | DIRETOR", page_icon="👑", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #FFFFFF; }
    .stButton>button { 
        background-color: #FFD700; color: #000; font-weight: 900; 
        font-size: 20px; border: 3px solid #000; border-radius: 0px; text-transform: uppercase;
    }
    p, span, div, h1, h2, h3, label { color: #000000 !important; font-family: 'Arial Black', sans-serif; }
    div[data-testid="stExpander"] { border: 2px solid #000 !important; border-radius: 0px; background-color: #FFF !important; }
    </style>
    """, unsafe_allow_html=True)

def gerar_avs_elite_final(p):
    return {
        "titulo": f"🏆 {p.upper()} — O CÓDIGO DA SOBERANIA",
        "corpo": f"O {p} é uma arma de influência social inquestionável. Engenharia árabe milimetrada para dominação absoluta. O rastro de quem não aceita ser ignorado.",
        
        # --- 2 VÍDEOS: 2 CENAS DE 06 SEGUNDOS (12s TOTAL) ---
        "v1": f"🎬 VÍDEO 1: IMPACTO BRUTAL (12s | 9:16)\n\nCENA 01 (0-06s): Macro do borrifador disparando névoa fina em slow motion. O frasco ocupa 50% da tela. Escala 1:1.\n\nCENA 02 (06-12s): Close lateral do {p} firme na palma da mão masculina. Texto Fixo: 'CHEIRO DE QUEM MANDA'.",
        
        "v2": f"🎬 VÍDEO 2: STATUS ABSOLUTO (12s | 9:16)\n\nCENA 01 (0-06s): Rastro social. Alguém parando o passo e virando o rosto bruscamente. Impacto imediato.\n\nCENA 02 (06-12s): Close no brasão real do {p} (Escala Real). Texto Fixo: 'ESTOQUE LIMITADO'.",
        
        # --- 3 IMAGENS: ESCALA REAL 1:1 ---
        "imgs": [
            f"📸 IMAGEM HERO (9:16): {p} em escala 1:1 na palma da mão masculina (base da palma ao topo dos dedos).",
            f"📸 IMAGEM LIFESTYLE (9:16): {p} ao lado de relógio premium 42mm para trava de percepção de tamanho.",
            f"📸 IMAGEM MACRO (9:16): Foco 90% na textura da tampa e selo holográfico de originalidade."
        ],
        
        # --- 4 TEXTOS: ELITE COPYWRITING ---
        "txts": {
            "TIKTOK SHOP": f"Pare de ser invisível. O código secreto da elite árabe chegou. {p} no carrinho laranja. 🛒",
            "INSTAGRAM": f"A estética do poder é olfativa. {p} é sua nova assinatura de autoridade. 👑",
            "FACEBOOK": f"Para quem exige o original: {p} Lattafa. Fixação bruta de 12h+. O respeito é imediato. 👔",
            "SITE GOOGLE": f"Análise Técnica {p}: Projeção expansiva de 3 metros e fixação eterna. O ápice do custo-benefício árabe."
        },
        "fixo": "💎 ITEM DE COLECIONADOR: ESTOQUE LIMITADO NO CARRINHO LARANJA.",
        "tags": f"#perfumesarabes #luxo #tiktokshop #autoridade #{p.lower().replace(' ','')} #viral"
    }

# --- INTERFACE EXECUTIVA ---
st.title("👑 AVS ELITE | DIRETOR CINEMATOGRÁFICO")
produto = st.text_input("AVS START COMMAND (PRODUTO):", value="Fakhar Black")

if st.button("🚀 EXECUTAR PROTOCOLO"):
    res = gerar_avs_elite_final(produto)
    st.header(res['titulo'])
    st.markdown(f"**{res['corpo']}**")
    st.divider()
    
    c1, c2, c3 = st.columns(3)
    with c1:
        st.subheader("📽️ VÍDEOS (2x 06s)")
        st.code(res['v1'], language=None)
        st.code(res['v2'], language=None)
    with c2:
        st.subheader("🎨 IMAGENS (9:16)")
        for i in res['imgs']: st.code(i, language=None)
    with c3:
        st.subheader("📱 ESTRATÉGIA (4)")
        st.warning("MENSAGEM FIXA:")
        st.code(res['fixo'], language=None)
        for k, v in res['txts'].items():
            st.write(f"**{k}**")
            st.code(v, language=None)
        st.code(res['tags'], language=None)

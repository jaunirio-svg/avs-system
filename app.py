import streamlit as st

# --- AVS LOCK: PROTEÇÃO ESTRUTURAL ---
st.set_page_config(page_title="AVS ELITE | DIRETOR", page_icon="👑", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #FFFFFF; }
    .stButton>button { 
        background-color: #FFD700; color: #000; font-weight: bold; 
        font-size: 20px; border: 2px solid #000; border-radius: 0px;
    }
    p, span, h1, h2, h3, div { color: #000000 !important; font-family: 'Arial', sans-serif; }
    div[data-testid="stExpander"] { border: 2px solid #000 !important; }
    .stInfo { background-color: #F0F0F0; border: 1px solid #000; color: #000; }
    </style>
    """, unsafe_allow_html=True)

def motor_diretor_avs(p):
    return {
        "titulo": f"🏆 O CÓDIGO DA SOBERANIA: {p.upper()}",
        "corpo": f"O {p} é uma arma de influência social. Engenharia árabe milimetrada para dominação absoluta. Enquanto o comum desaparece, o portador do {p} silencia o ambiente.",
        
        "v1": f"""🎬 **VÍDEO 1: IMPACTO (12s | 9:16)**
**CENA 01 (0-06s): GANCHO VISUAL**
- 0-3s: Macro do borrifador disparando. Escala Real.
- 3-6s: {p} na palma da mão (1:1). Fala: "Isso não é um perfume, é poder."

**CENA 02 (06-12s): CONVERSÃO**
- 6-9s: {p} sobre mármore. Proporção real.
- 9-12s: Texto Fixo: 'CHEIRO DE QUEM MANDA'.""",

        "v2": f"""🎬 **VÍDEO 2: STATUS (12s | 9:16)**
**CENA 01 (0-06s): REAÇÃO**
- 0-3s: Rastro olfativo. Pessoa vira o rosto (Social Proof).
- 3-6s: Close no brasão real. Tamanho real do detalhe.

**CENA 02 (06-12s): POSSE**
- 6-9s: {p} entrando no bolso interno do terno.
- 9-12s: Texto Fixo: 'SINTA O PESO DO OURO'.""",

        "imgs": [
            f"📸 **IMAGEM 1 (9:16):** {p} na palma da mão (Escala 1:1).",
            f"📸 **IMAGEM 2 (9:16):** {p} ao lado de relógio 42mm (Proporção).",
            f"📸 **IMAGEM 3 (9:16):** Close 90% foco no selo de realeza."
        ],
        
        "txts": {
            "TikTok": f"O {p} é o código secreto da elite. No carrinho laranja! 🛒",
            "Instagram": f"A estética do poder é olfativa. {p} é sua assinatura. 👑",
            "Facebook": f"Perfume árabe original: {p}. Autoridade imediata. 👔",
            "Site": f"Dossiê {p}: Projeção marcante e fixação de 12h+."
        },
        
        "fixo": "💎 ITEM DE COLECIONADOR: ESTOQUE LIMITADO.",
        "tags": f"#perfumesarabes #luxo #tiktokshop #{p.lower().replace(' ','')} #viral"
    }

st.title("👑 AVS ELITE | DIRETOR CINEMATOGRÁFICO")
produto = st.text_input("AVS START COMMAND (PRODUTO):")

if st.button("🚀 EXECUTAR PROTOCOLO"):
    if produto:
        res = motor_diretor_avs(produto)
        st.header(res['titulo'])
        st.write(res['corpo'])
        st.divider()
        
        c1, c2, c3 = st.columns(3)
        with c1:
            st.subheader("📽️ VÍDEOS (2x 06s)")
            with st.expander("VÍDEO 1", expanded=True): st.write(res['v1'])
            with st.expander("VÍDEO 2", expanded=True): st.write(res['v2'])
        with c2:
            st.subheader("🎨 IMAGENS (9:16)")
            for i in res['imgs']: st.info(i)
        with c3:
            st.subheader("📱 TEXTOS (4)")
            st.warning(f"📌 {res['fixo']}")
            for k, v in res['txts'].items():
                with st.expander(k, expanded=True): st.write(v)
            st.code(res['tags'])

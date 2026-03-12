import streamlit as st

# --- AVS LOCK: ARQUITETURA DE PODER ---
st.set_page_config(page_title="AVS ELITE | DIRETOR", page_icon="👑", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #FFFFFF; }
    .stButton>button { 
        background-color: #FFD700; color: #000; font-weight: 900; 
        font-size: 20px; border: 3px solid #000; border-radius: 0px;
        text-transform: uppercase;
    }
    p, span, div { color: #000000 !important; font-size: 16px; font-weight: 500; }
    div[data-testid="stExpander"] { border: 1px solid #000 !important; border-radius: 0px; }
    </style>
    """, unsafe_allow_html=True)

def motor_avs_elite(p):
    return {
        "titulo": f"🏆 {p.upper()} — A SOBERANIA OLFATIVA",
        "corpo": f"O {p} é uma arma de influência social inquestionável. Engenharia árabe milimetrada para quem domina o ambiente.",
        "v1": f"🎬 VÍDEO 1: IMPACTO BRUTAL (12s | 9:16)\n\nCENA 01 (0-06s): O GANCHO DE AUTORIDADE\n- 0.0s - 3.0s: Macro do borrifador. Névoa densa em slow motion. Escala 1:1.\n- 3.0s - 6.0s: {p} na palma da mão masculina. Movimento de firmeza. Fala: 'O mundo reconhece o cheiro do topo.'\n\nCENA 02 (06-12s): A CONVERSÃO DE STATUS\n- 6.0s - 9.0s: {p} sobre mármore. Proporção real.\n- 9.0s - 12.0s: Texto Fixo: 'CHEIRO DE QUEM MANDA'. Fala: 'Assuma o controle agora.'",
        "v2": f"🎬 VÍDEO 2: O INSTINTO DE POSSE (12s | 9:16)\n\nCENA 01 (0-06s): PROVA SOCIAL\n- 0.0s - 3.0s: Rastro do {p}. Alguém parando bruscamente para sentir.\n- 3.0s - 6.0s: Close no brasão metálico do {p}. Nitidez absoluta. Escala Real.\n\nCENA 02 (06-12s): O FECHAMENTO DE ELITE\n- 6.0s - 9.0s: Guardando o frasco no bolso interno do terno.\n- 9.0s - 12.0s: Texto Fixo: 'ESTOQUE LIMITADO'. Fala: 'Decida ser inesquecível.'",
        "imgs": [
            f"📸 IMAGEM 1 (9:16): {p} em escala real na palma da mão.",
            f"📸 IMAGEM 2 (9:16): {p} ao lado de relógio de luxo. Proporção real.",
            f"📸 IMAGEM 3 (9:16): Macro 90% foco no selo de autenticidade."
        ],
        "textos": {
            "TIKTOK SHOP": f"O {p} é o código secreto da elite. Se você não busca o topo, não use. 🛒",
            "INSTAGRAM": f"A estética do poder é olfativa. {p} é sua nova assinatura. 👑",
            "FACEBOOK": f"Para quem exige o original: {p} árabe. Autoridade convertida em rastro. 👔",
            "SITE": f"Análise técnica {p}: Projeção expansiva e fixação de 12h+."
        },
        "fixo": "💎 ITEM DE COLECIONADOR: ESTOQUE LIMITADO NO CARRINHO LARANJA.",
        "tags": f"#perfumesarabes #luxo #tiktokshop #autoridade #{p.lower().replace(' ','')} #viral"
    }

# --- INTERFACE ---
st.title("👑 AVS ELITE | DIRETOR")
produto = st.text_input("AVS START COMMAND (PRODUTO):")

if st.button("🚀 EXECUTAR PROTOCOLO"):
    if produto:
        res = motor_avs_elite(produto)
        st.header(res['titulo'])
        st.markdown(f"**{res['corpo']}**")
        st.divider()
        
        c1, c2, c3 = st.columns(3)
        
        with c1:
            st.subheader("📽️ VÍDEOS (2x 06s)")
            st.code(res['v1'], language=None) # O st.code já vem com botão de copiar automático
            st.code(res['v2'], language=None)

        with c2:
            st.subheader("🎨 IMAGENS (9:16)")
            for i in res['imgs']:
                st.code(i, language=None)

        with col3 if 'col3' in locals() else c3:
            st.subheader("📱 ESTRATÉGIA")
            st.warning("MENSAGEM FIXA:")
            st.code(res['fixo'], language=None)
            
            for k, v in res['textos'].items():
                st.write(f"**{k}**")
                st.code(v, language=None)
            
            st.warning("HASHTAGS:")
            st.code(res['tags'], language=None)

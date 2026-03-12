import streamlit as st

# --- AVS LOCK: ARQUITETURA DE PODER ---
st.set_page_config(page_title="AVS ELITE | DIRETOR", page_icon="👑", layout="wide")

st.markdown("""
    <style>
    /* Estética Minimalista de Luxo: Branco Absoluto e Preto Puro */
    .main { background-color: #FFFFFF; }
    .stButton>button { 
        background-color: #FFD700; color: #000; font-weight: 900; 
        font-size: 22px; border: 3px solid #000; border-radius: 0px;
        text-transform: uppercase; letter-spacing: 2px;
    }
    h1, h2, h3 { color: #000 !important; font-family: 'Times New Roman', serif; text-transform: uppercase; letter-spacing: 3px; }
    p, span, div { color: #000000 !important; font-size: 18px; font-weight: 500; }
    div[data-testid="stExpander"] { border: 2px solid #000 !important; border-radius: 0px; background-color: #FFF !important; }
    .stInfo { background-color: #F2F2F2; border: 1px solid #000; border-radius: 0px; color: #000; }
    </style>
    """, unsafe_allow_html=True)

def motor_avs_elite(p):
    return {
        "titulo": f"🏆 {p.upper()} — A SOBERANIA OLFATIVA",
        "corpo": f"O {p} é uma arma de influência social inquestionável. Engenharia árabe milimetrada para quem domina o ambiente. Enquanto a maioria desaparece na multidão, o portador do {p} impõe sua presença em silêncio.",
        
        "v1": f"""🎬 **VÍDEO 1: IMPACTO BRUTAL (12s | 9:16)**

**CENA 01 (0-06s): O GANCHO DE AUTORIDADE**
- 0.0s - 3.0s: Close macro no borrifador. Névoa densa em slow motion. Escala 1:1.
- 3.0s - 6.0s: {p} na palma da mão masculina. Movimento de firmeza. Fala: "O mundo reconhece o cheiro do topo."

**CENA 02 (06-12s): A CONVERSÃO DE STATUS**
- 6.0s - 9.0s: {p} sobre superfície de mármore. Proporção real ao olho humano.
- 9.0s - 12.0s: Texto Fixo: 'CHEIRO DE QUEM MANDA'. Fala: "Assuma o controle agora." """,

        "v2": f"""🎬 **VÍDEO 2: O INSTINTO DE POSSE (12s | 9:16)**

**CENA 01 (0-06s): PROVA SOCIAL**
- 0.0s - 3.0s: Rastro do {p}. Alguém parando bruscamente para sentir. Impacto imediato.
- 3.0s - 6.0s: Close no brasão metálico do {p}. Nitidez absoluta. Escala Real.

**CENA 02 (06-12s): O FECHAMENTO DE ELITE**
- 6.0s - 9.0s: Guardando o frasco no bolso interno do terno. Movimento milimetrado.
- 9.0s - 12.0s: Texto Fixo: 'ESTOQUE LIMITADO'. Fala: "Decida ser inesquecível." """,

        "imgs": [
            f"📸 **IMAGEM 1 (9:16):** {p} em escala real na palma da mão. Foco na autoridade do porte.",
            f"📸 **IMAGEM 2 (9:16):** {p} ao lado de relógio de luxo. Trava de proporcionalidade humana.",
            f"📸 **IMAGEM 3 (9:16):** Macro 90% foco no selo de autenticidade. Estética de joalheria."
        ],
        
        "textos": {
            "TIKTOK SHOP": f"O {p} é o código secreto da elite. Se você não busca o topo, não use. 🛒",
            "INSTAGRAM": f"A estética do poder é olfativa. {p} é sua nova assinatura. 👑",
            "FACEBOOK": f"Para quem exige o original: {p} árabe. Autoridade convertida em rastro. 👔",
            "SITE": f"Análise técnica {p}: Projeção expansiva e fixação de 12h+. Desempenho excepcional."
        },
        
        "fixo": "💎 ITEM DE COLECIONADOR: ESTOQUE LIMITADO NO CARRINHO LARANJA.",
        "tags": f"#perfumesarabes #luxo #tiktokshop #autoridade #{p.lower().replace(' ','')} #viral"
    }

# --- AVS START COMMAND ---
st.title("👑 AVS ELITE | DIRETOR CINEMATOGRÁFICO")
produto = st.text_input("AVS START COMMAND (PRODUTO):", placeholder="DIGITE O NOME DO PERFUME...")

if st.button("🚀 EXECUTAR PROTOCOLO"):
    if produto:
        res = motor_avs_elite(produto)
        st.header(res['titulo'])
        st.markdown(f"**{res['corpo']}**")
        st.divider()
        
        c1, c2, c3 = st.columns(3)
        with c1:
            st.subheader("📽️ VÍDEOS (2x 06s)")
            with st.expander("VÍDEO 1: IMPACTO", expanded=True): st.write(res['v1'])
            with st.expander("VÍDEO 2: STATUS", expanded=True): st.write(res['v2'])
        with c2:
            st.subheader("🎨 IMAGENS (9:16)")
            for i in res['imgs']: st.info(i)
        with c3:
            st.subheader("📱 ESTRATÉGIA")
            st.warning(f"📌 {res['fixo']}")
            for k, v in res['textos'].items():
                with st.expander(k, expanded=True): st.write(v)
            st.code(res['tags'])

import streamlit as st

# --- 04_AVS_LOCK: ARQUITETURA IMUTÁVEL ---
st.set_page_config(page_title="AVS PACKAGE V1.0", page_icon="📦", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #FFFFFF; }
    .stButton>button { 
        background-color: #FFD700; color: #000; font-weight: 900; 
        font-size: 20px; border: 3px solid #000; border-radius: 0px; text-transform: uppercase;
    }
    h1, h2, h3, p, span, div { color: #000000 !important; font-family: 'Arial Black', sans-serif; }
    </style>
    """, unsafe_allow_html=True)

def motor_avs_total(p):
    return {
        "titulo": f"🏆 {p.upper()} — SOBERANIA E MOVIMENTO",
        "v1": f"🎬 VÍDEO 1: IMPACTO CINÉTICO (12s | 9:16)\n\nCENA 01 (0-06s): GANCHO\n- 0-2s: Zoom In rápido borrifador (Escala 1:1).\n- 2-4s: Corte orbital (360º) frasco.\n- 4-6s: Push aproximação logo.\nFala: 'Isso não é um perfume, é seu novo código.'\n\nCENA 02 (06-12s): AÇÃO\n- 6-8s: Mão masculina pegando frasco (Rápido).\n- 8-10s: Shake câmera close líquido.\n- 10-12s: Texto pulsante: CARRINHO LARANJA.\nFala: 'Domine o ambiente agora.'",
        "v2": f"🎬 VÍDEO 2: STATUS EM MOVIMENTO (12s | 9:16)\n\nCENA 01 (0-06s): TRACKING\n- 0-3s: Câmera seguindo caminhada.\n- 3-6s: Snap Cut reação social rastro.\nFala: 'Impossível de ignorar.'\n\nCENA 02 (06-12s): FECHAMENTO\n- 6-9s: Movimento Handheld guardando no terno.\n- 9-12s: Zoom Out luxo + Texto: LINK NA BIO.\nFala: 'Ouro árabe. Estoque limitado.'",
        "imgs": [
            f"📸 HERO (9:16): {p} escala 1:1 na palma da mão (Base ao topo dos dedos).",
            f"📸 LIFESTYLE (9:16): {p} ao lado de relógio 42mm (Trava de proporção).",
            f"📸 MACRO (9:16): Foco 90% na tampa metálica e selo de realeza."
        ],
        "txts": {
            "TIKTOK SHOP": f"O algoritmo vai parar para este rastro. {p} no carrinho laranja! 🛒",
            "INSTAGRAM": f"A estética do poder é olfativa. {p} é sua nova assinatura. 👑",
            "FACEBOOK": f"Para quem exige o original: {p} árabe. Autoridade e fixação bruta. 👔",
            "SITE (A HISTÓRIA DO MITO)": f"📜 O DESPERTAR DE {p.upper()}\n\nNascido nas dunas do Oriente, o {p} não foi criado para agradar a todos, mas para destacar os poucos que lideram. Cada nota desta fragrância conta a história de uma conquista. Das notas de topo que impõem respeito imediato, ao fundo amadeirado que deixa um rastro de mistério e herança. Portar o {p} é carregar séculos de tradição árabe em uma engenharia moderna de sedução e poder. Não é apenas um perfume; é o registro olfativo da sua vitória."
        },
        "fixo": "💎 ITEM DE COLECIONADOR: ESTOQUE LIMITADO NO CARRINHO LARANJA.",
        "tags": f"#perfumesarabes #luxo #tiktokshop #autoridade #{p.lower().replace(' ','')} #viral"
    }

st.title("📦 AVS PACKAGE | DIRETOR")
produto = st.text_input("AVS START COMMAND (PRODUTO):")

if st.button("🚀 EXECUTAR PROTOCOLO COMPLETO"):
    if produto:
        res = motor_avs_total(produto)
        st.header(res['titulo'])
        st.divider()
        
        c1, c2, c3 = st.columns(3)
        with c1:
            st.subheader("📽️ VÍDEOS (MOVIMENTO)")
            st.code(res['v1'], language=None)
            st.code(res['v2'], language=None)
        with c2:
            st.subheader("🎨 IMAGENS (9:16)")
            for i in res['imgs']: st.code(i, language=None)
        with c3:
            st.subheader("📱 ESTRATÉGIA")
            st.warning("MENSAGEM FIXA")
            st.code(res['fixo'], language=None)
            for rede, texto in res['txts'].items():
                st.write(f"**{rede}**")
                st.code(texto, language=None)
            st.write("**HASHTAGS**")
            st.code(res['tags'], language=None)

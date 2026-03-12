import streamlit as st

# --- 04_AVS_LOCK: ARQUITETURA IMUTÁVEL ---
st.set_page_config(page_title="AVS PACKAGE V1.0", page_icon="📦", layout="centered")

# CSS para forçar visibilidade total no celular (Mobile First)
st.markdown("""
    <style>
    /* Força fundo branco e texto preto mesmo no modo escuro do celular */
    .stApp { background-color: #FFFFFF !important; }
    h1, h2, h3, p, span, div, label { color: #000000 !important; font-family: 'Arial Black', sans-serif; }
    
    /* Botão Dourado de Alta Visibilidade */
    .stButton>button { 
        background-color: #FFD700 !important; color: #000 !important; 
        font-weight: 900 !important; width: 100%; height: 3em;
        border: 3px solid #000 !important; border-radius: 5px !important;
    }
    
    /* Blocos de código com bordas visíveis */
    div[data-testid="stCodeBlock"] { border: 2px solid #000 !important; }
    </style>
    """, unsafe_allow_html=True)

def motor_avs_total(p):
    return {
        "titulo": f"🏆 {p.upper()} — SOBERANIA",
        "v1": f"🎬 VÍDEO 1 (12s | 9:16)\n\nCENA 01 (0-6s): GANCHO\n- 0-2s: Zoom In rápido borrifador (Escala 1:1).\n- 2-4s: Corte orbital 360º.\n- 4-6s: Push aproximação logo.\nFala: 'Isso não é um perfume, é seu novo código.'\n\nCENA 02 (06-12s): AÇÃO\n- 6-8s: Mão pegando frasco (Rápido).\n- 8-10s: Shake câmera close líquido.\n- 10-12s: Texto: CARRINHO LARANJA.\nFala: 'Domine o ambiente agora.'",
        "v2": f"🎬 VÍDEO 2 (12s | 9:16)\n\nCENA 01 (0-6s): TRACKING\n- 0-3s: Câmera seguindo caminhada.\n- 3-6s: Snap Cut reação rastro.\nFala: 'Impossível de ignorar.'\n\nCENA 02 (06-12s): FECHAMENTO\n- 6-9s: Guardando no terno.\n- 9-12s: Zoom Out + Texto: LINK NA BIO.\nFala: 'Ouro árabe. Estoque limitado.'",
        "imgs": [
            f"📸 HERO (9:16): {p} escala 1:1 na palma da mão.",
            f"📸 LIFESTYLE (9:16): {p} ao lado de relógio 42mm.",
            f"📸 MACRO (9:16): Foco 90% selo de realeza."
        ],
        "txts": {
            "TIKTOK SHOP": f"O algoritmo vai parar para este rastro. {p} no carrinho laranja! 🛒",
            "INSTAGRAM": f"A estética do poder é olfativa. {p} é sua nova assinatura. 👑",
            "FACEBOOK": f"Para quem exige o original: {p} árabe. Autoridade e fixação bruta. 👔",
            "SITE (HISTÓRIA DO MITO)": f"📜 O DESPERTAR DE {p.upper()}\n\nNascido nas dunas do Oriente, o {p} não foi criado para agradar a todos, mas para destacar os poucos que lideram. Cada nota desta fragrância conta a história de uma conquista. Das notas de topo que impõem respeito imediato, ao fundo amadeirado que deixa um rastro de mistério e herança. Portar o {p} é carregar séculos de tradição árabe. Não é apenas um perfume; é o registro olfativo da sua vitória."
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
        
        # No celular, as colunas vão se empilhar automaticamente
        st.subheader("📽️ VÍDEOS (MOVIMENTO)")
        st.code(res['v1'], language=None)
        st.code(res['v2'], language=None)
        
        st.divider()
        st.subheader("🎨 IMAGENS (9:16)")
        for i in res['imgs']: st.code(i, language=None)
        
        st.divider()
        st.subheader("📱 ESTRATÉGIA")
        st.warning("MENSAGEM FIXA")
        st.code(res['fixo'], language=None)
        for rede, texto in res['txts'].items():
            st.write(f"**{rede}**")
            st.code(texto, language=None)
        st.write("**HASHTAGS**")
        st.code(res['tags'], language=None)

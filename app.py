import streamlit as st

# --- AVS LOCK: ARQUITETURA DE PODER ---
st.set_page_config(page_title="AVS ELITE | DINÂMICO", page_icon="👑", layout="wide")

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

def gerar_avs_dinamico(p):
    return {
        "titulo": f"🏆 {p.upper()} — DINAMISMO ABSOLUTO",
        "v1": f"""🎬 VÍDEO 1: IMPACTO CINÉTICO (12s | 9:16)

CENA 01 (0-06s): O GANCHO (MOVIMENTO CONSTANTE)
- 0-2s: Zoom In rápido no borrifador + disparo de névoa (Escala 1:1).
- 2-4s: Corte para rotação orbital (360º) em torno do frasco.
- 4-6s: Movimento de 'Push' (aproximação) em direção ao logo.
Fala: "Isso não é um perfume, é o seu novo código de conduta."

CENA 02 (06-12s): A POSSE (CORTES RÁPIDOS)
- 6-8s: Mão masculina pegando o frasco com firmeza (Ação rápida).
- 8-10s: Shake de câmera leve enquanto o líquido balança dentro do vidro.
- 10-12s: Texto pulsante na tela: 'CARRINHO LARANJA'.
Fala: "Domine o ambiente antes de dizer uma palavra." """,

        "v2": f"""🎬 VÍDEO 2: STATUS EM MOVIMENTO (12s | 9:16)

CENA 01 (0-06s): REAÇÃO E TRACKING
- 0-3s: Câmera seguindo (Tracking) você caminhando. O rastro visual da fragrância.
- 3-6s: Close de reação: Pessoa vira o rosto bruscamente (Snap Cut).
Fala: "Invisível aos olhos, impossível de ignorar."

CENA 02 (06-12s): O FECHAMENTO (HANDHELD STYLE)
- 6-9s: Câmera na mão (estilo vblog de luxo) guardando o {p} no terno. Movimento orgânico.
- 9-12s: Zoom Out rápido revelando o cenário de luxo + Texto: 'LINK NA BIO'.
Fala: "Ouro árabe. Estoque limitado." """,

        "imgs": [
            f"📸 IMAGEM 1 (9:16): {p} em escala 1:1 sendo retirado de uma caixa premium (Ação capturada).",
            f"📸 IMAGEM 2 (9:16): Close no borrifador com gotas reais de água/perfume para textura.",
            f"📸 IMAGEM 3 (9:16): Lifestyle dinâmico: Perfume no console de um carro de luxo."
        ],
        "txts": {
            "TIKTOK": f"O algoritmo vai parar para este rastro. {p} no carrinho! 🛒",
            "INSTAGRAM": f"Movimento, status e autoridade. {p} é a escolha. 👑"
        },
        "tags": f"#perfumesarabes #luxo #tiktokshop #viral #{p.lower().replace(' ','')}"
    }

st.title("👑 AVS ELITE | DIRETOR DE MOVIMENTO")
produto = st.text_input("AVS START COMMAND (PRODUTO):")

if st.button("🚀 EXECUTAR PROTOCOLO DINÂMICO"):
    if produto:
        res = gerar_avs_dinamico(produto)
        st.header(res['titulo'])
        st.divider()
        c1, c2, c3 = st.columns(3)
        with c1:
            st.subheader("📽️ VÍDEOS (MOVIMENTO ATIVO)")
            st.code(res['v1'], language=None)
            st.code(res['v2'], language=None)
        with c2:
            st.subheader("🎨 IMAGENS (AÇÃO)")
            for i in res['imgs']: st.code(i, language=None)
        with c3:
            st.subheader("📱 ESTRATÉGIA")
            for k, v in res['txts'].items():
                st.write(f"**{k}**")
                st.code(v, language=None)
            st.code(res['tags'], language=None)

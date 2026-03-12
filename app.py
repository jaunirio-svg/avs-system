import streamlit as st

# --- 04_AVS_LOCK: ARQUITETURA IMUTÁVEL ---
st.set_page_config(page_title="AVS PACKAGE V1.0", page_icon="📦", layout="wide")

# CSS ADAPTÁVEL: Funciona em Dark Mode e Light Mode automaticamente
st.markdown("""
    <style>
    /* Estilização do Botão de Execução */
    .stButton>button { 
        background-color: #FFD700 !important; 
        color: #000000 !important; 
        font-weight: 900 !important; 
        width: 100%; 
        border: 2px solid #000 !important;
        border-radius: 8px !important;
    }
    
    /* Ajuste dos blocos de código para não sumirem no celular */
    div[data-testid="stCodeBlock"] {
        border: 2px solid #FFD700 !important;
        border-radius: 10px !important;
    }

    /* Melhora a leitura em telas pequenas (Mobile) */
    @media (max-width: 640px) {
        .main .block-container { padding: 10px !important; }
        h1 { font-size: 1.5rem !important; }
    }
    </style>
    """, unsafe_allow_html=True)

def motor_avs_total(p):
    return {
        "titulo": f"🏆 {p.upper()} — SOBERANIA E MOVIMENTO",
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
produto = st.text_input("AVS START COMMAND (PRODUTO):", placeholder="Nome do perfume...")

if st.button("🚀 EXECUTAR PROTOCOLO COMPLETO"):
    if produto:
        res = motor_avs_total(produto)
        st.header(res['titulo'])
        st.divider()
        
        # Estrutura em abas para economizar espaço no celular e organizar no notebook
        tab1, tab2, tab3 = st.tabs(["📽️ VÍDEOS", "🎨 IMAGENS", "📱 ESTRATÉGIA"])
        
        with tab1:
            st.code(res['v1'], language=None)
            st.code(res['v2'], language=None)
            
        with tab2:
            for i in res['imgs']:
                st.code(i, language=None)
                
        with tab3:
            st.write("📌 **MENSAGEM FIXA**")
            st.code(res['fixo'], language=None)
            for rede, texto in res['txts'].items():
                st.write(f"**{rede}**")
                st.code(texto, language=None)
            st.write("🏷️ **HASHTAGS**")
            st.code(res['tags'], language=None)

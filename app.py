import streamlit as st

# --- DESIGN DE ALTA PERFORMANCE ---
st.set_page_config(page_title="AVS ELITE SYSTEM", page_icon="👑", layout="wide")
st.markdown("""
    <style>
    .main { background-color: #F8F9FA; }
    .stButton>button { 
        background-color: #000000; color: #FFD700; font-weight: bold; 
        font-size: 22px; border-radius: 2px; border: 2px solid #FFD700; height: 3.5em; 
    }
    h1, h2, h3 { color: #000000 !important; font-family: 'Playfair Display', serif; text-transform: uppercase; letter-spacing: 2px; }
    .stExpander { background-color: #FFFFFF !important; border: 2px solid #000000 !important; }
    p { color: #1A1A1A !important; font-size: 18px; line-height: 1.6; }
    </style>
    """, unsafe_allow_html=True)

def gerar_avs_excepcional(p):
    return {
        "titulo": f"🏆 O CÓDIGO DA SOBERANIA: {p.upper()} – A FRAGRÂNCIA QUE SILENCIA AMBIENTES.",
        "corpo": f"""O {p} não é apenas um perfume, é uma arma de influência social. 
        Enquanto o homem comum usa fragrâncias que desaparecem em minutos, o portador do {p} deixa um rastro de mistério e autoridade que permanece na memória por horas. 
        Este é o ápice da engenharia árabe: uma explosão de especiarias finas que evolui para uma base amadeirada densa, projetada para quem não aceita ser ignorado. 
        Se você busca ser 'apenas mais um', este conteúdo não é para você. Mas se você busca o topo, o {p} é sua nova assinatura de poder.""",
        "v1": f"🎬 **CINEMATOGRAFIA 1 (O IMPACTO):**\n0-3s: Close no borrifador soltando a névoa em câmera lenta.\n3-9s: Transição rápida de uma roupa casual para um terno segurando o {p}.\n9-12s: Texto fixo na tela: 'Cheiro de quem manda'.",
        "v2": f"🎬 **CINEMATOGRAFIA 2 (A TENTAÇÃO):**\n0-3s: Reação de uma mulher parando o passo para sentir o rastro.\n3-9s: O frasco do {p} iluminado por luz dourada sobre mármore preto.\n9-12s: Texto fixo: 'Sinta o peso do ouro árabe'.",
        "msg_fixa": "💎 ITEM DE COLECIONADOR - ESTOQUE LIMITADO NO CARRINHO LARANJA.",
        "hashtags": f"#perfumesarabes #luxomasculino #perfumaria #modahomem #{p.lower().replace(' ','')}"
    }

st.title("👑 AVS ELITE | MÁQUINA DE DESEJO")
produto = st.text_input("INSIRA O NOME DO PRODUTO PARA ELEVAR O PADRÃO:", placeholder="Ex: Lattafa Asad")

if st.button("🚀 ATIVAR PROTOCOLO EXCEPCIONAL"):
    if produto:
        res = gerar_avs_excepcional(produto)
        st.success(f"Sistema Gerou Conteúdo de Superioridade para {produto}")

        # --- TITULO E CORPO EXTRAORDINÁRIOS ---
        st.markdown(f"## {res['titulo']}")
        with st.container():
            st.markdown(f"**{res['corpo']}**")
        
        st.divider()

        col1, col2 = st.columns(2)
        with col1:
            st.subheader("📽️ ROTEIROS CINEMATOGRÁFICOS")
            with st.expander("VÍDEO 1 - O IMPACTO", expanded=True): st.write(res["v1"])
            with st.expander("VÍDEO 2 - A TENTAÇÃO", expanded=True): st.write(res["v2"])

        with col2:
            st.subheader("📱 ESTRATÉGIA DE REDE")
            st.info(f"**📌 MENSAGEM FIXA:** {res['msg_fixa']}")
            st.warning(f"**🔥 5# VIRAIS:** {res['hashtags']}")
            
            with st.expander("COPYWRITING TIKTOK SHOP", expanded=True):
                st.write(f"Você não está comprando um perfume. Está comprando o respeito imediato. O {produto} é o segredo dos 1%. Clique no link e mude seu jogo.")

    else:
        st.error("Digite o nome da joia.")

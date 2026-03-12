import streamlit as st

# --- DESIGN DE ALTA PERFORMANCE (BRANCO E PRETO) ---
st.set_page_config(page_title="AVS ELITE SYSTEM", page_icon="👑", layout="wide")

st.markdown("""
    <style>
    /* Fundo Branco e Texto Preto Puro para Leitura Máxima */
    .main { background-color: #FFFFFF; color: #000000; }
    
    /* Botão Amarelo Impactante */
    .stButton>button { 
        background-color: #FFD700; color: #000000; font-weight: bold; 
        font-size: 20px; border-radius: 5px; border: 2px solid #000000; height: 3.5em; 
    }
    
    /* Campos de Conteúdo com Fundo Branco e Borda Preta */
    div[data-testid="stExpander"] { 
        background-color: #FFFFFF !important; 
        border: 2px solid #000000 !important; 
        border-radius: 0px; 
    }
    
    /* Forçar todas as fontes para Preto */
    p, span, label, h1, h2, h3, div { color: #000000 !important; font-family: 'Arial', sans-serif; }
    
    .stInfo { background-color: #F0F0F0; border: 1px solid #000; color: black; }
    </style>
    """, unsafe_allow_html=True)

# --- MOTOR DE INTELIGÊNCIA SUPERIOR ---
def gerar_avs_excepcional(p):
    return {
        "titulo_extraordinario": f"🏆 O CÓDIGO DA SOBERANIA: {p.upper()} – A FRAGRÂNCIA QUE SILENCIA AMBIENTES.",
        "corpo_superior": f"""O {p} não é apenas um perfume, é uma arma de influência social e dominação olfativa. Enquanto o homem comum se perde em fragrâncias genéricas que desaparecem em minutos, o portador desta joia árabe deixa um rastro de mistério e autoridade inquestionável. Este é o ápice da engenharia de luxo: uma explosão de especiarias raras que evolui para uma base amadeirada densa, projetada especificamente para quem não aceita ser ignorado. Se você busca ser 'apenas mais um', este conteúdo não é para você. Mas se você busca o topo da hierarquia, o {p} é sua nova assinatura de poder absoluta.""",
        "v1": f"🎬 **CINEMATOGRAFIA 1 (O IMPACTO):**\n- **0-3s:** Close macro no borrifador soltando a névoa sob luz dramática. Som de grave profundo.\n- **3-9s:** Corte seco do {p} sendo colocado sobre uma mesa de mármore. Legenda: 'Existem perfumes. E existe o {p}.'\n- **9-12s:** Texto fixo na tela: 'CHEIRO DE QUEM MANDA NO AMBIENTE'.",
        "v2": f"🎬 **CINEMATOGRAFIA 2 (A TENTAÇÃO):**\n- **0-3s:** Reação instintiva de alguém parando para sentir o rastro do {p}.\n- **3-9s:** Close no selo de originalidade e reflexo no vidro. Legenda: 'A estética da vitória.'\n- **9-12s:** Texto fixo na tela: 'SINTA O PESO DO OURO ÁRABE'.",
        "msg_fixa": "💎 ITEM DE COLECIONADOR: ESTOQUE LIMITADO NO CARRINHO LARANJA.",
        "hashtags": f"#perfumesarabes #luxo #tiktokshop #autoridade #{p.lower().replace(' ','')} #viral"
    }

# --- INTERFACE ---
st.title("👑 AVS ELITE | MÁQUINA DE PRODUÇÃO EXCEPCIONAL")
st.markdown("---")

produto = st.text_input("INSIRA O NOME DO PRODUTO PARA ELEVAR O PADRÃO:", placeholder="Ex: Lattafa Asad")

if st.button("🚀 ATIVAR PROTOCOLO DE SUPERIORIDADE"):
    if produto:
        res = gerar_avs_excepcional(produto)
        
        # --- BLOCO EXTRAORDINÁRIO (TÍTULO E CORPO) ---
        st.markdown(f"## {res['titulo_extraordinario']}")
        st.markdown(f"#### {res['corpo_superior']}")
        
        st.markdown("---")
        
        # --- ESTRUTURA DE CANAIS ---
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### 📽️ ROTEIROS CINEMATOGRÁFICOS")
            with st.expander("VÍDEO 1: O CHOQUE DE LUXO", expanded=True):
                st.write(res["v1"])
            with st.expander("VÍDEO 2: A ASSINATURA DO PODER", expanded=True):
                st.write(res["v2"])

        with col2:
            st.markdown("### 📱 ESTRATÉGIA DE REDE")
            st.info(f"**📌 MENSAGEM FIXA:** {res['msg_fixa']}")
            st.warning(f"**🔥 5# VIRAIS:** {res['hashtags']}")
            
            with st.expander("COPYWRITING DE ELITE (TIKTOK SHOP)", expanded=True):
                st.write(f"Você não está comprando um perfume. Está comprando o respeito imediato. O {produto} é o código secreto da elite. Clique e mude seu jogo agora.")

        # DOWNLOAD
        txt_final = f"{res['titulo_extraordinario']}\n\n{res['corpo_superior']}\n\n{res['msg_fixa']}\n{res['hashtags']}"
        st.download_button("📥 BAIXAR DOSSIÊ EXCEPCIONAL", txt_final, file_name=f"AVS_ELITE_{produto}.txt")
    else:
        st.error("Por favor, insira o nome da joia acima.")

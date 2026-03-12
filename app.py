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
        border: 1px solid #000000 !important; 
        border-radius: 0px; 
    }
    
    /* Forçar todas as fontes para Preto */
    p, span, label, h1, h2, h3, div { color: #000000 !important; font-family: 'Arial', sans-serif; }
    
    .stInfo { background-color: #F0F0F0; border: 1px solid #000; color: black; }
    </style>
    """, unsafe_allow_html=True)

# --- MOTOR DE INTELIGÊNCIA EXCEPCIONAL (ESTRUTURA COMPLETA) ---
def gerar_avs_completo_elite(p):
    return {
        # --- BLOCO EXTRAORDINÁRIO ---
        "titulo": f"🏆 O CÓDIGO DA SOBERANIA: {p.upper()} – A FRAGRÂNCIA QUE SILENCIA AMBIENTES.",
        "corpo": f"""O {p} não é apenas um perfume, é uma arma de influência social e dominação olfativa. Enquanto o homem comum se perde em fragrâncias genéricas, o portador desta joia árabe deixa um rastro de mistério e autoridade inquestionável. Este é o ápice da engenharia de luxo: uma explosão de especiarias raras para quem não aceita ser ignorado.""",
        
        # --- 2 VÍDEOS DE 12s (CENAS DE 6s SUBDIVIDIDAS) ---
        "v1_roteiro": f"""
        🎬 **VÍDEO 1: O CHOQUE DE AUTORIDADE (12s)**
        
        **CENA A (0-6s): O GANCHO DE ELITE**
        - **0-3s:** Macro do borrifador em câmera lenta disparando a névoa. (Visual Impact)
        - **3-6s:** Corte seco para o seu olhar de confiança segurando o {p}. (Identity)
        
        **CENA B (6-12s): A CONVERSÃO BRUTAL**
        - **6-9s:** O perfume sendo colocado com firmeza sobre mármore/vidro. (Status)
        - **9-12s:** Texto Fixo na Tela: "CHEIRO DE QUEM MANDA". (Call to Action)
        """,
        
        "v2_roteiro": f"""
        🎬 **VÍDEO 2: A TENTAÇÃO INEVITÁVEL (12s)**
        
        **CENA A (0-6s): O DESEJO INSTINTIVO**
        - **0-3s:** Alguém parando o passo e virando o neck (Rastro). (Social Proof)
        - **3-6s:** Close rápido nos detalhes dourados e brasão do {p}. (Product Beauty)
        
        **CENA B (6-12s): A ESCASSEZ DO OURO**
        - **6-9s:** Movimento de colocar o {p} no bolso interno de um terno/jaqueta. (Lifestyle)
        - **9-12s:** Texto Fixo na Tela: "SINTA O PESO DO OURO ÁRABE". (Scarcity)
        """,
        
        # --- 3 IMAGENS DE SUPERIORIDADE ---
        "imagens": [
            f"📸 **IMAGEM HERO:** {p} centralizado em fundo preto piano com iluminação dramática superior.",
            f"📸 **IMAGEM LIFESTYLE:** Mão com relógio de luxo segurando o {p} próximo ao volante de um carro.",
            f"📸 **IMAGEM CLOSE MACRO:** Foco extremo no selo holográfico e na textura da tampa do {p}."
        ],
        
        # --- ESTRATÉGIA DE REDE (TEXTOS) ---
        "msg_fixa": "💎 ITEM DE COLECIONADOR: ESTOQUE LIMITADO NO CARRINHO LARANJA.",
        "hashtags": f"#perfumesarabes #luxo #tiktokshop #autoridade #{p.lower().replace(' ','')} #viral",
        
        "copy_tiktok": f"Você não está comprando um perfume. Está comprando o respeito imediato. O {p} é o código secreto da elite. Clique e mude seu jogo agora.",
        "copy_insta": f"A estética do poder é olfativa. {p} é a assinatura de quem não precisa pedir licença para chegar. 👑 #Asad #Luxo",
        "copy_face": f"Para os poucos que buscam a perfeição: o {p} original finalmente chegou. Não é sobre cheiro, é sobre autoridade. Garanti o meu e o respeito é imediato. 👔💼"
    }

# --- INTERFACE ---
st.title("👑 AVS ELITE | MÁQUINA DE PRODUÇÃO TOTAL")
st.markdown("---")

produto = st.text_input("INSIRA O NOME DO PRODUTO PARA ELEVAR O PADRÃO:", placeholder="Ex: Lattafa Asad")

if st.button("🚀 ATIVAR PROTOCOLO DE SUPERIORIDADE"):
    if produto:
        res = gerar_avs_completo_elite(produto)
        
        # --- 1. BLOCO EXTRAORDINÁRIO ---
        st.markdown(f"## {res['titulo']}")
        st.markdown(f"**{res['corpo']}**")
        st.markdown("---")
        
        col1, col2, col3 = st.columns(3)
        
        # --- 2. VÍDEOS (ESTRUTURA VIRAL) ---
        with col1:
            st.markdown("### 📽️ CINEMATOGRAFIA (2x12s)")
            with st.expander("VÍDEO 1: DETALHAMENTO (0-6-12s)", expanded=True):
                st.write(res["v1_roteiro"])
            with st.expander("VÍDEO 2: DETALHAMENTO (0-6-12s)", expanded=True):
                st.write(res["v2_roteiro"])

        # --- 3. IMAGENS (SUPERIORIDADE VISUAL) - VOLTARAM! ---
        with col2:
            st.markdown("### 🎨 COMPOSIÇÃO DE ARTE (3)")
            for img in res["imagens"]:
                st.info(img)

        # --- 4. ESTRATÉGIA DE REDE (TEXTOS) ---
        with col3:
            st.markdown("### 📱 ESTRATÉGIA DE REDE")
            st.info(f"**📌 MENSAGEM FIXA:** {res['msg_fixa']}")
            st.warning(f"**🔥 5# VIRAIS:** {res['hashtags']}")
            
            with st.expander("COPY TIKTOK SHOP", expanded=True):
                st.write(res["copy_tiktok"])
            with st.expander("COPY INSTAGRAM", expanded=True):
                st.write(res["copy_insta"])
            with st.expander("COPY FACEBOOK", expanded=True):
                st.write(res["copy_face"])

        # DOWNLOAD
        txt_final = f"{res['titulo']}\n\n{res['corpo']}\n\n{res['v1_roteiro']}\n\n{res['v2_roteiro']}\n\n{res['msg_fixa']}\n{res['hashtags']}"
        st.download_button("📥 BAIXAR DOSSIÊ TOTAL", txt_final, file_name=f"AVS_ELITE_{produto}.txt")
    else:
        st.error("Insira o nome do perfume para ativar o protocolo.")

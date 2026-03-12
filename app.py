import streamlit as st

# --- DESIGN DE ALTA PERFORMANCE (BRANCO E PRETO) ---
st.set_page_config(page_title="AVS ELITE SYSTEM", page_icon="👑", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #FFFFFF; color: #000000; }
    .stButton>button { 
        background-color: #FFD700; color: #000000; font-weight: bold; 
        font-size: 20px; border-radius: 5px; border: 2px solid #000000; height: 3.5em; 
    }
    div[data-testid="stExpander"] { 
        background-color: #FFFFFF !important; 
        border: 2px solid #000000 !important; 
        border-radius: 0px; 
    }
    p, span, label, h1, h2, h3, div { color: #000000 !important; font-family: 'Arial', sans-serif; }
    .stInfo { background-color: #F0F0F0; border: 1px solid #000; color: black; }
    </style>
    """, unsafe_allow_html=True)

# --- MOTOR DE INTELIGÊNCIA EXCEPCIONAL (ESTRUTURA SUBDIVIDIDA) ---
def gerar_avs_excepcional(p):
    return {
        "titulo": f"🏆 O CÓDIGO DA SOBERANIA: {p.upper()} – A FRAGRÂNCIA QUE SILENCIA AMBIENTES.",
        "corpo": f"O {p} não é apenas um perfume, é uma arma de influência social e dominação olfativa. Enquanto o homem comum se perde em fragrâncias genéricas, o portador desta joia árabe deixa um rastro de autoridade inquestionável. Este é o ápice da engenharia de luxo: uma explosão de especiarias raras para quem não aceita ser ignorado.",
        
        "v1_roteiro": f"""
        🎬 **VÍDEO 1: O CHOQUE DE AUTORIDADE (12s)**
        
        **CENA A (0-6s): O GANCHO DE ELITE**
        *Subdivisão:*
        - 0-3s: Macro do borrifador em câmera lenta disparando. (Visual Impact)
        - 3-6s: Corte seco para o seu olhar de confiança segurando o {p}. (Identity)
        
        **CENA B (6-12s): A CONVERSÃO BRUTAL**
        *Subdivisão:*
        - 6-9s: O perfume sendo colocado sobre uma superfície de mármore/vidro. (Status)
        - 9-12s: Texto Fixo: "CHEIRO DE QUEM MANDA". (Call to Action)
        """,
        
        "v2_roteiro": f"""
        🎬 **VÍDEO 2: A TENTAÇÃO INEVITÁVEL (12s)**
        
        **CENA A (0-6s): O DESEJO INSTINTIVO**
        *Subdivisão:*
        - 0-3s: Alguém parando o passo e virando o pescoço (Rastro). (Social Proof)
        - 3-6s: Close no brasão e detalhes dourados do {p}. (Product Beauty)
        
        **CENA B (6-12s): A ESCASSEZ DO OURO**
        *Subdivisão:*
        - 6-9s: Movimento rápido de colocar o {p} no bolso de um terno/jaqueta. (Lifestyle)
        - 9-12s: Texto Fixo: "SINTA O PESO DO OURO ÁRABE". (Scarcity)
        """,
        
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
        
        st.markdown(f"## {res['titulo']}")
        st.markdown(f"**{res['corpo']}**")
        st.markdown("---")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### 📽️ CINEMATOGRAFIA (ESTRUTURA VIRAL)")
            with st.expander("VÍDEO 1: DETALHAMENTO DAS CENAS", expanded=True):
                st.write(res["v1_roteiro"])
            with st.expander("VÍDEO 2: DETALHAMENTO DAS CENAS", expanded=True):
                st.write(res["v2_roteiro"])

        with col2:
            st.markdown("### 📱 ESTRATÉGIA DE REDE")
            st.info(f"**📌 MENSAGEM FIXA:** {res['msg_fixa']}")
            st.warning(f"**🔥 5# VIRAIS:** {res['hashtags']}")
            
            with st.expander("COPYWRITING TIKTOK SHOP", expanded=True):
                st.write(f"Você não está comprando um perfume. Está comprando o respeito imediato. O {produto} é o código secreto da elite. Clique e mude seu jogo agora.")

        # DOWNLOAD
        txt_final = f"{res['titulo']}\n\n{res['corpo']}\n\n{res['v1_roteiro']}\n\n{res['v2_roteiro']}\n\n{res['msg_fixa']}\n{res['hashtags']}"
        st.download_button("📥 BAIXAR DOSSIÊ EXCEPCIONAL", txt_final, file_name=f"AVS_ELITE_{produto}.txt")
    else:
        st.error("Insira o nome do perfume para ativar o protocolo.")

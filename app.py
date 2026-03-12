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

# --- MOTOR DE INTELIGÊNCIA EXCEPCIONAL ---
def gerar_avs_completo_elite(p):
    return {
        "titulo": f"🏆 O CÓDIGO DA SOBERANIA: {p.upper()} – A FRAGRÂNCIA QUE SILENCIA AMBIENTES.",
        "corpo": f"""O {p} não é apenas um perfume, é uma arma de influência social e dominação olfativa. Enquanto o homem comum se perde em fragrâncias genéricas, o portador desta joia árabe deixa um rastro de autoridade inquestionável.""",
        
        # --- VÍDEOS COM SUBDIVISÃO 3s/3s ---
        "v1_roteiro": f"""
        🎬 **VÍDEO 1: O CHOQUE DE AUTORIDADE (12s | 9:16)**
        
        **CENA A (0-6s): O GANCHO DE ELITE**
        - **0-3s:** Close macro no borrifador disparando. Produto ocupa 40% da tela (Escala Real).
        - **3-6s:** Corte para o {p} sendo segurado firme. Mão deve envolver o frasco naturalmente.
        
        **CENA B (6-12s): A CONVERSÃO BRUTAL**
        - **6-9s:** O perfume posicionado sobre mármore. Proporção: Frasco deve ter 1/3 da altura do smartphone.
        - **9-12s:** Texto Fixo: "CHEIRO DE QUEM MANDA".
        """,
        
        "v2_roteiro": f"""
        🎬 **VÍDEO 2: A TENTAÇÃO INEVITÁVEL (12s | 9:16)**
        
        **CENA A (0-6s): O DESEJO INSTINTIVO**
        - **0-3s:** Rastro olfativo. Pessoa vira o rosto conforme você passa com o {p} na mão.
        - **3-6s:** Close no brasão. Escala 1:1 (Tamanho real do olho humano).
        
        **CENA B (6-12s): A ESCASSEZ DO OURO**
        - **6-9s:** Guardando o {p} no bolso interno de um terno. O frasco deve caber perfeitamente na palma.
        - **9-12s:** Texto Fixo: "SINTA O PESO DO OURO ÁRABE".
        """,
        
        # --- IMAGENS 9:16 COM TRAVA DE PROPORCIONALIDADE ---
        "imagens": [
            f"📸 **IMAGEM 1 (9:16) - ESCALA REAL:** {p} segurado por uma mão masculina. O frasco deve ocupar do início da palma até a base dos dedos. Fundo neutro luxo.",
            f"📸 **IMAGEM 2 (9:16) - POSICIONAMENTO:** {p} ao lado de um relógio de pulso (42mm) para travar a percepção de tamanho real do produto no cérebro do cliente.",
            f"📸 **IMAGEM 3 (9:16) - CLOSE DE AUTORIDADE:** Foco no topo da tampa. Proporção 90% preenchida pelo detalhe metálico. Sem distorção de lente."
        ],
        
        "msg_fixa": "💎 ITEM DE COLECIONADOR: ESTOQUE LIMITADO NO CARRINHO LARANJA.",
        "hashtags": f"#perfumesarabes #luxo #tiktokshop #autoridade #{p.lower().replace(' ','')} #viral"
    }

# --- INTERFACE ---
st.title("👑 AVS ELITE | MÁQUINA DE PRODUÇÃO TOTAL")
produto = st.text_input("INSIRA O PRODUTO:", placeholder="Ex: Lattafa Asad")

if st.button("🚀 ATIVAR PROTOCOLO DE SUPERIORIDADE"):
    if produto:
        res = gerar_avs_completo_elite(produto)
        st.markdown(f"### {res['titulo']}")
        st.markdown(f"{res['corpo']}")
        
        c1, c2, c3 = st.columns(3)
        with c1:
            st.markdown("### 📽️ VÍDEOS (9:16)")
            with st.expander("VÍDEO 1 - ROTEIRO", expanded=True): st.write(res["v1_roteiro"])
            with st.expander("VÍDEO 2 - ROTEIRO", expanded=True): st.write(res["v2_roteiro"])
        with c2:
            st.markdown("### 🎨 IMAGENS (9:16)")
            for img in res["imagens"]: st.info(img)
        with c3:
            st.markdown("### 📱 ESTRATÉGIA")
            st.info(f"**📌 FIXO:** {res['msg_fixa']}")
            st.warning(f"**🔥 5#:** {res['hashtags']}")
            with st.expander("COPY ELITE", expanded=True): st.write(f"O {produto} é o código secreto da elite. Clique e mude seu jogo.")

        txt_final = f"{res['titulo']}\n\n{res['v1_roteiro']}\n\n{res['v2_roteiro']}\n\n" + "\n".join(res["imagens"])
        st.download_button("📥 BAIXAR DOSSIÊ", txt_final, file_name=f"AVS_ELITE_{produto}.txt")

import streamlit as st

# --- CONFIGURAÇÃO DE DESIGN (BRANCO E PRETO) ---
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

# --- MOTOR DE INTELIGÊNCIA COMPLETA ---
def gerar_avs_elite_final(p):
    return {
        "titulo": f"🏆 O CÓDIGO DA SOBERANIA: {p.upper()} – A FRAGRÂNCIA QUE SILENCIA AMBIENTES.",
        "corpo": f"O {p} não é apenas um perfume, é uma arma de influência social. Enquanto o homem comum usa fragrâncias genéricas, o portador desta joia árabe deixa um rastro de autoridade inquestionável. Engenharia de luxo para quem não aceita ser ignorado.",
        
        "v1": f"""🎬 **VÍDEO 1: IMPACTO (12s | 9:16)**
        - **0-3s:** Close macro no borrifador disparando. Escala Real.
        - **3-6s:** Corte seco para o {p} sendo segurado firme na palma.
        - **6-9s:** Perfume posicionado sobre mármore. Proporção real.
        - **9-12s:** Texto Fixo: 'CHEIRO DE QUEM MANDA'.""",
        
        "v2": f"""🎬 **VÍDEO 2: STATUS (12s | 9:16)**
        - **0-3s:** Rastro olfativo. Pessoa vira o rosto ao sentir o {p}.
        - **3-6s:** Close no brasão. Tamanho real do detalhe.
        - **6-9s:** {p} sendo colocado no bolso interno de um terno.
        - **9-12s:** Texto Fixo: 'SINTA O PESO DO OURO'.""",
        
        "imagens": [
            f"📸 **IMAGEM 1 (9:16):** {p} na palma da mão masculina (Escala 1:1).",
            f"📸 **IMAGEM 2 (9:16):** {p} ao lado de um relógio de 42mm (Trava de Tamanho).",
            f"📸 **IMAGEM 3 (9:16):** Close 90% preenchido pela tampa e selo."
        ],
        
        "textos": {
            "TikTok Shop": f"Você não está comprando um perfume. Está comprando o respeito imediato. O {p} é o código secreto da elite. Clique no carrinho laranja!",
            "Instagram": f"A estética do poder é olfativa. {p} é a assinatura de quem não pede licença para chegar. 👑 #Luxo #Status",
            "Facebook": f"Dica de autoridade: O {p} original finalmente chegou. Qualidade absoluta e fixação eterna. Recomendo! 👔",
            "Site Google": f"Análise {p}: Fragrância de alta performance com projeção marcante e fixação de 12h+. O ápice do custo-benefício árabe."
        },
        
        "msg_fixa": "💎 ITEM DE COLECIONADOR: ESTOQUE LIMITADO NO CARRINHO LARANJA.",
        "hashtags": f"#perfumesarabes #luxo #tiktokshop #autoridade #{p.lower().replace(' ','')} #viral"
    }

# --- INTERFACE ---
st.title("👑 AVS ELITE | MÁQUINA DE PRODUÇÃO TOTAL")
produto = st.text_input("NOME DO PRODUTO PARA ELEVAR O PADRÃO:", placeholder="Ex: Lattafa Asad")

if st.button("🚀 ATIVAR PROTOCOLO DE SUPERIORIDADE"):
    if produto:
        res = gerar_avs_elite_final(produto)
        
        st.markdown(f"## {res['titulo']}")
        st.markdown(f"#### {res['corpo']}")
        st.divider()
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("### 📽️ VÍDEOS (9:16)")
            with st.expander("ROTEIRO VÍDEO 1", expanded=True): st.write(res["v1"])
            with st.expander("ROTEIRO VÍDEO 2", expanded=True): st.write(res["v2"])

        with col2:
            st.markdown("### 🎨 IMAGENS (9:16)")
            for img in res["imagens"]: st.info(img)

        with col3:
            st.markdown("### 📱 ESTRATÉGIA")
            st.info(f"**📌 FIXO:** {res['msg_fixa']}")
            st.warning(f"**🔥 5#:** {res['hashtags']}")
            for rede, copy in res["textos"].items():
                with st.expander(f"POST {rede}", expanded=True): st.write(copy)

        # DOWNLOAD COMPLETO
        txt_final = f"{res['titulo']}\n\n{res['corpo']}\n\n{res['v1']}\n\n{res['v2']}\n\n" + "\n".join(res["imagens"]) + "\n\n" + res["msg_fixa"]
        st.download_button("📥 BAIXAR DOSSIÊ TOTAL", txt_final, file_name=f"AVS_ELITE_{produto}.txt")

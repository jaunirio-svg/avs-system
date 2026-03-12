import streamlit as st

# --- DESIGN DE ALTA PERFORMANCE (CONTRASTE TOTAL) ---
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
    .stInfo { background-color: #F8F8F8; border: 1px solid #000; color: black; }
    </style>
    """, unsafe_allow_html=True)

# --- MOTOR DE INTELIGÊNCIA MILIMETRADA ---
def gerar_avs_milimetrado(p):
    return {
        "titulo": f"🏆 O CÓDIGO DA SOBERANIA: {p.upper()}",
        "corpo": f"O {p} é uma arma de influência social. Engenharia de luxo árabe para quem não aceita ser ignorado. Dominação olfativa pura.",
        
        "v1": f"""🎬 **VÍDEO 1: IMPACTO CINEMÁTICO (12s)**

**CENA 01 (0-06s): O GANCHO HIPNÓTICO**
- **0.0s - 1.5s:** (Visual) Close extremo no borrifador. (Áudio) Som de 'click' metálico.
- **1.5s - 4.0s:** (Visual) Spray saindo em Slow Motion. (Áudio/Fala) "Isso aqui não é um perfume..."
- **4.0s - 6.0s:** (Visual) O frasco aparece por completo na palma da mão (Escala 1:1). (Fala) "...é um código de poder."

**CENA 02 (06-12s): A PROVA DE STATUS**
- **6.0s - 9.0s:** (Visual) Você coloca o {p} sobre mármore, a câmera treme levemente no impacto. (Fala) "O rastro que silencia qualquer sala."
- **9.0s - 12.0s:** (Visual) Texto Fixo: 'CARRINHO LARANJA'. (Fala) "Garanta a sua assinatura hoje." """,
        
        "v2": f"""🎬 **VÍDEO 2: O INSTINTO DE POSSE (12s)**

**CENA 01 (0-06s): A REAÇÃO SOCIAL**
- **0.0s - 2.5s:** (Visual) Alguém cruza por você e vira o rosto bruscamente. (Áudio) Som de vento/passo rápido.
- **2.5s - 4.5s:** (Visual) Close no seu rosto com leve sorriso de confiança. (Fala) "Ninguém fica indiferente ao {p}."
- **4.5s - 6.0s:** (Visual) Transição rápida para o brasão dourado em 9:16.

**CENA 02 (06-12s): O FECHAMENTO DE ELITE**
- **6.0s - 9.5s:** (Visual) Você guarda o frasco no bolso interno de um terno escuro. (Fala) "O cheiro do ouro árabe agora na sua pele."
- **9.5s - 12.0s:** (Visual) Texto Fixo: 'LINK NA BIO / ESTOQUE LIMITADO'. (Fala) "Decida ser inesquecível." """,
        
        "imagens": [
            f"📸 **IMAGEM 1 (9:16):** {p} na palma da mão (Escala Real). Enquadramento do peito para baixo.",
            f"📸 **IMAGEM 2 (9:16):** {p} ao lado de um relógio premium (Trava de proporção humana).",
            f"📸 **IMAGEM 3 (9:16):** Macro 90% foco no selo. Nitidez total na textura do vidro."
        ],
        
        "textos": {
            "TikTok": f"O {p} é o segredo dos 1%. Clique no carrinho!",
            "Instagram": f"A estética do poder é olfativa. {p} é sua nova assinatura. 👑",
            "Facebook": f"Para quem busca o original: {p} árabe com fixação bruta. 👔",
            "Site": f"Análise técnica {p}: Projeção de 3 metros e fixação de 12h+."
        },
        
        "msg_fixa": "💎 ITEM DE COLECIONADOR: ESTOQUE LIMITADO NO CARRINHO LARANJA.",
        "hashtags": f"#perfumesarabes #luxo #tiktokshop #autoridade #{p.lower().replace(' ','')} #viral"
    }

# --- INTERFACE ---
st.title("👑 AVS ELITE | DIRETOR CINEMATOGRÁFICO")
produto = st.text_input("NOME DO PRODUTO:", placeholder="Ex: Lattafa Asad")

if st.button("🚀 ATIVAR PROTOCOLO MILIMETRADO"):
    if produto:
        res = gerar_avs_milimetrado(produto)
        
        st.markdown(f"## {res['titulo']}")
        st.markdown(f"#### {res['corpo']}")
        st.divider()
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("### 📽️ VÍDEOS (MILIMETRAGEM 2x 06s)")
            with st.expander("ROTEIRO 1: IMPACTO", expanded=True): st.write(res["v1"])
            with st.expander("ROTEIRO 2: STATUS", expanded=True): st.write(res["v2"])

        with col2:
            st.markdown("### 🎨 IMAGENS (9:16 | ESCALA REAL)")
            for img in res["imagens"]: st.info(img)

        with col3:
            st.markdown("### 📱 ESTRATÉGIA COMPLETA")
            st.info(f"**📌 FIXO:** {res['msg_fixa']}")
            st.warning(f"**🔥 5#:** {res['hashtags']}")
            for rede, copy in res["textos"].items():
                with st.expander(f"POST {rede}", expanded=True): st.write(copy)

        # DOWNLOAD
        txt_final = f"{res['titulo']}\n\n{res['v1']}\n\n{res['v2']}\n\n" + "\n".join(res["imagens"]) + f"\n\n{res['msg_fixa']}\n{res['hashtags']}"
        st.download_button("📥 BAIXAR PACOTE MILIMETRADO", txt_final, file_name=f"AVS_MILIMETRADO_{produto}.txt")

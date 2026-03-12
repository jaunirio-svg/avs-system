import streamlit as st

# --- CONFIGURAÇÃO ---
st.set_page_config(page_title="AVS NETWORK", page_icon="💎", layout="wide")

# CSS Profissional (Melhora a visibilidade dos textos)
st.markdown("""
    <style>
    .stButton>button { background-color: #FFD700; color: black; font-weight: bold; width: 100%; border-radius: 10px; height: 3em; border: none; }
    .main { background-color: #000000; color: white; }
    .stExpander { background-color: #1a1a1a !important; border: 1px solid #333 !important; }
    p { color: #ffffff !important; font-size: 16px; }
    </style>
    """, unsafe_allow_html=True)

def gerar_conteudo(prod):
    return {
        "v": [
            f"**Cena 1 (0-6s):** Gancho visual no frasco de {prod}.\n**Cena 2 (6-12s):** CTA para o Carrinho Laranja.",
            f"**Cena 1 (0-6s):** Close no brasão de luxo do {prod}.\n**Cena 2 (6-12s):** 'Link na Bio' para compra."
        ],
        "i": [f"📸 HERO: {prod} em destaque.", f"📸 LIFESTYLE: {prod} em cenário premium.", f"📸 CLOSE: Detalhes do selo."],
        "t": {
            "TikTok": f"O segredo árabe: {prod}. 💎 #Perfume #TikTokShop",
            "Instagram": f"Sinta o poder de {prod}. A sua nova assinatura. 👑",
            "Facebook": f"Perfume {prod} original disponível. Qualidade garantida!",
            "Site (SEO)": f"Análise técnica do {prod}: Fixação e projeção de elite."
        }
    }

st.title("💎 AVS NETWORK | Painel de Controle")
produto = st.text_input("NOME DO PRODUTO:", placeholder="Ex: Fakhar Black")

if st.button("🚀 GERAR 9 CONTEÚDOS AGORA"):
    if produto:
        res = gerar_conteudo(produto)
        st.success(f"PRODUÇÃO CONCLUÍDA para {produto}")
        
        c1, c2, c3 = st.columns(3)
        with c1:
            st.subheader("🎥 VÍDEOS")
            for i, v in enumerate(res["v"]):
                with st.expander(f"Vídeo {i+1}", expanded=True): st.write(v)
        with c2:
            st.subheader("🎨 IMAGENS")
            for img in res["i"]: st.info(img)
        with c3:
            st.subheader("📱 TEXTOS")
            for rede, txt in res["t"].items():
                with st.expander(rede): st.write(txt)
        
        # DOWNLOAD
        txt_final = f"PRODUTO: {produto}\n\n" + "\n".join([f"{k}: {v}" for k,v in res["t"].items()])
        st.download_button("📥 BAIXAR PACOTE DE TEXTOS", txt_final, file_name=f"AVS_{produto}.txt")
    else:
        st.error("Digite o nome de um produto.")

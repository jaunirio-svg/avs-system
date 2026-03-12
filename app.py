import streamlit as st
import io

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="AVS NETWORK", page_icon="💎", layout="wide")

# CSS para o estilo Dark de Luxo
st.markdown("""
    <style>
    .stButton>button { background-color: #FFD700; color: black; font-weight: bold; width: 100%; border-radius: 10px; border: none; height: 3em; }
    .main { background-color: #000000; color: white; }
    div[data-testid="stExpander"] { background-color: #1a1a1a; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- MOTOR DE INTELIGÊNCIA AVS ---
def processar_avs_completo(produto):
    return {
        "videos": [
            {"titulo": "🎬 VÍDEO 1: IMPACTO (0-12s)", "c1": f"0-6s: Gancho focado no peso e na exclusividade do {produto}.", "c2": "6-12s: Revelação do frasco + Chamada para o Carrinho Laranja."},
            {"titulo": "🎬 VÍDEO 2: STATUS (0-12s)", "c1": f"0-6s: Close macro nos detalhes dourados e textura do {produto}.", "c2": "6-12s: Borrifada em slow motion + Link na Bio."}
        ],
        "imagens": [
            f"🖼️ HERO: {produto} centralizado com iluminação premium.",
            f"🖼️ LIFESTYLE: {produto} em cenário de alto padrão (couro/mármore).",
            f"🖼️ CLOSE: Macro nos detalhes da tampa e selo de autenticidade."
        ],
        "textos": {
            "TikTok": f"O segredo da perfumaria árabe revelado. 💎 {produto} é presença garantida. Garanta o seu no carrinho! #Perfumaria #Luxo #Asad",
            "Instagram": f"A elegância é silenciosa, mas marcante. Conheça o {produto}, sua nova assinatura de elite. 👑 #Status #Rolex",
            "Facebook": f"Oportunidade única: Encontrei o {produto} original. Qualidade absoluta e fixação eterna. Recomendo!",
            "Site (SEO)": f"Análise Técnica: O {produto} redefine o conceito de projeção. Notas de topo especiadas com fundo amadeirado de alta performance."
        }
    }

# --- INTERFACE ---
st.title("💎 AVS NETWORK - Inteligência Autônoma")
st.write("Plataforma Multi-Produto do Almir")

produto_input = st.text_input("AVS START COMMAND (NOME DO PRODUTO):", placeholder="Ex: Asad, Fakhar, 9PM...")

if st.button("🚀 GERAR ESTRATÉGIA COMPLETA"):
    if produto_input:
        # Gera o conteúdo real
        dados = processar_avs_completo(produto_input)
        
        st.success(f"PRODUÇÃO CONCLUÍDA: 9 Conteúdos gerados para {produto_input}")
        
        # Distribuição em Colunas
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.header("🎥 VÍDEOS (2)")
            for v in dados["videos"]:
                with st.expander(v["titulo"], expanded=True):
                    st.write(f"**Cena 1:** {v['c1']}")
                    st.write(f"**Cena 2:** {v['c2']}")

        with col2:
            st.header("🎨 IMAGENS (3)")
            for img in dados["imagens"]:
                st.info(img)

        with col3:
            st.header("📱 TEXTOS (4)")
            for rede, txt in dados["textos"].items():
                with st.expander(rede):
                    st.write(txt)
        
        # Função de Download
        relatorio = f"PRODUTO: {produto_input}\n" + "="*30 + "\n"
        for k, v in dados["textos"].items():
            relatorio += f"\n[{k}]: {v}"
        
        st.download_button(label="📥 BAIXAR PACOTE TXT", data=relatorio, file_name=f"AVS_{produto_input}.txt", mime="text/plain")
    else:
        st.error("Por favor, digite o nome de um produto acima.")

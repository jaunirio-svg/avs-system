import streamlit as st

# --- CONFIGURAÇÃO VISUAL (Cores Claras para Melhor Ver) ---
st.set_page_config(page_title="AVS NETWORK", page_icon="💎", layout="wide")

st.markdown("""
    <style>
    /* Fundo claro para facilitar a visão */
    .main { background-color: #F5F5F5; color: #000000; }
    
    /* Botão Amarelo Vibrante do seu print */
    .stButton>button { 
        background-color: #FFD700; color: black; font-weight: bold; 
        width: 100%; border-radius: 8px; border: 2px solid #CCAC00; height: 3.5em; 
    }
    
    /* Caixas de texto brancas com bordas nítidas */
    div[data-testid="stExpander"] { 
        background-color: #FFFFFF !important; 
        border: 1px solid #D1D1D1 !important; 
        border-radius: 10px;
        color: #000000 !important;
    }
    
    /* Garantir que todo texto seja PRETO para leitura */
    p, span, label, h1, h2, h3 { color: #000000 !important; font-weight: 500; }
    .stInfo { background-color: #E3E3E3; color: black; border: none; }
    </style>
    """, unsafe_allow_html=True)

# --- MOTOR DE CONTEÚDO REAL ---
def gerar_estrategia_avs(p):
    return {
        "v1": f"🎬 **ROTEIRO VÍDEO 1: UNBOXING IMPACTO**\n\n**0-6 segundos:** Close no movimento de abrir a caixa do {p}. Mostre o reflexo da luz no vidro.\n\n**6-12 segundos:** Borrifada no ar e legenda: 'O perfume árabe que fixa 12h+'. Clique no link!",
        "v2": f"🎬 **ROTEIRO VÍDEO 2: STATUS E LUXO**\n\n**0-6 segundos:** Grave o {p} ao lado de um acessório de marca (relógio ou chave de carro).\n\n**6-12 segundos:** Texto na tela: 'Cheiro de quem manda no ambiente'. Garanta o seu agora!",
        "img": [
            f"📸 FOTO 1: {p} em destaque (Fundo branco limpo).",
            f"📸 FOTO 2: Mão segurando o {p} (Uso real).",
            f"📸 FOTO 3: Macro no selo de originalidade (Confiança)."
        ],
        "txt": {
            "TikTok": f"🚨 O perfume que viralizou! O {p} da Lattafa chegou. Fixação absurda e rastro de elogios. Garanta no carrinho! 🛒 #PerfumeArabe #{p}",
            "Instagram": f"Sofisticação tem nome: {p}. 👑 Uma fragrância imponente para quem busca o topo. Link na Bio. 💎",
            "Facebook": f"Dica: O {p} original é imbatível na fixação. Encontrei o estoque com preço justo aqui! 👔🔥",
            "Site Google": f"Análise {p}: Perfume de alta performance, notas orientais e projeção marcante. O melhor custo-benefício de 2026."
        }
    }

# --- INTERFACE ---
st.title("💎 AVS NETWORK | Painel de Controle Profissional")
st.subheader("Geração de Conteúdo em Massa")

produto = st.text_input("DIGITE O NOME DO PERFUME:", placeholder="Ex: Lattafa Asad")

if st.button("🚀 GERAR 9 CONTEÚDOS AGORA"):
    if produto:
        data = gerar_estrategia_avs(produto)
        st.success(f"Tudo pronto para o {produto}!")
        
        c1, c2, c3 = st.columns(3)
        
        with c1:
            st.markdown("### 🎥 VÍDEOS")
            with st.expander("VER ROTEIRO VÍDEO 1", expanded=True):
                st.write(data["v1"])
            with st.expander("VER ROTEIRO VÍDEO 2", expanded=True):
                st.write(data["v2"])

        with c2:
            st.markdown("### 🎨 IMAGENS")
            for i in data["img"]:
                st.info(i)

        with c3:
            st.markdown("### 📱 TEXTOS")
            for rede, texto in data["txt"].items():
                with st.expander(f"POST {rede}", expanded=True):
                    st.write(texto)
                
        st.divider()
        # DOWNLOAD
        full_text = f"AVS STRATEGY - {produto}\n\n" + data["v1"] + "\n\n" + data["v2"] + "\n\n" + "\n".join(data["txt"].values())
        st.download_button("📥 BAIXAR PACOTE TXT", full_text, file_name=f"AVS_{produto}.txt")
    else:
        st.error("Por favor, digite o nome do perfume primeiro.")

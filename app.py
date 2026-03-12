import streamlit as st

# --- DESIGN DE ELITE ---
st.set_page_config(page_title="AVS ELITE", page_icon="👑", layout="wide")
st.markdown("""
    <style>
    .main { background-color: #FAFAFA; }
    .stButton>button { 
        background-color: #000000; color: #FFD700; font-weight: bold; 
        font-size: 20px; border-radius: 5px; border: 2px solid #FFD700; height: 3.5em; 
    }
    .stButton>button:hover { background-color: #FFD700; color: black; }
    div[data-testid="stExpander"] { background-color: #FFFFFF !important; border: 1px solid #000 !important; border-radius: 0px; }
    p, h1, h2, h3 { color: #000000 !important; font-family: 'Georgia', serif; }
    </style>
    """, unsafe_allow_html=True)

def gerar_estrategia_excepcional(p):
    return {
        "v1": f"🎬 **ROTEIRO 1: O CHOQUE DE LUXO (0-12s)**\n\n**Hook (0-3s):** Close extremo no borrifador soltando a névoa. Som de violino tenso.\n**Contexto (3-8s):** Corte rápido para você guardando o {p} em um cofre ou gaveta de veludo. Legenda: 'Existem perfumes. E existe o {p}.'\n**CTA (8-12s):** Olhar direto para a câmera. 'Não clique se você não aguenta ser notado.'",
        "v2": f"🎬 **ROTEIRO 2: A ASSINATURA DO PODER (0-12s)**\n\n**Hook (0-3s):** Som de motor de carro esportivo. O {p} aparece no console.\n**Contexto (3-8s):** Transição de roupa comum para terno/vestido de gala ao segurar o frasco. Legenda: 'O cheiro da sua primeira vitória.'\n**CTA (8-12s):** 'Link na Bio. Poucas unidades para quem sabe o que quer.'",
        "img": [
            f"👑 **HERO:** {p} banhado por uma luz dourada lateral, sombras dramáticas.",
            f"👑 **LIFESTYLE:** O {p} sobre uma mesa de mármore preto com uma taça de cristal ao lado.",
            f"👑 **MACRO:** Foco na textura do vidro e no selo holográfico de realeza."
        ],
        "txt": {
            "TikTok": f"Para de usar o que todo mundo usa. 🤫 O {p} não é um perfume, é um código de entrada para o topo. Fixação que atravessa o dia e rastro que silencia qualquer sala. Se quer ser comum, compre outro. Se quer ser elite, o carrinho laranja está aí. 💎🔥 #LuxoArabe #{p} #Poder",
            "Instagram": f"A estética do sucesso é olfativa. 👑 O {p} traduz a imponência de quem não precisa pedir licença para chegar. Uma joia da perfumaria árabe agora ao seu alcance. Decida ser memorável hoje. Link na Bio. 🏺✨",
            "Facebook": f"Para os poucos que buscam a perfeição: o {p} original finalmente chegou. Não é sobre cheiro, é sobre autoridade. Garanti o meu e o respeito é imediato. 👔💼",
            "Site Google": f"Dossiê Técnico {p}: Uma obra-prima da engenharia olfativa oriental. Notas de Oud e especiarias finas que criam uma aura de exclusividade. Performance brutal de projeção e fixação de 12h+ na pele."
        }
    }

st.title("👑 AVS ELITE | Engenharia de Desejo")
produto = st.text_input("QUAL PRODUTO VAMOS ELEVAR AO TOPO?", placeholder="Ex: Lattafa Asad")

if st.button("🚀 DISPARAR PROTOCOLO EXCEPCIONAL"):
    if produto:
        data = gerar_estrategia_excepcional(produto)
        st.success(f"Protocolo de Luxo Ativado para {produto}")
        
        c1, c2, c3 = st.columns(3)
        with c1:
            st.markdown("### 📽️ CINEMATOGRAFIA")
            with st.expander("VÍDEO 1: IMPACTO VISUAL", expanded=True): st.write(data["v1"])
            with st.expander("VÍDEO 2: STATUS", expanded=True): st.write(data["v2"])
        with c2:
            st.markdown("### 📸 COMPOSIÇÃO DE ARTE")
            for i in data["img"]: st.info(i)
        with c3:
            st.markdown("### ✍️ COPYWRITING DE ELITE")
            for rede, texto in data["txt"].items():
                with st.expander(f"ESTRATEGIA {rede}", expanded=True): st.write(texto)
        
        relatorio = f"PROTOCOLO EXCEPCIONAL AVS - {produto}\n\n" + data["v1"] + "\n\n" + data["v2"] + "\n\n" + "\n".join(data["txt"].values())
        st.download_button("📥 BAIXAR DOSSIÊ DE LUXO", relatorio, file_name=f"AVS_ELITE_{produto}.txt")
    else:
        st.error("Insira o nome da joia (produto).")

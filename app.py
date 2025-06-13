import streamlit as st
import matplotlib.pyplot as plt
from dados import carregar_dados
from graficos import grafico_evolucao, grafico_mortalidade_stack
import matplotlib.patches as mpatches
import io

# Aplica o estilo CSS personalizado
css = """
<style>
    [data-baseweb="tab"] button {
    color: #333 !important;
    }
    [data-baseweb="tab"] button[aria-selected="true"] {
    color: #0b3c5d !important;
    font-weight: bold;
    }

      [data-testid="stSidebar"] {
        min-width: 100px;
        max-width: 120px;
        background: linear-gradient(to left , #eaeded ,#137ea8);
        padding: 0.5rem;
        border-right: 1px solid #dee2e6;
    }


    .sidebar-title-vertical {
        writing-mode: vertical-rl;
        text-orientation: upright;
        font-family: 'Arial', sans-serif;
        font-size: 14px;
        color: white;
        font-weight: bold;
        margin: 1rem auto;
        text-align: center;
    }

    .stApp {
        background: linear-gradient(to left , #eaeded , #eaeded);
    }
</style>
"""

# Carregar dados
(
    df_pop, df_dens, df_racio, df_cresc,
    df_idade_media, df_taxa_alteracao_natural,
    df_nascimentos, df_obitos,
    df_esperanca_vida, df_esperanca_vida_homens80, df_esperanca_vida_mulheres80,
    df_mortalidade_antes40, df_mortalidade_antes60, df_mortalidade_entre15e50,
    df_taxa_migracao_liquida, df_mortalidade_entre15e50Homens, df_mortalidade_entre15e50Mulheres
) = carregar_dados()

# Grupos de gráficos
grupos = {
    "População e Estrutura": [
        (df_pop, "População Total", "Milhares de Habitantes", "Populacao"),
        (df_dens, "Densidade Populacional", "Habitantes/km²", "Densidade"),
        (df_racio, "Rácio de Género", "Homens por Mulher", "RacioGenero"),
        (df_cresc, "Taxa de Crescimento Populacional", "%", "Crescimento")
    ],
    "Natalidade e Mortalidade": [
        (df_nascimentos, "Nascimentos", "Milhares", "Nascimentos"),
        (df_obitos, "Óbitos", "Milhares", "Obitos"),
        (df_taxa_alteracao_natural, "Alteração Natural", "Milhares", "TaxaAlteracaoNatural"),
        (df_esperanca_vida, "Esperança de Vida", "Anos", "EsperancaVida")
    ],
    "Mortalidade Específica": [
        (df_mortalidade_antes40, "Mortalidade antes dos 40", "Óbitos/1.000 nascimentos", "MortalidadeAntes40"),
        (df_mortalidade_antes60, "Mortalidade antes dos 60", "Óbitos/1.000 nascimentos", "MortalidadeAntes60"),
        (df_mortalidade_entre15e50Homens, "Mortalidade 15–50 (Homens)", "Óbitos/1.000 vivos aos 15", "MortalidadeEntre15e50Homens"),
        (df_mortalidade_entre15e50Mulheres, "Mortalidade 15–50 (Mulheres)", "Óbitos/1.000 vivas aos 15", "MortalidadeEntre15e50Mulheres")
    ],
    "Indicadores Adicionais": [
        (df_idade_media, "Idade Média", "Anos", "IdadeMedia"),
        (df_taxa_migracao_liquida, "Migração Líquida", "Milhares", "TaxaMigracaoLiquida"),
        (df_esperanca_vida_homens80, "Esperança Vida aos 80 (Homens)", "Anos", "EsperancaVidaHomens80"),
        (df_esperanca_vida_mulheres80, "Esperança Vida aos 80 (Mulheres)", "Anos", "EsperancaVidaMulheres80")
    ]
}

# Interface
st.set_page_config(page_title="Indicadores Demográficos", layout="wide")
st.markdown(css, unsafe_allow_html=True)
st.sidebar.markdown('<div class="sidebar-title-vertical">📊 INDICADORES DEMOGRÁFICOS</div>', unsafe_allow_html=True)

# Escolha do grupo
grupo_escolhido = st.selectbox("Escolha o grupo de indicadores:", list(grupos.keys()))

# Criar legenda compacta
fig_legend = plt.figure(figsize=(6, 0.4), dpi=300)
ax_legend = fig_legend.add_axes([0, 0, 1, 1])
ax_legend.axis('off')

patches = [
    mpatches.Patch(color='orange', label='América'),
    mpatches.Patch(color='red', label='Europa'),
    mpatches.Patch(color='purple', label='Oceania'),
    mpatches.Patch(color='blue', label='África'),
    mpatches.Patch(color='green', label='Ásia')
]

ax_legend.legend(
    handles=patches,
    loc='center',
    ncol=5,
    frameon=False,
    fontsize='xx-small',
    columnspacing=0.5,
    handlelength=1.0,
    handletextpad=0.4,
    borderpad=0.0
)

buf = io.BytesIO()
fig_legend.savefig(buf, format="png", bbox_inches="tight", transparent=True, pad_inches=0)
buf.seek(0)
st.image(buf)

# Tabs com 2 gráficos por aba
subtab1, subtab2 = st.tabs(["Gráficos 1 e 2", "Gráficos 3 e 4"])

with subtab1:
    for i in range(2):
        df, titulo, ylabel, dado = grupos[grupo_escolhido][i]
        fig, ax = plt.subplots(figsize=(6, 2))
        grafico_evolucao(df, titulo, ylabel, dado, 'linha', ax)
        fig.patch.set_alpha(0.0)
        st.pyplot(fig, transparent=True)

with subtab2:
    for i in range(2, 4):
        df, titulo, ylabel, dado = grupos[grupo_escolhido][i]
        fig, ax = plt.subplots(figsize=(6, 2))
        grafico_evolucao(df, titulo, ylabel, dado, 'linha', ax)
        fig.patch.set_alpha(0.0)
        st.pyplot(fig, transparent=True)

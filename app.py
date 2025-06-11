import streamlit as st
import matplotlib.pyplot as plt
from dados import carregar_dados
from graficos import grafico_evolucao

# Aplica o estilo CSS personalizado
css = """
<style>
    [data-testid="stSidebar"] {
        min-width: 250px;
        max-width: 350px;
        background-color: #f8f9fa;
        padding: 1rem;
        border-right: 1px solid #dee2e6;
        background: linear-gradient(to left , #cbd3d6 ,#137ea8);
    }

    [data-testid="stSidebar"] .css-1d391kg {
        font-family: 'Arial', sans-serif;
    }

    .stSelectbox label {
        font-size: 16px;
        font-weight: bold;
        color: #02394e;
        margin-bottom: 5px;
    }

    .stSelectbox div[data-baseweb="select"] {
        border-radius: 5px;
    }

    .stApp {
        background: linear-gradient(to left , #cbd3d6, #cbd3d6);
    }

    [data-testid="stSidebar"] h2 {
        font-size: 20px;
        color: white;
        font-weight: bold;
        text-align: left;
        margin-bottom: 20px;
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
st.sidebar.title("📊 Indicadores Demográficos")
grupo_escolhido = st.sidebar.selectbox("Escolha um grupo de indicadores:", list(grupos.keys()))
st.markdown(css, unsafe_allow_html=True)
# Tabs para mobile-friendly layout (2 gráficos por tab)
tab1, tab2 = st.tabs(["Gráficos 1 e 2", "Gráficos 3 e 4"])

# Tab 1 – primeiros dois gráficos
with tab1:
    fig, axs = plt.subplots(1, 2, figsize=(12, 5))
    for i in range(2):
        df, titulo, ylabel, dado = grupos[grupo_escolhido][i]
        grafico_evolucao(df, titulo, ylabel, dado, axs[i])
    st.pyplot(fig,transparent=True)

# Tab 2 – últimos dois gráficos
with tab2:
    fig, axs = plt.subplots(1, 2, figsize=(12, 5))
    for i in range(2, 4):
        df, titulo, ylabel, dado = grupos[grupo_escolhido][i]
        grafico_evolucao(df, titulo, ylabel, dado, axs[i - 2])
    st.pyplot(fig,transparent=True)

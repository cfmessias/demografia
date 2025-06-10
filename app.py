# app.py
import streamlit as st
import matplotlib.pyplot as plt
from dados import carregar_dados
from graficos import grafico_evolucao, grafico_evolucao1

# Carregar dados
(
    df_pop, df_dens, df_racio, df_cresc, 
    df_idade_media, df_taxa_alteracao_natural, 
    df_nascimentos, df_obitos, 
    df_esperanca_vida, df_esperanca_vida_homens80, df_esperanca_vida_mulheres80, 
    df_mortalidade_antes40, df_mortalidade_antes60, df_mortalidade_entre15e50, 
    df_taxa_migracao_liquida, df_mortalidade_entre15e50Homens,df_mortalidade_entre15e50Mulheres
) = carregar_dados()

# Agrupamento dos dados por temas
grupo_graficos = {
    "População e estrutura": [
        (df_pop, "População Total", "Milhares de Habitantes", "Populacao"),
        (df_dens, "Densidade Populacional", "Pessoas por km²", "Densidade"),
        (df_racio, "Rácio de Género", "Homens por 100 Mulheres", "RacioGenero"),
        (df_cresc, "Taxa de Crescimento Populacional", "%", "Crescimento")
    ],
    "Natalidade e mortalidade": [
        (df_nascimentos, "Nascimentos", "Milhares", "Nascimentos"),
        (df_obitos, "Óbitos", "Milhares", "Obitos"),
        (df_taxa_alteracao_natural, "Taxa de Alteração Natural", "Milhares", "TaxaAlteracaoNatural"),
        (df_esperanca_vida, "Esperança de Vida ao Nascer", "Anos", "EsperancaVida")
    ],
    "Mortalidade específica": [
        (df_mortalidade_antes40, "Mortalidade antes dos 40", "Óbitos por 1.000 nascimentos", "MortalidadeAntes40"),
        (df_mortalidade_antes60, "Mortalidade antes dos 60", "Óbitos por 1.000 nascimentos", "MortalidadeAntes60"),        
        (df_mortalidade_entre15e50Homens, "Mortalidade entre 15 e 50 (Homens)", "Óbitos por 1.000 homens vivos aos 15", "MortalidadeEntre15e50Homens"),
        (df_mortalidade_entre15e50Mulheres, "Mortalidade entre 15 e 50 (Mulheres)", "Óbitos por 1.000 mulheres vivas aos 15", "MortalidadeEntre15e50Mulheres"),
        (df_esperanca_vida_homens80, "Esperança de Vida aos 80 (Homens)", "Anos", "EsperancaVidaHomens80"),
        (df_esperanca_vida_mulheres80, "Esperança de Vida aos 80 (Mulheres)", "Anos", "EsperancaVidaMulheres80")
    ],
    "Indicadores adicionais": [
        (df_idade_media, "Idade Média", "Anos", "IdadeMedia"),
        (df_taxa_migracao_liquida, "Taxa de Migração Líquida", "Milhares", "TaxaMigracaoLiquida")
    ]
}

# Interface
st.set_page_config(layout="wide")
st.sidebar.title("Visualização Demográfica")
grupo_escolhido = st.sidebar.selectbox("Escolha um grupo de indicadores", list(grupo_graficos.keys()))

# Obter os gráficos do grupo escolhido
graficos = grupo_graficos[grupo_escolhido]

# Mostrar até 4 gráficos por página
num_graficos = len(graficos)
linhas = (num_graficos + 1) // 2  # até 2 colunas por linha
fig, axs = plt.subplots(linhas, 2, figsize=(16, 6 * linhas), subplot_kw=dict(aspect='auto'))
axs = axs.flatten()

for i, (df, titulo, ylabel, dado) in enumerate(graficos):
    grafico_evolucao1(df, titulo, ylabel, dado, axs[i])

# Esconder eixos vazios (caso menos de 4 gráficos)
for j in range(i + 1, len(axs)):
    axs[j].axis('off')

st.pyplot(fig)

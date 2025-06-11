import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

# Desenhar todos os gráficos sem legenda
for i, (df, titulo, ylabel, dado) in enumerate(grupo):
    grafico_evolucao(df, titulo, ylabel, dado, axs[i], mostrar_legenda=False)

# Criar legenda global com as cores dos continentes
cores_continentes = {
    "África": "#1f77b4",
    "América": "#ff7f0e",
    "Ásia": "#2ca02c",
    "Europa": "#d62728",
    "Oceania": "#9467bd"
}

# Criar handles da legenda
handles = [Line2D([0], [0], marker='o', color='w', label=continente,
                  markerfacecolor=cor, markersize=10)
           for continente, cor in cores_continentes.items()]

# Criar figura invisível com legenda
fig_legenda, ax_legenda = plt.subplots()
ax_legenda.axis('off')  # sem eixos
legenda = ax_legenda.legend(handles=handles, title="Continente", loc='center')
legenda.get_frame().set_facecolor('none')  # fundo transparente
legenda.get_frame().set_edgecolor('none')

fig_legenda.patch.set_alpha(0.0)  # fundo da figura transparente

# Mostrar legenda no Streamlit
st.pyplot(fig_legenda, transparent=True)

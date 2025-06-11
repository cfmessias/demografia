import matplotlib.pyplot as plt

cores_continentes = {
    "África": "#1f77b4",
    "América": "#ff7f0e",
    "Ásia": "#2ca02c",
    "Europa": "#d62728",
    "Oceania": "#9467bd"
}

def grafico_evolucao(dados, titulo, ylabel, dado, tipo,ax):
    continentes = dados["Continente"].unique()

    for continente in continentes:
        df_continente = dados[dados["Continente"] == continente]
        cor = cores_continentes.get(continente, None)
        
        if tipo == 'barra':
            ax.bar(df_continente["Year"], df_continente[dado], label=continente, color=cor, alpha=0.7)
        else:
            ax.plot(df_continente["Year"], df_continente[dado], label=continente, color=cor)

    ax.set_title(titulo)
    ax.set_ylabel(ylabel)
    ax.set_xlabel("Ano")
    ax.grid(True, linestyle="--", alpha=0.5)
    legenda = ax.legend(title="Continente", loc="best")
    legenda.get_frame().set_facecolor("none")


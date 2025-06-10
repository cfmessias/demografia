# graficos.py
import matplotlib.pyplot as plt


def grafico_evolucao(df,titulo, ylabel,dado,ax):
    for continente in df["Continente"].unique():
        dados = df[df["Continente"] == continente]
        ax.plot(dados["Year"], dados[dado], label=continente)
    ax.set_title(titulo)
    ax.set_xlabel("Ano")
    ax.set_ylabel(ylabel)
    ax.legend(title="Continente")
    ax.grid(True)

def grafico_evolucao1(df, titulo, ylabel, dado, ax, linewidth=3):
    # Definir cores para cada continente
    cores = {
        'África': '#137ea8',
        'Ásia': '#d35400', 
        'Europa': '#239b56',
        'América': '#7b241c',
        'Oceania': '#f1c40f'
    }
    
    for continente in df["Continente"].unique():
        dados = df[df["Continente"] == continente]
        cor = cores.get(continente, 'black')  # cor padrão se não encontrar
        ax.plot(dados["Year"], dados[dado], 
                label=continente, 
                color=cor, 
                linewidth=linewidth)
    ax.set_title(titulo)
    ax.set_xlabel("Ano")
    ax.set_ylabel(ylabel)
    ax.legend(title="Continente")
    ax.grid(True)
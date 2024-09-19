##Estrutura de um dashboard## --- Biblioteca e Documentação DashPlotly: dash.plotly.com
#Layout -> Tudo que será visualizado
#Callbacks -> Funcionalidades (zoom, prints, botões) que o tornam dinâmico

from dash import Dash, html, dcc, Output, Input
import pandas as pd
import plotly.express as px

app = Dash(__name__)

df = pd.read_excel("cursos-prouni.xlsx")
#Esta linha lê o arquivo Excel "cursos-prouni.xls" e armazena os dados na váriavel df

fig = px.bar(df, x="nota_integral_ampla", y="uf_busca", color="uf_busca", barmode="group")
#px chamada plotly -- bar é o gráfico (barras) -- x="Produto" é o eixo X -- y="Quantidade" é o eixo y -- color="ID Loja" define uma cor para cada ID LOJA
#barmode="group" define o tipo de gráfico, que é em barras agrupado

opcoes = list(df['uf_busca'].unique())
#Lista que pega os IDs na coluna "ID Loja" -- unique pega apenas 1 de cada.

opcoes.append("Nacional")
#Adiciona a string "Nacional" no final da lista opcoes

app.layout = html.Div(children=[
    html.H1(children='Notas PROUNI 2018'),
    html.H2(children='UFs com maiores notas exigidas'),
    dcc.Dropdown(opcoes, value='teste1', id='uf_busca'),

    dcc.Graph(
        id='grafico_quantidade_notas',
        figure=fig
    )

])

@app.callback(
    Output('grafico_quantidade_notas', 'figure'),
    Input('uf_busca', 'value')
    
)

def update_output(value):
    if value == "Nacional":
        fig = px.bar()(df, x="uf_busca", y="nota_integral_ampla", color="uf_busca", barmode="group")
    else:
        tabela_filtrada = df.loc[df['uf_busca'] == value, :]
        fig = px.bar(tabela_filtrada, x="uf_busca", y="nota_integral_ampla", color="uf_busca", barmode="group")

    return fig

if __name__ == '__main__':
    app.run(debug=True)



    


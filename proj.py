import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt


st.set_page_config(layout="wide", page_title="Análise de Crédito")


df = pd.read_csv("credito.csv")


traduzir_colunas = {
    'default': 'Inadimplente',
    'idade': 'Idade',
    'sexo': 'Sexo',
    'dependentes': 'Dependentes',
    'escolaridade': 'Escolaridade',
    'estado_civil': 'Estado Civil',
    'salario_anual': 'Salário Anual',
    'tipo_cartao': 'Tipo de Cartão',
    'meses_de_relacionamento': 'Meses de Relacionamento',
    'qtd_produtos': 'Quantidade de Produtos',
    'iteracoes_12m': 'Interações 12M',
    'meses_inativo_12m': 'Meses Inativos 12M',
    'limite_credito': 'Limite de Crédito',
    'valor_transacoes_12m': 'Valor Transações 12M',
    'qtd_transacoes_12m': 'Quantidade Transações 12M'
}
df.rename(columns=traduzir_colunas, inplace=True)
df['Inadimplente'] = df['Inadimplente'].map({0: 'Não', 1: 'Sim'})


st.write("Visualização dos Dados de Crédito")
st.dataframe(df.head())


st.sidebar.markdown("# Selecione o gráfico")
mostrar_inadimplentes_por_idade = st.sidebar.checkbox("Inadimplência por Idade", value=True)
mostrar_inadimplencia_sexo = st.sidebar.checkbox("Inadimplência por Sexo", value=True)
mostrar_salario = st.sidebar.checkbox("Distribuição do Salário Anual", value=True)
mostrar_limite_credito_tipo_cartao = st.sidebar.checkbox("Limite de Crédito por Tipo de Cartão", value=True)



col1, col2 = st.columns(2)

with col1:
    if mostrar_inadimplentes_por_idade:
        st.subheader("Inadimplência por Faixa Etária")
        fig_idade = px.histogram(df, x="Idade", color="Inadimplente", barmode="group", 
                                title="")
        st.plotly_chart(fig_idade, use_container_width=True)

    if mostrar_salario:
        st.subheader("Distribuição do Salário Anual")
        df_salario = df.groupby('Salário Anual').size().reset_index(name='count')
        fig_salario = px.bar(df_salario, x="Salário Anual", y="count", 
                            title="", color="Salário Anual")
        st.plotly_chart(fig_salario, use_container_width=True)

   



with col2:
    if mostrar_inadimplencia_sexo:
        st.subheader("Inadimplência por Gênero")
        fig_sexo = px.pie(df[df['Inadimplente'] == 'Sim'], names="Sexo", color="Sexo", 
                          title="")
        st.plotly_chart(fig_sexo, use_container_width=True)

    if mostrar_limite_credito_tipo_cartao:
        st.subheader("Limite de Crédito por Tipo de Cartão")
        fig_box = px.box(df, x='Tipo de Cartão', y='Limite de Crédito', color='Tipo de Cartão', 
                         color_discrete_sequence=px.colors.qualitative.Set2, 
                         labels={'Limite de Crédito': 'Limite de Crédito'},
                         title='')
        st.plotly_chart(fig_box, use_container_width=True)



    

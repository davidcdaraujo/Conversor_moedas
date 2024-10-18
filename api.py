import streamlit as st
import requests

# Função para realizar a conversão
def converter(moeda_base, moeda_destino, valor):
    url = f'https://v6.exchangerate-api.com/v6/363f4bd4dc6a73d2adde4775/pair/{moeda_base}/{moeda_destino}'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        taxa_conversao = data['conversion_rate']
        valor_convertido = valor * taxa_conversao
        return f"{valor} {moeda_base} = {valor_convertido:.2f} {moeda_destino}"
    else:
        return "Erro."

# Interface do Streamlit
st.title('Conversor de Moedas')

# Entradas do usuário
moeda_base = st.text_input("Moeda base:", 'USD').upper()
moeda_destino = st.text_input("Moeda destino:", 'EUR').upper()
valor = st.number_input("Digite o valor a ser convertido:", min_value=0.0, value=1.0)

# Botão para converter
if st.button('Converter'):
    resultado = converter(moeda_base, moeda_destino, valor)
    st.write(resultado)
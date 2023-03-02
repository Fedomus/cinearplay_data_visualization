import streamlit as st
import pandas as pd

st.title('')

DATA_URL = ('https://datos.arsat.com.ar/dataset/7b39da75-957b-4a70-8ae4-c801b69e2a75/resource/4e44f9ec-e280-4cc3-84f3-ea9935f0165a/download/cinear-visualizaciones-totales-2023-01_v1.csv')
DATA_USUARIOS_URL=('https://datos.arsat.com.ar/dataset/7b39da75-957b-4a70-8ae4-c801b69e2a75/resource/b5fa629c-a435-4b93-82f5-b1c8589c9c4a/download/cinear-usuarios-unicos-visualizaciones-2023-01_v1.csv')
DATA_USUARIOS_NUEVOS_URL = ('https://datos.arsat.com.ar/dataset/7b39da75-957b-4a70-8ae4-c801b69e2a75/resource/af95daed-ad0f-4ce6-8642-18ea913be6f6/download/cinear-nuevos-usuarios-2023-01_v1.csv')
DATA_HORAS_URL =('https://datos.arsat.com.ar/dataset/7b39da75-957b-4a70-8ae4-c801b69e2a75/resource/5c280bb8-f95c-41bb-8982-44ac2837837f/download/cinear-total-horas-vistas-2023-01_v1.csv')

@st.cache_data
def load_data():
    data = pd.read_csv(DATA_URL)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data['indice_tiempo'] = pd.to_datetime(data['indice_tiempo'])
    return data

@st.cache_data
def load_data_usuarios():
    data = pd.read_csv(DATA_USUARIOS_URL)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data['indice_tiempo'] = pd.to_datetime(data['indice_tiempo'])
    return data

@st.cache_data
def load_data_usuarios_nuevo():
    data = pd.read_csv(DATA_USUARIOS_NUEVOS_URL)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data['indice_tiempo'] = pd.to_datetime(data['indice_tiempo'])
    return data

@st.cache_data
def load_data_horas():
    data = pd.read_csv(DATA_HORAS_URL)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data['indice_tiempo'] = pd.to_datetime(data['indice_tiempo'])
    return data


    
data_load_state = st.text('Cargando la data...')

data = load_data()
usuarios_data = load_data_usuarios()
usuarios_nuevos = load_data_usuarios_nuevo()
horas = load_data_horas()

data_load_state.text("La data fue cargada con éxito!")

st.title('Cine.ar Play Data')

st.subheader('Visualizaciones totales en el tiempo')
st.line_chart(data=data, x='indice_tiempo', y='visualizaciones_totales', width=0, height=0, use_container_width=True)

st.subheader('Cantidad de usuarios unicos con visualizaciones en el tiempo')
st.line_chart(data=usuarios_data, x='indice_tiempo', y='usuarios_unicos_con_visualizaciones', width=0, height=0, use_container_width=True)

st.subheader('Nuevos usuarios por mes')
st.line_chart(data=usuarios_nuevos, x='indice_tiempo', y='nuevos_usuarios_por_mes_registrados', width=0, height=0, use_container_width=True)

st.subheader('Horas vistas en el tiempo')
st.line_chart(data=horas, x='indice_tiempo', y='total_horas_vistas', width=0, height=0, use_container_width=True)
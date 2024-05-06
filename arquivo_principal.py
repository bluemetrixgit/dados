import pandas as pd
import numpy as np
import streamlit as st
from dashboard import main
from contas_desenquadradas import projetobackoffice2,guide
from taxa_de_gestao import stramlit_visualizacao,calculando_gestao_btg_full
import base64


st.set_page_config(layout = 'wide')
background_image = "LOGO_BLUEMETRIX_VERTICAL jpg.jpg"

st.markdown(
    f"""
    <iframe src="data:image/jpg;base64,{base64.b64encode(open(background_image, 'rb').read()).decode(

    )}" style="width:4000px;height:3500px;position: absolute;top:-40vh;left:-1000px;opacity: 0.2;background-size: cover;background-position: center;"></iframe>
    """,
    unsafe_allow_html=True
)
paginas = ['Dados Bmrtx','Taxa de gestão','Enquadramento de contas']
paginas_radio = st.sidebar.radio('',paginas)

if paginas_radio == 'Dados Bmrtx':
    dashboard_bmtrx = main.Dashboard.criando_dashboard()

if paginas_radio == 'Enquadramento de contas':
    enquadramento_carteiras = projetobackoffice2.Enquandramento_de_carteiras.streamlit_visulização()

if paginas_radio == 'Taxa de gestão':
    taxa_de_gestao = stramlit_visualizacao.Taxa_de_gestao_streamlit.taxa_de_gestao_streamlit()
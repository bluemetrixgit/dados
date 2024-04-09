import pandas as pd
import numpy as np
import streamlit as st
from dashboard import main
from contas_desenquadradas import projetobackoffice2,guide
from taxa_de_gestao import stramlit_visualizacao,calculando_gestao_btg_full



st.set_page_config(layout = 'wide')
paginas = ['Dados Bmrtx','Taxa de gestão','Enquadramento de contas']
paginas_radio = st.sidebar.radio('',paginas)

if paginas_radio == 'Dados Bmrtx':
    dashboard_bmtrx = main.Dashboard.criando_dashboard()

if paginas_radio == 'Enquadramento de contas':
    enquadramento_carteiras = projetobackoffice2.Enquandramento_de_carteiras.streamlit_visulização()

if paginas_radio == 'Taxa de gestão':
    taxa_de_gestao = stramlit_visualizacao.Taxa_de_gestao_streamlit.taxa_de_gestao_streamlit()
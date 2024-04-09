import streamlit as st
import datetime
from sqlalchemy import create_engine
from io import BytesIO
import io
import pandas as pd
import numpy as np
import openpyxl as op
import xlsxwriter
from xlsxwriter import Workbook
import base64
from io import BytesIO
import io
import xlsxwriter as xlsxwriter
import datetime
import time
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Column, Float, Integer, String, DateTime
from io import StringIO
from dotenv import load_dotenv
import mysql.connector
import os
from sqlalchemy.engine import URL
from taxa_de_gestao.calculando_gestao_btg_full import CalculandoTaxadeGestao
# print('*'*50)



class Taxa_de_gestao_streamlit():
    def __init__(self):
        print('hello')

    def taxa_de_gestao_streamlit():
        connection_string = URL.create(
        drivername="mysql+pymysql",
        username="admin",
        password="bluemetrix",
        host="bmrtx-2024.c540o2gu0k2c.us-east-1.rds.amazonaws.com",
        port=3306,
        database="Bluemetrix"
        )
        
        dia_e_hora = datetime.datetime.now()


        st.header('Calculo e armazenamento dos dados da Taxa de Gestão')

        def registrar_dados_no_Mysql(dados):
            engine = create_engine(connection_string)
            dados.to_sql('taxa_admin',con=engine, if_exists='append',index=False)



        dia_e_hora = datetime.datetime.now().strftime("%Y-%m-%d")

        calculadora = CalculandoTaxadeGestao()


        guias = 'BTG','Guide','Ágora','Consulta'
        radio = st.sidebar.radio('',guias)

        if radio == 'BTG':
            planilha_de_controle_uploaded = st.sidebar.file_uploader(
                label='Solte o arquivo de Controle de Contratos',
                type=['xlsx'],
                key='upload_planilha_de_controle'
            )

            pl_uploaded = st.sidebar.file_uploader(
                label='Solte o arquivo de PL',
                type=['xlsx'],
                key='upload_pl'
            )
            # try:
            if planilha_de_controle_uploaded and pl_uploaded:
                dados_btg = calculadora.calculando_tx_gestao_BTG(planilha_de_controle_uploaded, pl_uploaded)


            if dados_btg is not None:

                output4 = io.BytesIO()
                with pd.ExcelWriter(output4, engine='xlsxwriter') as writer:
                    dados_btg.to_excel(writer,sheet_name='BTG', index=False)
                output4.seek(0)
                st.download_button(data=output4,file_name=f'BTG___{dia_e_hora}.xlsx',key='download_button',label='Download')        
        
            if st.button(f'Armazenar taxa de gestao BTG:   {dia_e_hora}',key='botao_btg'):
                try:
                    registrar_dados_no_Mysql(dados_btg)
                    st.success('Taxa registrada!')
                except:
                    st.warning('Erro no registro ')
            if st.button(f'Ver tabela BTG:  {dia_e_hora}'):

                st.dataframe(dados_btg)          
            # except:
            #     pass



        elif radio == 'Guide':
            planilha_de_controle_uploaded = st.sidebar.file_uploader(
                label='Solte o arquivo de Controle de Contratos',
                type=['xlsx'],
                key='upload_planilha_de_controle_guide'
            )

            pl_uploaded = st.sidebar.file_uploader(
                label='Solte o arquivo de PL',
                type=['xlsx'],
                key='upload_pl_guide'
            )
            try:
                
                    
                if planilha_de_controle_uploaded and pl_uploaded:
                    dados_guide = calculadora.calculando_tx_gestao_GUIDE(planilha_de_controle_uploaded, pl_uploaded)
                
                if dados_guide is not None:

                    output5 = io.BytesIO()
                    with pd.ExcelWriter(output5, engine='xlsxwriter') as writer:
                        dados_guide.to_excel(writer,sheet_name='Guide', index=False)
                    output5.seek(0)
                    st.download_button(data=output5,file_name=f'GUIDE___{dia_e_hora}.xlsx',key='download_button',label='Download')     

                if st.button(f'Armazenar taxa de gestao GUIDE:   {dia_e_hora}',key='botao_guide'):
                    try:
                        registrar_dados_no_Mysql(dados_guide)
                        st.success('Taxa calculada e registrada!')
                    except:
                        st.error('Não foi possivel executar')
                if st.button(f'Ver tabela Guide:  {dia_e_hora}',key='tabela_guide'):
                    st.dataframe(dados_guide)
            except:
                pass



        elif radio == 'Ágora':

            planilha_de_controle_uploaded = st.sidebar.file_uploader(
                label='Solte o arquivo de Controle de Contratos',
                type=['xlsx'],
                key='upload_planilha_de_controle_agora'
            )

            pl_uploaded = st.sidebar.file_uploader(
                label='Solte o arquivo de PL',
                type=['xlsx'],
                key='upload_pl_agora'
            )
            try:
                if planilha_de_controle_uploaded and pl_uploaded:
                    dados_agora = calculadora.calculando_tx_gestao_AGORA(planilha_de_controle_uploaded, pl_uploaded)
                
                if st.button(f'Armazenar taxa de gestao Ágora:   {dia_e_hora}',key='botao_agora'):
                    try:
                        registrar_dados_no_Mysql(dados_agora)
                        st.success('Taxa calculada e registrada!')
                    except:
                        st.error('Não foi possivel executar')

                if st.button(f'Ver tabela Ágora:  {dia_e_hora}',key='tabela_agora'):
                    st.dataframe(dados_agora)
                if dados_agora is not None:

                    output2 = io.BytesIO()
                    with pd.ExcelWriter(output2, engine='xlsxwriter') as writer:
                        dados_agora.to_excel(writer,sheet_name='Agora', index=False)
                    output2.seek(0)
                    st.download_button(data=output2,file_name=f'Agora___{dia_e_hora}.xlsx',key='download_button',label='Download')         
            except:
                pass

        if radio == 'Consulta':

            def consultar_data_base(data=None,conta=None):
                engine = create_engine(connection_string)

                consultar_sql = " SELECT * FROM taxa_admin"

                if data:
                    consultar_sql += f" WHERE Data = '{data}'"
                if conta:
                    consultar_sql += f" AND conta = '{conta}" if not data else f" AND conta = '{conta}'"

                resultados = pd.read_sql(consultar_sql,engine)
                return resultados

            def consultar_banco_de_dados_por_periodo(data_inicio, data_fim):
                engine = create_engine(connection_string)
                query = f"SELECT * FROM taxa_admin WHERE data BETWEEN '{data_inicio}' AND '{data_fim}'"
                arquivo_consulta = pd.read_sql(query, engine)
                return arquivo_consulta

            conta_input = st.sidebar.text_input('Digite a conta : ')

            data_inicio = st.sidebar.date_input("Data de Início")
            data_fim = st.sidebar.date_input("Data Fim")


            if data_inicio <= data_fim and st.sidebar.button('Consultar por período: '):
                arquivo_consulta_filtro2 = consultar_banco_de_dados_por_periodo(data_inicio, data_fim)
                arquivo_consulta_filtro = arquivo_consulta_filtro2.groupby('conta')['Valor_de_cobrança'].sum().reset_index()
                st.dataframe(arquivo_consulta_filtro)
                st.success(f"Valor total acumualdo para o período e de:  R$ {arquivo_consulta_filtro['Valor_de_cobrança'].sum():,.2f}")

            def consultar_banco_de_dados_completo():
                engine = create_engine(connection_string)
                arquivo_consulta = pd.read_sql(" SELECT * FROM taxa_admin",engine)
                return arquivo_consulta

            if st.sidebar.button("Consultar Banco de Dados"):
                arquivo_consulta = consultar_banco_de_dados_completo()
                st.dataframe(arquivo_consulta)
            try:
                if arquivo_consulta is not None:

                    output1 = io.BytesIO()
                    with pd.ExcelWriter(output1, engine='xlsxwriter') as writer:
                        arquivo_consulta.to_excel(writer,sheet_name='consulta', index=False)
                    output1.seek(0)
                    st.download_button(data=output1,file_name=f'consulta___{dia_e_hora}.xlsx',key='download_button',label='Download filtro')  
            except:
                pass 
            try:
                if arquivo_consulta_filtro is not None:

                    output7 = io.BytesIO()
                    with pd.ExcelWriter(output7, engine='xlsxwriter') as writer:
                        arquivo_consulta_filtro.to_excel(writer,sheet_name='consulta', index=False)
                    output7.seek(0)
                    st.download_button(data=output7,file_name=f'consulta___{dia_e_hora}.xlsx',key='download_button',label='Exporta toda base')  
            except:
                pass              





import pandas as pd
import streamlit as st
import openpyxl
import numpy as np
import plotly.graph_objects as pgo
import base64
from io import BytesIO
import io
import xlsxwriter as xlsxwriter
from contas_desenquadradas.guide import Contas_desenquadradas
from  contas_desenquadradas.guide import Btg_contas_desenquadradas


class Enquandramento_de_carteiras():
    def __init__(self):
          print('hello')
    def streamlit_visulização():
                    
        paginas = ['BTG','Guide']
        seletor_de_pagina = st.sidebar.radio("",paginas)

        if seletor_de_pagina == 'BTG':
            df = None
            daf = None


            upload_file = st.sidebar.file_uploader(label='Solte o arquivo de PL',type=['xlsx'],key='upload1')

            if upload_file  is not None:
                    
                    try:df = pd.read_excel(upload_file)
                    except Exception as e:st.write(f'Faltando arquivos:{e}')

            upload_file2 = st.sidebar.file_uploader(label='Solte o arquivo da planilha de Controle ',type=['xlsx'],key='upload2')

            if upload_file2  is not None:
                    try: daf = pd.read_excel(upload_file2,2,skiprows=1)
                    except Exception as e:st.write(f'Faltando arquivos:{e}')
                
            if df is not None and daf is not None:

                teste = Btg_contas_desenquadradas()
                arquivo_final = teste.manipulando_pl_BTG(df,daf)
                filtro_pl_0 = teste.pl_zerado_btg(arquivo_final)
                filtro_pl_abaixo_100k = teste.filtrando_pl_100(arquivo_final)
                filtro_income = teste.income_btg(arquivo_final)
                filtro_abaixo100k = teste.cemk_e_income(arquivo_final)

                st.subheader('Contas com valor de PL abaixo de R$100.000,00')
                st.dataframe(filtro_abaixo100k)
                st.subheader('Contas Income com PL abaixo de R$60.000,00')
                st.dataframe(filtro_income)
                st.subheader('Contas com valor de PL abaixo de R$1000,00')
                st.dataframe(filtro_pl_abaixo_100k)
                st.subheader('Contas zeradas partindo da planilha de controle')
                st.dataframe(filtro_pl_0)

            
                
                if arquivo_final is not None:
                    
                    
                    output4 = io.BytesIO()
                    st.markdown(" Download excel clientes com Saldo abaixo de R$ 100.000,00")
                    with pd.ExcelWriter(output4, engine='xlsxwriter') as writer:
                        filtro_abaixo100k.to_excel(writer,sheet_name='abaixo_de_100k.xlsx',index=False)
                    
                    output4.seek(0)
                    st.download_button(label="Clique para fazer o download",data=output4,file_name='Cliente com saldo abaixo de 100k.xlsx',key='download_button')

                    output1 = io.BytesIO()
                    st.markdown(" Download excel clientes income e saldo menor R$ 60.000,00")
                    with pd.ExcelWriter(output1, engine='xlsxwriter') as writer:
                        filtro_income.to_excel(writer,sheet_name='income.xlsx',index=False)
                    
                
                    output1.seek(0)
                    st.download_button(label="Clique para fazer o download",data=output1,file_name='Income_abaixo_60k.xlsx',key='download_button1')

                    output2 = io.BytesIO()
                    st.markdown(" Download excel clientes com Saldo abaixo de R$ 1000,00")

                    with pd.ExcelWriter(output2, engine='xlsxwriter') as writer:
                        filtro_pl_abaixo_100k.to_excel(writer,
                                                    sheet_name='pl_abaixo_1000k.xlsx',
                                                    index=False)

                    output2.seek(0)
                    st.download_button(label="Clique para fazer o download",data=output2,file_name='Cliente_saldo_1000.xlsx',key='download_button2')

                    output3 = io.BytesIO()
                    st.markdown(" Download excel clientes com Saldo 0,00")
                    with pd.ExcelWriter(output3, engine='xlsxwriter') as writer:
                        filtro_pl_0.to_excel(writer,sheet_name='contas_0.xlsx',index=False)   
                    output3.seek(0)
                    st.download_button(label="Clique para fazer o download",data=output3,file_name='Contas_zeradas.xlsx',key='download_button3')
                

        if seletor_de_pagina == "Guide":
            df = None
            daf = None
            
            upload_file3 = st.sidebar.file_uploader(label='Solte o arquivo de PL',type=['xlsx'],key='upload3')
            if upload_file3  is not None:
                try: df = pd.read_excel(upload_file3)
                except Exception as e:st.write(f'Faltando arquivos:{e}')

            ####    arquivo 2
                
            upload_file4 = st.sidebar.file_uploader(label='Solte o arquivo da planilha de Controle ',type=['xlsx'],key='upload4')
            if upload_file4  is not None:
                    try: daf = pd.read_excel(upload_file4,3,skiprows=1).iloc[:,[1,2,4,5,7,8,12,-1]]
                    except Exception as e:st.write(f'Faltando arquivos:{e}')

            if df is not None and daf is not None:

                    teste = Contas_desenquadradas()
                    arquivo_final = teste.manipulado_pl_guide(df,daf)
                    pl_0 = teste.pl_0(arquivo_final)
                    filtro_pl_abaixo_100k = teste.income_abaixo_100(arquivo_final)
                    filtro_income = teste.income(arquivo_final)
                    filtro_abaixo100k = teste.filtro_pl_100(arquivo_final)

                    st.subheader('Contas com valor de PL abaixo de R$100.000,00')
                    st.dataframe(filtro_abaixo100k)
                    st.subheader('Contas Income com PL abaixo de R$60.000,00')
                    st.dataframe(filtro_income)
                    st.subheader('Contas com valor de PL abaixo de R$1000,00')
                    st.dataframe(filtro_pl_abaixo_100k)
                    st.subheader('Contas zeradas partindo da planilha de controle')
                    st.dataframe(pl_0)

                    if arquivo_final is not None:

                        output5 = io.BytesIO()
                        st.markdown(" Download excel clientes com Saldo abaixo de R$ 100.000,00")
                        with pd.ExcelWriter(output5, engine='xlsxwriter') as writer:
                            filtro_abaixo100k.to_excel(writer,sheet_name='abaixo_de_100k.xlsx',index=False)
                        
                        output5.seek(0)
                        st.download_button(label="Clique para fazer o download",data=output5,file_name='Cliente com saldo abaixo de 100k.xlsx',key='download_button')

                
                        output6 = io.BytesIO()
                        st.markdown(" Download excel clientes income e saldo menor R$ 60.000,00")
                        with pd.ExcelWriter(output6, engine='xlsxwriter') as writer:
                            filtro_income.to_excel(writer,sheet_name='income.xlsx',index=False)
                        output6.seek(0)
                        st.download_button(label="Clique para fazer o download",data=output6,file_name='Income_abaixo_60k.xlsx',key='download_button1')


                        output7 = io.BytesIO()
                        st.markdown(" Download excel clientes com Saldo abaixo de R$ 1000,00")

                        with pd.ExcelWriter(output7, engine='xlsxwriter') as writer:
                            filtro_pl_abaixo_100k.to_excel(writer,
                                                        sheet_name='pl_abaixo_1000k.xlsx',
                                                        index=False)

                        output7.seek(0)
                        st.download_button(label="Clique para fazer o download",data=output7,file_name='Cliente_saldo_1000.xlsx',key='download_button2')


                        output8 = io.BytesIO()
                        st.markdown(" Download excel clientes com Saldo 0,00")
                        with pd.ExcelWriter(output8, engine='xlsxwriter') as writer:
                            pl_0.to_excel(writer,sheet_name='contas_0.xlsx',index=False)   
                        output8.seek(0)
                        st.download_button(label="Clique para fazer o download",data=output8,file_name='Contas_zeradas.xlsx',key='download_button3')
                            
    #st.download_button(

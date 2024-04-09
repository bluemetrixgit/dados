
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import streamlit as st
import openpyxl as op
import xlsxwriter
from xlsxwriter import Workbook
import base64
from io import BytesIO
import io
import xlsxwriter as xlsxwriter
import datetime
import time
import os
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Column, Float, Integer, String, DateTime
from io import StringIO



class CalculandoTaxadeGestao():

    def __init__(self):
        self.planilha_de_controle = None
        self.pl = None

    def calculando_tx_gestao_BTG(self, uploaded_planilha_de_controle=None, uploaded_pl=None):

        if uploaded_planilha_de_controle is not None:
            try:
                self.planilha_controle = pd.read_excel(uploaded_planilha_de_controle, sheet_name=2, skiprows=1)
            except Exception as e:
                st.write(f'Faltando arquivos:{e}')

        if uploaded_pl is not None:
            try:
                self.pl = pd.read_excel(uploaded_pl)
            except Exception as e:
                st.write(f'Faltando arquivos:{e}')



        calculo_diario = 1/252
        dia_e_hora = datetime.datetime.now().strftime("%Y-%m-%d")

        self.planilha_controle['Conta'] = self.planilha_controle['Conta'].astype(str).str[:-2].map(lambda x: '00'+x)
        self.planilha_controle = self.planilha_controle[['Conta','Taxa de Gestão']]

        self.planilha_controle.rename(columns={'Taxa de Gestão':'Taxa_de_Gestão','Conta':'conta'},inplace=True)
        tx_gestao = pd.merge(self.planilha_controle,self.pl, left_on='conta',right_on='Conta',how='outer')
        tx_gestao = tx_gestao[['conta','Taxa_de_Gestão','Valor']].rename(columns={'Valor':'VALOR'})
        selecionar_data = st.date_input('Data')
        tx_gestao['Data'] = selecionar_data
        tx_gestao['Tx_Gestão_Diaria'] = ((tx_gestao['Taxa_de_Gestão']+1)**calculo_diario-1)*100
        tx_gestao['Valor_de_cobrança'] = tx_gestao['VALOR']*(tx_gestao['Tx_Gestão_Diaria'])/100
        tx_gestao = tx_gestao.dropna(subset=['conta'])
        return tx_gestao


        
    def calculando_tx_gestao_GUIDE(self,uploaded_planilha_de_controle,uploaded_pl):
                
        if uploaded_planilha_de_controle is not None:
            try:
                self.planilha_controle = pd.read_excel(uploaded_planilha_de_controle, sheet_name=3, skiprows=1)
            except Exception as e:
                st.write(f'Faltando arquivos:{e}')

        if uploaded_pl is not None:
            try:
                self.guide_pl = pd.read_excel(uploaded_pl)
            except Exception as e:
                st.write(f'Faltando arquivos:{e}')
    
        calculo_diario = 1/252
        dia_e_hora = datetime.datetime.now().strftime("%Y-%m-%d")

        self.planilha_controle = self.planilha_controle[['Conta','Taxa de Gestão']]
        self.guide_pl = self.guide_pl[['CLIE_ID','SALDO_BRUTO']].rename(columns={'CLIE_ID':'Conta','SALDO_BRUTO':'VALOR'})
        self.guide_pl = self.guide_pl.groupby('Conta')['VALOR'].sum().reset_index()
        self.guide_pl['Conta'] = self.guide_pl['Conta'].astype(str)
        self.planilha_controle['Conta'] = self.planilha_controle['Conta'].str[:-1]
        tx_gestao = pd.merge(self.planilha_controle,self.guide_pl,on='Conta',how='outer').dropna().rename(columns={'Conta':'conta',
                                                                                                         'Taxa de Gestão':'Taxa_de_Gestão'}).reset_index(drop='index')
        selecionar_data = st.date_input('Data')
        tx_gestao['Data'] = selecionar_data
        tx_gestao['Tx_Gestão_Diaria'] = ((tx_gestao['Taxa_de_Gestão']+1)**calculo_diario-1)*100
        tx_gestao[f'Valor_de_cobrança'] = tx_gestao['VALOR']*(tx_gestao['Tx_Gestão_Diaria'])/100   
        
        return tx_gestao



    def calculando_tx_gestao_AGORA(self,uploaded_planilha_de_controle,uploaded_pl):
        
        if uploaded_planilha_de_controle is not None:
            try:
                self.planilha_controle = pd.read_excel(uploaded_planilha_de_controle, sheet_name=5, skiprows=1)
            except Exception as e:
                st.write(f'Faltando arquivos:{e}')

        if uploaded_pl is not None:
            try:
                self.pl_agora = pd.read_excel(uploaded_pl)
            except Exception as e:
                st.write(f'Faltando arquivos:{e}')
            

        self.planilha_controle = self.planilha_controle[['Nome','Conta','Taxa de Gestão']].iloc[:-5,:]
        self.pl_agora = self.pl_agora.iloc[3:,:]



        bovespa_vista_start = self.pl_agora[self.pl_agora['Gestora'] == 'BOVESPA A VISTA'].index[0]
        bovespa_vista_end = self.pl_agora[self.pl_agora['Gestora'] == 'BOVESPA OPC'].index[0]
        bovespa_vista_data = self.pl_agora.iloc[bovespa_vista_start :bovespa_vista_end].iloc[:-5]

        #tesouro_direto_start = pl_agora[pl_agora['Unnamed: 2'] == 'Codigo Cliente'].index[0]#.searchsorted(0)[0]
        tesouro_direto_start = self.pl_agora[self.pl_agora['Gestora']=='BMF'].index[-1]
        tesouro_direto_end = self.pl_agora[self.pl_agora['Gestora'] == 'FUNDOS'].index[0]
        tesouro_direto_data = self.pl_agora.iloc[tesouro_direto_start :tesouro_direto_end].iloc[:-5]

        renda_fixa_start = self.pl_agora[self.pl_agora['Gestora'] == 'FUNDOS'].index[-1]
        renda_fixa_end = self.pl_agora[self.pl_agora['Gestora'] == 'ALUGUEL'].index[0]
        renda_fixa_data = self.pl_agora.iloc[renda_fixa_start:renda_fixa_end]

        aluguel_start = self.pl_agora[self.pl_agora['Gestora'] == 'ALUGUEL'].index[0]
        aluguel_end = self.pl_agora[self.pl_agora['Gestora'] == 'GARANTIAS'].index[0]
        aluguel_data = self.pl_agora.iloc[aluguel_start :aluguel_end]

        garantias_start = self.pl_agora[self.pl_agora['Gestora'] == 'ALUGUEL'].index[-1]
        garantias_end = self.pl_agora.shape[0]
        garantias_data = self.pl_agora.iloc[garantias_start:garantias_end]

        bovespa_vista_data['Valor_pl'] = bovespa_vista_data['Unnamed: 12']*bovespa_vista_data['Unnamed: 13']

        bovespa_vista_data_agregado = bovespa_vista_data.groupby('Unnamed: 4')['Valor_pl'].sum().reset_index().rename(columns={'Unnamed: 4':'BLUEMETRIX'})

        tesouro_direto_agregado = tesouro_direto_data.groupby('BLUEMETRIX')['Unnamed: 6'].sum().reset_index()

        renda_fixa_agregado = renda_fixa_data.groupby('BLUEMETRIX')['Unnamed: 8'].sum().reset_index()

        garantias_agregado = garantias_data.groupby('Unnamed: 3')['Unnamed: 12'].sum().reset_index().rename(columns={'Unnamed: 3':'BLUEMETRIX'})

        tx_gestao= pd.merge(bovespa_vista_data_agregado,tesouro_direto_agregado, on='BLUEMETRIX',how='outer').merge(
            renda_fixa_agregado, on='BLUEMETRIX',how='outer'
        ).merge(garantias_agregado,how='outer',on='BLUEMETRIX')

        if 'Nome' in tx_gestao['BLUEMETRIX'].values and 'CPF' in tx_gestao['BLUEMETRIX'].values:
            # Elimine as linhas que contenham 'Nome' ou 'CPF' nos valores
            tx_gestao= tx_gestao[(tx_gestao['BLUEMETRIX'] != 'Nome') & (tx_gestao['BLUEMETRIX'] != 'CPF')]
        else:
            print("As palavras 'Nome' e 'CPF' não foram encontradas nos valores das linhas.")

        tranformar_colunas_em_numericas = ['Valor_pl','Unnamed: 6','Unnamed: 8','Unnamed: 12']
        for coluna in tranformar_colunas_em_numericas:
            tx_gestao[coluna] = tx_gestao[coluna].astype(float)
        arrumar_nomes = {
            'AFRISIO DE SOUZA VIEIRA LIMA FILHO':'Afrisio de Souza Vieira Lima Filho',
            'BRUNO CESAR PESQUERO PONCE JAIME':'Bruno Cesar Pesquero Ponce Jaime ',
            'MARCELO JAIME FERREIRA':'Marcelo Jaime Ferreira',
            'MARCIA CARVALHO GAZETA':'Márcia Carvalho Gazeta',
            'OTAVIO ALVES FORTE':'Otávio Alves Forte',
            'SERGIO LINCOLN DE MATOS ARRUDA':'Sergio Lincoln de Matos Arruda',
            'SILEDE SATYRO DE SA RIBEIRO':'Silede Satyro de Sá Ribeiro',
            'J & M CONSULTORIA EMPRESARIAL LTDA':'J & M Consultoria Empresarial LTDA  '    
        }
        tx_gestao['BLUEMETRIX'] = tx_gestao['BLUEMETRIX'].replace(arrumar_nomes)
        colunas_numericas = tx_gestao.select_dtypes(include=[np.number])
        tx_gestao['VALOR'] = round(colunas_numericas.sum(axis=1),2)
        tx_gestao = tx_gestao.iloc[:,[0,-1]].merge(self.planilha_controle,left_on='BLUEMETRIX',right_on='Nome',how='left').rename(columns={
            'Taxa de Gestão':'Taxa_de_Gestão',
            'Conta':'conta'
        })

        calculo_diario = 1/252
        dia_e_hora = datetime.datetime.now().strftime("%Y-%m-%d")
        selecionar_data = st.date_input('Data')
        tx_gestao['Data'] = selecionar_data
        tx_gestao['Tx_Gestão_Diaria'] = ((tx_gestao['Taxa_de_Gestão']+1)**calculo_diario-1)*100
        tx_gestao[f'Valor_de_cobrança'] = tx_gestao['VALOR']*(tx_gestao['Tx_Gestão_Diaria'])/100   
        tx_gestao = tx_gestao.iloc[:,[3,4,1,5,6,7]]
        return tx_gestao



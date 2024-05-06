import pandas as pd
import plotly.graph_objects as go
import gunicorn
from pprint import pprint
import streamlit as st
import numpy as np
from datetime import datetime,timedelta
import openpyxl





class Dashboard():
    def __init__(self):
        print('hello')
    def criando_dashboard():        
        lista_pag =[0,1,2,3,4,5]
        @st.cache_data
        def le_excel(x,y):
            df_dic = pd.read_excel(x,y)
            return df_dic

        btg = le_excel(r'Controle de Contratos - Atualizado Fevereiro de 2024 (3).xlsx',2)
        guide = le_excel(r'Controle de Contratos - Atualizado Fevereiro de 2024 (3).xlsx',3)
        genial = le_excel(r'Controle de Contratos - Atualizado Fevereiro de 2024 (3).xlsx',4)
        agora = le_excel(r'Controle de Contratos - Atualizado Fevereiro de 2024 (3).xlsx',5)
        orama = le_excel(r'Controle de Contratos - Atualizado Fevereiro de 2024 (3).xlsx',6)
        novas = le_excel(r'Controle de Contratos - Atualizado Fevereiro de 2024 (3).xlsx',7)
        co_admin = pd.read_excel(r'Controle de Contratos - Carteiras Co-Administradas.xlsx',1,skiprows=1).iloc[:-5,:]


        ###########
        # renomeando colunas periodo de 2023
        # ##########
        lista_core0=[btg,guide,genial,agora,orama,co_admin]
        lista_core = [btg,guide,genial,agora,orama]
        lista_core2 = [guide,genial]



        for corretora in lista_core0:
            nome_ultima_col = corretora.columns[-1]

            novo_nome = 'Março/2024'
            corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)

        for corretora in lista_core0:
            nome_ultima_col = corretora.columns[-2]

            novo_nome = 'Fevereiro/2024'
            corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)

        for corretora in lista_core0:
            nome_ultima_col = corretora.columns[-3]

            novo_nome = 'Janeiro/2024'
            corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)


        for corretora in lista_core:
            nome_ultima_col = corretora.columns[-4]

            novo_nome = 'Dezembro/2023'
            corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)
        for corretora in lista_core:
            nome_ultima_col = corretora.columns[-5]

            novo_nome = 'Novembro/2023'
            corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)

        for corretora in lista_core:
            nome_ultima_col = corretora.columns[-6]

            novo_nome = 'Outubro/2023'
            corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)


        for corretora in lista_core:
            nome_ultima_col = corretora.columns[-7]

            novo_nome = 'Setembro/2023'
            corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)
            lista_core = [btg,guide,genial,agora,orama,novas]

        for corretora in lista_core:
            nome_ultima_col = corretora.columns[-8]

            novo_nome = 'Agosto/2023'
            corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)


        for corretora in lista_core:
            nome_ultima_col = corretora.columns[-9]

            novo_nome = 'julho/2023'
            corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)


        for corretora in lista_core:
            nome_ultima_col = corretora.columns[-10]

            novo_nome = 'junho/2023'
            corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)



        for corretora in lista_core:
            nome_ultima_col = corretora.columns[-11]

            novo_nome = 'Maio/2023'
            corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)


        for corretora in lista_core:
            nome_ultima_col = corretora.columns[-12]

            novo_nome = 'Abril/2023'
            corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)



        for corretora in lista_core:
            nome_ultima_col = corretora.columns[-13]

            novo_nome = 'Março/2023'
            corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)


        for corretora in lista_core2:
            nome_ultima_col = corretora.columns[-14]

            novo_nome = 'fereiro/2023'
            corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)

        for corretora in lista_core2:
            nome_ultima_col = corretora.columns[-15]

            novo_nome = 'Janeiro/2023'
            corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)

            
        ###########
        # renomeando colunas periodo de 2022
        # ##########

        for corretora in lista_core2:
            nome_ultima_col = corretora.columns[-16]

            novo_nome = 'Dezembro/2022'
            corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)


        for corretora in lista_core2:
            nome_ultima_col = corretora.columns[-17]

            novo_nome = 'Novembro/2022'
            corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)


        for corretora in lista_core2:
            nome_ultima_col = corretora.columns[-18]

            novo_nome = 'Outubro/2022'
            corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)


        for corretora in lista_core2:
            nome_ultima_col = corretora.columns[-19]

            novo_nome = 'Setembro/2022'
            corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)


        for corretora in lista_core2:
            nome_ultima_col = corretora.columns[-20]

            novo_nome = 'Agosto/2022'
            corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)


        for corretora in lista_core2:
            nome_ultima_col = corretora.columns[-21]

            novo_nome = 'julho/2022'
            corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)


        for corretora in lista_core2:
            nome_ultima_col = corretora.columns[-22]

            novo_nome = 'junho/2022'
            corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)



        for corretora in lista_core2:
            nome_ultima_col = corretora.columns[-23]

            novo_nome = 'Maio/2022'
            corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)


        for corretora in lista_core2:
            nome_ultima_col = corretora.columns[-24]

            novo_nome = 'Abril/2022'
            corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)


        for corretora in lista_core2:
            nome_ultima_col = corretora.columns[-25]

            novo_nome = 'Março/2022'
            corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)



        for corretora in lista_core2:
            nome_ultima_col = corretora.columns[-26]

            novo_nome = 'fereiro/2022'
            corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)

        for corretora in lista_core2:
            nome_ultima_col = corretora.columns[-27]

            novo_nome = 'Janeiro/2022'
            corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)


        ###########
        # renomeando colunas periodo de 2021
        # ##########

        for corretora in lista_core2:
            nome_ultima_col = corretora.columns[-28]

            novo_nome = 'Dezembro/2021'
            corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)


        for corretora in lista_core2:
            nome_ultima_col = corretora.columns[-29]

            novo_nome = 'Novembro/2021'
            corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)


        for corretora in lista_core2:
            nome_ultima_col = corretora.columns[-30]

            novo_nome = 'Outubro/2021'
            corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)


        for corretora in lista_core2:
            nome_ultima_col = corretora.columns[-31]

            novo_nome = 'Setembro/2021'
            corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)


        for corretora in lista_core2:
            nome_ultima_col = corretora.columns[-32]

            novo_nome = 'Agosto/2021'
            corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)


        for corretora in lista_core2:
            nome_ultima_col = corretora.columns[-33]

            novo_nome = 'julho/2021'
            corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)


        for corretora in lista_core2:
            nome_ultima_col = corretora.columns[-34]

            novo_nome = 'junho/2021'
            corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)



        for corretora in lista_core2:
            nome_ultima_col = corretora.columns[-35]

            novo_nome = 'Maio/2021'
            corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)


        for corretora in lista_core2:
            nome_ultima_col = corretora.columns[-36]

            novo_nome = 'Abril/2021'
            corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)


        for corretora in lista_core2:
            nome_ultima_col = corretora.columns[-37]

            novo_nome = 'Março/2021'
            corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)


        for corretora in lista_core2:
            nome_ultima_col = corretora.columns[-38]

            novo_nome = 'fereiro/2021'
            corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)

        for corretora in lista_core2:
            nome_ultima_col = corretora.columns[-39]

            novo_nome = 'Janeiro/2021'
            corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)

        ###########
        # renomeando colunas periodo de 2021
        # ##########


        for corretora in lista_core2:
            nome_ultima_col = corretora.columns[-40]

            novo_nome = 'Dezembro/2020'
            corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)


        for corretora in lista_core2:
            nome_ultima_col = corretora.columns[-41]

            novo_nome = 'Novembro/2020'
            corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)


        for corretora in lista_core2:
            nome_ultima_col = corretora.columns[-42]

            novo_nome = 'Outubro/2020'
            corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)


        for corretora in lista_core2:
            nome_ultima_col = corretora.columns[-43]

            novo_nome = 'Setembro/2020'
            corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)


        for corretora in lista_core2:
            nome_ultima_col = corretora.columns[-44]

            novo_nome = 'Agosto/2020'
            corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)


        for corretora in lista_core2:
            nome_ultima_col = corretora.columns[-45]

            novo_nome = 'julho/2020'
            corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)


        for corretora in lista_core2:
            nome_ultima_col = corretora.columns[-46]

            novo_nome = 'junho/2020'
            corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)


        for corretora in lista_core2:
            nome_ultima_col = corretora.columns[-47]

            novo_nome = 'Maio/2020'
            corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)


        for corretora in lista_core2:
            nome_ultima_col = corretora.columns[-48]

            novo_nome = 'Abril/2020'
            corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)


        for corretora in lista_core2:
            nome_ultima_col = corretora.columns[-49]

            novo_nome = 'Março/2020'
            corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)


        for corretora in lista_core2:
            nome_ultima_col = corretora.columns[-50]

            novo_nome = 'fereiro/2020'
            corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)

        for corretora in lista_core2:
            nome_ultima_col = corretora.columns[-51]

            novo_nome = 'Janeiro/2020'
            corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)


        ###########                        ###########
        # Padrozinar as colunas de todos os df para conseguir concatenar o arquivo em seguida
        # ##########                        ###########





        ###########        
        # Tratando dados BTG
        # ##########   
        #print(btg.colum)

        colunas_remover_btg = ['Mesa de Operação.1','Backoffice.2',     
        'Gestão/ Head comercial',
        
        'Anbima',
        'Unnamed: 20',
        'Unnamed: 21',
        'Unnamed: 22',
        'Financeiro',
        'Unnamed: 24',
        'Unnamed: 25',
        'Unnamed: 27','Backoffice.1'
        ]

        for colunas in colunas_remover_btg:
            btg.drop(columns=[colunas],inplace=True)
        
            ########### 
        # Tratando dados GUIDE
        # ##########

        colunas_remover_guide = [
        'Unnamed: 15', 'Unnamed: 16',
        'Unnamed: 17', 'Mesa de Operação ', 'Gestão/ Head comercial',
        'Backoffice .2', 'Anbima',  'Unnamed: 23',
        'Unnamed: 24', 'Unnamed: 25', 'Unnamed: 27',
        ]

        for col in colunas_remover_guide:
            guide.drop(columns=[col],inplace = True)

        ###########  
        # Tratando dados GENIAL
        # ##########  

        colunas_remover_genial = [
            'Mesa de Operação ',
            'Gestão/ Head comercial', 'Backoffice ', 'Anbima',
            'Unnamed: 20', 'Unnamed: 21', 'Financeiro', 'Unnamed: 23',
            'Unnamed: 24', 'Unnamed: 25', ]

        for col in colunas_remover_genial:
            genial.drop(columns=[col],inplace =True)



        ########### 
        # Tratando dados Agora
        # ##########      

        colunas_remover_agora = [
            'Mesa de Operação ',
            'Gestão/ Head comercial', 'Backoffice ', 'Anbima',
            'Unnamed: 20', 'Unnamed: 21']
        for col in colunas_remover_agora:
            agora.drop(columns=[col],inplace=True)

        ###########     
        # Tratando dados Agora
        # ##########   
            
        colunas_remover_orama = [ 'Mesa de Operação ', 'Backoffice ',
            'Anbima', 'Unnamed: 19', 'Unnamed: 20']
        for col in colunas_remover_orama:
            orama.drop(columns=[col],inplace=True)



        ###########           ###########
        # Tratando corrigindo nome das colunas 
        # ##########           ###########    

        for corretora in lista_core:
            nome_ultima_col = corretora.columns[0]

            novo_nome = 'Corretora'
            corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)

        for corretora in lista_core:
            nome_ultima_col = corretora.columns[1]

            novo_nome = 'Nome_cliente'
            corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)

        for corretora in lista_core:
            nome_ultima_col = corretora.columns[2]

            novo_nome = 'Conta'
            corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)

        for corretora in lista_core:
            nome_ultima_col = corretora.columns[3]

            novo_nome = 'Escritorio'
            corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)

        for corretora in lista_core:
            nome_ultima_col = corretora.columns[4]

            novo_nome = 'UF'
            corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)

        for corretora in lista_core:
            nome_ultima_col = corretora.columns[5]

            novo_nome = 'Assessor'
            corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)

        for corretora in lista_core:
            nome_ultima_col = corretora.columns[7]

            novo_nome = 'Status'
            corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)

        for corretora in lista_core:
            nome_ultima_col = corretora.columns[8]

            novo_nome = 'Exeção'
            corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)

        for corretora in lista_core:
            nome_ultima_col = corretora.columns[9]

            novo_nome = 'Inicio da gestão'
            corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)

        for corretora in lista_core:
            nome_ultima_col = corretora.columns[10]

            novo_nome = 'Data do distrato'
            corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)

        for corretora in lista_core:
            nome_ultima_col = corretora.columns[11]

            novo_nome = 'Carteira'
            corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)

        for corretora in lista_core:
            nome_ultima_col = corretora.columns[12]

            novo_nome = 'Taxa de gestão'
            corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)

        for corretora in lista_core:
            nome_ultima_col = corretora.columns[13]

            novo_nome = 'Benchmark'
            corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)

        for corretora in lista_core:
            nome_ultima_col = corretora.columns[14]

            novo_nome = 'Taxa de performance'
            corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)

        for corretora in lista_core:
            corretora = corretora.iloc[1:-5]

            ['index', 'Corretora', 'Nome_cliente', 'Conta', 'Escritorio', 'UF',
       'Assessor', 'Mesa de Operação', 'Status', 'Exeção', 'Inicio da gestão',
       'Data do distrato', 'Carteira', 'Taxa de gestão', 'Benchmark',
       'Taxa de performance', 'Unnamed: 23', 'Unnamed: 28', 'Unnamed: 29',
       'Unnamed: 30']
            
        co_admin =co_admin.rename(columns={                
            'Cliente':'Nome_cliente',
            'Escritório':'Escritorio',
            'Operador':'Mesa de Operação',
            'Início da Gestão':'Inicio da gestão',
            'Data distrato':'Data do distrato',
            'Taxa de Gestão':'Taxa de gestão',
            'Benchmark TX. Perf':'Benchmark',
            'TX. Perf.':'Taxa de performance'})

        
        arquivo_final = pd.concat([btg,guide,genial,agora,orama,co_admin]).reset_index()

        arquivo_final.drop(columns=['index'],inplace=True)
        arquivo_final.drop(988,inplace=True)
        linhas_para_retirar = [588,593,983,984,985,986,987,1019,1020,1021,1022,1023,1036,1037,1038,1039,1040,1041,1044,1045,1046,1047,1048]
        arquivo_final.drop(linhas_para_retirar,inplace=True)
        arquivo_final.drop(1018,inplace=True)

        arquivo_final = arquivo_final[[
            'Corretora', 'Nome_cliente', 'Conta', 'Escritorio', 'UF', 'Assessor',
            'Mesa de Operação', 'Status', 'Exeção', 'Inicio da gestão',
            'Data do distrato', 'Carteira', 'Taxa de gestão',
                'Benchmark','Taxa de performance','Janeiro/2020', 'fereiro/2020', 'Março/2020',
            'Abril/2020', 'Maio/2020', 'junho/2020', 'julho/2020', 'Agosto/2020',
            'Setembro/2020', 'Outubro/2020', 'Novembro/2020', 'Dezembro/2020',
            'Janeiro/2021', 'fereiro/2021', 'Março/2021', 'Abril/2021', 'Maio/2021',
            'junho/2021', 'julho/2021', 'Agosto/2021', 'Setembro/2021',
            'Outubro/2021', 'Dezembro/2021', 'Novembro/2021', 'fereiro/2022',
            'Março/2022', 'Abril/2022', 'Maio/2022', 'junho/2022', 'julho/2022',
            'Agosto/2022', 'Setembro/2022', 'Outubro/2022', 'Novembro/2022',
            'Dezembro/2022', 'Janeiro/2023', 'fereiro/2023',
                'Março/2023', 'Abril/2023', 'Maio/2023',
            'junho/2023', 'julho/2023', 'Agosto/2023', 'Setembro/2023',
            'Outubro/2023','Novembro/2023','Dezembro/2023','Janeiro/2024','Fevereiro/2024','Março/2024'
        ]]

        col_fill_na = ['Janeiro/2020', 'fereiro/2020', 'Março/2020',
            'Abril/2020', 'Maio/2020', 'junho/2020', 'julho/2020', 'Agosto/2020',
            'Setembro/2020', 'Outubro/2020', 'Novembro/2020', 'Dezembro/2020',
            'Janeiro/2021', 'fereiro/2021', 'Março/2021', 'Abril/2021', 'Maio/2021',
            'junho/2021', 'julho/2021', 'Agosto/2021', 'Setembro/2021',
            'Outubro/2021', 'Dezembro/2021', 'Novembro/2021', 'fereiro/2022',
            'Março/2022', 'Abril/2022', 'Maio/2022', 'junho/2022', 'julho/2022',
            'Agosto/2022', 'Setembro/2022', 'Outubro/2022', 'Novembro/2022',
            'Dezembro/2022', 'Janeiro/2023', 'fereiro/2023',
                'Março/2023', 'Abril/2023', 'Maio/2023',
            'junho/2023', 'julho/2023', 'Agosto/2023', 'Setembro/2023',
            'Outubro/2023','Novembro/2023','Dezembro/2023','Janeiro/2024','Fevereiro/2024','Março/2024'
        ]

        for col in col_fill_na:
            arquivo_final[col] = arquivo_final[col].fillna(0)


        arquivo_final['Inicio da gestão'] = pd.to_datetime(arquivo_final['Inicio da gestão'],errors='coerce')
        arquivo_final['Inicio da gestão'] = arquivo_final['Inicio da gestão'].dt.strftime('%d/%m/%Y')    


        arquivo_final['Data do distrato'] = pd.to_datetime(arquivo_final['Data do distrato'],errors='coerce')
        arquivo_final['Data do distrato'] = arquivo_final['Data do distrato'].dt.strftime('%d/%m/%Y') 

        aporte_e_retiradas_Novembro_2023 =pd.read_excel('Aportes e Retiradas Novembro.xlsx')
        aporte_e_retiradas_Novembro_2023 = aporte_e_retiradas_Novembro_2023.rename(columns={
            'CONTA':'Conta_Novembro_2023',
            'APORTES':'Aportes em Novembro 2023',
            'RETIRADAS':'Retiradas em Novembro 2023'
        })
        aporte_e_retiradas_Dezembro_2023 = pd.read_excel('Aportes e Retiradas Dezembro.xlsx')
        aporte_e_retiradas_Dezembro_2023 = aporte_e_retiradas_Dezembro_2023.rename(columns={
            'CONTA':'Conta_Dezembro_2023',
            'APORTES':'Aportes em Dezembro 2023',
            'RETIRADAS':'Retiradas em Dezembro 2023'
        })
        aporte_e_retiradas_Janeiro2024 = pd.read_excel('Aportes e Retiradas Janeiro.xlsx')
        aporte_e_retiradas_Janeiro2024 = aporte_e_retiradas_Janeiro2024.rename(columns={
            'Conta':'Conta_janeiro_2024',
            'Aportes':'Aportes em Janeiro_2024',
            'Retiradas':'Retiradas em Janeiro_2024'
        })

        aporte_e_retiradas_Fevereiro_2024 = pd.read_excel('Aportes e Retiradas Fevereiro.xlsx')
        aporte_e_retiradas_Fevereiro_2024 = aporte_e_retiradas_Fevereiro_2024.rename(columns={
            'Conta':'Conta_fevereiro_2024',
            'Aportes':'Aportes em Fevereiro_2024',
            'Retiradas':'Retiradas em Fevereiro_2024'
        })

        aporte_e_retiradas_Marco_2024 = pd.read_excel('Aportes e Retiradas Março.xlsx')
        aporte_e_retiradas_Marco_2024 = aporte_e_retiradas_Marco_2024.rename(columns={
            'Conta':'Conta_março_2024',
            'Aportes':'Aportes em Março 2024',
            'Retiradas':'Retiradas em Março 2024'
        })

        aporte_e_retiradas_abril_2024 = pd.read_excel('Aportes e Retiradas Abril.xlsx')
        aporte_e_retiradas_abril_2024 = aporte_e_retiradas_abril_2024.rename(columns={
            'Conta':'Conta_abril_2024',
            'Aportes':'Aportes em Abril 2024',
            'Retiradas':'Retiradas em Abril 2024'
        }).drop(columns='Nome')

        

        arquivo_final = arquivo_final.merge(aporte_e_retiradas_Novembro_2023,left_on='Conta',right_on='Conta_Novembro_2023',how='outer').reset_index()
        arquivo_final = arquivo_final[['Corretora', 'Nome_cliente', 'Conta', 'Escritorio', 'UF', 'Assessor',
            'Mesa de Operação', 'Status', 'Exeção', 'Inicio da gestão',
            'Data do distrato', 'Carteira', 'Taxa de gestão', 'Benchmark',
            'Taxa de performance','Aportes em Novembro 2023',
            'Retiradas em Novembro 2023',  'Janeiro/2020', 'fereiro/2020', 'Março/2020',
            'Abril/2020', 'Maio/2020', 'junho/2020', 'julho/2020', 'Agosto/2020',
            'Setembro/2020', 'Outubro/2020', 'Novembro/2020', 'Dezembro/2020',
            'Janeiro/2021', 'fereiro/2021', 'Março/2021', 'Abril/2021', 'Maio/2021',
            'junho/2021', 'julho/2021', 'Agosto/2021', 'Setembro/2021',
            'Outubro/2021', 'Dezembro/2021', 'Novembro/2021', 'fereiro/2022',
            'Março/2022', 'Abril/2022', 'Maio/2022', 'junho/2022', 'julho/2022',
            'Agosto/2022', 'Setembro/2022', 'Outubro/2022', 'Novembro/2022',
            'Dezembro/2022', 'Janeiro/2023', 'fereiro/2023', 'Março/2023',
            'Abril/2023', 'Maio/2023', 'junho/2023', 'julho/2023', 'Agosto/2023',
            'Setembro/2023', 'Outubro/2023','Novembro/2023','Dezembro/2023','Janeiro/2024','Fevereiro/2024','Março/2024'
        ]]


        arquivo_final = arquivo_final.merge(aporte_e_retiradas_Dezembro_2023,left_on='Conta',right_on='Conta_Dezembro_2023',how='outer').merge(
            aporte_e_retiradas_Janeiro2024,left_on='Conta',right_on='Conta_janeiro_2024',how='outer').merge(
                aporte_e_retiradas_Fevereiro_2024,left_on='Conta',right_on='Conta_fevereiro_2024',how='outer').merge(
                aporte_e_retiradas_Marco_2024,left_on='Conta',right_on='Conta_março_2024',how='outer').merge(
                aporte_e_retiradas_abril_2024,left_on='Conta',right_on='Conta_abril_2024',how='outer').reset_index()


        arquivo_final = arquivo_final[['Corretora', 'Nome_cliente', 'Conta', 'Escritorio', 'UF', 'Assessor',
            'Mesa de Operação', 'Status', 'Exeção', 'Inicio da gestão',
            'Data do distrato', 'Carteira', 'Taxa de gestão', 'Benchmark',
            'Taxa de performance','Aportes em Março 2024','Retiradas em Março 2024',
            'Aportes em Novembro 2023','Aportes em Dezembro 2023','Aportes em Janeiro_2024','Aportes em Fevereiro_2024',
            'Retiradas em Novembro 2023', 'Retiradas em Dezembro 2023','Retiradas em Janeiro_2024','Retiradas em Fevereiro_2024',
            'Janeiro/2020', 'fereiro/2020', 'Março/2020',
            'Abril/2020', 'Maio/2020', 'junho/2020', 'julho/2020', 'Agosto/2020',
            'Setembro/2020', 'Outubro/2020', 'Novembro/2020', 'Dezembro/2020',
            'Janeiro/2021', 'fereiro/2021', 'Março/2021', 'Abril/2021', 'Maio/2021',
            'junho/2021', 'julho/2021', 'Agosto/2021', 'Setembro/2021',
            'Outubro/2021', 'Dezembro/2021', 'Novembro/2021', 'fereiro/2022',
            'Março/2022', 'Abril/2022', 'Maio/2022', 'junho/2022', 'julho/2022',
            'Agosto/2022', 'Setembro/2022', 'Outubro/2022', 'Novembro/2022',
            'Dezembro/2022', 'Janeiro/2023', 'fereiro/2023', 'Março/2023',
            'Abril/2023', 'Maio/2023', 'junho/2023', 'julho/2023', 'Agosto/2023',
            'Setembro/2023', 'Outubro/2023','Novembro/2023','Dezembro/2023','Janeiro/2024','Fevereiro/2024','Março/2024']]

        arquivo_final_copia = arquivo_final.copy()


        try:
            contas_ativas_e_inativas = st.toggle('Contas Ativas e Inativas',key='Seletor_de_contas_ativas')

                
            col1,col2,col3 = st.columns(3)

            try:
                mes_escolhido_de_valores_para_contas = st.sidebar.selectbox('Selecione o mês :',col_fill_na,key='seleiconar_mes_para_somar',)
            except:
                ''

            opcoes_do_seletor_corretora = arquivo_final_copia['Corretora'].unique()
            opcoes_do_seletor_corretora = [opcao for opcao in opcoes_do_seletor_corretora if pd.notna(opcao) and opcao != "Corretora"]

            opcoes_do_seletor_escritorio = arquivo_final_copia['Escritorio'].unique()
            opcoes_do_seletor_escritorio = [opcao for opcao in opcoes_do_seletor_escritorio if pd.notna(opcao) and opcao != "Escritório"]

            opcoes_do_seletor_estado = arquivo_final_copia['UF'].unique()
            opcoes_do_seletor_estado = [opcao for opcao in opcoes_do_seletor_estado if pd.notna(opcao) and opcao != "UF"]


            multiselec_para_corretoras = st.sidebar.multiselect('Selecione a/as Corretoras :' ,
                                                                options=opcoes_do_seletor_corretora,
                                                                default = opcoes_do_seletor_corretora,
                                                                key='seletor_corretoras')
            multiselec_para_escritorio = st.sidebar.multiselect('Selecione o/os Escritorios :' , 
                                                                options=opcoes_do_seletor_escritorio,
                                                                default=opcoes_do_seletor_escritorio,
                                                                key='seletor_escritorio')
            multiselec_para_estados = st.sidebar.multiselect('Selecione o/os Estados :' ,
                                                            options=opcoes_do_seletor_estado,
                                                            default=opcoes_do_seletor_estado,
                                                            key='seletor_estado')

            arquivo_final['Inicio da gestão'] = arquivo_final['Inicio da gestão'].fillna("01/01/2023")
            arquivo_final['Inicio da gestão'] = pd.to_datetime(arquivo_final['Inicio da gestão'],errors='coerce')
            arquivo_final['Data do distrato'] = pd.to_datetime(arquivo_final['Data do distrato'],errors='coerce')


            def filtragem_de_dados(filtragem_de_dados1):
                if multiselec_para_corretoras and multiselec_para_escritorio and multiselec_para_estados:   
                    filtragem_de_dados1 = arquivo_final_copia.loc[arquivo_final['Corretora'].isin(multiselec_para_corretoras)]
                    filtragem_de_dados2 = filtragem_de_dados1.loc[arquivo_final['Escritorio'].isin(multiselec_para_escritorio)]
                    filtragem_de_dados3 = filtragem_de_dados2.loc[arquivo_final['UF'].isin(multiselec_para_estados)]
                    return filtragem_de_dados3


            night_colors = ['rgb(56, 75, 126)', 'rgb(18, 36, 37)', 'rgb(34, 53, 101)',
                        'rgb(36, 55, 57)', 'rgb(6, 4, 4)']
            sunflowers_colors = ['rgb(177, 127, 38)', 'rgb(205, 152, 36)', 'rgb(99, 79, 37)',
                                'rgb(129, 180, 179)', 'rgb(124, 103, 37)']
            irises_colors = ['rgb(33, 75, 99)', 'rgb(79, 129, 102)', 'rgb(151, 179, 100)',
                            'rgb(175, 49, 35)', 'rgb(36, 73, 147)']
            cafe_colors =  ['rgb(146, 123, 21)', 'rgb(177, 180, 34)', 'rgb(206, 206, 40)',
                        'rgb(175, 51, 21)', 'rgb(35, 36, 21)','rgb(146, 123, 21)', 'rgb(177, 180, 34)', 'rgb(206, 206, 40)',
                        'rgb(175, 51, 21)', 'rgb(35, 36, 21)']
            categorical_Accent= "#7FC97F", "#BEAED4", "#FDC086", "#FFFF99", "#386CB0", "#F0027F","#7FC97F", "#BEAED4", "#FDC086", "#FFFF99", "#386CB0", "#F0027F","#7FC97F", "#BEAED4", "#FDC086", "#FFFF99", "#386CB0", "#F0027F"
            Set1 = "#e41a1c", "#377eb8", "#4daf4a", "#ff7f00", "#984ea3", "#999999"
            Blues="#08306b", "#08519c", "#2171b5", "#4292c6", "#6baed6", "#9ecae1", "#c6dbef","#08306b", "#08519c", "#2171b5","#08306b", "#08519c", "#2171b5", "#4292c6", "#6baed6", "#9ecae1", "#c6dbef","#08306b", "#08519c", "#2171b5"
            Greens="#00441b", "#006d2c", "#238b45", "#41ab5d", "#74c476", "#a1d99b", "#c7e9c0","#00441b", "#006d2c", "#238b45"
            RdBu = ["#67001f", "#b2182b", "#d6604d", "#f4a582", "#fddbc7", "#d1e5f0", "#92c5de", "#4393c3", "#2166ac","#67001f", "#b2182b", "#d6604d", "#f4a582", "#fddbc7",
            "#d1e5f0", "#92c5de", "#4393c3", "#2166ac","#67001f", "#b2182b", "#d6604d", "#f4a582", "#fddbc7", "#d1e5f0", "#92c5de", "#4393c3", "#2166ac",
            "#67001f", "#b2182b", "#d6604d", "#f4a582", "#fddbc7", "#d1e5f0", "#92c5de", "#4393c3", "#2166ac","#67001f", "#b2182b", "#d6604d", "#f4a582", "#fddbc7", "#d1e5f0", "#92c5de", "#4393c3",
            "#2166ac","#67001f", "#b2182b", "#d6604d", "#f4a582", "#fddbc7", "#d1e5f0", "#92c5de", "#4393c3", "#2166ac","#67001f", "#b2182b", "#d6604d", "#f4a582", "#fddbc7", "#d1e5f0", "#92c5de", "#4393c3", "#2166ac",
            "#67001f", "#b2182b", "#d6604d", "#f4a582", "#fddbc7", "#d1e5f0", "#92c5de", "#4393c3", "#2166ac","#67001f", "#b2182b", "#d6604d", "#f4a582", "#fddbc7", "#d1e5f0", "#92c5de", "#4393c3",
            "#2166ac","#67001f", "#b2182b", "#d6604d", "#f4a582", "#fddbc7", "#d1e5f0", "#92c5de", "#4393c3", "#2166ac"]

            Pastel1= "#fbb4ae", "#b3cde3", "#ccebc5", "#decbe4", "#fed9a6", "#ffffcc", "#e5d8bd","#fbb4ae", "#b3cde3", "#ccebc5", "#decbe4",
            Paired = "#a6cee3", "#1f78b4", "#b2df8a", "#33a02c", "#fb9a99", "#e31a1c", "#fdbf6f", "#ff7f00","#a6cee3", "#1f78b4", "#b2df8a", "#33a02c",
            cores_vibrantes = ['#FF5733', '#33FF57', '#3366FF', '#FF33C7', '#FFFF33','#FF5733', '#33FF57', '#3366FF', '#FF33C7', '#FFFF33','#FF5733', '#33FF57', '#3366FF', '#FF33C7', '#FFFF33']
            cores_verao = ['#FFD700', '#87CEFA', '#FF6347', '#32CD32', '#FFA07A','#FFD700', '#87CEFA', '#FF6347', '#32CD32', '#FFA07A','#FFD700', '#87CEFA', '#FF6347', '#32CD32', '#FFA07A']
            cores_claras = ['#F0F8FF', '#FFDAB9', '#FAFAD2', '#E0FFFF', '#FFE4E1','#F0F8FF', '#FFDAB9', '#FAFAD2', '#E0FFFF', '#FFE4E1','#F0F8FF', '#FFDAB9', '#FAFAD2', '#E0FFFF', '#FFE4E1','#F0F8FF', '#FFDAB9', '#FAFAD2', '#E0FFFF', '#FFE4E1']
            cores_sofisticadas_1 = ['#4C72B0', '#DD8452', '#55A868', '#C44E52', '#8172B3','#4C72B0', '#DD8452', '#55A868', '#C44E52', '#8172B3','#4C72B0', '#DD8452', '#55A868', '#C44E52', '#8172B3']
            cores_sofisticadas_2 = ['#618C7E', '#CA896D', '#7A69A4', '#AA7E6E', '#7A92A3','#618C7E', '#CA896D', '#7A69A4', '#AA7E6E', '#7A92A3','#618C7E', '#CA896D', '#7A69A4', '#AA7E6E', '#7A92A3']
            cores_sofisticadas_3 = ['#836F78', '#678B8B', '#B68F52', '#7E7B9D', '#A64B73','#836F78', '#678B8B', '#B68F52', '#7E7B9D', '#A64B73','#836F78', '#678B8B', '#B68F52', '#7E7B9D', '#A64B73']
            cores_sofisticadas_4 = ['#6A0572', '#AB83A1', '#5AC4BE', '#F6AE2D', '#FF622E','#6A0572', '#AB83A1', '#5AC4BE', '#F6AE2D', '#FF622E','#6A0572', '#AB83A1', '#5AC4BE', '#F6AE2D', '#FF622E']
            cores_sofisticadas_5 = ['#3F3FBF', '#A84A5B', '#708D81', '#D35D6E', '#7C696D','#3F3FBF', '#A84A5B', '#708D81', '#D35D6E', '#7C696D','#3F3FBF', '#A84A5B', '#708D81', '#D35D6E', '#7C696D']
            cores_sofisticadas_6 = ['#0076C0', '#FF4C00', '#004E66', '#FFD100', '#009287','#0076C0', '#FF4C00', '#004E66', '#FFD100', '#009287','#0076C0', '#FF4C00', '#004E66', '#FFD100', '#009287']


            colunas_to_numeric = ['Janeiro/2020', 'fereiro/2020',
                'Março/2020', 'Abril/2020', 'Maio/2020', 'junho/2020', 'julho/2020',
                'Agosto/2020', 'Setembro/2020', 'Outubro/2020', 'Novembro/2020',
                'Dezembro/2020', 'Janeiro/2021', 'fereiro/2021', 'Março/2021',
                'Abril/2021', 'Maio/2021', 'junho/2021', 'julho/2021', 'Agosto/2021',
                'Setembro/2021', 'Outubro/2021', 'Dezembro/2021', 'Novembro/2021',
                'fereiro/2022', 'Março/2022', 'Abril/2022', 'Maio/2022', 'junho/2022',
                'julho/2022', 'Agosto/2022', 'Setembro/2022', 'Outubro/2022',
                'Novembro/2022', 'Dezembro/2022', 'Janeiro/2023', 'fereiro/2023',
                'Março/2023', 'Abril/2023', 'Maio/2023', 'junho/2023', 'julho/2023',
                'Agosto/2023', 'Setembro/2023', 'Outubro/2023','Novembro/2023','Dezembro/2023','Janeiro/2024','Fevereiro/2024','Março/2024']
            
            with col1:
                

                dataframe_filtrado = filtragem_de_dados(arquivo_final_copia)
                try:
                    dataframe_filtrado['Soma_dos_valores'] = dataframe_filtrado[mes_escolhido_de_valores_para_contas].sum()
                except:
                    st.warning('Não foi possivel obter esses valores')
                if contas_ativas_e_inativas:
                    dataframe_filtrado = dataframe_filtrado[dataframe_filtrado['Status'].isin(['Ativo','Inativo','Inativa','Ativa'])]    




                
                grafico_indicador_de_pl = go.Figure(data=[go.Indicator(
                    value=  dataframe_filtrado["Soma_dos_valores"].iloc[-1],
                    number={"prefix":"R$"},
                    title = {'text': f'{multiselec_para_corretoras}<br><span style="font-size:0.9em;color:#FFA500">{multiselec_para_escritorio}</span><br><span style="font-size:0.8em;color:#4682B4">{multiselec_para_estados}</span>'}
                )])
                grafico_indicador_de_pl.update_layout(title=dict(text='PL Total',
                                                                font=dict(size=40),
                                                                x=0.3,
                                                                y=0.9),
                                                                paper_bgcolor='rgba(0,0,0,0)')
                
                cahart_json_str = grafico_indicador_de_pl.to_json()
                cleaned_html = cahart_json_str[1:-1].replace("'","")
                
                

                st.plotly_chart(grafico_indicador_de_pl,
                                use_container_width=True)

                var_percentual = ((dataframe_filtrado.iloc[:, -2].sum() - dataframe_filtrado[mes_escolhido_de_valores_para_contas].sum())/dataframe_filtrado[mes_escolhido_de_valores_para_contas].sum())*100
        
                st.metric(label=f'A variação do mês selecionado para o período atual para e de {var_percentual:,.2f}%',
                        value=f' Mês atual : R${dataframe_filtrado.iloc[:,-2].sum():,.2f}',
                        delta=f'Património período selecionado : R${dataframe_filtrado[mes_escolhido_de_valores_para_contas].sum():,.2f}')



                

                base_de_dados_para_grafico_de_linhas_pltotal = dataframe_filtrado.groupby('Soma_dos_valores')[colunas_to_numeric].value_counts().reset_index()
                for cols in colunas_to_numeric:
                    base_de_dados_para_grafico_de_linhas_pltotal[cols] = pd.to_numeric(base_de_dados_para_grafico_de_linhas_pltotal[cols],errors='coerce')

                base_de_dados_para_grafico_de_linhas_pltotal1= base_de_dados_para_grafico_de_linhas_pltotal.groupby('Soma_dos_valores')[colunas_to_numeric].sum().reset_index()
                base_de_dados_melted_pltotal = base_de_dados_para_grafico_de_linhas_pltotal1.melt(id_vars=['Soma_dos_valores'], var_name='Data', value_name='Valor')

                
                comparacao_pl_ao_longo_do_tempo = go.Figure()
                for assessor, dados in base_de_dados_melted_pltotal.groupby('Soma_dos_valores'):
                    comparacao_pl_ao_longo_do_tempo.add_trace(go.Scatter(
                        x=dados['Data'],
                        y=dados['Valor'],
                        mode='lines',
                        
                    ))
                    comparacao_pl_ao_longo_do_tempo.update_layout(paper_bgcolor='rgba(0,0,0,0)',
                                                     plot_bgcolor='rgba(0,0,0,0)',
                    title=dict(text='Evolução Bluemetrix ao Longo do tempo',
                                                                font=dict(size=20),
                                                                x=0.2,
                                                                y=0.9),
                                                         
                    showlegend=False,
                    legend_title='Assessor',
                    height=500,
                    width = 500,   
            xaxis=dict(
                    showticklabels=True,  # Ative a exibição de rótulos no eixo x
                    tickmode='array',    # Modo de exibição de rótulos
                    tickvals=dados['Data'][::6],  # Ajuste os valores dos rótulos para cada 6 períodos
                    ticktext=dados['Data'][::6],        
                    ))

                    comparacao_pl_ao_longo_do_tempo.update_yaxes(range=[0,350000000]) 
                    st.plotly_chart(comparacao_pl_ao_longo_do_tempo)

                base_de_dados_para_grafico_de_linhas_pl_assessores = dataframe_filtrado.groupby('Assessor')[colunas_to_numeric].value_counts().reset_index()
                for cols in colunas_to_numeric:
                    base_de_dados_para_grafico_de_linhas_pl_assessores[cols] = pd.to_numeric(base_de_dados_para_grafico_de_linhas_pl_assessores[cols],errors='coerce')

                base_de_dados_para_grafico_de_linhas_pl_assessores2 = base_de_dados_para_grafico_de_linhas_pl_assessores.groupby('Assessor')[colunas_to_numeric].sum().reset_index().nlargest(10,colunas_to_numeric[-1])
                base_de_dados_melted = base_de_dados_para_grafico_de_linhas_pl_assessores2.melt(id_vars=['Assessor'], var_name='Data', value_name='Valor')


                captacao_dos_assessores = go.Figure()
                for assessor, dados in base_de_dados_melted.groupby('Assessor'):
                    captacao_dos_assessores.add_trace(go.Scatter(
                        x=dados['Data'],
                        y=dados['Valor'],
                        mode='lines',
                        name=assessor,
                    ))
                    captacao_dos_assessores.update_layout(paper_bgcolor='rgba(0,0,0,0)',
                                                     plot_bgcolor='rgba(0,0,0,0)',
                    title=dict(text='Evolução PL dos Assessores ao longo do tempo',
                                                                font=dict(size=20),
                                                                x=0.1,
                                                                y=0.9),
                                                                showlegend=True,
                                                                legend_title='Assessor',
                                                                height=600,
                                                                width = 650,   
                                                                xaxis=dict(
                    showticklabels=True,  # Ative a exibição de rótulos no eixo x
                    tickmode='array',    # Modo de exibição de rótulos
                    tickvals=dados['Data'][::6],  # Ajuste os valores dos rótulos para cada 6 períodos
                    ticktext=dados['Data'][::6],       
                    ))      

                st.plotly_chart(captacao_dos_assessores)

                
                contagem_de_operadores = dataframe_filtrado['Mesa de Operação'].value_counts().reset_index()


                clientes_por_operador = go.Figure(data=
                                                            [go.Bar(
                                                                x=contagem_de_operadores['Mesa de Operação'],
                                                                    y=contagem_de_operadores['count'],
                                                                    marker_color=cores_sofisticadas_6,
                                                                    
                                                                    

                                                                        )])
                clientes_por_operador.update_layout(paper_bgcolor='rgba(0,0,0,0)',
                                                     plot_bgcolor='rgba(0,0,0,0)',title=dict(text='Contas operadas por operador',
                                                                font=dict(size=30),
                                                                x=0.1,
                                                                y=0.9))
                clientes_por_operador.update_yaxes(range=[0,400])
                st.plotly_chart(clientes_por_operador,use_container_width=True)

                pl_por_operador = dataframe_filtrado.groupby('Mesa de Operação')['Outubro/2023'].sum().reset_index()
                grafico_pl_por_operador = go.Figure(data=
                                                            [go.Bar(
                                                                x=pl_por_operador['Mesa de Operação'],
                                                                    y=pl_por_operador['Outubro/2023'],
                                                                    marker_color=irises_colors,
                                                                    

                                                                        )])
                grafico_pl_por_operador.update_layout(paper_bgcolor='rgba(0,0,0,0)',
                                                     plot_bgcolor='rgba(0,0,0,0)',
                                                     title=dict(text='PL por operador',
                                                                font=dict(size=30),
                                                                x=0.2,
                                                                y=0.9))
                st.plotly_chart(grafico_pl_por_operador,use_container_width=True)

                #------------->>>>
                escritorio_base_de_dados = dataframe_filtrado.groupby('Escritorio')[colunas_to_numeric].value_counts().reset_index()
                for cols in colunas_to_numeric:
                    escritorio_base_de_dados[cols] = pd.to_numeric(escritorio_base_de_dados[cols],errors='coerce')

                escritorio_base_de_dados2 = escritorio_base_de_dados.groupby('Escritorio')[colunas_to_numeric].sum().reset_index()
                escritorio_base_de_dados_melted = escritorio_base_de_dados2.melt(id_vars=['Escritorio'], var_name='Data', value_name='Valor')

                
                escritorios_pl = go.Figure()
                for assessor, dados in escritorio_base_de_dados_melted.groupby('Escritorio'):
                    escritorios_pl.add_trace(go.Scatter(
                        x=dados['Data'],
                        y=dados['Valor'],
                        mode='lines',
                        name=assessor,
                    ))
                    escritorios_pl.update_layout(paper_bgcolor='rgba(0,0,0,0)',
                                                     plot_bgcolor='rgba(0,0,0,0)',
                    title=dict(text='Evolução PL dos Escritorios ao longo do tempo',
                                                                font=dict(size=20),
                                                                x=0.1,
                                                                y=0.9),
                                                                showlegend=True,
                                                                legend_title='Escritorios',
                                                                height=600,
                                                                width = 560,   
                                                                xaxis=dict(
                    showticklabels=True,  # Ative a exibição de rótulos no eixo x
                    tickmode='array',    # Modo de exibição de rótulos
                    tickvals=dados['Data'][::6],  # Ajuste os valores dos rótulos para cada 6 períodos
                    ticktext=dados['Data'][::6],
                        
                    ))      


            with col2:
                
                
                st.subheader('Entrada de Clientes')
                data_atual = datetime.now()
                data_30_dias = datetime.now()

                dataframe_filtrado['Data do distrato'] = pd.to_datetime(dataframe_filtrado['Data do distrato'],errors='coerce')
                dataframe_filtrado['Inicio da gestão'] = pd.to_datetime(dataframe_filtrado['Inicio da gestão'],errors='coerce')

                default_start_date = dataframe_filtrado['Inicio da gestão'].min() 
                default_start_date2 = dataframe_filtrado['Inicio da gestão'].max() 
                start_date = pd.to_datetime(st.date_input("Start Date",
                    min_value=dataframe_filtrado['Inicio da gestão'].min(),
                    max_value=dataframe_filtrado['Inicio da gestão'].max(),
                    value=default_start_date))

                end_date = pd.to_datetime(st.date_input("End Date",
                    min_value=dataframe_filtrado['Inicio da gestão'].min(),
                    max_value=dataframe_filtrado['Inicio da gestão'].max(),
                    value=default_start_date2))


                filtrando_dados_por_periodo = (dataframe_filtrado['Inicio da gestão'] >= start_date) & (dataframe_filtrado['Inicio da gestão'] <= end_date)
                contando_entrada_de_cliente_pelo_periodo = filtrando_dados_por_periodo.sum()


                st.metric(label='',value=f' Entrada de clientes :  {contando_entrada_de_cliente_pelo_periodo}')

                lista_aportes = ['Aportes em Novembro 2023','Aportes em Dezembro 2023','Aportes em Janeiro_2024',
                                 'Aportes em Fevereiro_2024','Aportes em Março 2024','Aportes em Abril 2024',]
                
                st.markdown("<br>", unsafe_allow_html=True)
                seletor_periodo_aportes = st.selectbox('',lista_aportes,key='Seletor_periodo_aportes')
                valor_total_aportes = dataframe_filtrado[seletor_periodo_aportes].sum()
                valor_formato = "${:,.2f}".format(valor_total_aportes)
                st.metric(label=seletor_periodo_aportes,value=valor_formato)


                pl_assessores = dataframe_filtrado.groupby('Assessor')[mes_escolhido_de_valores_para_contas].sum().reset_index()
                
                grafico_pl_assessores = go.Figure(data=
                                                    [go.Bar(
                                                        x=pl_assessores['Assessor'],
                                                        y=pl_assessores[mes_escolhido_de_valores_para_contas],
                                                        marker_color=RdBu,
                                                                        )])
                grafico_pl_assessores.update_layout(paper_bgcolor='rgba(0,0,0,0)',
                                                     plot_bgcolor='rgba(0,0,0,0)',
                                                     title=dict(text='PL Assessores por periodo',
                                                                font=dict(size=30),
                                                                x=0.2,
                                                                y=0.9),
                                                                    xaxis=dict(
                                                                showticklabels=False  ),
                                                                height=600
                                                                )
                st.markdown("<br>", unsafe_allow_html=True)
                st.markdown("<br>", unsafe_allow_html=True)
                st.plotly_chart(grafico_pl_assessores,use_container_width=True)
                colunas_to_numeric2 = [ 'Novembro/2021',
                'fereiro/2022', 'Março/2022', 'Abril/2022', 'Maio/2022', 'junho/2022',
                'julho/2022', 'Agosto/2022', 'Setembro/2022', 'Outubro/2022',
                'Novembro/2022', 'Dezembro/2022', 'Janeiro/2023', 'fereiro/2023',
                'Março/2023', 'Abril/2023', 'Maio/2023', 'junho/2023', 'julho/2023',
                'Agosto/2023', 'Setembro/2023', 'Outubro/2023','Novembro/2023','Dezembro/2023','Janeiro/2024','Fevereiro/2024']
                for colunas in colunas_to_numeric2:
                    arquivo_final_copia[colunas] = pd.to_numeric(arquivo_final_copia[colunas],errors='coerce')

                comparacao_evolucao_pl_por_corretora = dataframe_filtrado.groupby('Corretora') [colunas_to_numeric2].value_counts().reset_index()
                for cols in colunas_to_numeric2:
                    comparacao_evolucao_pl_por_corretora[cols] = pd.to_numeric(comparacao_evolucao_pl_por_corretora[cols],errors='coerce')
                comparacao_evolucao_pl_por_corretora2 = comparacao_evolucao_pl_por_corretora.groupby('Corretora')[colunas_to_numeric2].sum().reset_index()
                comparacao_corretora_melted = comparacao_evolucao_pl_por_corretora2.melt(id_vars=['Corretora'],var_name='Data',value_name='Valor')
                comparacao_corretora = go.Figure()
                for Corretora, dados in comparacao_corretora_melted.groupby('Corretora'):
                    comparacao_corretora.add_trace(go.Scatter(
                        x=dados['Data'],
                        y=dados['Valor'],
                        mode='lines',
                        name=Corretora
                    ))
                comparacao_corretora.update_layout(paper_bgcolor='rgba(0,0,0,0)',
                                                     plot_bgcolor='rgba(0,0,0,0)',
                title='Evolução dos Valores por Corretora ao Longo do Tempo',
                showlegend=True,
                height=500,
                width = 555,   
            xaxis=dict(
                    showticklabels=True,
                    tickmode='array',    
                    tickvals=dados['Data'][::6],
                    ticktext=dados['Data'][::6],      
                ))
                st.plotly_chart(comparacao_corretora)

                dados_para_grafico_de_status = dataframe_filtrado['Status'].value_counts().reset_index()
                grafico_status = go.Figure(data=
                                                    [go.Bar(
                                                        x=dados_para_grafico_de_status['count'],
                                                        y=dados_para_grafico_de_status['Status'],
                                                        marker_color=cores_sofisticadas_5,
                                                        orientation='h'
                                                                        )])
                grafico_status.update_layout(paper_bgcolor='rgba(0,0,0,0)',
                                                     plot_bgcolor='rgba(0,0,0,0)',
                                                     title=dict(text='Status das contas',
                                                                font=dict(size=30),
                                                                x=0.2,
                                                                y=0.9))
                st.plotly_chart(grafico_status,use_container_width=True)


                estado_base_de_dados = dataframe_filtrado.groupby('UF')[colunas_to_numeric].value_counts().reset_index()
                for cols in colunas_to_numeric:
                    estado_base_de_dados[cols] = pd.to_numeric(estado_base_de_dados[cols],errors='coerce')

                estado_base_de_dados2 = estado_base_de_dados.groupby('UF')[colunas_to_numeric].sum().reset_index()
                estado_base_de_dados_melted = estado_base_de_dados2.melt(id_vars=['UF'], var_name='Data', value_name='Valor')

                
                estado_pl = go.Figure()
                for assessor, dados in estado_base_de_dados_melted.groupby('UF'):
                    estado_pl.add_trace(go.Scatter(
                        x=dados['Data'],
                        y=dados['Valor'],
                        mode='lines',
                        name=assessor,
                    ))
                    estado_pl.update_layout(paper_bgcolor='rgba(0,0,0,0)',
                                                     plot_bgcolor='rgba(0,0,0,0)',
                    title=dict(text='Evolução PL das Regiões ao longo do tempo',
                                                                font=dict(size=20),
                                                                x=0.1,
                                                                y=0.9),
                                                                showlegend=True,
                                                                legend_title='Regiões',
                                                                height=600,
                                                                width = 550,   
                                                                xaxis=dict(
                    showticklabels=True,  
                    tickmode='array',   
                    tickvals=dados['Data'][::6],  
                    ticktext=dados['Data'][::6],       
                    ))      

                st.plotly_chart(estado_pl)


            



            with col3:
                
                dataframe_filtrado['Data do distrato'] = pd.to_datetime(dataframe_filtrado['Data do distrato'],errors='coerce')

                data_atual = datetime.now()
                data_30_dias = datetime.now()

                dataframe_filtrado_sem_colunas_vazias_para_distrato = dataframe_filtrado.copy()
                dataframe_filtrado_sem_colunas_vazias_para_distrato  = dataframe_filtrado_sem_colunas_vazias_para_distrato.dropna(subset=['Data do distrato'])

                default_end_date = dataframe_filtrado_sem_colunas_vazias_para_distrato['Data do distrato'].min()
                default_end_date2 =  dataframe_filtrado_sem_colunas_vazias_para_distrato['Data do distrato'].max()

                default_start_date = pd.to_datetime(default_end_date)
                try:
                    st.subheader('Saida de Clientes')
                    start_date = pd.to_datetime(st.date_input("Start Date",
                        min_value=dataframe_filtrado_sem_colunas_vazias_para_distrato['Data do distrato'].min(),
                        max_value=dataframe_filtrado_sem_colunas_vazias_para_distrato['Data do distrato'].max(),
                        value=default_end_date))

                    end_date = pd.to_datetime(st.date_input("End Date",
                        min_value=dataframe_filtrado_sem_colunas_vazias_para_distrato['Data do distrato'].min(),
                        max_value=dataframe_filtrado_sem_colunas_vazias_para_distrato['Data do distrato'].max(),
                        value=default_end_date2))

                    filtrando_dados_por_periodo_distrato = (dataframe_filtrado['Data do distrato'] >= start_date) & (dataframe_filtrado['Data do distrato'] <= end_date)
                    contando_entrada_de_cliente_pelo_periodo_distrato= filtrando_dados_por_periodo_distrato.sum()
                
                    st.metric(label='',value=f' Saída de clientes :  {contando_entrada_de_cliente_pelo_periodo_distrato}')
                except:
                    st.write('Não ouve saida de clientes para essa filtragem')


                lista_resgates = ['Retiradas em Novembro 2023', 'Retiradas em Dezembro 2023',
                                  'Retiradas em Janeiro_2024','Retiradas em Fevereiro_2024',
                                  'Retiradas em Março 2024','Retiradas em Abril 2024']
                st.markdown("<br>", unsafe_allow_html=True)
                seletor_periodo_resgates = st.selectbox('',lista_resgates,key='Seletor_periodo_resgates')
                valor_total_resgates = dataframe_filtrado[seletor_periodo_resgates].sum()
                valor_formato_resgates = "${:,.2f}".format(valor_total_resgates)
                st.metric(label=seletor_periodo_resgates,value=valor_formato_resgates)
                dataframe_filtrado['Outubro/2023'] = pd.to_numeric(dataframe_filtrado['Outubro/2023'],errors='coerce')
                pl_assessores_atual = dataframe_filtrado.groupby('Assessor')['Outubro/2023'].sum().nlargest(10).reset_index()

                grafico_pl_assessores_atual = go.Figure(data=
                                                    [go.Bar(
                                                        x=pl_assessores_atual['Assessor'],
                                                        y=pl_assessores_atual['Outubro/2023'],
                                                        marker_color=Blues,
                                                                        )])
                grafico_pl_assessores_atual.update_layout(paper_bgcolor='rgba(0,0,0,0)',
                                                     plot_bgcolor='rgba(0,0,0,0)',
                                                     title=dict(text='Top 10 PL Assessores Outubro/2023',
                                                                font=dict(size=20),
                                                                x=0.2,
                                                                y=0.9),
                                                                height = 600)
                st.markdown("<br>", unsafe_allow_html=True)
                st.markdown("<br>", unsafe_allow_html=True)
                st.plotly_chart(grafico_pl_assessores_atual,use_container_width=True)


                contagem_de_perfis = dataframe_filtrado['Carteira'].value_counts().reset_index()
                contagem_de_perfis['Carteira'] = contagem_de_perfis['Carteira'].str.replace(' INC','INC')

                grafico_barras_perfil_de_carteira = go.Figure(data=
                                                            [go.Bar(
                                                                x=contagem_de_perfis['Carteira'],
                                                                    y=contagem_de_perfis['count'],
                                                                    marker_color='indianred',
                                                                        )])
                grafico_barras_perfil_de_carteira.update_layout(paper_bgcolor='rgba(0,0,0,0)',
                                                     plot_bgcolor='rgba(0,0,0,0)',
                                                     title=dict(text='Perfil de carteiras',
                                                            font=dict(size=40),
                                                            x=0.3,
                                                            y=0.9))
                st.plotly_chart(grafico_barras_perfil_de_carteira,use_container_width=True)
                pl_por_corretoras = dataframe_filtrado.groupby('Corretora')[mes_escolhido_de_valores_para_contas].sum().reset_index()
                grafico_pl_corretoras = go.Figure(data=
                                                    [go.Bar(
                                                        x=pl_por_corretoras[mes_escolhido_de_valores_para_contas],
                                                        y=pl_por_corretoras['Corretora'],
                                                        marker_color=sunflowers_colors,
                                                        orientation='h'
                                                                        )])
                grafico_pl_corretoras.update_layout(paper_bgcolor='rgba(0,0,0,0)',
                                                     plot_bgcolor='rgba(0,0,0,0)',
                                                     title=dict(text='PL por Corretora',
                                                                font=dict(size=30),
                                                                x=0.2,
                                                                y=0.9))
                st.plotly_chart(grafico_pl_corretoras,use_container_width=True)

                pl__escritorios = dataframe_filtrado.groupby('Escritorio')[mes_escolhido_de_valores_para_contas].sum().reset_index()

                pl_estado_barras = go.Figure(data=
                                                    [go.Bar(
                                                        x=pl__escritorios['Escritorio'],
                                                        y=pl__escritorios[mes_escolhido_de_valores_para_contas],
                                                        marker_color=cores_sofisticadas_2,
                                                                        )])
                pl_estado_barras.update_layout(paper_bgcolor='rgba(0,0,0,0)',
                                                     plot_bgcolor='rgba(0,0,0,0)',
                                                     title=dict(text='Património dos Escritorios',
                                                                font=dict(size=30),
                                                                x=0.2,
                                                                y=0.9,
                                                                ),
                                                                height = 600,
                                                                width = 500)
                st.plotly_chart(pl_estado_barras,use_container_width=True)

        except:
            st.warning('Selecione pelo menos 1 opção em todos os seletores ou selecione outro mês(os meses de Maio/2020 até Setembro/2020 não contém dados!)')




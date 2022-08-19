from distutils.command.clean import clean
import re
from leitor import Leitor
import pandas as pd

class Coletor:
    #Atributos
    planilha_alunos_raw = None
    planilha_KA_raw = None

    dicionario_alunos = None

    @staticmethod
    def coletar_dados():
        # Carrega planilha de alunos com Nome e Id 
        Coletor.planilha_alunos_raw = pd.read_csv(Leitor.caminho_planilha_alunos,
                                                  dtype={'Id':str})


        # Carrega planilha da Khan Academy 
        Coletor.planilha_KA_raw = pd.read_csv(Leitor.caminho_planilha_KA)
        
        # Lê os alunos da planilha de alunos
        Coletor.definir_alunos()
        Coletor.definir_recomendacoes_aluno()

    @staticmethod
    def definir_alunos():
        # Cria dicionário que mapeia id -> nome do aluno
        Coletor.dicionario_alunos = Coletor.planilha_alunos_raw.set_index('Id').to_dict()['Nome']

        print(Coletor.dicionario_alunos)

    @staticmethod
    def definir_recomendacoes_aluno():
        # preenche os espaços vazio com zeros
        Coletor.planilha_KA_raw.fillna(0, inplace=True, axis = 1)
        
        alunos = []

        # para cada aluno na planilha de alunos...
        for id_aluno in Coletor.dicionario_alunos:
            # condição para "pegar" a recomendação do aluno: Nome do aluno terminar com seu Id
            condicao = Coletor.planilha_KA_raw['Nome do aluno'].str.endswith(id_aluno)
            recomendacoes_aluno = Coletor.planilha_KA_raw[condicao]

            num_recomendacoes = recomendacoes_aluno['Nome da recomendação'].unique().size
            percentual_tentativas = 0
            desempenho_medio = 0

            #print(id_aluno, num_recomendacoes)

            recomendacao_infos = []
            # para cada recomendação nas recomendações do aluno...
            for recomendacao in recomendacoes_aluno['Nome da recomendação'].unique():
                # colete os dados daquela recomendação
                dados_da_recomendacao = recomendacoes_aluno[recomendacoes_aluno['Nome da recomendação'] == recomendacao]
                
                pontos_na_recomendacao = 0
                if dados_da_recomendacao['Número de tentativas'].values[0] != 0:
                    percentual_tentativas += 1
                    pontos_na_recomendacao = (dados_da_recomendacao['Pontuação na data final'].values[0] 
                                              /
                                              dados_da_recomendacao['Pontos possíveis'].values[0])*100
                    desempenho_medio += pontos_na_recomendacao
                
                recomendacao_infos.append((recomendacao, pontos_na_recomendacao))
            
            percentual_tentativas /= num_recomendacoes
            desempenho_medio /= num_recomendacoes
            alunos.append([Coletor.dicionario_alunos[id_aluno], percentual_tentativas, desempenho_medio, recomendacao_infos])
            #print(recomendacao, pontos_na_recomendacao, percentual_tentativas, desempenho_medio)
        

        for aluno in alunos:
            print(aluno[0], aluno[1], aluno[2])
            

            
            
            








        
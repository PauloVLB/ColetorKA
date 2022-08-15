from distutils.command.clean import clean
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
        
        Coletor.definir_alunos()
        Coletor.definir_recomendacoes_aluno()

        #print('Caminho da planilha de alunos ' + Leitor.caminho_planilha_alunos)
        #print('Caminho da planilha da Khan Academy ' + Leitor.caminho_planilha_KA)
        #print('Caminho do diretório destino ' + Leitor.caminho_diretorio_destino)

    @staticmethod
    def definir_alunos():
        # Cria dicionário que mapeia id -> nome do aluno
        Coletor.dicionario_alunos = Coletor.planilha_alunos_raw.set_index('Id').to_dict()['Nome']

        print(Coletor.dicionario_alunos)

    @staticmethod
    def definir_recomendacoes_aluno():
        # para cada aluno na planilha de alunos...
        for id_aluno in Coletor.dicionario_alunos:
            # condição para "pegar" a recomendação do aluno: Nome do aluno terminar com seu Id
            condicao = Coletor.planilha_KA_raw['Nome do aluno'].str.endswith(id_aluno)
            recomendacoes_aluno = Coletor.planilha_KA_raw[condicao]
            
            # preenche os espaços vazio com zeros
            recomendacoes_aluno.fillna(0, inplace=True, axis = 1)

            
            
            








        
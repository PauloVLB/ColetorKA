from leitor import Leitor

class Coletor:

    @staticmethod
    def coletar_dados():
        print('Caminho da planilha de alunos ' + Leitor.caminho_planilha_alunos)
        print('Caminho da planilha da Khan Academy ' + Leitor.caminho_planilha_KA)
        print('Caminho do diretório destino ' + Leitor.caminho_diretorio_destino)
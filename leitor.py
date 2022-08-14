from tkinter import filedialog

class Leitor:
    # Atributos
    caminho_planilha_alunos = ""
    caminho_planilha_KA = ""
    caminho_diretorio_destino = ""

    @staticmethod
    def selecionar_arquivo(titulo_janela='Selecionar Arquivo', tipos_aceitos=()):
        return filedialog.askopenfilename(
            title=titulo_janela,
            filetypes=(tipos_aceitos,)
        )   # cria a caixa de seleção de arquivos e retorna seu caminho absoluto
    
    @staticmethod
    def selecionar_diretorio(titulo_janela='Selecionar Diretório'):
        return filedialog.askdirectory(title=titulo_janela) # cria a caixa de seleção de diretórios e retorna seu caminho absoluto
    
    @staticmethod
    def selecionar_planilha_alunos():
        tipos_aceitos = ('CSV Files', '*.csv')  # lista de tipos que sao mostrados na caixa de seleção
        
        Leitor.caminho_planilha_alunos = Leitor.selecionar_arquivo(titulo_janela='Selecionar Planilha de Alunos', 
                                                            tipos_aceitos=tipos_aceitos)

    @staticmethod
    def selecionar_planilha_KA():
        tipos_aceitos = ('CSV Files', '*.csv')  
        Leitor.caminho_planilha_KA = Leitor.selecionar_arquivo(titulo_janela='Selecionar Planilha da Khan Academy', 
                                                        tipos_aceitos=tipos_aceitos)

    @staticmethod 
    def selecionar_diretorio_destino():
        Leitor.caminho_diretorio_destino = Leitor.selecionar_diretorio('Selecionar Diretório Destino')

    @staticmethod
    def selecionar_recomendacoes():
        print('selecionar recomendacoes')



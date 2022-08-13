from tkinter import filedialog
from tkinter import Button
from tkinter import Tk

def selecionar_arquivo():
    tipos_aceitos = ('CSV Files', '*.csv')  # lista de tipos que sao mostrados na caixa de seleção

    caminho_arquivo_mapeamento = filedialog.askopenfilename(
        title='Selecionar arquivo de mapeamento',
        filetypes=(tipos_aceitos,)
    )   # cria a caixa de seleção de arquivos 

    print(caminho_arquivo_mapeamento)  # teste: mostra o nome do arquivo selecionado




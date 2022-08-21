from tkinter import Button, Tk, Label, ttk
from leitor import Leitor
from coletor import Coletor

def exibir_janela_principal():
    janela_principal = Tk()                           # cria a janela principal
    janela_principal.title("Gerador de Planilhas KA") # atualiza nome da janela  

    largura_janela = 375  # largura da janela principal
    altura_janela = 170   # altura da janela principal

    largura_tela = janela_principal.winfo_screenwidth()  # largura da tela
    altura_tela = janela_principal.winfo_screenheight()  # altura da tela

    center_x = int(largura_tela/2 - largura_janela / 2)  # centro da tela no eixo x
    center_y = int(altura_tela/2 - altura_janela / 2)    # centro da tela no eixo y

    janela_principal.geometry(f'{largura_janela}x{altura_janela}+{center_x}+{center_y}') # define posicionamento e tamanho da janela

    exibir_opcoes(janela_principal)  # exibe as opções do menu na janela principal
    
    janela_principal.mainloop() # renderiza e exuta a janela principal

def exibir_opcoes(janela_principal):
    # lista de opções e nome de seus botões e funções callback
    lista_opcoes = [('Planilha de alunos', 'Selecionar Arquivo', Leitor.selecionar_planilha_alunos), 
                    ('Planilha da Khan Academy', 'Selecionar Arquivo', Leitor.selecionar_planilha_KA),
                    ('Selecionar Pasta Destino', 'Selecionar Pasta', Leitor.selecionar_diretorio_destino),
                    ('Selecionar Recomendações', 'Selecionar', Coletor.selecionar_recomendacoes),
                    ('Coletar todos os dados', 'Coletar Dados!', Coletor.coletar_dados), 
                    ]  
    
    criar_opcoes(lista_opcoes, janela_principal) # itera pela lista e renderiza na janela principal


def criar_opcoes(lista_opcoes, janela_principal):
    for [idx, [titulo, botao, callback]] in enumerate(lista_opcoes): # para cada opcao, enumerando-as
        texto_opcao = f'{idx+1}. {titulo}'     # cria o titulo da opcao com seu número
        opcao = Label(janela_principal,     
                      text=texto_opcao)        # cria a label

        idx *= 2
        botao_selecionar = Button(janela_principal,    
                                  text=botao,
                                  command=callback)   # cria o botao, chama a funcao de callback
        
        opcao.grid(sticky='w', column=0, row=idx)             # renderiza a label, alinha à esquerda (w = west)
        botao_selecionar.grid(sticky='e', column=1, row=idx)  # renderiza o botao, alinha à direita (e = east)
        
        ttk.Separator(janela_principal, orient="horizontal").grid(row=idx+1,column=0,
                                                                  columnspan=4, ipadx=200) # cria um separador 

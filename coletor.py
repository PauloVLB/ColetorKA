from tkinter import Listbox, Scrollbar, Frame, messagebox, Tk, Button
from turtle import right
from leitor import Leitor
from pathlib import Path
import pandas as pd

class Coletor:
    #Atributos
    planilha_alunos_raw = None
    ja_carreguei_planilha_alunos = False
    planilha_KA_raw = None
    ja_carreguei_planilha_KA = False

    dicionario_alunos = {}

    todas_recomendacoes = []
    recomendacoes_selecionadas = []

    @staticmethod
    def coletar_dados():
        # Carrega planilha de alunos com Nome e Id 
        if len(Leitor.caminho_planilha_alunos) > 2:
            Coletor.planilha_alunos_raw = pd.read_csv(Leitor.caminho_planilha_alunos,
                                                    dtype={'Id':str})
            Coletor.ja_carreguei_planilha_alunos = True
        #else:
        #    print("Não selecionou planilha de alunos")
        #    return

        # Carrega planilha da Khan Academy 
        if len(Leitor.caminho_planilha_KA) > 2:
            if(not Coletor.ja_carreguei_planilha_KA):
                Coletor.planilha_KA_raw = pd.read_csv(Leitor.caminho_planilha_KA)
                Coletor.todas_recomendacoes = Coletor.planilha_KA_raw['Nome da recomendação'].unique()
                Coletor.recomendacoes_selecionadas = Coletor.todas_recomendacoes
                Coletor.ja_carreguei_planilha_KA = True
        else:
            Coletor.mostrar_mensagem("Você precisa selecionar a planilha da Khan Academy antes")
            return
        # Lê os alunos da planilha de alunos
        Coletor.definir_alunos()
        Coletor.coletar_dados_finais()

    @staticmethod
    def definir_recomendacoes(janela_recomendacoes, lista_recomendacoes):
        Coletor.recomendacoes_selecionadas.clear()
        
        for selecionada in lista_recomendacoes.curselection():
            Coletor.recomendacoes_selecionadas.append(lista_recomendacoes.get(selecionada))
        
        janela_recomendacoes.destroy()

    @staticmethod 
    def mostrar_mensagem(mensagem):
        messagebox.showinfo(title="Aviso", message=mensagem)

    @staticmethod
    def selecionar_recomendacoes():
        if len(Leitor.caminho_planilha_KA) <= 2:
            Coletor.mostrar_mensagem("Você precisa selecionar a planilha da Khan Academy antes")
            return

        Coletor.planilha_KA_raw = pd.read_csv(Leitor.caminho_planilha_KA)
        Coletor.ja_carreguei_planilha_KA = True
        Coletor.todas_recomendacoes = Coletor.planilha_KA_raw['Nome da recomendação'].unique()

        janela_recomendacoes = Tk()
        janela_recomendacoes.title('Seleção de Recomendações')
        janela_recomendacoes.geometry('450x300')

        selecao = Frame(janela_recomendacoes)
        barra_rolagem = Scrollbar(selecao, orient="vertical")
        lista_recomendacoes = Listbox(selecao, selectmode="extended", yscrollcommand=barra_rolagem.set,
                                      width="400", height="15")

        barra_rolagem.config(command=lista_recomendacoes.yview)

        selecao.pack()
        barra_rolagem.pack(side="right", fill="y")
        lista_recomendacoes.pack(expand = True, fill = "both")

        botao_selecionar = Button(janela_recomendacoes,    
                                  text='Selecionar',
                                  command= lambda : Coletor.definir_recomendacoes(janela_recomendacoes,
                                                                                  lista_recomendacoes))
        botao_selecionar.pack(side="bottom")

        recomendacoes = Coletor.todas_recomendacoes
        
        for each_item in range(len(recomendacoes)):
            lista_recomendacoes.insert("end", recomendacoes[each_item])
            
            # coloring alternative lines of listbox
            lista_recomendacoes.itemconfig(each_item,
                    bg = "lightgray" if each_item % 2 == 0 else "gray")
            
        lista_recomendacoes.mainloop()


    @staticmethod
    def definir_alunos():
        # Cria dicionário que mapeia id -> nome do aluno
        if Coletor.ja_carreguei_planilha_alunos:
            Coletor.dicionario_alunos = Coletor.planilha_alunos_raw.set_index('Id').to_dict()['Nome']
        else:
            nomes_alunos = Coletor.planilha_KA_raw['Nome do aluno'].unique()
            for nome_id in nomes_alunos:
                aluno = nome_id.split('_')
                nome = aluno[0]
                id = aluno[1]
                Coletor.dicionario_alunos[id] = nome
        # print(Coletor.dicionario_alunos)

    @staticmethod
    def coletar_dados_finais():
        # preenche os espaços vazio com zeros
        Coletor.planilha_KA_raw.fillna(0, inplace=True, axis = 1)
        
        alunos = []

        # para cada aluno na planilha de alunos...
        for id_aluno in Coletor.dicionario_alunos:
            # condição para "pegar" a recomendação do aluno: Nome do aluno terminar com seu Id
            condicao = Coletor.planilha_KA_raw['Nome do aluno'].str.endswith(id_aluno)
            recomendacoes_aluno = Coletor.planilha_KA_raw[condicao]

            num_recomendacoes = len(Coletor.recomendacoes_selecionadas)
            percentual_tentativas = 0
            desempenho_medio = 0

            #print(id_aluno, num_recomendacoes)

            recomendacao_infos = []
            # para cada recomendação nas recomendações do aluno...
            for recomendacao in Coletor.recomendacoes_selecionadas:
                # colete os dados daquela recomendação
                dados_da_recomendacao = recomendacoes_aluno[recomendacoes_aluno['Nome da recomendação'] == recomendacao]

                if dados_da_recomendacao.empty:
                    print("Aluno sem recomendação:", end=' ')
                    print(id_aluno, Coletor.dicionario_alunos[id_aluno], recomendacao)
                #    return

                # se o número de tentativas não é zero:
                pontos_na_recomendacao = 0
                if not dados_da_recomendacao.empty and dados_da_recomendacao['Número de tentativas'].values[0] != 0:
                    # aumente o número de tentativas
                    percentual_tentativas += 1

                    # converta os pontos daquela recomendação para percentual
                    pontos_na_recomendacao = (dados_da_recomendacao['Pontuação na data final'].values[0] 
                                              /
                                              dados_da_recomendacao['Pontos possíveis'].values[0])*100
                    
                    # some os pontos no desempenho médio
                    desempenho_medio += pontos_na_recomendacao
                
                # salve o nome e os pontos daquela recomendação
                recomendacao_infos.append((recomendacao, pontos_na_recomendacao))
            
            # calcule a média, dividindo pela quantidade de recomendações
            percentual_tentativas /= num_recomendacoes
            desempenho_medio /= num_recomendacoes

            # salve o aluno com seus dados preliminares
            alunos.append([Coletor.dicionario_alunos[id_aluno], percentual_tentativas, desempenho_medio, recomendacao_infos])

        # cria uma nova tabela (dataframe) para o resultado
        resultado = pd.DataFrame()

        # para cada aluno, com seu ID
        for [id, aluno] in enumerate(alunos):
            # defina o nome
            resultado.at[id, 'Nome do aluno'] = aluno[0]

            # a porcentagem de tentativas (convertendo . para ,)
            resultado.at[id, 'Porcentagem de Tentativas'] = str(round(aluno[1]*100, 2)).replace('.', ',')

            # o desempenho médio (convertendo . para ,)
            desempenho_medio_arredondado = (round(aluno[2], 2))
            resultado.at[id, 'Desempenho Médio'] = str(desempenho_medio_arredondado).replace('.', ',')
            
            # a pontuação (convertendo . para ,)
            pontuacao = round(desempenho_medio_arredondado/100, 2)
            resultado.at[id, 'Pontuação'] = str(pontuacao).replace('.', ',')
            
            # para cada recomendação desse aluno (índice 3 do vetor):
            for recomendacao in aluno[3]:
                # atribua os pontos dessa recomendação (índice 0 é o nome e índice 1 é o valor)
                resultado.at[id, recomendacao[0]] = str(round(recomendacao[1],2)).replace('.', ',') 

        # salve no destino
        caminho_KA = Leitor.caminho_planilha_KA.split('/') 
        nome_arquivo_resultado = f'Resultado_{caminho_KA[-1]}'

        caminho_destino = Path(Leitor.caminho_diretorio_destino, nome_arquivo_resultado)
        resultado.to_csv(caminho_destino)

        Coletor.mostrar_mensagem('Dados coletados com sucesso!')
        exit()
        # imprima algo no terminal (TESTE)
        # print("cabo")
        #print(resultado[['Nome do aluno', 'Pontuação', 'Porcentagem de Tentativas']])

            

            
            
            








        
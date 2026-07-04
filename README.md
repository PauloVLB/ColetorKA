# ColetorKA

Coletor de dados das planilhas recebidas pela plataforma Khan Academy.

---

## 📖 O que este programa faz?

Este programa facilita o trabalho de consolidação de dados da **Khan Academy**. Ele junta as informações de diferentes planilhas (como a lista de alunos e o relatório da plataforma) em um único arquivo, facilitando a visualização do desempenho da turma.

---

## 🚀 Como Usar o Programa

Se você já possui o arquivo executável do programa (o arquivo que você clica para abrir), siga estes passos simples:

1. **Abra o Programa**: Dê um duplo clique no arquivo executável (ele terá o nome do programa). Uma janela com opções se abrirá.
2. **Selecione a Planilha de Alunos**:
   * Clique no botão **"Selecionar Arquivo"** ao lado de "1. Planilha de alunos".
   * Procure e selecione o arquivo `.csv` que contém a lista dos seus alunos.
3. **Selecione a Planilha da Khan Academy**:
   * Clique no botão **"Selecionar Arquivo"** ao lado de "2. Planilha da Khan Academy".
   * Procure e selecione o relatório que você baixou da Khan Academy (também em formato `.csv`).
4. **Escolha onde salvar o resultado**:
   * Clique em **"Selecionar Pasta"** ao lado de "3. Selecionar Pasta Destino".
   * Escolha a pasta no seu computador onde deseja que o novo arquivo seja salvo.
5. **Selecione as Recomendações (Opcional)**:
   * Clique em **"Selecionar"** ao lado de "4. Selecionar Recomendações" para escolher quais atividades deseja incluir.
6. **Gere a Planilha**:
   * Clique no botão **"Coletar Dados!"** ao lado de "5. Coletar todos os dados".
7. **Pronto!**: Uma mensagem de sucesso aparecerá e o novo arquivo estará na pasta que você escolheu.

---

## 🛠️ Como Gerar o Executável

Se você deseja gerar o arquivo executável a partir do código fonte deste repositório, siga estes passos:

> ⚠️ **IMPORTANTE**: Para gerar um executável para **Windows**, você deve executar estes passos em uma máquina com **Windows**. O executável gerado no Linux só funcionará no Linux.

### Pré-requisitos
* **Python** instalado na sua máquina.
* Acesso ao terminal ou prompt de comando.

### Passo a Passo

1. **Instale as Bibliotecas Necessárias**:
   Abra o terminal na pasta do projeto e execute:
   ```bash
   pip install pandas pyinstaller
   ```

2. **Gere o Executável**:
   No terminal, execute o comando:
   ```bash
   pyinstaller --onefile --noconsole --name ColetorKA main.py
   ```
   * *O parâmetro `--onefile` garante que todas as dependências sejam empacotadas em um único arquivo.*
   * *O parâmetro `--noconsole` evita que uma janela preta de terminal abra em segundo plano (útil para programas com interface gráfica).*

3. **Localize o Arquivo**:
   O executável será gerado dentro da pasta **`dist`**, que aparecerá na pasta raiz do projeto.

---

## ❓ Possíveis Problemas e Soluções (Especialmente no Windows)

### 1. O antivírus bloqueou o programa
* **Problema**: O Windows Defender ou outro antivírus pode identificar o executável gerado pelo PyInstaller como uma ameaça (Falso Positivo).
* **Solução**: Você pode adicionar o arquivo como uma exceção no seu antivírus ou desativá-lo temporariamente para rodar o programa.

### 2. O programa abre e fecha imediatamente ou não abre
* **Problema**: Pode estar faltando alguma dependência interna ou o programa encontrou um erro que não pôde ser exibido.
* **Solução**: Tente gerar o executável **sem** o parâmetro `--noconsole` (ou seja, use apenas `pyinstaller --onefile main.py`). Isso fará com que uma janela de terminal abra junto com o programa, exibindo possíveis erros que ajudam no diagnóstico.

### 3. Problemas com Interface Gráfica no Linux
* **Problema**: A janela não abre.
* **Solução**: Pode ser necessário instalar o pacote de interface gráfica do Python (`python3-tk`). No Ubuntu/Debian, use: `sudo apt-get install python3-tk`.

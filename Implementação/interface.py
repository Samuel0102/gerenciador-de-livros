"""Esse módulo representa a interface gráfica do problema de livros

Fora implementada uma interface no terminal

Autores: Samuel Pacheco, Maria Erbs e Thaís Junkes
"""
from classe_gerenciador import GerenciadorDeLivros
from os import system

# instanciação do gerenciador, para comando de processos
Gerenciador = GerenciadorDeLivros()

# função lambda para limpeza de terminal
cls = lambda : system("cls")

# laço para continuidade do menu
while True:
    print("=-=-=-=-=-=Menu=-=-=-=-=")
    print("C - Cadastrar novo livro\nP - Pesquisar livro\nR - Remover livro\nS - Sair")
    print("=-=-=-=-=-==-=-=-=-=-=-=")

    opcao = input("Função desejada: ").upper()

    cls()

    # cadastro do livro
    if opcao == "C":
        Gerenciador.cadastrar_livro()

        print("=-=-=-=-=-=-==-=-=-=-=-==-=-=-=")
        print(Gerenciador.salvar_livro())
        print("=-=-=-=-=-=-==-=-=-=-=-==-=-=-=")
    
    # pesquisa do livro
    elif opcao == "P":
        codigo_do_livro = input("Digite o código identificador dado: ")

        print("=-=-=-=-=-=-=-=-Resultado=-=-=-=-=-=-=-=-")
        print(Gerenciador.pesquisar_livro(codigo_do_livro))
        print("=-=-=-=-=-=-==-=-=-=-=-==-=-=-=--=-=-=-=-")

    # remoção do livro
    elif opcao == "R":
        codigo_do_livro = input("Digite o código identificador dado: ")

        mensagem = Gerenciador.remover_livro(codigo_do_livro)

        print("=-=-=-=-=-=-==-=-=-=-=-==-=-=-=")
        print("\n" + mensagem + "\n")
        print("=-=-=-=-=-=-==-=-=-=-=-==-=-=-=")

    # saída do programa
    elif opcao == "S":
        break

    # controle de entrada
    elif opcao not in "//R//P//C//S//":
        print("Opção Inválida")

    # limpeza de terminal
    input("Enter para continuar...")
    cls()


    
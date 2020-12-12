"""Esse módulo representa uma das classes do problema de livros

Fora implementada a classe Gerenciador de Livros

Autores: Samuel Pacheco, Maria Erbs e Thaís Junkes
"""
from os import path, remove
from classe_livro import Livro
from classe_digital import Digital
from classe_fisico import Fisico


class GerenciadorDeLivros:
    """Classe que comanda os processos do problema

    Args:
        dados (list): todos os dados referentes a um livro(digital/fisico)
        diretorio_execucao (str): diretorio onde encontra-se o atual arquivo py
    """


    def __init__(self):
        """Método construtor

        """
        self.__dados = []
        self.__diretorio_execucao = path.dirname(path.abspath(__file__))

    def cadastrar_livro(self):
        """Método para obter informações sobre o livro

        Esse método é responsável por instanciar uma das classes
        Digital ou Fisico, recebendo dados para passagem nos atributos

        """
        tipo_de_livro = input("Digite o tipo de livro(F/D): ").upper()
        nome = input("Nome do Livro: ")
        autor = input("Autor do Livro: ")
        editora = input("Editora: ")
        ano_publicacao = input("Ano de publicacao: ")
        categoria = input("Gênero: ")

        if tipo_de_livro == "F":
            adicional = input("Tipo de capa: ")
            LivroAtual = Fisico(adicional, nome, autor, editora, ano_publicacao, categoria)

        elif tipo_de_livro == "D":
            adicional= input("Link de acesso: ")
            LivroAtual = Digital(adicional, nome, autor, editora, ano_publicacao, categoria)

        else:
            print("Tipo Inválido :C")

        self.__dados = [LivroAtual.get_codigo(),LivroAtual.get_nome(),LivroAtual.autor,
                        LivroAtual.editora, LivroAtual.ano_publicacao, LivroAtual.categoria,
                        adicional
                        ]

    def pesquisar_livro(self, codigo_do_livro: str):
        """Método responsável por pesquisar livro nos registros

        A pesquisa é feita através de identificação com código identificador
        Caso o livro seja encontrado, o conteúdo do arquivo txt é impresso no
        terminal

        Args:
            codigo_do_livro (str): código de identificação do livro, dado previamente

        Returns:
            str: resultado da busca(informações/erro)
        """
        try:
            arquivo_registro = open(self.__diretorio_execucao + f"\\Registros\\Livro_cod_{codigo_do_livro}.txt" , "r")
            resultado = arquivo_registro.read()
            arquivo_registro.close()
        except:
            resultado = "Livro não encontrado nos registros :C"

        return resultado

    def remover_livro(self, codigo_do_livro: str):
        """Método para remover livro do diretório de registros
    
        Procura o arquivo txt através do código identificador
        após remove ele do diretório

        Args:
            codigo_do_livro (str): código de identificação do livro, dado previamente

        Returns:
            str : mensagem para retorno no terminal
        """
        try:
            arquivo_registro = self.__diretorio_execucao + f"\\Registros\\Livro_cod_{codigo_do_livro}.txt"
            remove(arquivo_registro)
            mensagem = "Livro removido dos registros! "
        except:
            mensagem = "Livro não encontrado nos registros :C"

        return mensagem

    def salvar_livro(self):
        """Método responsável por escrever informações no arquivo txt

        Após instanciação de um dos tipos, esse método obtém o atributo
        referente aos dados fornecidos a respeito do livro, então
        ele utiliza uma lista de identificadores

        Returns:
           str : mensagem para retorno no terminal
        """
        arquivo_registro = open(self.__diretorio_execucao + f"\\Registros\\Livro_cod_{self.__dados[0]}.txt" , "w")

        identificadores = ["Código: ", "Nome do Livro: ", "Autor: ", 
                            "Editora: ", "Ano Publicação: ", "Categoria: ",
                             "Link de acesso/ Tipo de capa: "]

        for identicador, dado in enumerate(self.__dados):
            arquivo_registro.write(identificadores[identicador] + dado + "\n")

        mensagem = f"O livro foi cadastrado com sucesso!\nCódigo de identificação: {self.__dados[0]}"

        return mensagem
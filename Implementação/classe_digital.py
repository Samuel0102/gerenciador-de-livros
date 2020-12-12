"""Esse módulo representa uma das classes do problema de livros

Fora implementada a classe filha Digital

Autores: Samuel Pacheco, Maria Erbs e Thaís Junkes
"""
from classe_livro import Livro


class Digital(Livro):
    """Classe que representa um livro digital do mundo real

    Args:
        Livro (Livro): Classe pai Livro, contendo atributos básicos
        nome (str) : nome do livro
        autor (str) : autor do livro
        editora (str) : editora do livro
        ano_publicacao (str) : ano de publicação do livro
        categoria (str) : gênero do livro

    """


    def __init__(self, link_de_acesso: str, nome: str, autor: str, editora: str, ano_publicacao: str, categoria: str):
        """Método construtor

        Args:
            link_de_acesso (str): link de acesso do livro(site)
            nome (str): nome do livro 
            autor (str): autor do livro
            editora (str): editora do livro
            ano_publicacao (str): ano de publicação do livro
            categoria (str): gênero do livro
        """
        self.__link_de_acesso = link_de_acesso
        super().__init__(nome, autor, editora, ano_publicacao, categoria)
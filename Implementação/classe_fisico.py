"""Esse módulo representa uma das classes do problema de livros

Fora implementada a classe filha Fisico

Autores: Samuel Pacheco, Maria Erbs e Thaís Junkes
"""
from classe_livro import Livro


class Fisico(Livro):
    """Classe que representa um livro físico do mundo real

    Args:
        Livro (Livro): Classe pai Livro, contendo atributos básicos
        nome (str) : nome do livro
        autor (str) : autor do livro
        editora (str) : editora do livro
        ano_publicacao (str) : ano de publicação do livro
        categoria (str) : gênero do livro

    """


    def __init__(self, tipo_de_capa: str, nome: str, autor: str, editora: str, ano_publicacao: str, categoria: str):
        """Método construtor

        Args:
            tipo_de_capa (str): tipo de capa do livro
            nome (str): nome do livro 
            autor (str): autor do livro
            editora (str): editora do livro
            ano_publicacao (str): ano de publicação do livro
            categoria (str): gênero do livro
        """
        self.tipo_de_capa = tipo_de_capa
        super().__init__(nome, autor, editora, ano_publicacao, categoria)

"""Esse módulo representa uma das classes do problema de livros

Fora implementada a classe pai Livro

Autores: Samuel Pacheco, Maria Erbs e Thaís Junkes
"""
from random import randint


class Livro:
    """Essa classe representa um livro da vida real

    Args:
        nome (str) : nome do livro
        autor (str) : autor do livro
        editora (str) : editora do livro
        ano_publicacao (str) : ano de publicação do livro
        categoria (str) : gênero do livro
        codigo (str) : identificador do livro, para consultas

    """


    def __init__(self, nome: str, autor: str, editora: str, ano_publicacao: str, categoria:str):
        """Método construtor 

        Args:
            nome (str) : nome do livro
            autor (str) : autor do livro
            editora (str) : editora do livro
            ano_publicacao (str) : ano de publicação do livro
            categoria (str) : gênero do livro
        """
        self.__nome = nome
        self.autor = autor
        self.editora = editora
        self.ano_publicacao = ano_publicacao
        self.categoria = categoria
        self.__codigo = ""

    def get_nome(self):
        """Método para obter dado privado

        Returns:
            str : atributo referente ao livro
        """
        return self.__nome

    def get_codigo(self):
        """Método para preencher atributo vazio

        Returns:
            str : código identificador do livro
        """
        codigo = str(randint(1,9))+str(randint(1,9))+str(randint(1,9))
        self.__codigo = codigo
        return self.__codigo 
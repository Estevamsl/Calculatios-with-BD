from abc import ABC, abstractmethod
import pymysql.cursors

from __erros__.__err import ConectionsErrors
from Conections__.Types.PyMySQL.__pyM__ import Conections
from Conections__.Types.SQLAlchemy__.__SQLAl__ import Conections


class CRUDInsert__:
    class CRUDINSERT(object):  # CRUD().CRUDINSERT().Insert()
        class Insert(object):
            """ Inserir dados na base de dados MySQL """

            # CRUD().CRUDINSERT().Insert().__SUM__()
            def __SUM__(self, __n1__: int, __n2__: int) -> any:
                con = Conections().DBPy
                # __soma__ = (
                #     f'A soma de {__n1__} e {__n2__} é: {__n1__ + __n2__}')
                __soma__ = __n1__ + __n2__
                try:
                    with con.cursor() as cursor:
                        try:
                            cursor.execute(
                                f'insert into Soma(number1, number2, Soma) values ({__n1__}, {__n2__}, {__soma__})')
                            con.commit()
                        except:
                            print(
                                '\033[31mNão foi possível Inserir dados ao bd\033[m')
                        else:
                            print(
                                '\033[34mDados inseridos ao BD com sucesso\033[m')
                except:
                    print('\033[31mHouve um pequeno error\033[m')

            # CRUD().CRUDINSERT().Insert().__SUB__()
            def __SUB__(self, __n1__: int, __n2__: int) -> any:
                con = Conections().DBPy
                # __subtracao__ = (
                #     f'A subtração de {__n1__} e {__n2__} é: {__n1__ - __n2__}')
                __subtracao__ = __n1__ - __n2__
                try:
                    with con.cursor() as cursor:
                        try:
                            cursor.execute(
                                f'insert into Subtracao(number1, number2, Subtracao) values ({__n1__}, {__n2__}, {__subtracao__})')
                            con.commit()
                        except:
                            print(
                                '\033[31mNão foi possível Inserir dados ao bd\033[m')
                        else:
                            print(
                                '\033[34mDados inseridos ao BD com sucesso\033[m')
                except:
                    print('\033[31mHouve um pequeno error\033[m')

            # CRUD().CRUDINSERT().Insert().__PRO__()

            def __PRO__(self, __n1__: int, __n2__: int) -> any:
                con = Conections().DBPy
                # __produto__ = (
                #     f'O produto de {__n1__} e {__n2__} é: {__n1__ * __n2__}')
                __produto__ = __n1__ * __n2__
                try:
                    with con.cursor() as cursor:
                        try:
                            cursor.execute(
                                f'insert into Produto(number1, number2, Produto) values ({__n1__}, {__n2__}, {__produto__})')
                            con.commit()
                        except:
                            print(
                                '\033[31mNão foi possível Inserir dados ao bd\033[m')
                        else:
                            print(
                                '\033[34mDados inseridos ao BD com sucesso\033[m')
                except:
                    print('\033[31mHouve um pequeno error\033[m')

            # CRUD().CRUDINSERT().Insert().__DIV__()
            def __DIV__(self, __n1__: int, __n2__: int) -> any:
                con = Conections().DBPy
                # __divisao__ = (
                #     f'A divisão de {__n1__} e {__n2__} é: {__n1__ / __n2__}')
                __divisao__ = __n1__ + __n2__
                try:
                    with con.cursor() as cursor:
                        try:
                            cursor.execute(
                                f'insert into Divisao(number1, number2, Divisao) values ({__n1__}, {__n2__}, {__divisao__})')
                            con.commit()
                        except:
                            print(
                                '\033[31mNão foi possível Inserir dados ao bd\033[m')
                        else:
                            print(
                                '\033[34mDados inseridos ao BD com sucesso\033[m')
                except:
                    print('\033[31mHouve um pequeno error\033[m')

from abc import ABC, abstractmethod
import pymysql.cursors
import pandas as pd
import sqlalchemy

from __erros__.__err import ConectionsErrors
from Conections__.Types.PyMySQL.__pyM__ import Conections
from Conections__.Types.SQLAlchemy__.__SQLAl__ import Conections


class CRUDConsult__:
    class CRUDCONSULT(object):  # CRUD().CRUDCONSULT().Consult().__C__
        class Consult(object):
            """ Utilizar a lib sqlalchemy e pandas para consultar os dados no BD """

            class Consult_Por_Operacao(object):
                @property
                def __sm__(self):  # CRUD().CRUDCONSULT().Consult().Consult_Por_Operacao().__sm__
                    conn = Conections().DBPy
                    try:
                        pass
                        with conn.cursor() as cursor:
                            try:
                                cursor.execute('Select * from soma')
                                __cons__ = cursor.fetchall()
                                for __c__ in __cons__:
                                    print(__c__)
                            except:
                                print(
                                    '\033[31mNão foi possível consultar a tabela Soma na Base de dados\033[m')
                            else:
                                print('Dados consultados com sucesso')
                    except:
                        print('\033[31mHouve um pequeno erro\033[m')

                @property
                def __sb__(self):  # CRUD().CRUDCONSULT().Consult().Consult_Por_Operacao().__sb__
                    conn = Conections().DBPy
                    try:
                        pass
                        with conn.cursor() as cursor:
                            try:
                                cursor.execute('select * from Subtracao')
                                __cons__ = cursor.fetchall()
                                for __c__ in __cons__:
                                    print(__c__)
                            except:
                                print(
                                    '\033[31mNão foi possível consultar os dados no BD\033[m')
                            else:
                                print('Dados do BD consultados com sucesso')
                    except:
                        pass
                        print('Houve um pequeno erro')

                @property
                def __pro__(self):  # CRUD().CRUDCONSULT().Consult().Consult_Por_Operacao().__pro__
                    conn = Conections().DBPy
                    try:
                        pass
                        with conn.cursor() as cursor:
                            try:
                                cursor.execute('Select * from Produto')
                                __cons__ = cursor.fetchall()
                                for __c__ in __cons__:
                                    print(__c__)
                            except:
                                print(
                                    '\033[31mNão foi possível consultar os dados no BD\033[m')
                            else:
                                print('Dados consultados no BD com sucesso')
                    except:
                        pass
                        print("\033[31mHouve um pequeno erro\033[m")

                @property
                def __di__(self):  # CRUD().CRUDCONSULT().Consult().Consult_Por_Operacao().__di__
                    pass
                    conn = Conections().DBPy
                    try:
                        with conn.cursor() as cursor:
                            try:
                                cursor.execute('Select * from Divisao')
                                __cons__ = cursor.fetchall()
                                for __c__ in __cons__:
                                    print(__c__)
                            except:
                                print(
                                    '\033[31mNão foi possível consultar os dados no BD')
                            else:
                                print('Dados consultados no BD com sucesso')
                    except:
                        print('\033[31mHouve um pequeno erro\033[m')

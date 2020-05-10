""" SQLAlchemy """
from abc import ABC, abstractmethod
import pymysql.cursors
import pandas as pd
import sqlalchemy
from sqlalchemy import Column as COLUN, Integer as INT, VARCHAR as STR
from sqlalchemy.ext.declarative import declarative_base

from __erros__.__err import ConectionsErrors


class Conections(object):
    @property
    def DBPy(self):
        """ Conexão ao Banco de Dados via lib PyMySQL """
        try:
            db = pymysql.connect(
                host='localhost',
                user='root',
                password='',
                db='python',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )
            return db

        except:
            raise ConectionsErrors().SQLError(
                '\033[31mNão foi possível estabelecer a conxão segura do servidor  MySQL\033[m')
        else:
            print('Conexão realizada com sucesso')

    @property
    def DBAc(self):
        """ Conexão ao Banco de Dados via lib do SqlAlchemy """
        pass
        try:
            engine = sqlalchemy.create_engine(
                'mysql+pymysql://root:@localhost:3306/python')
            return engine
        except:
            raise ConectionsErrors().SQLError(
                '\033[31mNão foi possível estabelecer a conxão segura do servidor  MySQL\033[m')
        else:
            print('Conexão realizada com sucesso')

from abc import ABC, abstractmethod
import pymysql.cursors
import pandas as pd
import sqlalchemy
from sqlalchemy import Column as COLUN, Integer as INT, VARCHAR as STR
from sqlalchemy.ext.declarative import declarative_base

from __erros__.__err import ConectionsErrors
from Conections__.Types.PyMySQL.__pyM__ import Conections
from Conections__.Types.SQLAlchemy__.__SQLAl__ import Conections


# BASE = declarative_base()


class CRUDCreate__:
    class CRUDCREATE(object):  # CRUD().CRUDCONSULT().Consult().__C__
        class Create(object):
            """ Utilizar a lib sqlalchemy e pandas para consultar os dados no BD """

            @property
            def __C__(self):
                # df = pd.read_sql_table('Soma', Conections().DBAc)
                # print(df.head())
                conn = Conections().DBPy
                try:
                    with conn.cursor() as cursor:
                        try:
                            cursor.execute('SELECT * FROM Soma')
                            # conn.commit()
                            consult = cursor.fetchall()
                        except:
                            print('Não foi possível consultar ao bd')
                    print(consult)
                except:
                    print('Houve um pequeno error')

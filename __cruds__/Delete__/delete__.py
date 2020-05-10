from abc import ABC, abstractmethod
import pymysql.cursors
import pandas as pd
import sqlalchemy

from __erros__.__err import ConectionsErrors
from Conections__.Types.PyMySQL.__pyM__ import Conections
from Conections__.Types.SQLAlchemy__.__SQLAl__ import Conections


class CRUDDelete__:
    class CRUDDELL(object):  # CRUD().CRUDDELL().Dell().__I__(1)
        class Dell(object):
            def __D__(self, __id__: int) -> any:
                con = Conections().DBPy
                try:
                    with con.cursor() as cursor:
                        try:
                            cursor.execute('SELECT * FROM Soma')
                            con.commit()
                        except:
                            print(
                                '\033[31mNão foi possível deletar dados do bd\033[m')
                        else:
                            print('Dados deletados com sucesso')
                except:
                    print('\033[31mHouve um pequeno error\033[m')

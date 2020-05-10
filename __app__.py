""" Error ao inserir os dados dos cálculos na Base de Dados """

from abc import ABC, abstractmethod
import pymysql.cursors
import pandas as pd
import sqlalchemy
from sqlalchemy import Column as COLUN, Integer as INT, VARCHAR as STR
from sqlalchemy.ext.declarative import declarative_base


# BASE = declarative_base()


class ConectionsErrors(object):
    class CalcsError(Exception):
        pass

    class SQLError(Exception):
        pass

    class CreateTableError(Exception):
        pass

    class ConsultError(Exception):
        pass

    class InsertError(Exception):
        pass

    class DellError(Exception):
        pass

    class UpdatedError(Exception):
        pass


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


# class Create(object):
#     """ Criação da table ao Banco de Dados via duas libs: PyMySQL and Pandas"""
#     class Calculos(BASE):
#         __tablename__ = 'Calculos'
#         id = COLUN(INT, primary_key=True)
#         numero1 = COLUN(INT)
#         numero2 = COLUN(INT)

#         resultado = COLUN(STR(200))
#     Calculos.__table__.create(Conections().DBAc)

class CRUD:
    class CRUDCONSULT(object):  # CRUD().CRUDCONSULT().Consult().__C__
        class Consult(object):
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
                                print(__cons__)
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
                                print(__cons__)
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
                                print(__cons__)
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
                            except:
                                print(
                                    '\033[31mNão foi possível consultar os dados no BD')
                            else:
                                print('Dados consultados no BD com sucesso')
                    except:
                        print('\033[31mHouve um pequeno erro\033[m')

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

    class CRUDUPDATE(object):  # CRUD().CRUDUPDATE().Update().__Up__()
        class Update(object):
            """ Irá atualizar os dados na base de dados Mysql """

            def __Up__(self):
                con = Conections().DBPy
                try:
                    with con.cursor() as cursor:
                        try:
                            cursor.execute('SELECT * FROM Soma')
                            con.commit()
                        except:
                            print(
                                '\033[31mNão foi possível atualizar os dados do bd\033[m')
                        else:
                            print('Dados atualizados com sucesso')
                except:
                    print('\033[31mHouve um pequeno error\033[m')

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


class interface(ABC):
    # @abstractmethod
    def somar(self, __n1__: int, __n2__: int) -> any: pass
    # @abstractmethod
    def subtrair(self, __n1__: int, __n2__: int) -> any: pass
    # @abstractmethod
    def produto(self, __n1__: int, __n2__: int) -> any: pass
    # @abstractmethod
    def dividir(self, __n1__: float, __n2__: float) -> any: pass


class __Calculadora__(ABC):
    def __init__(self, __n1__: int) -> any:
        self.__n1__ = __n1__

    def __add__(self, __n2__: int) -> any:
        return self.__n1__ + __n2__.__n1__

    def __sub__(self, __n2__: int) -> any:
        return self.__n1__ - __n2__.__n1__

    def __mul__(self, __n2__: int) -> any:
        return self.__n1__ * __n2__.__n1__

    def __truediv__(self, __n2__: int) -> any:
        return self.__n1__ / __n2__.__n1__

    def __del__(self):
        return f'{__class__.__name__} destruída da memória'


class Mixin(interface):
    @property
    def __prin__(self) -> any:
        print(
            '\n\033[34m[1]\033[m - \033[36mBD:\033[m\n\033[34m[2]\033[m - \033[36mRealizar Calculos:\033[m\n\033[34m[3]\033[m - \033[36mSair:\033[m')

    @property
    def __calcs__(self) -> any:
        print(
            '\n\033[34m[1]\033[m - \033[36mSomar:\033[m\n\033[34m[2]\033[m - \033[36mSubtrair:\033[m\n\033[34m[3]\033[m - \033[36mProduto:\033[m\n\033[34m[4]\033[m - \033[36mDividir:\033[m\n\033[34m[5]\033[m - \033[36mSair Para ir ao Menu Principal:\033[m')

    @property
    def __bd__(self) -> any:
        print(
            '\n\033[34m[1]\033[m - \033[36mConsultar:\033[m\n\033[34m[2]\033[m - \033[36mInserir:\033[m\n\033[34m[3]\033[m - \033[36mAtualizar:\033[m\n\033[34m[4]\033[m - \033[36mDeletar:\033[m\n\033[34m[5]\033[m - \033[36mSair Para ir ao Menu Principal:\033[m')

    def soma(self, __n1__: int, __n2__: int) -> any:
        __a1__ = __Calculadora__(__n1__)
        __a2__ = __Calculadora__(__n2__)
        res = __a1__ + __a2__
        print(res)

    def subtrair(self, __n1__: int, __n2__: int) -> any:
        __a1__ = __Calculadora__(__n1__)
        __a2__ = __Calculadora__(__n2__)
        res = __a1__ - __a2__
        print(res)

    def produto(self, __n1__: int, __n2__: int) -> any:
        __a1__ = __Calculadora__(__n1__)
        __a2__ = __Calculadora__(__n2__)
        res = __a1__ * __a2__
        print(res)

    def dividir(self, __n1__: float, __n2__: float) -> any:
        __a1__ = __Calculadora__(__n1__)
        __a2__ = __Calculadora__(__n2__)

        try:
            res = __a1__ / __a2__
            print(res)
        except ZeroDivisionError:
            print(f'Não foi possível dividir {__a1__} por {__n2__}')


class __MixinCalculadora__(Mixin):
    def __init__(self) -> any:
        from os import system
        self.system = system
        system('cls')
        print('\033[35mClaculadora:\033[m')

    def __call__(self) -> any:
        return self.__n1__

    def __str__(self) -> any:
        return f'Método da classe {__class__.__name__}'

    def __repr__(self) -> any:
        return super().__repr__()


class Main(__MixinCalculadora__):

    @property
    def OP_Calculos(self) -> any:
        __op__ = 1
        while (__op__ > 0):
            self.__calcs__  # Realizar Cálculos - 2

            try:
                __op__ = int(input('Digite a sua opção: \033[36m'))
                print('\033[m')
            except ValueError:
                print('Houve um erro de valor')

            try:
                __n1__ = int(
                    input('Digite o primeiro número: \033[36m'))
                print('\033[m')
            except ValueError:
                print('Houve um erro de valor')
            try:
                __n2__ = int(
                    input('Digite o segundo número: \033[36m'))
                print('\033[m')
            except ValueError:
                print('Houve um erro de valor')

            if (__op__ == 1):
                super().somar(__n1__, __n2__)
                CRUD().CRUDINSERT().Insert().__SUM__(__n1__, __n2__)
                # self.system('cls')
            elif (__op__ == 2):
                super().subtrair(__n1__, __n2__)
                CRUD().CRUDINSERT().Insert().__SUB__(__n1__, __n2__)
                # self.system('cls')
            elif (__op__ == 3):
                super().produto(__n1__, __n2__)
                CRUD().CRUDINSERT().Insert().__PRO__(__n1__, __n2__)
                # self.system('cls')
            elif (__op__ == 4):
                super().dividir(__n1__, __n2__)
                CRUD().CRUDINSERT().Insert().__DIV__(__n1__, __n2__)
                # self.system('cls')
            else:
                __op__ = 0
                self.system('cls')

                # Implementar o conceito de Recursion para voltar ao Menu Principal

    @property
    def OP_Bd(self) -> any:
        __op__ = 1
        while (__op__ > 0):
            self.__bd__  # Realizar Cálculos - 2

            try:
                __op__ = int(input('Digite a sua opção: \033[36m'))
                print('\033[m')
            except ValueError:
                print('\033[31mHouve um erro de valor\033[m')

            if (0 > __op__ > 5):
                print('Opção incorreta, tente novamente')
            else:
                if (__op__ == 1):
                    # super().somar(__n1__, __n2__)
                    # self.system('cls')
                    print('Consulte aqui no seu BD')
                    print('\033[34m[1]\033[m - \033[36mSomar:\033[36m\n\033[34m[2]\033[m - \033[36mSubtrair:\033[m\n\033[34m[3]\033[m - \033[36mProduto\033[m\n\033[34m[4]\033[m - \033[36mDivisão:\033[m')

                    try:
                        __op__ = int(input('Digite a sua opção: \033[30m'))
                        print('\033[m')
                    except ValueError:
                        print(
                            "\033[31mErr de tipo, favor tentar novamente\033[m")

                    if (__op__ == 1):
                        pass
                        CRUD().CRUDCONSULT().Consult().Consult_Por_Operacao().__sm__
                    elif (__op__ == 2):
                        pass
                        CRUD().CRUDCONSULT().Consult().Consult_Por_Operacao().__sb__
                    elif (__op__ == 3):
                        pass
                        CRUD().CRUDCONSULT().Consult().Consult_Por_Operacao().__pro__
                    elif (__op__ == 4):
                        pass
                        CRUD().CRUDCONSULT().Consult().Consult_Por_Operacao().__di__
                    elif (__op__ == 5):
                        __op__ = 0

                    CRUD().CRUDCONSULT().Consult().__C__
                    pass
                elif (__op__ == 2):
                    # super().subtrair(__n1__, __n2__)
                    # self.system('cls')
                    print('Insere aqui no seu BD')
                    pass
                elif (__op__ == 3):
                    # super().produto(__n1__, __n2__)
                    # self.system('cls')
                    print('Atualiza os seus dados aqui no BD')
                    CRUD().CRUDUPDATE().Update().__Up__()
                    pass
                elif (__op__ == 4):
                    # super().dividir(__n1__, __n2__)
                    # self.system('cls')
                    print('Deleta seu dados aqui no BD')
                    CRUD().CRUDDELL().Dell().__D__(1)
                    pass
                else:
                    __op__ = 0
                    self.system('cls')

    # def OP_MENU(self) -> any:
    #     pass
    #     __op__ = 1
    #     while (__op__ > 0):
    #         pass
    #         try:
    #             __op__ = int(input('Digite a sua opção: \033[36m'))
    #             print('\033[m')
    #         except ValueError:
    #             print(
    #                 '\033[31mErro de tipo, por favor digitar novamente a opção')

    @property
    def main(self) -> any:
        pass
        __op__ = 1
        while (__op__ != 0):
            self.__prin__  # Menu Principal
            #
            # self.__calcs__  # Realizar Cálculos - 2
            # Sair - 3
            # break
            try:
                __op__ = int(input('Digite a sua opção: \033[36m'))
                print('\033[m')
            except ValueError:
                print('\033[31mHouve um erro de valor\033[m')

            if (__op__ > 0):

                if (0 > __op__ > 3):
                    pass
                    print(
                        '\033[31mOpção Incorreta, Tente outra novamente\033[m')

                else:
                    if (__op__ > 3 or __op__ < 0):
                        print('\033[31mTente escolher uma opção válida')
                    else:
                        if (__op__ == 1):
                            print('Menu do BD')
                            self.OP_Bd

                        elif (__op__ == 2):

                            self.OP_Calculos

                        else:
                            __op__ = 0
                            self.system('cls')


class Calculos(Main):
    pass


if __name__ == '__main__':
    __c__ = Calculos()
    __c__.main
    # Consult().__C__()

from abc import ABC, abstractmethod
from __erros__.__err import ConectionsErrors
from Conections__.Types.PyMySQL.__pyM__ import Conections
from Conections__.Types.SQLAlchemy__.__SQLAl__ import Conections


class CRUDUpdate__:
    class CRUDUPDATE(object):
        class Update(object):
            """ Irá atualizar os dados na base de dados Mysql """

            def __Up__(self):
                con = Conections().DBPy
                try:
                    with con.cursor() as cursor:
                        try:
                            cursor.execute('''select ifnull(__s__.number1, '0') as number1 , ifnull(__s__.number2, '0') as number2, ifnull(__s__.Soma, '0') as Soma, 
                                           ifnull(__sub__.number1, '0') as number, ifnull(__sub__.number2, '0') as number2, ifnull(__sub__.Subtracao, '0') as Subtracao, 
                                            ifnull(__p__.number1, '0') as number1, ifnull(__p__.number2, '0') as number2, ifnull(__p__.Produto, '0') as Produto,
                                             ifnull(__d__.number1, '0') as number1, ifnull(__d__.number2, '0') as number2, ifnull(__d__.Divisao, '0') as Divisao
                                                from Soma __s__
                                                    left join Subtracao __sub__
                                                    on __s__.id=__sub__.id
                                                    left join Divisao __d__
                                                    on __s__.id=__d__.id
                                                    left join Produto __p__
                                                    on __s__.id=__p__.id
                            ''')
                            __cur__ = cursor.fetchall()
                            for __c__ in __cur__:
                                print(__c__)
                        except:
                            print(
                                '\033[31mNão foi possível consultar os dados do bd\033[m')
                        else:
                            print('Dados consultados com sucesso')
                except:
                    print('\033[31mHouve um pequeno error\033[m')
                __op__ = 1
                while (__op__ > 0):
                    print('\n\033[34m[1]\033[m - \033[36mSomar:\033[36m\n\033[34m[2]\033[m - \033[36mSubtrair:\033[m\n\033[34m[3]\033[m - \033[36mProduto\033[m\n\033[34m[4]\033[m - \033[36mDivisão:\033[m\n\033[34m[5]\033[m - \033[36mSair:\033[m')

                    try:
                        __op__ = int(input('Digite a sua opção: \033[36m'))
                        print('\033[m')
                    except ValueError:
                        print(
                            '\033[31mHouve um erro de tipo, tente novamente\033[m')

                    try:
                        __n1__ = int(input('Digite o 1° Número: \033[36m'))
                        print('\033[m')
                    except ValueError:
                        print('\033[31mNúmero incorreto\033[m')

                    try:
                        __n2__ = int(input('Digite o 2° Número: \033[36m'))
                        print('\033[m')
                    except ValueError:
                        print('\033[31mNúmero incorreto')

                    if (__op__ < 0 or __op__ > 5):
                        print('\033[31mEscolha errada, tente novamente\033[m')
                    else:
                        if (__op__ == 1):
                            try:
                                with con.cursor() as cursor:
                                    try:
                                        cursor.execute('select * from Soma')
                                        __cur__ = cursor.fetchall()
                                    except:
                                        print(
                                            '\033[31mNão foi possível consultar os dados no BD\033[m')
                                    else:
                                        print('Dados consultados com sucesso')
                                    for __c__ in __cur__:
                                        print(f'\033[33m{__c__}\033[m')
                            except:
                                print('\033[31mHouve um pequeno erro\033[m')
                            try:
                                __id__ = int(
                                    input('\nDigite o seu ID referente a sua operação a ser atualizada: \033[36m'))
                                print('\033[m')
                            except ValueError:
                                print('\033[31mHouve um erro de tipo\033[m')
                            try:
                                __res__ = __n1__ + __n2__
                            except ArithmeticError:
                                print(
                                    '\033[31mHouve um pequeno erro no cálculo\033[m')
                            try:
                                with con.cursor() as cursor:
                                    try:
                                        cursor.execute(
                                            f'UPDATE soma SET number1 = {__n1__} WHERE id={__id__}')
                                        con.commit()
                                        cursor.execute(
                                            f'UPDATE soma SET number2 = {__n2__} WHERE id = {__id__} ')
                                        con.commit()
                                        cursor.execute(
                                            f'UPDATE soma SET Soma = {__res__} WHERE id = {__id__} ')
                                        con.commit()
                                    except:
                                        print(
                                            '\033[31mNão foi possível atualizar os dados do bd\033[m')
                                    else:
                                        print('Dados atualizados com sucesso')
                            except:
                                print('\033[31mHouve um pequeno erro\033[m')

                        elif (__op__ == 2):
                            try:
                                with con.cursor() as cursor:
                                    try:
                                        cursor.execute(
                                            'select * from Subtracao')
                                        __cur__ = cursor.fetchall()
                                    except:
                                        print(
                                            '\033[31mNão foi possível consultar os dados no BD\033[m')
                                    else:
                                        print('Dados consultados com sucesso')
                                    for __c__ in __cur__:
                                        print(f'\033[33m{__c__}\033[m')
                            except:
                                print('\033[31mHouve um pequeno erro\033[m')
                            try:
                                __id__ = int(
                                    input('\nDigite o seu ID referente a sua operação a ser atualizada: \033[36m'))
                                print('\033[m')
                            except ValueError:
                                print('\033[31mHouve um erro de tipo\033[m')
                            try:
                                __res__ = __n1__ - __n2__
                            except ArithmeticError:
                                print(
                                    '\033[31mHouve um pequeno erro no cálculo\033[m')
                            try:
                                with con.cursor() as cursor:
                                    try:
                                        cursor.execute(
                                            f'UPDATE subtracao SET number1 = {__n1__} WHERE id = {__id__} ')
                                        con.commit()
                                        cursor.execute(
                                            f'UPDATE subtracao SET number2 = {__n2__} WHERE id = {__id__} ')
                                        con.commit()
                                        cursor.execute(
                                            f'UPDATE subtracao SET Subtracao = {__res__} WHERE id = {__id__} ')
                                        con.commit()
                                    except:
                                        print(
                                            '\033[31mNão foi possível atualizar os dados\033[m')
                                    else:
                                        print('Dados atualizados com sucesso')
                            except:
                                print('\033[31mHouve um pequeno Erro\033[m')

                        elif (__op__ == 3):
                            try:
                                with con.cursor() as cursor:
                                    try:
                                        cursor.execute('select * from Produto')
                                        __cur__ = cursor.fetchall()
                                    except:
                                        print(
                                            '\033[31mNão foi possível consultar os dados no BD\033[m')
                                    else:
                                        print('Dados consultados com sucesso')
                                    for __c__ in __cur__:
                                        print(f'\033[33m{__c__}\033[m')
                            except:
                                print('\033[31mHouve um pequeno erro\033[m')
                            try:
                                __id__ = int(
                                    input('\nDigite o seu ID referente a sua operação a ser atualizada: \033[36m'))
                                print('\033[m')
                            except ValueError:
                                print('\033[31mHouve um erro de tipo\033[m')
                            try:
                                __res__ = __n1__ * __n2__
                            except ArithmeticError:
                                print(
                                    '\033[31mHouve um pequeno erro no cálculo\033[m')
                            try:
                                with con.cursor() as cursor:
                                    try:
                                        cursor.execute(
                                            f'UPDATE produto SET number1 = {__n1__} WHERE id = {__id__} ')
                                        con.commit()

                                        cursor.execute(
                                            f'UPDATE produto SET number2 = {__n2__} WHERE id = {__id__} ')
                                        con.commit()
                                        cursor.execute(
                                            f'UPDATE produto SET Produto = {__res__} WHERE id = {__id__} ')
                                        con.commit()
                                    except:
                                        print(
                                            '\033[31mNão foi possível atualizar os dados\033[m')
                                    else:
                                        print('Dados atualizados com sucesso')
                            except:
                                print('\033[31mHouve um pequeno erro\033[m')

                        elif (__op__ == 4):
                            try:
                                with con.cursor() as cursor:
                                    try:
                                        cursor.execute('select * from Divisao')
                                        __cursor__ = cursor.fetchall()
                                    except:
                                        print(
                                            '\033[31mNão foi possível consultar os dados no BD\033[m')
                                    else:
                                        print('Dados consultados com sucesso')
                                    for __c__ in __cursor__:
                                        print(f'\033[33m{__c__}\033[m')
                            except:
                                print('\033[31mHouve um peqeuno erro\033[m')
                            try:
                                __id__ = int(
                                    input('\nDigite o seu ID referente a sua operação a ser atualizada: \033[36m'))
                                print('\033[m')
                            except ValueError:
                                print(
                                    '\033[31mErro na hora de colocar id certo\033[31m')
                            try:
                                __res__ = __n1__ / __n2__
                            except ArithmeticError:
                                print(
                                    '\033[31mHouve um pequeno erro no cálculo\033[m')
                            try:
                                with con.cursor() as cursor:
                                    try:
                                        cursor.execute(
                                            f'UPDATE divisao SET number1={__n1__} WHERE id={__id__}')
                                        con.commit()
                                        cursor.execute(
                                            f'UPDATE divisao SET number2 = {__n2__} WHERE id = {__id__} ')
                                        con.commit()
                                        cursor.execute(
                                            f'UPDATE divisao SET Divisao = {__res__} WHERE id = {__id__} ')
                                        con.commit()
                                    except:
                                        print(
                                            '\033[31mNão foi possível atualizar os dados\033[m')
                                    else:
                                        print('Dados atualizados com sucesso')
                            except:
                                print('\033[31mHouve um peqeuno erro\033[m')
                        else:
                            __op__ = 0

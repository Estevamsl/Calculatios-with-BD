from __cruds__.__consult__.consult__ import CRUDConsult__
from __cruds__.Delete__.delete__ import CRUDDelete__
from __cruds__.__insert__.insert__ import CRUDInsert__
from __cruds__.__update__.update__ import CRUDUpdate__
from __cruds__.__create__.create__ import CRUDCreate__

from __interfaces__.interface__ import interface

from __Methods__.__mixins import Mixin
from __Methods__.__calculatioMIXIN import __MixinCalculadora__

# BASE = declarative_base()


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
                # super().somar(__n1__, __n2__)
                CRUDInsert__().CRUDINSERT().Insert().__SUM__(__n1__, __n2__)
                # CRUDConsult__().
                # self.system('cls')
            elif (__op__ == 2):
                super().subtrair(__n1__, __n2__)
                CRUDInsert__().CRUDINSERT().Insert().__SUB__(__n1__, __n2__)
                # self.system('cls')
            elif (__op__ == 3):
                super().produto(__n1__, __n2__)
                CRUDInsert__().CRUDINSERT().Insert().__PRO__(__n1__, __n2__)
                # self.system('cls')
            elif (__op__ == 4):
                super().dividir(__n1__, __n2__)
                CRUDInsert__().CRUDINSERT().Insert().__DIV__(__n1__, __n2__)
                # self.system('cls')
            else:
                __op__ = 0
                self.system('cls')

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
                    # self.system('cls')
                    print('\033[34m[1]\033[m - \033[36mSomar:\033[36m\n\033[34m[2]\033[m - \033[36mSubtrair:\033[m\n\033[34m[3]\033[m - \033[36mProduto\033[m\n\033[34m[4]\033[m - \033[36mDivisão:\033[m')

                    try:
                        __op__ = int(input('Digite a sua opção: \033[30m'))
                        print('\033[m')
                    except ValueError:
                        print(
                            "\033[31mErr de tipo, favor tentar novamente\033[m")

                    if (__op__ == 1):
                        pass
                        CRUDConsult__().CRUDCONSULT().Consult().Consult_Por_Operacao().__sm__
                    elif (__op__ == 2):
                        pass
                        CRUDConsult__().CRUDCONSULT().Consult().Consult_Por_Operacao().__sb__
                    elif (__op__ == 3):
                        pass
                        CRUDConsult__().CRUDCONSULT().Consult().Consult_Por_Operacao().__pro__
                    elif (__op__ == 4):
                        pass
                        CRUDConsult__().CRUDCONSULT().Consult().Consult_Por_Operacao().__di__
                    elif (__op__ == 5):
                        __op__ = 0

                    # CRUDConsult__().CRUDCONSULT().Consult().__C__
                    pass
                elif (__op__ == 2):
                    # self.system('cls')
                    print('Insere aqui no seu BD')
                    CRUDInsert__().CRUDINSERT().Insert().__SUM__(1, 2)
                    CRUDInsert__().CRUDINSERT().Insert().__SUB__(1, 2)
                    CRUDInsert__().CRUDINSERT().Insert().__PRO__(1, 2)
                    CRUDInsert__().CRUDINSERT().Insert().__DIV__(1, 2)
                    pass
                elif (__op__ == 3):
                    # self.system('cls')
                    # A classe CRUDUpdate__() irá fazer todo o seu trabalho
                    CRUDUpdate__().CRUDUPDATE().Update().__Up__()
                    pass
                elif (__op__ == 4):
                    # self.system('cls')
                    print('Deleta seu dados aqui no BD')
                    CRUDDelete__().CRUDDELL().Dell().__D__(1)
                    pass
                else:
                    __op__ = 0
                    self.system('cls')

    @property
    def main(self) -> any:
        pass
        __op__ = 1
        while (__op__ != 0):
            self.__prin__  # Menu Principal

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

from abc import ABC, abstractmethod
from __interfaces__.interface__ import interface


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

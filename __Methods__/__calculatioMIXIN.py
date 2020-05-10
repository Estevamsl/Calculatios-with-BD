from __Methods__.__mixins import Mixin


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

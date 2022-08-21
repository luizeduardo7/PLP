import abc
class Pessoa(abc.ABC):
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    @abc.abstractmethod
    def definir_id(self, id):
        pass


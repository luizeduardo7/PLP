from pessoa import Pessoa

class Medico(Pessoa):
    def __init__(self, nome):
        super().__init__(nome)

    def definir_id(self, id):
        if(len(id) <= 3):
            self.id = id
        else:
            print('O ID deve ter no máximo 3 caracteres alfa-numéricos')

    def nome_medico(self):
        return super().nome



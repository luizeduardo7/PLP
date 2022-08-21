from pessoa import Pessoa

class Paciente(Pessoa):
    __qtd_paciente = 0
    def __init__(self, nome):
        super().__init__(nome)
        Paciente.__qtd_paciente += 1
    
    def __del__(self):
        Paciente.__qtd_paciente -= 1
    
    def definir_id(self, id):
        if(len(id) <= 5):
            self.id = id
        else:
            print('O ID deve ter no máximo 5 caracteres alfa-numéricos')
    
    def definir_prontuario(self, prontuario):
        self.prontuario = prontuario

    def pacientes_ativos():
        return Paciente.__qtd_paciente

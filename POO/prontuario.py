from datetime import datetime
from medicamento import Medicamento
from medico import Medico

class Prontuario:
    __registro = list()
    def __init__(self):
        self.__registro = []
    
    def insere_procedimento(self, medicamento, posologia, medico, str_date, str_hora):
        
        date = datetime.strptime(str_date, '%d-%m-%Y').date()
        hour = datetime.strptime(str_hora, '%H:%M').time()
        self.str_date = str(date)
        self.str_hora = str(hour)
        self.medicamento = Medicamento.nome_medicamento(medicamento)
        self.posologia = posologia
        self.medico = Medico.nome_medico(medico)

        dados = dict()
        dados = {'medicamento': self.medicamento , 'posologia': self.posologia, 'medico': self.medico,
        'data': self.str_date, 'hora': self.str_hora}

        self.__registro.append(list(dados.values()))

    def exibe_prontuario(self):
        for i in self.__registro:
            print(*i, sep = ' - ')
            

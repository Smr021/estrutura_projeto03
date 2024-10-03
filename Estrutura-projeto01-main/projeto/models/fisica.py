from abc                               import ABC, abstractmethod
from projeto.models.pessoa             import Pessoa
from projeto.models.endereco           import Endereco
from projeto.models.enums.sexo         import Sexo
from projeto.models.enums.estadoCivil  import EstadoCivil

@abstractmethod
class Fisica(Pessoa,ABC):
    def __init__(self,id:str,nome:str,telefone:str,email:str,
                 endereco: Endereco,
                 sexo: Sexo ,
                 estadoCivil:EstadoCivil, 
                 dataNascimento: str ) -> None:
        super().__init__(id ,nome ,telefone ,email ,sexo ,endereco )
        self.sexo           = sexo
        self.estadoCivil    = estadoCivil
        self.dataNascimento = self._verificar_dataNascimento(dataNascimento)

    def _verificar_dataNascimento(self,valor):
        '''Método para verificação de data de nascimento'''
        self._verificar_dataNascimento_tipo_invalido(valor)
        self._verificar_dataNascimento_vazio_invalido(valor)


        self.dataNascimento = valor
        return self.dataNascimento


    def _verificar_dataNascimento_tipo_invalido(self,valor):
        """Método para verificação de data de nascimento invalido"""
        if not isinstance (valor,str):
            raise TypeError('A data de nascimento deve ser um texto.')

    def _verificar_dataNascimento_vazio_invalido(self,valor):
         if not valor.strip(): 
             raise TypeError('A data de nascimento não pode estar vazio.')


    def __str__(self) -> str:
        return (
            f"{super().__str__()}"
            f"\nCPF: {self.cpf}"
            f"\nRG: {self.rg}"
            f"\nData de nascimento: {self.dataNascimento}"
            f"\nSexo: {self.sexo.value}"
            )  
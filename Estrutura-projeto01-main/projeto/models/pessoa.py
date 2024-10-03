from abc import ABC, abstractmethod
from projeto.models.enums.sexo import Sexo
from projeto.models.endereco import Endereco

@abstractmethod
class Pessoa(ABC):
    def __init__(self,id:int,nome:str,telefone:str,email:str,sexo:Sexo, endereco:Endereco) -> None:
        self.id       = self._verificar_id(id)
        self.nome     = self._verificar_nome(nome)
        self.telefone = self._verificar_telefone(telefone)
        self.email    = self._verificar_email(email)
        self.sexo     = sexo
        self.endereco = Endereco

    def _verificar_nome(self,valor):
        self._verificar_nome_invalido(valor)
        self._verificar_nome_tipo_vazio_invalido(valor)

        self.nome = valor
        return self.nome
    
    def _verificar_id(self,valor):
        self._verificar_id_invalido(valor)
        self._verificar_id_tipo_vazio_invalido(valor)
        self._verificar_id_negativa(valor)
        

        self.id = valor
        return self.id
    
    def _verificar_telefone(self,valor):
        self._verificar_telefone_invalido(valor)
        self._verificar_telefone_tipo_vazio_invalido(valor)

        self.telefone = valor
        return self.telefone
    
    def _verificar_email(self,valor):
        self._verificar_email_invalido(valor)
        self._verificar_email_tipo_vazio_invalido(valor)

        self.email = valor
        return self.email
    


    def _verificar_id_invalido(self,valor):
         if not isinstance (valor,int):
             raise TypeError('O id deve ser um inteiro.')
        
    def _verificar_id_tipo_vazio_invalido(self,valor):
         if valor == None: 
             raise TypeError('O id não pode estar vazio.')
         
    def _verificar_id_negativa(self,valor):
         if valor < 0:
             raise ValueError("A idade não pode ser negativa ")
    
    def _verificar_nome_invalido(self,valor):
         if not isinstance (valor,str):
             raise TypeError('O nome deve ser um texto.')
        
    def _verificar_nome_tipo_vazio_invalido(self,valor):
         if not valor.strip(): 
             raise TypeError('O nome não pode estar vazio.')

    def _verificar_telefone_invalido(self,valor):
         if not isinstance (valor,str):
             raise TypeError('O telefone deve ser um texto.')
        
    def _verificar_telefone_tipo_vazio_invalido(self,valor):
         if not valor.strip(): 
             raise TypeError('O telefone não pode estar vazio.')

    def _verificar_email_invalido(self,valor):
         if not isinstance (valor,str):
             raise TypeError('O email deve ser um texto.')
        
    def _verificar_email_tipo_vazio_invalido(self,valor):
         if not valor.strip(): 
             raise TypeError('O email não pode estar vazio.')


    def __str__(self) -> str:
        return (
            f"\n Nome: {self.nome}"
            f"\n Idade: {self.idade}"
            f"\n Sexo: {self.sexo}"
            )
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # def _verificar_idade(self,valor):
    #     self._verificar_idade_tipo_invalido(valor)
    #     self._verificar_idade_negativa(valor)
    #     self._verificar_idade_acima_de_130(valor)

    #     self.idade = valor
    #     return self.idade


    # def _verificar_idade_tipo_invalido(self,valor):
    #     if not isinstance(valor,int):
    #         raise TypeError("A idade de ser um numero inteiro. ")
    
    # def _verificar_idade_negativa(self,valor):
    #     if valor < 0:
    #         raise ValueError("A idade não pode ser negativa ")

    # def _verificar_idade_acima_de_130(self,valor):
    #      if valor > 130:
    #         raise ValueError("A idade não pode ser acima de 130 anos ")
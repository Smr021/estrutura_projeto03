from projeto.models.funcionario        import Funcionario
from projeto.models.endereco           import Endereco
from projeto.models.enums.sexo         import Sexo
from projeto.models.enums.estadoCivil  import EstadoCivil
from projeto.models.enums.setor        import Setor

class Engenheiro(Funcionario):
    def __init__(self,id:str,nome:str,telefone:str,email:str,
                 endereco: Endereco,
                 sexo: Sexo ,
                 estadoCivil:EstadoCivil, 
                 dataNascimento: str ,cpf:str,rg:str,matricula:str,setor:Setor,salario:float) -> None:
        super().__init__(id, nome ,telefone ,email ,endereco ,sexo ,estadoCivil ,dataNascimento)
        self.crea = self._verificar_crea(crea)

    def _verificar_crea(self,valor):
        '''Método para verificação do CREA'''
    

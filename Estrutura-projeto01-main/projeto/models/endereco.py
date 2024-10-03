from projeto.models.enums.unidadeFederativa import UnidadeFederativa

class Endereco():
    def __init__(self, logradouro: str, numero: int, complamento: str, cep: str, cidade: str, uf: UnidadeFederativa) -> None:
        self.lougradouro = self._verificar_logradouro(logradouro)
        self.numero      = self._verificar_numero(numero)
        self.complemento = self._verificar_complemento(complamento)
        self.cep         = self._verificar_cep(cep)
        self.cidade      = self._verificar_cidade(cidade)
        self.uf          = uf

    
    def _verificar_logradouro(self,valor):
        self._verificar_logradouro_invalido(valor)
        self._verificar_logradouro_tipo_vazio_invalido(valor)

        self.logradouro = valor
        return self.logradouro
    
    
    def _verificar_numero(self,valor):
        self._verificar_numero_vazio(valor)

        self.numero = valor
        return self.numero
    
    
    def _verificar_complemento(self,valor):
        self._verificar_complemento_invalido(valor)
        self._verificar_complemento_vazio_invalido(valor)

        self.complemento = valor
        return self.complemento
    
    
    def _verificar_cep(self,valor):
        self._verificar_cep_vazio_invalido(valor)

        self.cep = valor
        return self.cep
    
    
    def _verificar_cidade(self,valor):
        self._verificar_cidade_invalido(valor)
        self._verificar_cidade_vazio_invalido(valor)

        self.cidade = valor
        return self.cidade
    
    
    def _verificar_logradouro_invalido(self,valor):
         if not isinstance (valor,str):
             raise TypeError('O logradouro deve ser um texto.')
        
    def _verificar_logradouro_tipo_vazio_invalido(self,valor):
         if not valor.strip(): 
             raise TypeError('O logradouro não pode estar vazio.')
#==================================================================
    
    def _verificar_numero_vazio(self,valor):
        if not valor.strip(): 
            raise TypeError('O numero não pode estar vazio.')
        
 #==================================================================   
    
    def _verificar_complemento_invalido(self,valor):
        if not isinstance (valor,str):
            raise TypeError('O complemento deve ser um texto.')
        
    def _verificar_complemento_vazio_invalido(self,valor):
        if not valor.strip(): 
            raise TypeError('O complemento não pode estar vazio.')
#==================================================================
    
    
        
    def _verificar_cep_vazio_invalido(self,valor):
        if not valor.strip(): 
            raise TypeError('O cep não pode estar vazio.')
#==================================================================
    
    def _verificar_cidade_invalido(self,valor):
        if not isinstance (valor,str):
            raise TypeError('A cidade deve ser um texto.')
        
    def _verificar_cidade_vazio_invalido(self,valor):
        if not valor.strip(): 
            raise TypeError('A cidade não pode estar vazio.')
#==================================================================


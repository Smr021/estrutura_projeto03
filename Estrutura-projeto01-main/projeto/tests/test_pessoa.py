import pytest
from projeto.models.pessoa import Pessoa
from projeto.models.enums.sexo import Sexo
from projeto.models.enums.unidadeFederativa import UnidadeFederativa
from projeto.models.endereco import Endereco


@pytest.fixture
def pessoa_valida():
    # Instanciando classe pessoa.
    pessoa = Pessoa(515 ,'Gabriel Fuboca','71555-9555','gabriel.fuboca@gmail.com'
                    ,Sexo.MASCULINO,
                    Endereco('Rua A', '33','logo ali', '45658-565','salvador'
                             ,UnidadeFederativa.SAO_PAULO))
    return pessoa

def test_id_valido(pessoa_valida):
    assert pessoa_valida.id == 515

def test_nome_valido(pessoa_valida):
    assert pessoa_valida.nome == "Gabriel Fuboca"

def test_telefone_valido(pessoa_valida):
    assert pessoa_valida.telefone == '71555-9555'    

def test_email_valido(pessoa_valida):
    assert pessoa_valida.email == 'gabriel.fuboca@gmail.com'    


def test_verificar_id_invalido():
    with pytest.raises(TypeError,match='O id deve ser um inteiro.'):
        Pessoa("515",'Gabriel Fuboca','71555-9555','gabriel.fuboca@gmail.com'
                    ,Sexo.MASCULINO,
                    Endereco('Rua A', '33','logo ali', '45658-565','salvador'
                             ,UnidadeFederativa.SAO_PAULO))

def test_verificar_id_tipo_vazio_invalido():
    with pytest.raises(TypeError,match= 'O id deve ser um inteiro.'):
        Pessoa(None,'Gabriel Fuboca','71555-9555','gabriel.fuboca@gmail.com'
                    ,Sexo.MASCULINO,
                    Endereco('Rua A', '33','logo ali', '45658-565','salvador'
                             ,UnidadeFederativa.SAO_PAULO))

def test_verificar_nome_invalido():
    with pytest.raises(TypeError,match='O nome deve ser um texto.'):
        Pessoa(515,55,'71555-9555','gabriel.fuboca@gmail.com'
                    ,Sexo.MASCULINO,
                    Endereco('Rua A', '33','logo ali', '45658-565','salvador'
                             ,UnidadeFederativa.SAO_PAULO))

def test_verificar_nome_tipo_vazio_invalido():
    with pytest.raises(TypeError,match= 'O nome não pode estar vazio.'):
        Pessoa(515,'','71555-9555','gabriel.fuboca@gmail.com'
                    ,Sexo.MASCULINO,
                    Endereco('Rua A', '33','logo ali', '45658-565','salvador'
                             ,UnidadeFederativa.SAO_PAULO))


def test_verificar_telefone_invalido():
    with pytest.raises(TypeError,match='O telefone deve ser um texto.'):
        Pessoa(515,'Gabriel Fuboca',71598959,'gabriel.fuboca@gmail.com'
                    ,Sexo.MASCULINO,
                    Endereco('Rua A', '33','logo ali', '45658-565','salvador'
                             ,UnidadeFederativa.SAO_PAULO))

def test_verificar_telefone_tipo_vazio_invalido():
    with pytest.raises(TypeError,match= 'O telefone não pode estar vazio.'):
                Pessoa(515,'Gabriel Fuboca','','gabriel.fuboca@gmail.com'
                    ,Sexo.MASCULINO,
                    Endereco('Rua A', '33','logo ali', '45658-565','salvador'
                             ,UnidadeFederativa.SAO_PAULO))

 

def test_verificar_email_invalido():
    with pytest.raises(TypeError,match='O email deve ser um texto.'):
                Pessoa(515,'Gabriel Fuboca','71555-9555',555
                    ,Sexo.MASCULINO,
                    Endereco('Rua A', '33','logo ali', '45658-565','salvador'
                             ,UnidadeFederativa.SAO_PAULO))


def test_verificar_email_tipo_vazio_invalido():
    with pytest.raises(TypeError,match= 'O email não pode estar vazio.'):
                Pessoa(515,'Gabriel Fuboca','71555-9555',''
                    ,Sexo.MASCULINO,
                    Endereco('Rua A', '33','logo ali', '45658-565','salvador'
                             ,UnidadeFederativa.SAO_PAULO))













































# def test_pessoa_mudar_nome_valido(pessoa_valida):
#     assert pessoa_valida.nome == 'Marta'

# def test_pessoa_idade_valida(pessoa_valida):
#     assert pessoa_valida.idade == 22
 

 
# def test_pessoa_idade_negativa():
#     with pytest.raises(ValueError, match="A idade não pode ser negativa "):
#         Pessoa("Marta",-23,Sexo.FEMININO)

# def test_idade_acima_de_130_retorna_mensagem():
#     with pytest.raises(ValueError, match="A idade não pode ser acima de 130 anos "):
#         Pessoa("Marta",131,Sexo.FEMININO)

# def test_pessoa_idade_tipo_invalido_retorna_mensagem_erro():
#     with pytest.raises(TypeError, match="A idade de ser um numero inteiro. "):
#         Pessoa("Marta","131",Sexo.FEMININO)


#     # assert verificação usa como verdade o que foi estabelicido
#     # quando quiser testar o codigo. digite no terminal: pytest

import pytest
from projeto.models.endereco import Endereco
from projeto.models.enums.unidadeFederativa import UnidadeFederativa

# Boas práticas de progamação.
@pytest.fixture
def endereco_valido():
    endereco = Endereco('Rua A', '33','logo ali', '45658-565','salvador',
                        UnidadeFederativa.SAO_PAULO)
    return endereco

def test_logradouro_valido(endereco_valido):
    assert endereco_valido.logradouro == 'Rua A'    

def test_numero_valido(endereco_valido):
    assert endereco_valido.numero == '33'

def test_complemento_valido(endereco_valido):
    assert endereco_valido.complemento == 'logo ali'

def test_cep_valido(endereco_valido):
    assert endereco_valido.cep == '45658-565'

def test_cidade_valido(endereco_valido):
    assert endereco_valido.cidade == 'salvador'



def test_verificar_logradouro_invalido():
    with pytest.raises(TypeError,match='O logradouro deve ser um texto.'):
        Endereco(44, '33','logo ali', '45658-565','salvador',UnidadeFederativa.SAO_PAULO)


def test_verificar_logradouro_tipo_vazio_invalido():
    with pytest.raises(TypeError,match= 'O logradouro não pode estar vazio.'):
        Endereco("",'33','logo ali','45658-565','salvador',UnidadeFederativa.SAO_PAULO)


def test_verificar_numero_vazio():
    with pytest.raises(TypeError,match='O numero não pode estar vazio.'):
        Endereco('Rua A', '','logo ali', '45658-565','salvador',UnidadeFederativa.SAO_PAULO)


def test_verificar_complemento_invalido():
    with pytest.raises(TypeError,match='O complemento deve ser um texto.'):
        Endereco('Rua A', '33',55, '45658-565','salvador',UnidadeFederativa.SAO_PAULO)

def test_verificar_complemento_vazio_invalido():
    with pytest.raises(TypeError,match='O complemento não pode estar vazio.'):
        Endereco('Rua A', '33','', '45658-565','salvador',UnidadeFederativa.SAO_PAULO)

def test_verificar_cep_vazio_invalido():
    with pytest.raises(TypeError,match='O cep não pode estar vazio.'):
        Endereco('Rua A', '33','logo ali', '','salvador',UnidadeFederativa.SAO_PAULO)

def test_verificar_cidade_invalido():
    with pytest.raises(TypeError,match='A cidade deve ser um texto.'):
        Endereco('Rua A', '33','logo ali', '45658-565',99,UnidadeFederativa.SAO_PAULO)

def test_verificar_cidade_vazio_invalido():
    with pytest.raises(TypeError,match='A cidade não pode estar vazio.'):
        Endereco('Rua A', '33','logo ali', '45658-565','',UnidadeFederativa.SAO_PAULO)



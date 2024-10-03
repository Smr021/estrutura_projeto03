import pytest
from projeto.models.fisica import Fisica
from projeto.models.endereco import Endereco
from projeto.models.enums.unidadeFederativa import UnidadeFederativa
from projeto.models.enums.sexo import Sexo
from projeto.models.enums.estadoCivil import EstadoCivil

# Boas práticas de progamação.
@pytest.fixture
def fisica_valida():
    fisica = Fisica(515,'Gabriel Fuboca','71555-9555','gabriel.fuboca@gmail.com',
                    Endereco('Rua A', '33','logo ali', '45658-565','salvador',
                             UnidadeFederativa.SAO_PAULO),
                             Sexo.MASCULINO,
                             EstadoCivil.SOLTEIRO,'25/10/2005')
    return fisica

def test_verificar_dataNascimento_tipo_invalido(fisica_valida):
    assert fisica_valida.dataNascimento == '25/10/2005'

def test_verificar_dataNascimento_tipo_invalido():
    with pytest.raises(TypeError,match = 'A data de nascimento deve ser um texto.'):
        Fisica(515,'Gabriel Fuboca','71555-9555','gabriel.fuboca@gmail.com',
                    Endereco('Rua A', '33','logo ali', '45658-565','salvador',
                             UnidadeFederativa.SAO_PAULO),
                             Sexo.MASCULINO,
                             EstadoCivil.SOLTEIRO,55)

def test_verificar_dataNascimento_vazio_invalido():
    with pytest.raises(TypeError,match = 'A data de nascimento não pode estar vazio.'):
        Fisica(515,'Gabriel Fuboca','71555-9555','gabriel.fuboca@gmail.com',
                    Endereco('Rua A', '33','logo ali', '45658-565','salvador',
                             UnidadeFederativa.SAO_PAULO),
                             Sexo.MASCULINO,
                             EstadoCivil.SOLTEIRO,'')
    


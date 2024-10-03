import pytest
from projeto.models.funcionario import Funcionario
from projeto.models.endereco import Endereco
from projeto.models.enums.unidadeFederativa import UnidadeFederativa
from projeto.models.enums.sexo import Sexo
from projeto.models.enums.estadoCivil import EstadoCivil
from projeto.models.enums.setor import Setor

# Boas práticas de progamação.
@pytest.fixture
def funcionario_valido():
    funcionario = Funcionario(515,'Gabriel Fuboca','71555-9555','gabriel.fuboca@gmail.com',
                    Endereco('Rua A', '33','logo ali', '45658-565','salvador',
                             UnidadeFederativa.SAO_PAULO),
                             Sexo.MASCULINO,
                             EstadoCivil.SOLTEIRO,55,
                             '956.745.558-78',
                             '15.457.598-74',
                             '0101',
                             Setor.ENGENHARIA,1000)
    return funcionario

#===============================================================================================

def test_verificar_cpf_tipo_invalido(funcionario_valido):
    assert funcionario_valido.cpf == '956.745.558-78'

def test_verificar_rg_tipo_invalido(funcionario_valido):
    assert funcionario_valido.rg == '15.457.598-74'

def test_verificar_matricula_tipo_invalido(funcionario_valido):
    assert funcionario_valido.matricula == '0101'

def test_verificar_salario_tipo_invalido(funcionario_valido):
    assert funcionario_valido.salario == 1000



def test_verificar_cpf_tipo_invalido():
    with pytest.raises(TypeError,match = 'O CPF deve ser um texto.'):
        Funcionario(515,'Gabriel Fuboca','71555-9555','gabriel.fuboca@gmail.com',
                    Endereco('Rua A', '33','logo ali', '45658-565','salvador',UnidadeFederativa.SAO_PAULO),Sexo.MASCULINO,EstadoCivil.SOLTEIRO,'25/10/2005',00,'15.457.598-74','0101',Setor.ENGENHARIA,1000)

def test_verificar_cpf_vazio_invalido():
    with pytest.raises(TypeError,match = 'O CPF não pode estar vazio.'):
        Funcionario(515,'Gabriel Fuboca','71555-9555','gabriel.fuboca@gmail.com',
                    Endereco('Rua A', '33','logo ali', '45658-565','salvador',
                             UnidadeFederativa.SAO_PAULO),
                             Sexo.MASCULINO,
                             EstadoCivil.SOLTEIRO,'25/10/2005',
                             '',
                             '15.457.598-74',
                             '0101',
                             Setor.ENGENHARIA,1000)
        


#===============================================================================================




def test_verificar_rg_tipo_invalido():
    with pytest.raises(TypeError,match = 'O RG deve ser um texto.'):
        Funcionario(515,'Gabriel Fuboca','71555-9555','gabriel.fuboca@gmail.com',
                    Endereco('Rua A', '33','logo ali', '45658-565','salvador',
                             UnidadeFederativa.SAO_PAULO),
                             Sexo.MASCULINO,EstadoCivil.SOLTEIRO,
                             '25/10/2005',"956.745.558-78",00,'0101',Setor.ENGENHARIA,1000)

def test_verificar_rg_vazio_invalido():
    with pytest.raises(TypeError,match = 'O RG não pode estar vazio.'):
        Funcionario(515,'Gabriel Fuboca','71555-9555','gabriel.fuboca@gmail.com',
                    Endereco('Rua A', '33','logo ali', '45658-565','salvador',
                             UnidadeFederativa.SAO_PAULO),
                             Sexo.MASCULINO,
                             EstadoCivil.SOLTEIRO,'25/10/2005',
                             '956.745.558-78',
                             '',
                             '0101',
                             Setor.ENGENHARIA,1000)

#===============================================================================================

def test_verificar_matricula_tipo_invalido():
    with pytest.raises(TypeError,match = 'A Matricula deve ser um texto.'):
        Funcionario(515,'Gabriel Fuboca','71555-9555','gabriel.fuboca@gmail.com',
                    Endereco('Rua A', '33','logo ali', '45658-565',
                             'salvador',UnidadeFederativa.SAO_PAULO),
                             Sexo.MASCULINO,EstadoCivil.SOLTEIRO,
                             '25/10/2005',"956.745.558-78",'15.457.598-74',000,Setor.ENGENHARIA,1000)

def test_verificar_matricula_vazio_invalido():
    with pytest.raises(TypeError,match = 'A Matricula não pode estar vazio.'):
        Funcionario(515,'Gabriel Fuboca','71555-9555','gabriel.fuboca@gmail.com',
                    Endereco('Rua A', '33','logo ali', '45658-565','salvador',
                             UnidadeFederativa.SAO_PAULO),
                             Sexo.MASCULINO,
                             EstadoCivil.SOLTEIRO,'25/10/2005',
                             '956.745.558-78',
                             '15.457.598-74',
                             '',
                             Setor.ENGENHARIA,1000)

#===============================================================================================
def test_verificar_salario_vazio_invalido():
    with pytest.raises(ValueError,match = 'O campo do salario não pode ser deixado em branco.'):
        Funcionario(515,'Gabriel Fuboca','71555-9555','gabriel.fuboca@gmail.com',
                    Endereco('Rua A', '33','logo ali', '45658-565','salvador',
                             UnidadeFederativa.SAO_PAULO),
                             Sexo.MASCULINO,
                             EstadoCivil.SOLTEIRO,'25/10/2005',
                             '956.745.558-78',
                             '15.457.598-74',
                             '0101',
                             Setor.ENGENHARIA,None)

def test_verificar_salario_tipo_invalido():
    with pytest.raises(TypeError,match = 'O salario deve ser um numero.'):
        Funcionario(515,'Gabriel Fuboca','71555-9555','gabriel.fuboca@gmail.com',
                    Endereco('Rua A', '33','logo ali', '45658-565','salvador',
                             UnidadeFederativa.SAO_PAULO),
                             Sexo.MASCULINO,EstadoCivil.SOLTEIRO,
                             '25/10/2005',"956.745.558-78",'15.457.598-74','0101',Setor.ENGENHARIA,"1000")





def test_verificar_salario_negativo_invalido():
    with pytest.raises(ValueError,match = 'O salario não pode ser negativo.'):
        Funcionario(515,'Gabriel Fuboca','71555-9555','gabriel.fuboca@gmail.com',
                    Endereco('Rua A', '33','logo ali', '45658-565','salvador',
                             UnidadeFederativa.SAO_PAULO),
                             Sexo.MASCULINO,
                             EstadoCivil.SOLTEIRO,'25/10/2005',
                             '956.745.558-78',
                             '15.457.598-74',
                             '0101',
                             Setor.ENGENHARIA,-1000)
        


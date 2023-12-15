from behave import given, when, then

from src.saude.test_medicamento import TestMedicamento
import time

teste = None

@given(u'dado as informações sobre um medicamento: {nome} e {descricao}')
def step_impl(context, nome, descricao):
    context.teste = TestMedicamento(nome, descricao)  
    time.sleep(5)
    
@when(u'eu clicar em Cadastrar Medicamento')
def step_impl(context):
    context.teste.executar_teste()
    time.sleep(8)

@then(u'as informações do medicamento são exibidas corretamente: {resultado}')
def step_impl(context, resultado):
    assert context.teste.nome_medicamento == resultado, f'[Falha] O teste deveria cadastrar: {resultado}'
    time.sleep(2)
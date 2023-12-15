from behave import given, when, then

from src.saude.test_procedimento import TestProcedimento
import time

teste = None

@given(u'dado as informações sobre um procedimento: {procedimento}, {numero} e {descricao}')
def step_impl(context, procedimento, numero, descricao):
    context.teste = TestProcedimento(procedimento, numero, descricao)  
    time.sleep(5)
    
@when(u'eu clicar em Cadastrar Procedimento')
def step_impl(context):
    context.teste.executar_teste()
    time.sleep(8)

@then(u'as informações do procedimento são exibidas corretamente: {procedimento}, {numero} e {descricao}')
def step_impl(context, procedimento, numero, descricao):
    assert context.teste.procedimento == procedimento, f'[Falha] O teste deveria cadastrar: {procedimento}'
    assert context.teste.numero_procedimento == numero, f'[Falha] O teste deveria cadastrar o nº: {numero}'
    assert context.teste.descricao_procedimento == descricao, f'[Falha] O teste deveria cadastrar a descrição: {descricao}'
    time.sleep(2)
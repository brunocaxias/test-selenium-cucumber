from behave import given, when, then

from src.saude.test_doenca_cronica import TestDoencaCronica
import time

teste = None

@given(u'dado as informações sobre uma doenca crônica: {nome} e {descricao}')
def step_impl(context, nome, descricao):
    context.teste = TestDoencaCronica(nome, descricao)  
    time.sleep(5)
    
@when(u'eu clicar em Cadastrar Doença Crônica')
def step_impl(context):
    context.teste.executar_teste()
    time.sleep(8)

@then(u'as informações da doença crônica são exibidas corretamente: {nome} e {descricao}')
def step_impl(context, nome, descricao):
    assert context.teste.nome_doenca == nome, f'[Falha] O teste deveria cadastrar: {nome}'
    assert context.teste.descricao_doenca == descricao, f'[Falha] O teste deveria cadastrar a descrição: {descricao}'
    time.sleep(2)
from behave import given, when, then

from src.test_deficiencia import TestDeficiencia
import time

testeDeficiencia = None

@given(u'dado as informações sobre uma deficiênca: {deficiencia} e {categoria}')
def step_impl(context, deficiencia, categoria):
    context.testeDeficiencia = TestDeficiencia(deficiencia, categoria)  
    time.sleep(5)
    
@when(u'eu clicar em Cadastrar Deficiência')
def step_impl(context):
    context.testeDeficiencia.executar_teste()
    time.sleep(8)


@then(u'as informações da deficiência são exibidas corretamente: {resultado}')
def step_impl(context, resultado):
    assert context.testeDeficiencia.nome_deficiencia == resultado, f'[Falha] O teste deveria cadastrar: {resultado}'
    time.sleep(2)
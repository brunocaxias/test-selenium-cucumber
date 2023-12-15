from behave import given, when, then

from src.test_categoria import TestCategoria
import time

testeCategoria  = None

@given(u'dado as informações sobre uma categoria deficiênca: {categoria}')
def step_impl(context, categoria):
    context.testeCategoria = TestCategoria(categoria)  
    time.sleep(5)
    
@when(u'eu clicar em {acao}')
def step_impl(context, acao):
    context.testeCategoria.executar_teste()
    time.sleep(8)


@then(u'as informações da deficiência são exibidas corretamente: {resultado}')
def step_impl(context):
    assert(context.testeCategoria.categoria)
    time.sleep(2)

# @given(u'eu tenho {nome} e {descricao}')
# def step_impl(context, nome, descricao):
#     context.testeCategoria = TestInsertCategoria(nome, descricao)
#     context.testeCategoria.abrir_site()
#     time.sleep(5)
    
# @when(u'eu clicar em {acao}')
# def step_impl(context, acao):

#     context.testeCategoria.click_create_row_button()
#     context.testeCategoria.preencher_formulario()
#     time.sleep(8)


# @then(u'o resultado será {resultado}')
# def step_impl(context):
#     context.testeCategoria.conferir_insercao()
#     time.sleep(2)
#     context.testeCategoria.fechar_navegador()




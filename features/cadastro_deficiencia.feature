Feature: Cadastro de Categoria

  Scenario Outline: Cadastrar uma categoria com sucesso
    Given dado as informações sobre uma categoria deficiênca: <categoria>
    When eu clicar em <acao>
    Then as informações da deficiência são exibidas corretamente: <resultado>
    Examples:
      |categoria        |acao                  |resultado|
      |Categoria Teste|Cadastrar categoria|Categoria Teste|
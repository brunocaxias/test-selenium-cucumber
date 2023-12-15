Feature: Cadastro de Categoria

  Scenario Outline: Cadastrar uma categoria com sucesso
    Given dado as informações sobre uma categoria deficiênca: <categoria>
    When eu clicar em Cadastrar Categoria
    Then as informações da categoria são exibidas corretamente: <resultado>
    Examples:
      |categoria        |resultado      |
      |Categoria Teste  |Categoria Teste|
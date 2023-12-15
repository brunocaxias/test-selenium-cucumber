Feature: Cadastro de doença crônica

  Scenario Outline: Cadastrar uma doença crônica com sucesso
    Given dado as informações sobre uma doenca crônica: <nome> e <descricao>
    When eu clicar em Cadastrar Doença Crônica
    Then as informações da doença crônica são exibidas corretamente: <nome> e <descricao>
    Examples:
      |nome        |descricao                |
      |Doença Teste|Descricao da Doença Teste|
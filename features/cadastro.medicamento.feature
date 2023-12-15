Feature: Cadastro de medicamento

  Scenario Outline: Cadastrar um medicamento com sucesso
    Given dado as informações sobre um medicamento: <nome> e <descricao>
    When eu clicar em Cadastrar Medicamento
    Then as informações do medicamento são exibidas corretamente: <resultado>
    Examples:
      |nome             |descricao                     |resultado        |
      |Medicamento Teste|Descricao do Medicamento Teste|Medicamento Teste|
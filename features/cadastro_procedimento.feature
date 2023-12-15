Feature: Cadastro de procedimento

  Scenario Outline: Cadastrar um procedimento
    Given dado as informações sobre um procedimento: <procedimento>, <numero> e <descricao>
    When eu clicar em Cadastrar Procedimento
    Then as informações do procedimento são exibidas corretamente: <procedimento>, <numero> e <descricao>
    Examples:
      |procedimento      |numero  |descricao                   |
      |Procedimento Teste|PROC-000|Descricao Procedimento Teste|
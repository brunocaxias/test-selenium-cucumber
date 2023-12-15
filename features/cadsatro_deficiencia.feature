Feature: Cadastro de deficiênca

  Scenario Outline: Cadastrar uma deficiênca com sucesso
    Given dado as informações sobre uma deficiênca: <deficiencia> e <categoria>
    When eu clicar em Cadastrar Deficiência
    Then as informações da deficiência são exibidas corretamente: <resultado>
    Examples:
      |deficiencia      |categoria      |resultado        |
      |Deficiência Teste|Categoria Teste|Deficiência Teste|
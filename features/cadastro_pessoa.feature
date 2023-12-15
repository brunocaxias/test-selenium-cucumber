Feature: Cadastro de Pessoa

  Scenario Outline: Cadastrar uma pessoa com sucesso
    Given  uma pessoa com <nome>, <CPF>, <email>, <dataNascimento>, <contato>, <RG>, <rendaFamiliar>, <etinia> e <sexo>
    When a pessoa é cadastrada
    Then o cadastro é bem-sucedido
    And as informações da pessoa são exibidas corretamente
    Examples:
      |nome        |CPF             |email           |dataNascimento   |contato          |RG         |rendaFamiliar|etinia |sexo       |
      |"João Silva"|"123.456.789-09"|"joão@email.com"|"01/01/1990"     |"(27) 91110-2223"|"0.000.000"|7800.00      |"PARDO"|"MASCULINO"|


  Scenario Outline: Associar uma pessoa a deficiência
    Given  uma pessoa com <nome>, <CPF>, <deficiencia> e <categoriaDeficiencia>
    When a pessoa já consta como cadastrada
    Then a associação é bem sucedidade
    And as informações da defificência da pessoa são exibidas corretamente
    Examples:
      |nome        |CPF             |deficiencia|categoriaDeficiencia|
      |"João Silva"|"123.456.789-09"|"Transtorno do Espectro Autista (TEA)"|"COGNITIVA"|
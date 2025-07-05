Feature: Cultivo de plantações

  Scenario: Plantar uma semente com sucesso
    Given o jogador tem 1 semente de cenoura no inventário
    And o terreno está arado
    When o jogador planta a semente
    Then a semente é removida do inventário
    And uma planta de cenoura é criada no terreno

  Scenario: Tentar plantar sem semente
    Given o jogador não tem sementes
    And o terreno está arado
    When o jogador tenta plantar
    Then uma mensagem de erro é exibida: "Você não tem sementes!"

  Scenario: Tentar plantar em terreno não arado
    Given o jogador tem 1 semente de milho no inventário
    And o terreno não está arado
    When o jogador tenta plantar
    Then uma mensagem de erro é exibida: "O terreno precisa estar arado!"

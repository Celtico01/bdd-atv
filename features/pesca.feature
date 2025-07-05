Feature: Sistema de pesca

  Scenario: Pescar com sucesso
    Given o jogador está ao lado de um lago
    And o jogador tem uma vara de pesca
    When o jogador lança a linha no lago
    Then um peixe é adicionado ao inventário

  Scenario: Tentar pescar sem vara
    Given o jogador está ao lado de um lago
    And o jogador não tem uma vara de pesca
    When o jogador tenta pescar
    Then uma mensagem de erro é exibida: "Você precisa de uma vara de pesca!"

  Scenario: Tentar pescar longe do lago
    Given o jogador está longe do lago
    And o jogador tem uma vara de pesca
    When o jogador tenta pescar
    Then uma mensagem de erro é exibida: "Você precisa estar próximo ao lago!"
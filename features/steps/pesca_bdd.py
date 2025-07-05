from behave import *
from logica_jogo.player import Player
from logica_jogo.terreno import Terreno

@given('o jogador está ao lado de um lago')
def step_impl(context):
    context.jogador = Player()
    context.jogador.proximo_ao_lago = True

@given('o jogador está longe do lago')
def step_impl(context):
    context.jogador = Player()
    context.jogador.proximo_ao_lago = False

@given('o jogador tem uma vara de pesca')
def step_impl(context):
    context.jogador.vara_pesca = True

@given('o jogador não tem uma vara de pesca')
def step_impl(context):
    context.jogador.vara_pesca = False

@when('o jogador lança a linha no lago')
@when('o jogador tenta pescar')
def step_impl(context):
    context.resultado = context.jogador.pescar()

@then('um peixe é adicionado ao inventário')
def step_impl(context):
    assert "peixe" in context.jogador.inventario

@then('uma mensagem de erro é exibida: "Você precisa de uma vara de pesca!"')
def step_impl(context):
    assert context.resultado == "Você precisa de uma vara de pesca!"

@then('uma mensagem de erro é exibida: "Você precisa estar próximo ao lago!"')
def step_impl(context):
    assert context.resultado == "Você precisa estar próximo ao lago!"
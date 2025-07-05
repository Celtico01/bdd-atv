from behave import *
from logica_jogo.player import Player
from logica_jogo.terreno import Terreno

@given('o jogador tem 1 semente de cenoura no inventário')
def step_impl(context):
    context.jogador = Player()
    context.jogador.inventario['cenoura'] = 1

@given('o jogador tem 1 semente de milho no inventário')
def step_impl(context):
    context.jogador = Player()
    context.jogador.inventario['milho'] = 1

@given('o jogador não tem sementes')
def step_impl(context):
    context.jogador = Player()

@given('o terreno está arado')
def step_impl(context):
    context.terreno = Terreno(arado=True)

@given('o terreno não está arado')
def step_impl(context):
    context.terreno = Terreno(arado=False)

@when('o jogador planta a semente')
def step_impl(context):
    context.resultado = context.jogador.plantar(context.terreno)

@when('o jogador tenta plantar')
def step_impl(context):
    context.resultado = context.jogador.plantar(context.terreno)

@then('a semente é removida do inventário')
def step_impl(context):
    assert context.resultado == "Plantado com sucesso"

@then('uma planta de cenoura é criada no terreno')
@then('uma planta de milho é criada no terreno')
def step_impl(context):
    assert context.terreno.planta in ["cenoura", "milho"]

@then('uma mensagem de erro é exibida: "Você não tem sementes!"')
def step_impl(context):
    assert context.resultado == "Você não tem sementes!"

@then('uma mensagem de erro é exibida: "O terreno precisa estar arado!"')
def step_impl(context):
    assert context.resultado == "O terreno precisa estar arado!"
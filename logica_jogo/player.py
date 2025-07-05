class Player:
    def __init__(self):
        self.inventario = {}
        self.vara_pesca = False
        self.proximo_ao_lago = False

    def plantar(self, terreno):
        if not terreno.arado:
            return "O terreno precisa estar arado!"
        for planta in ["cenoura", "milho"]:
            if self.inventario.get(planta, 0) > 0:
                self.inventario[planta] -= 1
                terreno.planta = planta
                return "Plantado com sucesso"
        return "Você não tem sementes!"

    def pescar(self):
        if not self.vara_pesca:
            return "Você precisa de uma vara de pesca!"
        if not self.proximo_ao_lago:
            return "Você precisa estar próximo ao lago!"
        self.inventario["peixe"] = self.inventario.get("peixe", 0) + 1
        return "Peixe pescado"
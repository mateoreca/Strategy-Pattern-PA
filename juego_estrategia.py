class Movimiento:
    def mover(self):
        pass

class Ataque:
    def atacar(self):
        pass

class MoverSoldado(Movimiento):
    def mover(self):
        return "El soldado se mueve a pie."
    
class MoverArquero(Movimiento):
    def mover(self):
        return "El arquero se mueve a distancia."

class MoverCaballero(Movimiento):
    def mover(self):
        return "El caballero se mueve a caballo."

class AtacarSoldado(Ataque):
    def atacar(self):
        return "El soldado ataca con espada."

class AtacarArquero(Ataque):
    def atacar(self):
        return "El arquero ataca con arco y flechas."

class AtacarCaballero(Ataque):
    def atacar(self):
        return "El caballero ataca con lanza."

class Unidad:
    def __init__(self, comportamiento_movimiento, tipo_ataque):
        self.comportamiento_movimiento = comportamiento_movimiento
        self.tipo_ataque = tipo_ataque

    def mover(self):
        return self.comportamiento_movimiento.mover()

    def atacar(self):
        return self.tipo_ataque.atacar()

soldado = Unidad(MoverSoldado(), AtacarSoldado())
arquero = Unidad(MoverArquero(), AtacarArquero())
caballero = Unidad(MoverCaballero(), AtacarCaballero())

print(soldado.mover())
print(soldado.atacar())
print(arquero.mover())
print(arquero.atacar())
print(caballero.mover())
print(caballero.atacar())


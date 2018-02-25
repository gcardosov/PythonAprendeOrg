class Persona:
    def __init__(self,edad,nombre):
        self.edad = edad
        self.nombre = nombre
        print "Se ha creado a", self.nombre, "de", self.edad

    def hablar(self,palabras ="No se que decir"):
        print self.nombre,': ', palabras

juan = Persona(18,"Juan")
juan.hablar("Hola estoy hablando")

luis = Persona(20,"Luis")
luis.hablar("Hola estoy hablando")
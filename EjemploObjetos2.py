class Persona:
    def __init__(self):
        self.edad = 18
        self.nombre = "juan"
        print "Se ha creado a", self.nombre, "de", self.edad

    def hablar(self,palabras ="No se que decir"):
        print self.nombre,':', palabras

juan = Persona()
juan.hablar()
juan.hablar("Hola estoy hablando")

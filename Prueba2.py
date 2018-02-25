class Persona:
    def __init__(self):
        self.edad=18
        self.nombre = "Gerardo"
        print "Se ha creado a"
        self.nombre, "de", self.edad

    def hablar (self, palabras):
        print self.nombre,':', palabras

juan = Persona()
juan.hablar("Estoy hablando")


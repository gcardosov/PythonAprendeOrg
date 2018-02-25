class Estudiante:
    def __init__(self):
        self.edad = 18
        self.nombre = "Julieta"
        print "Se ha creado a una estudianta llamada", self.nombre, "con edad de", self.edad

    def hablar(self,palabras):
        print self.nombre,':', palabras

julieta = Estudiante()
julieta.hablar("Hola putito")
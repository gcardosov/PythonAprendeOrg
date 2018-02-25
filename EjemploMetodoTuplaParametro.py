class Persona:
    def __init__(self,edad,nombre):
        self.edad = edad
        self.nombre = nombre
        print "Se ha creado a", self.nombre, "de", self.edad

    def hablar(self,**palabras):
        for frase in palabras:
            print self.nombre,': ', palabras[frase]

juan = Persona(30,"Juan")
juan.hablar(t1="Hola estoy hablando",t2="este soy yo")

luis = Persona(18,"Luis")
luis.hablar(t1="Hola estoy hablando",t2="este soy yo")

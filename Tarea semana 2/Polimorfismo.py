class Ave:
    def volar(self):
        return "Estoy volando"

class Pinguino(Ave):
    def volar(self):
        return "No puedo volar"

class Golondrina(Ave):
    def volar(self):
        return "Estoy volando alto"

# Uso
aves = [Pinguino(), Golondrina()]
for ave in aves:
    print(ave.volar())

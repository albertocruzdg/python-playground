class Person:
  # name = "Juan"
  # last_name = "Medina"
  # heigth = 1.5

  def __init__(self, name, last_name, heigth):
    self.name = name
    self.last_name = last_name
    self.heigth = heigth

  def greet(self, guest):
    print(self.name, ': Hola', guest.name, "mi nombre es", self.name)

nacho = Person("Juan Ignacio", "Medina", 1.5)
beto = Person("Alberto", "Cruz", 1.8)

nacho.greet(beto)
beto.greet(nacho)
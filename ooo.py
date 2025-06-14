class perro:
    def __init__ (self, mojadez_nariz, size, name, rascadas):
        self.mojadez = mojadez_nariz
        self.size = size
        self.name = name
        self.rascar = rascadas

    def tocar_nariz(self):
        print(f"Procedo a tocar la nariz de {self.name} y me di cuenta que")
        print(f"Mojadez de nariz de {self.name}: {self.mojadez}")

    def rascar_panzita(self):
        print("Ahora le rasco la panzita y")
        if self.rascar >= 3:
            print(f"{self.name} dice:")
            for i in range(rascada):
                print("Wow") 
        elif self.rascar == 2:
            print(f"{self.name} dice:")
            for i in range(2):
                print("Wow")
        else:
            print(f"{self.name} dice:")
            print("Wow")


rascada = int(input("¿Cuántas veces quieres rascarla?: "))
mady = perro("mucha", "minion", "mady", rascada)

mady.tocar_nariz()
mady.rascar_panzita()





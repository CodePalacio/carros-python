class Carro:
    def __init__(self, modelo, marca, ano):
        self.modelo = modelo
        self.marca = marca
        self.ano = ano
    def __str__(self) -> str:
        return "{}, {}, {}".format(self.modelo, self.marca, self.ano)

siena   = Carro("Siena","Fiat","1997")
mobi    = Carro("Mobi","Fiat","2012")
argo    = Carro("Argo","Fiat","2017")
hb20    = Carro("Hb20","Hyundai","2018")
gol     = Carro("Gol","Volkswagen","2007")
civic   = Carro("Civic","Honda","2008")


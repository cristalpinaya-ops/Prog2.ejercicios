class Anuncio:
    def __init__(self, num=0, pre=0.1):
        self.__numero = num
        self.__precio = pre

    def getPrecio(self):
        return self.__precio
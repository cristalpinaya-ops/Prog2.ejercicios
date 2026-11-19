class Artista:
    def __init__(self, nom, car, anios):
        self.__nombre = nom
        self.__ci = car
        self.__aniosExp = anios

    def getAnios(self):
        return self.__aniosExp

    def getNombre(self):
        return self.__nombre
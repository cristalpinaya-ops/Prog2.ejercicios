from Artista import Artista


class Obra:

    def __init__(self, titulo, material,
                 nom1, car1, anio1,
                 nom2, car2, anio2):

        self._titulo = titulo
        self._material = material

        self._artista1 = Artista(nom1, car1, anio1)
        self._artista2 = Artista(nom2, car2, anio2)

        self._anuncio = None

    def agregarAnuncio(self, anun):
        self._anuncio = anun

    def getArt1(self):
        return self._artista1

    def getArt2(self):
        return self._artista2

    def getAnuncio(self):
        return self._anuncio
from Obra import Obra


class Pintura(Obra):

    def __init__(self, titulo, material,
                 nom1, car1, anio1,
                 nom2, car2, anio2, gen):

        super().__init__(titulo, material,
                         nom1, car1, anio1,
                         nom2, car2, anio2)

        self.__genero = gen
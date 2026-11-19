from Anuncio import Anuncio
from Pintura import Pintura


class Main:

    def __init__(self):

        
        a1 = Anuncio(1, 2500)
        a2 = Anuncio(2, 3500)

        # INCISO A
   

        p1 = Pintura("monalisa", "oleo",
                     "davinci", 123, 20,
                     "joel", 321, 10, "intriga")

        p2 = Pintura("monalisa", "oleo",
                     "adrian", 444, 4,
                     "maria", 555, 15, "retrato")

        
        p1.agregarAnuncio(a1)

        print(" INCISO A ")

        print("Pintura 1 tiene anuncio:", p1.getAnuncio() != None)
        print("Pintura 2 tiene anuncio:", p2.getAnuncio() != None)


        # INCISO B
     

        artistas = [
            p1.getArt1(),
            p1.getArt2(),
            p2.getArt1(),
            p2.getArt2()
        ]

        mayor = artistas[0]

        for artista in artistas:

            if artista.getAnios() > mayor.getAnios():
                mayor = artista

        print("\n INCISO B ")

        print("Artista con mayor experiencia:", mayor.getNombre())

        print("Años de experiencia:", mayor.getAnios())


        # INCISO C
       

        p2.agregarAnuncio(a2)

        

        total = p1.getAnuncio().getPrecio() + p2.getAnuncio().getPrecio()

        print("\n INCISO C ")

        print("Precio pintura 1:", p1.getAnuncio().getPrecio())

        print("Precio pintura 2:", p2.getAnuncio().getPrecio())

        print("Monto total de venta:", total)




if __name__ == "__main__":
    Main()
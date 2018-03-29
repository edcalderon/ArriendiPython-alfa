import sys
from Outs import *
from Articulo import *
from Comentario import *
from Renta import *
from Conexion import *

class Run:

    def __init__(self):
     self.break_while = 1
     self.articulos = []
     self.switcher = {
        "1": self.AgregarDatosFicticios,
        "2": self.VerArticulos,
        "3": self.AgregarComentarios,
        "4": self.VerComentarios,
        "5": self.Salir
        }

    def AgregarDatosFicticios(self):

    def AgregarDatosFicticios(self):

        a1 = Articulo(1,666,"taladro")
        GuardarArticulo(1,666,"taladro")
        a2 = Articulo(2,999,"papa")
        GuardarArticulo("2","999","papa")
        print(a1.toString())
        print(a2.toString())
        self.articulos.append(a1)
        self.articulos.append(a2)

    def VerArticulos(self):
        print("lista de articulos: ")
        for art in self.articulos:
            print(art.toString())

    def AgregarComentarios(self):
        id_a_buscar = input("ingrese el id del articulo : ")
        art = Articulo.BuscarArticuloPorId(id_a_buscar,self.articulos)
        if art is not None:
            puntuacion = input("ingrese la puntuacion: ")
            descripcion = input("ingrese la descripcion: ")
            c1 = Comentario(art,puntuacion,descripcion)
            Articulo.comentarios.append(c1)
            print("comentario añadido")
        else:
            print("id no valido")

    def VerComentarios(self):
         print("lista de comentarios: ")
         for coment in Articulo.comentarios:
             print(coment.toString())

    def Salir(self):
        print("chaito")
        sys.exit(0)

    def run(self):
        while self.break_while == 1:
            Outs().display_menu()
            opcion = input("ingrese una opcion: ")
            action = self.switcher.get(str(opcion))
            if str(opcion) in self.switcher:
                action()
            else:
                print("{0} no es una opcion valida".format(opcion))

if __name__ == "__main__":
    Run().run()

import sys
from Mensaje import *
from Articulo import *
from Comentario import *
from Renta import *
#from Conexion import *
from Usuario import *
from Arrendador import *

class Run:

    usuario_actual = None

    def __init__(self):
     self.break_while = 1
     self.articulos = []
     self.switcher_operaciones = {
        "1": self.AgregarDatosFicticios,
        "2": self.VerArticulos,
        "3": self.AgregarComentarios,
        "4": self.VerComentarios,
        "5": self.AgregarArticulos,
        "6": self.VerMisArticulos,
        "7": self.SerArrendador,
        "8": self.Arrendar,
        "9": self.Volver,
        "10": self.Salir
        }

    def AgregarDatosFicticios(self):
        a1 = Articulo(666,"taladro","arriendi")
        a2 = Articulo(999,"papa","arriendi")
#        GuardarArticulo(1,666,"taladro","arriendi")
#        GuardarArticulo(2,999,"papa","arriendi")
        self.articulos.append(a1)
        self.articulos.append(a2)
        print("Datos ingresados correctamente")

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
            print("comentario añadido correctamente")
        else:
            print("id no valido")

    def VerComentarios(self):
         print("lista de comentarios: ")
         for coment in Articulo.comentarios:
             print(coment.toString())

    def AgregarArticulos(self):
        opcion = input("cuantos articulos desea ingresar: ")
        for i in range (0,int(opcion)):
            nombre = input("nombre del articulo {0}: ".format(i+1))
            precio = input("precio del articulo {0}: ".format(i+1))
            propietario = input("propietario del articulo {0}: ".format(i+1))
            a1 = Articulo(str(precio),str(nombre),str(propietario))
            self.articulos.append(a1)
            print("articulo {0} ingresado correctamente".format(i+1))

    def VerMisArticulos(self):
        print("Tus articulos: ")
        for art in self.articulos:
            if art.getPropietario() == Run.usuario_actual.getNombre():
                print (art.toString())

    def SerArrendador(self):
            Mensaje().display_menu_registroArrendador()
            opcion = input("ingrese una opcion: ")
            if opcion == "1":
                cedula = input("ingrese su cedula: ")
                celular = input("ingrese su celular: ")
                direccion= input("ingrese su dureccion: ")
                Arr1 = Arrendador(int(cedula),int(celular),str(direccion))
                Arrendador.arrendadores.append(Arr1)
                Run.usuario_actual.setIsArrendador(True)
                print("Arrendador ingresado correctamente")
                print(Arr1.toString())
            if opcion == "2":
                Mensaje().display_menu_operaciones()

    def Arrendar(self):
         if Run.usuario_actual.isArrendador == True:
             Mensaje().display_menu_zonaArrendador()
             opcion = input("ingrese una opcion: ")
             if opcion == "1":
                    print("construyeme")
             if opcion == "2":
                    print("construyeme")
             if opcion == "3":
                    print("construyeme")
             if opcion == "4":
                   Mensaje().display_menu_operaciones()
         else:
             print ("no eres arrendador")

    def Volver(self):
        Run().run()

    def Salir(self):
        print("chaito")
        sys.exit(0)

    def run(self):
        u1 = Usuario("arriendi","god")
        Usuario.users.append(u1)
        while self.break_while == 1:
            Mensaje().display_menu_bienvenida()
            opcion = input("ingrese una opcion: ")
            if opcion == "1":
                usuario = input("ingrese el usuario: ")
                for usr in Usuario.users:
                    if usr.getNombre() == usuario:
                        contraseña = input("ingrese la contraseña: ")
                        if usr.getPassword() == contraseña:
                            Run.usuario_actual = Usuario.BuscarUsuarioPorNombre(usuario,Usuario.users)
                            while self.break_while == 1:
                                print(" \n Hola Usuario {0} ".format(usuario.upper()))
                                Mensaje().display_menu_operaciones()
                                opcion = input("ingrese una opcion: ")
                                action = self.switcher_operaciones.get(str(opcion))
                                if str(opcion) in self.switcher_operaciones:
                                    action()
                                else:
                                    print("{0} no es una opcion valida".format(opcion))
                        else:
                            print("contraseña incorrecta")
                    else:
                        print("usuario no encontrado")

            if opcion == "2":
                Mensaje().display_menu_registroUsuario()
                nombre = input("ingrese un nombre de usuario: ")
                password = input("ingrese un nombre una constraseña: ")
                u1 = Usuario(nombre,password)
                Usuario.users.append(u1)
                print ("Usuario creado correctamente")
                print ("estas son tus credenciales:")
                print(u1.toString())



if __name__ == "__main__":
    Run().run()

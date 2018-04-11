import sys
import datetime
from Mensaje import *
from Articulo import *
from Comentario import *
from Renta import *
from Conexion import *
from Usuario import *
from Arrendador import *
from Arrendatario import *

class Run:

    usuario_actual = None
    articulos = []
    def __init__(self):
     self.break_while = 1
     self.break_while_2 = 1


     self.switcher_operaciones = {
        "0": Usuario.TablaDeUsuarios,
        "1": self.AgregarDatosFicticios,
        "2": self.VerArticulos,
        "3": self.AgregarComentarios,
        "4": self.VerComentarios,
        "5": self.AgregarArticulos,
        "6": self.VerMisArticulos,
        "7": self.SerArrendador,
        "8": self.PonerEnRenta,
        "9": self.Rentar,
        "10": Articulo.MejorPrecioArticulo,
        "11": Renta.ArticuloMasDisponible,
        "12": Articulo.MenosUso,
        "13": self.TiempoRestanteArticulo,
        "14": Arrendador.CalificarArrendador,
        "15": Arrendatario.CalificarArrendatario,
        "16": Arrendatario.mejoresArrendatarios,
        "17": Arrendador.PeoresArrendadores,
        "18": self.Volver,
        "19": self.Salir

        }

    def AgregarDatosFicticios(self):
    #    a1 = Articulo(666,"taladro",Run.usuario_actual)
    #    a2 = Articulo(999,"papa",Run.usuario_actual)
        Conexion.setArticulosBase()
        Conexion.cargarArticulos()

    #    Run.articulos.append(a1)
    #    Run.articulos.append(a2)
    #    Run.usuario_actual.articulos.append(a1)
    #    Run.usuario_actual.articulos.append(a1)
    #    rent1 = Renta(a1,Run.usuario_actual,5)
    #    Renta.rentas.append(rent1)
    #    rent1.setTiempoArriendo(3)
    #    rent1.setArrendatario(Usuario.BuscarUsuarioPorNombre('arriendi2',Usuario.users))
    #    rent1.isDisponible = False
    #    Run.usuario_actual.rentas.append(rent1)


#        Conexion.cargarRentas()

        print("Datos ingresados correctamente")

    def VerArticulos(self):
        print("lista de articulos: ")
        for art in Run.articulos2:
            print(art.toString())

    def AgregarComentarios(self):
        id_a_buscar = input("ingrese el id del articulo : ")
        art = Articulo.BuscarArticuloPorId(id_a_buscar,Run.articulos)
        if art is not None:
            puntuacion = input("ingrese la puntuacion: ")
            descripcion = input("ingrese la descripcion: ")
            c1 = Comentario(art,puntuacion,descripcion)
            Articulo.comentarios.append(c1)
            print("comentario añadido correctamente")
        else:
            print("id no valido")

    def VerComentarios(self):
         print("Lista de comentarios: ")
         for coment in Articulo.comentarios:
             print(coment.toString())

    def AgregarArticulos(self):
        opcion = input("cuantos articulos desea ingresar: ")
        for i in range(0,int(opcion)):
            nombre = input("nombre del articulo {0}: ".format(i + 1))
            precio = input("precio del articulo {0}: ".format(i + 1))
            paux = input("propietario del articulo {0}: ".format(i + 1))
            propietario = Usuario.BuscarUsuarioPorNombre(paux,Usuario.users)
            if propietario:
                a1 = Articulo(str(precio),str(nombre),propietario)
                self.articulos.append(a1)
                Run.usuario_actual.articulos.append(a1)
                Conexion.guardarArticulos(precio,nombre,propietario.getNombre())
                print("articulo {0} ingresado correctamente".format(i + 1))
            else:
                print("propietario no encontrado")
    @staticmethod
    def VerMisArticulos():
        if Run.articulos:
            print("**********************Estos son tus articulos: *******************************************")
            for art in Run.articulos:
                if art.getPropietario() == Run.usuario_actual:
                    print(art.toString())
            return True
        else:
            return None

    def SerArrendador(self):
            Mensaje().display_menu_registroArrendador()
            opcion = input("ingrese una opcion: ")
            if opcion == "1":
                cedula = input("ingrese su cedula: ")
                celular = input("ingrese su celular: ")
                direccion = input("ingrese su direccion: ")
                Arr1 = Arrendador(Run.usuario_actual.getNombre(),Run.usuario_actual.getPassword(),int(cedula),int(celular),str(direccion))
                Arrendador.arrendadores.append(Arr1)
                #Arr1 = Arrendatario(Run.usuario_actual.getNombre(),Run.usuario_actual.getPassword(),int(cedula),int(celular),str(direccion))
                #Arrendatario.arrendatarios.append(Arr1)
                Run.usuario_actual.setIsArrendador(True)
                Conexion.guardarArrendador(Run.usuario_actual.getNombre(),Run.usuario_actual.getPassword(),str(cedula),str(celular),str(direccion))
                print("Arrendador {0} ingresado correctamente.".format(Arr1.getNombre().upper()))
                print(Arr1.toString())
            if opcion == "2":
                Mensaje().display_menu_operaciones()

    def PonerEnRenta(self):
        self.break_while_2 = 1
        if Run.usuario_actual.isArrendador == True:
            while self.break_while_2 == 1:
                 Mensaje().display_menu_zonaArrendador()
                 opcion = input("ingrese una opcion: ")
                 if Run.usuario_actual.articulos:
                     if opcion == "1":
                            if Run().VerMisArticulos() == True:
                                    print("")
                                    id_art = input("ingrese el ID del articulo a arrendar: ")
                                    art = Articulo.BuscarArticuloPorId(id_art,Run.articulos)
                                    periodo = input("ingrese el periodo minimo que desea arrendar el articulo {0} en dias:".format(art.getNombre().upper()))
                                    rent1 = Renta(art,Run.usuario_actual,periodo)
                                    Renta.rentas.append(rent1)
                                    Run.usuario_actual.rentas.append(rent1)
                                    Conexion.guardarRentas(art.getNombre(),Run.usuario_actual.getNombre(),periodo,"")
                                    print("renta añadida:")
                                    print(rent1.toString())
                            elif Run().VerMisArticulos() == None:
                                print("aun no has publicado articulos, volver, opcion Agregar articulos")
                     if opcion == "2":
                          if Run().VerMisRentas() == True:
                                    print("")
                                    id_renta = input("ingrese el ID de la renta a cancelar: ")
                                    rent1 = Renta.BuscarRentaPorId(id_renta,Renta.rentas)
                                    print(rent1)
                                    rent1.setIsDisponible(False)
                                    rent1.getArticulo().setArrendado(False)
                                    print("renta cambiada")
                                    print(rent1.toString())
                          elif Run().VerMisRentas() == None:
                                print("aun no publicas articulos en renta, volver, opcion Rentar")
                     if opcion == "3":
                            Run().VerMisArriendos()
                 else:
                    print("no tienes articulos aun, ingresa un articulo, volver + opción 5")
                 if opcion == "4":
                    Mensaje().display_menu_operaciones()
                    self.break_while_2 = 0
        else:
             print("No puedes publicar Rentas de articulos, registrate como Arrendador, opcion 7 ")

    @staticmethod  # metodo de arrendador
    def VerMisArriendos():
        if Renta.rentas:
            print("Tienes las siguientes publicaciones de arriendo:")
            for renta in Renta.rentas:
                if renta.getArrendador() == Run.usuario_actual:
                    print(renta.toString())
        else:
            return None

    def Rentar(self):
        self.break_while_2 = 1
        if Run.usuario_actual.isArrendador == True:
            while self.break_while_2 == 1:
                 Mensaje().display_menu_zonaRenta()
                 opcion = input("ingrese una opcion: ")
                 if opcion == "1":
                        Run().VerRentasDisponibles()
                 if opcion == "2":
                        if Run().VerRentasDisponibles() == True:
                            print("")
                            id_renta = input("ingrese el ID de la renta deseada: ")
                            Mensaje.ImprimirKey('dias')
                            _time = int(input())
                            rent1 = Renta.BuscarRentaPorId(id_renta,Renta.rentas)
                            rent1.setTiempoArriendo(_time)
                            if rent1.avaible == True:
                                rent1.setArrendatario(Run.usuario_actual)
                                rent1.isDisponible = False
                                Run.usuario_actual.rentas.append(rent1)
                                rent1.getArticulo().setVecesUsado()
                                rent1.getArticulo().setArrendado(True)
                                print("renta concretada")
                            elif rent1.avaible == False:
                                Run.Rentar(self)
                        else:
                            print("aun no hay rentas disponibles")
                 if opcion == "3":
                     Run().VerMisRentas()
                 if opcion == "4":
                    Mensaje().display_menu_operaciones()
                    self.break_while_2 = 0
        else:
             print("No puedes rentar articulos aun, inscribete como arrendatario, opcion 7 ")


    def VerRentasDisponibles(self): #metodo de renta
        if not Renta.rentas:
            print("No hay rentas aun, pon en renta un articulo, opcion 8")
            return None
        else:
            print("**********lista de articulos en renta disponibles:**************")
            for renta in Renta.rentas:
                if renta.isDisponible == True:
                    print(renta.toString())
            return True
    def VerMisRentas(self): #metodo de renta
        if Run.usuario_actual.rentas:
            print("**********lista de mis rentas:**************")
            for renta in Run.usuario_actual.rentas:
                    print(renta.toString())
            return True
        else:
           return None

    def TiempoRestanteArticulo(self):
        _list = []
        for i in Run.usuario_actual.rentas:
            _list.append(i)
        if len(_list) == 0:
            Mensaje.ImprimirKey('SinRentas')
        elif len(_list) > 0:
            Run.VerMisRentas(self)
            Mensaje.ImprimirKey('id')
            _id = int(input())
            _a = int(len(_list))
            for i in range(0,_a):
                obj = _list[i]
                if int(obj.getId()) == _id:
                    aux1 = obj.getTiempoArriendo()
                    aux2 = datetime.datetime.now()
                    aux3 = aux1 - aux2
                    Mensaje.TiempoRestante(obj,aux3)

    def Volver(self):
        Run().run()

    def Salir(self):
        print("chaito")
        sys.exit(0)

    def run(self):
        Mensaje.AddMessages()             #puebla el dicionario de mensajes
        Conexion.setUsuariosBase()        #setea usuarios predefinidos en usuarios.txt
        Conexion.cargarUsuarios()         #cargar los usuarios, uncluidos los dios
        while self.break_while == 1:
            Mensaje().ImprimirKey2('display_menu_bienvenida')
    #       Mensaje().display_menu_bienvenida() # me gustan mas las funcunciones xD
            opcion = input("ingrese una opcion: ")
            if opcion == "1" or opcion == "s" or opcion == "si":
                usuario = input("ingrese el usuario: ")
                Run.usuario_actual = Usuario.BuscarUsuarioPorNombre(usuario,Usuario.users)
                if Run.usuario_actual:
                           contraseña = input("ingrese la contraseña: ")
                           if Run.usuario_actual.getPassword() == str(contraseña):  #sin el +\n me dice que la contraseña esta mala
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

            if opcion == "2" or opcion == "n" or opcion == "no":
                Mensaje().display_menu_registroUsuario()
                user = input("ingrese un nombre de usuario: ")
                passw = input("ingrese un nombre una constraseña: ")
                u1 = Usuario(user,passw)
                Usuario.users.append(u1)
                print("Usuario creado correctamente")
                print("estas son tus credenciales:")
                Conexion.guardarUsuarios(user,passw)
                Conexion.cargarUsuarios()
                print(u1.toString())




if __name__ == "__main__":
    Run().run()

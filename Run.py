import sys
import datetime
from Mensaje import *
from Articulo import *
from Comentario import *
from Renta import *
#from Conexion import *
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
        "1": self.AgregarDatosFicticios,
        "2": self.VerArticulos,
        "3": self.AgregarComentarios,
        "4": self.VerComentarios,
        "5": self.AgregarArticulos,
        "6": self.VerMisArticulos,
        "7": self.SerArrendador,
        "8": self.PonerEnRenta,
        "9": self.Rentar,
        "10": self.MejorPrecioArticulo,
        "11": self.ArticuloMasDisponible,
        "12": self.MenosUso,
        "13": self.TiempoRestanteArticulo,
        "14": self.Volver,
        "15": self.Salir
        }

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

    def MenosUso(self):
        _list = []
        Mensaje.ImprimirKey('NombreUsado')
        _name = str(input())
        for i in Articulo.articles:
            aux = Articulo.articles[i]
            if str(aux.getNombre()) == _name:
                if aux.getArrendado() == False:
                    _list.append(aux)
        _list.sort(key=lambda articulo: articulo.getVecesUsado(), reverse=False)
        _a = len(_list)
        for i in range(0,_a):
            obj = _list[i]
            aux1 = obj.getId()
            aux2 = obj.getNombre()
            aux3 = obj.getTipo()
            aux4 = obj.getPrecio()
            aux5 = obj.getPropietario().getNombre()
            aux6 = obj.getVecesUsado()
            Mensaje.MenosUsos(aux1,aux2,aux3,aux4,aux5,aux6)

    def MejorPrecioArticulo(self):
        _list = []
        type = None
        Mensaje.ImprimirKey('tipoNombre')
        auxInt = int(input())
        if auxInt == 1:
            Mensaje.ImprimirKey('tipo')
            option = str(input())
            for i in Articulo.articles:
                aux = Articulo.articles[i]
                if str(aux.getTipo()) == option:
                    _list.append(aux)
        elif auxInt == 2:
            Mensaje.ImprimirKey('nombre')
            option = str(input())
            for i in Articulo.articles:
                aux = Articulo.articles[i]
                if str(aux.getNombre()) == option:
                    _list.append(aux)
        _list.sort(key=lambda articulo: articulo.getPrecio(), reverse=False)
        _a = len(_list)
        for i in range(0,_a):
            obj = _list[i]
            aux1 = obj.getId()
            aux2 = obj.getNombre()
            aux3 = obj.getTipo()
            aux4 = obj.getPrecio()
            if (obj.getArrendado()) == False:
                aux5 = 'SI'
            elif (obj.getArrendado()) == True:
                aux5 = 'NO'
            aux6 = (obj.getPropietario()).getNombre()
            Mensaje.MejoresArticulos(aux1,aux2,aux3,aux4,aux5,aux6)

    def ArticuloMasDisponible(self):
        _list = []
        Mensaje.ImprimirKey('PorNombre')
        name = str(input())
        _a = len((Renta.getRentas()))
        for i in range(0,_a):
            aux = Renta.rentas[i]
            if name == (aux.getArticulo()).getNombre():
                _list.append(aux)
        _list.sort(key=lambda articulo: articulo.getFechafin(), reverse=True)
        _a = len(_list)
        for i in range(0,_a):
            obj = _list[i]
            if obj.getIsDisponible() == True:
                aux1 = obj.getArticulo().getId()
                aux2 = obj.getArticulo().getNombre()
                aux3 = obj.getArticulo().getTipo()
                aux4 = obj.getArticulo().getPrecio()
                aux5 = obj.getArticulo().getPropietario().getNombre()
                Mensaje.ImprimirDisponibilidadArticulos(obj,aux1,aux2,aux3,aux4,aux5)

    def AgregarDatosFicticios(self):
        a1 = Articulo(666,"taladro",Run.usuario_actual)
        a2 = Articulo(999,"papa",Run.usuario_actual)
#        GuardarArticulo(1,666,"taladro","arriendi")
#        GuardarArticulo(2,999,"papa","arriendi")
        Run.articulos.append(a1)
        Run.articulos.append(a2)
        Run.usuario_actual.articulos.append(a1)
        Run.usuario_actual.articulos.append(a1)
        print("Datos ingresados correctamente")

    def VerArticulos(self):
        print("lista de articulos: ")
        for art in Run.articulos:
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
            a1 = Articulo(str(precio),str(nombre),propietario)
            self.articulos.append(a1)
            Run.usuario_actual.articulos.append(a1)
            print("articulo {0} ingresado correctamente".format(i + 1))

    @staticmethod
    def VerMisArticulos():
        print("**********************Estos son tus articulos: *******************************************")
        for art in Run.articulos:
            if art.getPropietario() == Run.usuario_actual:
                print(art.toString())

    def SerArrendador(self):
            Mensaje().display_menu_registroArrendador()
            opcion = input("ingrese una opcion: ")
            if opcion == "1":
                cedula = input("ingrese su cedula: ")
                celular = input("ingrese su celular: ")
                direccion = input("ingrese su direccion: ")
                Arr1 = Arrendador(Run.usuario_actual.getNombre(),Run.usuario_actual.getPassword(),int(cedula),int(celular),str(direccion))
                Arrendador.arrendadores.append(Arr1)
                Arr1 = Arrendatario(Run.usuario_actual.getNombre(),Run.usuario_actual.getPassword(),int(cedula),int(celular),str(direccion))
                Arrendatario.arrendatarios.append(Arr1)
                Run.usuario_actual.setIsArrendador(True)
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
                            Run().VerMisArticulos()
                            print("")
                            id_art = input("ingrese el ID del articulo a arrendar: ")
                            art = Articulo.BuscarArticuloPorId(id_art,Run.articulos)
                            periodo = input("ingrese el periodo minimo que desea arrendar el articulo {0} en dias:".format(art.getNombre().upper()))
                            rent1 = Renta(art,Run.usuario_actual,periodo)
                            Renta.rentas.append(rent1)
                            Run.usuario_actual.rentas.append(rent1)
                            print("renta añadida:")
                            print(rent1.toString())
                     if opcion == "2":
                            Run().VerMisArriendos()
                            print("")
                            id_renta = input("ingrese el ID de la renta a cancelar: ")
                            rent1 = Renta.BuscarRentaPorId(id_renta,Renta.rentas)
                            print(rent1)
                            rent1.setIsDisponible(False)
                            rent1.getArticulo().setArrendado(False)
                            print("renta cambiada")
                            print(rent1.toString())
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
        print("Tienes las siguientes publicaciones de arriendo:")
        for renta in Renta.rentas:
            if renta.getArrendador() == Run.usuario_actual:
                print(renta.toString())

    def Rentar(self):
        self.break_while_2 = 1
        if Run.usuario_actual.isArrendador == True:
            while self.break_while_2 == 1:
                 Mensaje().display_menu_zonaRenta()
                 opcion = input("ingrese una opcion: ")
                 if opcion == "1":
                        Run().VerRentasDisponibles()
                 if opcion == "2":
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
        else:
            print("**********lista de articulos en renta disponibles:**************")
            for renta in Renta.rentas:
                if renta.isDisponible == True:
                    print(renta.toString())

    def VerMisRentas(self): #metodo de renta
        if not Run.usuario_actual.rentas:
            print("No tienes rentas aun, pon en renta un articulo o renta uno, opcion 8 o 9")
        else:
            print("**********lista de mis rentas:**************")
            for renta in Run.usuario_actual.rentas:
                    print(renta.toString())


    def Volver(self):
        Run().run()

    def Salir(self):
        print("chaito")
        sys.exit(0)

    def run(self):
        Mensaje.AddMessages()
        u1 = Usuario("arriendi","god")  # usuario dios
        Usuario.users.append(u1)
        u1.setIsArrendador(True)          # arrendador por defecto
        u2 = Usuario("arriendi2","god2")  # usuario dios2
        Usuario.users.append(u2)
        u2.setIsArrendador(True)          # arrendador por defecto2
        while self.break_while == 1:
            Mensaje().display_menu_bienvenida()
            opcion = input("ingrese una opcion: ")
            if opcion == "1" or opcion == "s" or opcion == "si":
                usuario = input("ingrese el usuario: ")
                Run.usuario_actual = Usuario.BuscarUsuarioPorNombre(usuario,Usuario.users)
                if Run.usuario_actual:
                           contraseña = input("ingrese la contraseña: ")
                           if Run.usuario_actual.getPassword() == contraseña:
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
                nombre = input("ingrese un nombre de usuario: ")
                password = input("ingrese un nombre una constraseña: ")
                u1 = Usuario(nombre,password)
                Usuario.users.append(u1)
                print("Usuario creado correctamente")
                print("estas son tus credenciales:")
                print(u1.toString())



if __name__ == "__main__":
    Run().run()

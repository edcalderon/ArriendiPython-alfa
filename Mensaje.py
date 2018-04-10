import datetime
from Renta import *
class Mensaje:

    messages = {}
    messages2 = {
        'display_menu_bienvenida':'\n\tBIENVENIDO A ARRIENDIAPP\n\t  ¿Arriendo? Arrinedi!\n\n    ¿Es usted un usuario registrado?\n    1. Si\n    2. No, registrar\n '

    }

    def AddMessages():
        Mensaje.messages.setdefault('tipoNombre','¿Desea buscar por tipo o por nombre? Oprima\n1 para tipo\n2 para nombre')
        Mensaje.messages.setdefault('nombre','Ingrese el nombre')
        Mensaje.messages.setdefault('id','Ingrese el id')
        Mensaje.messages.setdefault('tipo','Ingrese el tipo')
        Mensaje.messages.setdefault('Nombre','Nombre: ')
        Mensaje.messages.setdefault('Tipo','Tipo: ')
        Mensaje.messages.setdefault('Precio','Precio: ')
        Mensaje.messages.setdefault('Disponible','Disponible: ')
        Mensaje.messages.setdefault('Propietario','Propietario: ')
        Mensaje.messages.setdefault('ID','ID: ')
        Mensaje.messages.setdefault('PorNombre','Ingrese el nombre de los articulos para los que desea ver la mayor disponibilidad de tiempo')
        Mensaje.messages.setdefault('FechaIni','Fecha Inicial: ')
        Mensaje.messages.setdefault('FechaFin','Fecha Final: ')
        Mensaje.messages.setdefault('FechaEntrega','Fecha Entrega: ')
        Mensaje.messages.setdefault('TiempoRestante','El tiempo restante para realizar la entrega es:')
        Mensaje.messages.setdefault('Usado','Veces usado: ')
        Mensaje.messages.setdefault('NombreUsado','Ingrese el nombre de los articulos para los que desea ver el menor uso')
        Mensaje.messages.setdefault('dias', 'Ingrese los dias por el cual va a rentarlo')
        Mensaje.messages.setdefault('MasTiempo', 'No puedes rentar el articulo por un tiempo mayor al que va a estar disponible')
        Mensaje.messages.setdefault('SinRentas', 'No puedes consultar el tiempo restante de un articulo porque no tienes rentas actuales')
        Mensaje.messages.setdefault('Calificar', 'Ingrese la id del usuario a calificar')
        Mensaje.messages.setdefault('NuevaCalificacion', 'Ingrese la calificacion que le quiera dar a este usuario\nDebe ser un numero entero entre 1 y 5')
        Mensaje.messages.setdefault('Calificacion', 'Calificacion: ')
        Mensaje.messages.setdefault('Calificadores','Numero de calificaciones: ')
        Mensaje.messages.setdefault('NewCalificacion','Nueva calificacion: ')
        Mensaje.messages.setdefault('MejoresArrendadtarios', 'Lista de los arrendatarios')

    @staticmethod
    def ImprimirKey2(key):
        print(Mensaje.messages2[key])


    def ImprimirKey(key):
        print(Mensaje.messages[key])

    def MejoresArticulos(id,nombre,tipo,precio,arredado,propietario):
        print(Mensaje.messages['ID'],id,sep='\t')
        print(Mensaje.messages['Nombre'],nombre,Mensaje.messages['Tipo'],tipo,Mensaje.messages['Precio'],precio,Mensaje.messages['Disponible'],arredado,Mensaje.messages['Propietario'],propietario,sep='\t')

    def ImprimirFecha(self,key):
        if key == 'FechaIni':
            print(Mensaje.messages['FechaIni'],(datetime.datetime.ctime((Renta.getFechaini(self)))))
        elif key == 'FechaFin':
            print(Mensaje.messages['FechaFin'],(datetime.datetime.ctime((Renta.getFechafin(self)))))
        elif key == 'FechaEntrega':
            print(Mensaje.messages['FechaEntrega'],(datetime.datetime.ctime((Renta.getTiempoArriendo(self)))))

    def ImprimirDisponibilidadArticulos(self,id,nombre,tipo,precio,propietario):
        print(Mensaje.messages['ID'],id,sep='\t')
        print(Mensaje.messages['Nombre'],nombre,Mensaje.messages['Tipo'],tipo,Mensaje.messages['Precio'],precio,Mensaje.messages['Propietario'],propietario,sep='\t')
        Mensaje.ImprimirFecha(self,'FechaFin')

    def MenosUsos(id,nombre,tipo,precio,propietario,usado):
        print(Mensaje.messages['ID'],id,Mensaje.messages['Usado'],usado,sep='\t')
        print(Mensaje.messages['Nombre'],nombre,Mensaje.messages['Tipo'],tipo,Mensaje.messages['Precio'],precio,Mensaje.messages['Propietario'],propietario,sep='\t')

    def TiempoRestante(self,queda):
        Mensaje.ImprimirFecha(self,'FechaFin')
        Mensaje.ImprimirFecha(self, 'FechaEntrega')
        Mensaje.ImprimirKey('TiempoRestante')
        print(queda)

    def IdNombreCalificacion(id,nombre,calificacion):
        print(Mensaje.messages['ID'],id,Mensaje.messages['Nombre'],nombre,Mensaje.messages['Calificacion'],calificacion, sep='\t')

    def Calificacion(id,nombre,calificacion,calificadores):
        print(Mensaje.messages['ID'],id,Mensaje.messages['Nombre'],nombre,Mensaje.messages['NewCalificacion'],calificacion,Mensaje.messages['Calificadores'],calificadores, sep='\t')

    def display_menu_bienvenida(self):
        print("""
          BIENVENIDO A ARRIENDIAPP
            ¿Arriendo? Arrinedi!

        ¿Es usted un usuario registrado?
        1. Si
        2. No, registrar

        """)

    def display_menu_operaciones(self):
        print("""
        Estas son las operaciones disponibles:

        1. Agregar datos ficticios.
        2. Ver todos los articulos.
        3. Comentar articulos.
        4. Ver Comentarios.
        5. Agregar articulos.
        6. Ver mis articulos.
        7. Ser arrendador.
        8. Poner en Renta articulos.
        9. Rentar articulos.
        10. Mejor precio articulos
        11. Buscar articulo con la mayor disponibilidad
        12. Articulo con menos uso
        13. Tiempo restante articulo
        14. Calificar Arrendador
        15. Calificar Arrendatario
        16: Mejores arrendatarios
        17. Volver Inicio.
        18. Salir.
        """)

    def display_menu_registroUsuario(self):
        print("""
        ***********************************
            Registro de nuevo usuario
        ***********************************
        """)
    def display_menu_registroArrendador(self):
        print("""

        *********************************************************************************
                                     Registro Arrendador
        *********************************************************************************
        Para poner en renta un articulo debes convierte en un arrendador,
        para ello necesitamos mas informacion sobre ti, como cedula y datos de contacto.
        este proceso ademas te permite rentar articulos como arrendatario.
        ¿estas de acuerdo ?

        1.Si
        2.No


        """)
    def display_menu_zonaArrendador(self):
        print("""

        *********************************************************************************
                                      Zona  Arrendador
        *********************************************************************************
        estas son sus operaciones

        1.Publicar un articulo en renta
        2.Cancelar una publicacion de renta
        3.Ver tus articulos en renta
        4.Volver


        """)
    def display_menu_zonaRenta(self):
        print("""

        *********************************************************************************
                                      Zona  Rentas
        *********************************************************************************
        estas son sus operaciones

        1.Ver rentas disponibles
        2.Rentar
        3.Ver mi rentas
        4.Volver


        """)

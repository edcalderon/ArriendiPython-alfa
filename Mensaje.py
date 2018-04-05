class Mensaje:

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
        10. Volver Inicio.
        11. Salir.
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

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
        8. Arrendar articulo.
        9. Ver Rentas disponibles
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
                                     Registro arrendador
        *********************************************************************************
        Para poner en renta un articulo debes convierte en un arrendador,
        para ello necesitamos mas informacion sobre ti, como cedula y datos de contacto.
        ¿estas de acuerdo ?

        1.Si
        2.No


        """)
    def display_menu_zonaArrendador(self):
        print("""

        *********************************************************************************
                                      Zona  arrendador
        *********************************************************************************
        estas son sus operaciones

        1.Arrendar tus articulos
        2.Cancelar Arriendo
        3.Ver tus arriendo
        4.Volver


        """)

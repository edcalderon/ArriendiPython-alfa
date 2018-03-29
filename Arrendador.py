from Usuario import * 

class Arrendador(Usuario):
    def _init_(self,identificacion,nombre,_password):
        super()._init_(self,identificacion,nombre,_password)

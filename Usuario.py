import time
from Articulo import *
class Usuario:

    id_usuarios = 0        #contador
    calificacion = 3
    usuarios = {}
    users = []
    dickeys = []
    calificadores = 1     #contador

    def __init__(self,nombre,_password):
            self._setId(Usuario.id_usuarios)
            self.setNombre(nombre)
            self.setPassword(_password)
            self.setDate()
            self.setIsArrendador(False)
            self.articulos = []
            self.rentas = []

            Usuario._setUsuarios(self)
            Usuario._setDickeys(self)


    def toString(self):
         srt = "id:" + str(self.getId()) + " nombre de usuario:" + str(self.getNombre()) + " constraseña:" + str(self.getPassword())
         return srt


    def BuscarUsuarioPorNombre(nombre_a_buscar,list_usr=[]):
        for usr in list_usr:
            if usr.getNombre() == str(nombre_a_buscar):
                return usr


    def _setId(self,id_usuarios):
        Usuario.id_usuarios+=1
        self.id = Usuario.id_usuarios
    def getId(self):
        return self.id
    def setNombre(self,nombre):
        self.nombre = nombre
    def getNombre(self):
        return self.nombre
    def setPassword(self,_password):
        self._password = _password
    def getPassword(self):
        return self._password
    def setDate(self):
        self.date = time.asctime()
    def getDate(self):
        return self.date
    def setIsArrendador(self,valor):
        self.isArrendador = bool(valor)
    def getIsArrendador(self):
        return self.isArrendador
    def setCalificacion(self,calificacion):
        self.calificadores+=1
        self.calificacion = int((self.calificacion + calificacion) / (self.calificadores))
    def getCalificacion(self):
        return self.calificacion

    def _setUsuarios(self):
        Usuario.usuarios.setdefault(self.getId(),self)
    def _setDickeys(self):       #Agrega las keys a una lista
        Usuario.dickeys.append(self.getId())
    def getKeys():              #Retorna todas las keys de forma ordenada
        Usuario.dickeys.sort()
        return Usuario.dickeys
    def getUsuario(key):        #Retorna un usuario en especifico del diccionario
        return Usuario.usuarios[key]
    def _AllGets(self):
        atributos = []
        aux1 = self.getId()
        aux2 = self.getNombre()
        aux3 = self.getPassword()
        aux4 = self.getCalificacion()
        aux5 = self.getDate()
        atributos.append(aux1)
        atributos.append(aux2)
        atributos.append(aux3)
        atributos.append(aux4)
        atributos.append(aux5)
        return atributos

    def GetAllUsuarios():
        return Usuario.usuarios
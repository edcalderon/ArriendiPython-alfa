from Articulo import *

class Comentario:


   def __init__(self,articulo,puntuacion,descripcion):
       self.articulo = articulo
       self.puntuacion = puntuacion
       self.descripcion = descripcion

   def toString(self):
       srt = "id= " + str(self.articulo.getId())+ " puntuacion = " + str(self.puntuacion) + " descripcion = "+ str(self.descripcion)
       return srt

   def setPuntuacion(self,puntuacion):
        self.puntuacion = puntuacion

   def getPuntuacion(self):
        return puntuacion

   def setDescripcion(self,descripcion):
        self.descripcion = descripcion

   def getDescripcion(self):
        return descripcion

   def setArticulo(self,articulo):
        self.articulo = articulo

   def getArticulo(self):
        return articulo

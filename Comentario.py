from Articulo import *

class Comentario:


   def __init__(self,articulo,puntuacion,descripcion):
       self.setArticulo(articulo)
       self.setPuntuacion(puntuacion)
       self.setDescripcion(descripcion)

   def toString(self):
       srt = "[" + "Id articulo:" + str(self.articulo.getId()) + " Nombre articulo:" + str(self.articulo.getNombre()) + " Puntuacion:" + str(self.puntuacion) + " Descripcion:" + str(self.descripcion) + "]"
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

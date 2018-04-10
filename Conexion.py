from pathlib import Path
data_folder = Path("C:/")

from Run import *
from Usuario import *

class Conexion:

	@staticmethod
	def cargarUsuarios():
		file = open("usuarios.txt","r")
		for line in file:
			x = line.split(',')
			user = Usuario(x[0],x[1])
			Usuario.users.append(user)

	def guardarUsuarios(user,passw):
		 with open("usuarios.txt", "a") as file:
			 srt = user+","+passw
			 file.write(srt+"\n")

	def cargarArticulos():
		from Run import Run
		file = open("articulos.txt","r")
		for line in file:
			x = line.split(',')
			user = Usuario.BuscarUsuarioPorNombre(x[2].strip(),Usuario.users)
			articulo = Articulo(x[0],x[1],user)
			Run.articulos.append(articulo)
			user.articulos.append(articulo)

	def guardarArticulos(precio,nombre,propietario):
		 with open("articulos.txt", "a") as file:
			 srt = precio+","+nombre+","+propietario
			 file.write(srt)

	def cargarRentas():
		from Renta import Renta
		from Run import Run
		file = open("rentas.txt","r")
		for line in file:
			x = line.split(',')
			articulo = Articulo.BuscarArticuloPorNombre(str(x[0]),Run.articulos)
			arrendador = Usuario.BuscarUsuarioPorNombre(x[1].strip(),Usuario.users)
			arrendatario = Usuario.BuscarUsuarioPorNombre(x[3].strip(),Usuario.users)
			renta = Renta(articulo,arrendador,x[2],arrendatario)
			Renta.rentas.append(renta)
			arrendador.rentas.append(renta)
			arrendatario.rentas.append(renta)

	def guardarRentas(articulo,arrendador,periodo,arrendatario):
		 with open("rentas.txt", "a") as file:
			 srt = articulo+","+arrendador+","+periodo+","+arrendatario
			 file.write(srt)

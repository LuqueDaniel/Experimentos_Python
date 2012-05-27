#!/usr/bin/env python
#*-* encoding: utf-8 *-*

# Algoritmo de la amistad - Sheldon Cooper (The Big Bang Theory)

import random  #Modulo para generar numeros de forma aleatoria


class algoritmoAmistad(object):
	def __init__(self):
		self.llamar_por_telefono()

	def __decidir(self):  #Funcion para generar la respuesta aleatoria
		self.random_list = []
		self.par_list = []

		for i in range(10):  # Se genera una lista con 10 elementos cuyos valores son aleatorios
			self.random_list.append(random.randint(1,50))  # Agrega un numero aleatorio a la lista

		self.x = 0
		for i in self.random_list:
			if (self.random_list[self.x] % 2) == 0:  # Comprueba si el numero es par
				self.par_list.append(self.random_list[self.x])  # Si el numero es par lo agrega a una lista
				self.x += 1
			else:
				self.x += 1
				continue

	def esperar_respuesta(self, func, func2):  # Funcion de pasarela
		print "Esperar respuesta..."
		self.__decidir()

		if len(self.par_list) > 4:
			func()
		else:
			func2()

	def __selector(self, lista):  # Función que escoge un elemento de una lista de forma aleatoria
		self.num = []
		self.lista = lista

		self.x = 0
		while len(self.num) < len(self.lista):
			self.num.append(self.x)
			self.x += 1

		result = random.choice(self.num)

		return self.lista[result]

	def comenzar_amistad(self):
		print "Comenzar amistad"

	def llamar_por_telefono(self):
		print "Llamar a su casa"
		self.esperar_respuesta(self.invitar_comer, self.dejar_mensaje)

	def dejar_mensaje(self):
		print "No esta en casa, dejar mensaje"
		self.esperar_respuesta(self.invitar_comer, self.llamar_por_telefono)

	def invitar_comer(self):
		print "Invitar a comer"
		self.esperar_respuesta(self.comenzar_amistad, self.invitar_tomar_bebida)

	def invitar_tomar_bebida(self):
		print "Invitar a tomar una bebida caliente"
		self.esperar_respuesta(self.select_bebida, self.actividad_recreativa)

	def select_bebida(self):
		self.bebidas = ["Pepsi","7Up","Fanta de naranja","Cerveza","Café"]
		print "Tomar",self.__selector(self.bebidas)
		self.comenzar_amistad()

	def actividad_recreativa(self):
		print "¿Qué tal una actividad recreativa?"
		self.actividades = ["Cocina","Carreras de caballos","Programar","Leer"]

		self.x = 0
		while self.x < 4: #Bucle para escoger actividad
			self.actividad = self.__selector(self.actividades)

			self.resp = str(raw_input("Te gusta la actividad %s (Si/No) " % (self.actividad))).lower()

			if self.resp == "si":
				break
			elif self.resp == "no":
				self.x += 1
				continue
			else:
				print "Respuesta no valida"
				continue

		if self.x == 4:
			self.actividad_aleatoria(self.actividades)
		else:
			self.vamos_juntos()

	def vamos_juntos(self):
		print "Hagamos eso juntos"
		print "Yo pago"
		self.comenzar_amistad()

	def actividad_aleatoria(self,acti):
		print "Entonces haremos:",self.__selector(acti)
		print "Yo pago"
		self.comenzar_amistad()


algoritmo = algoritmoAmistad()  #Instanciar la clase
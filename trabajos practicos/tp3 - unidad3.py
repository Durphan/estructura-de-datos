import numpy as np

ejercicio = int(input("Seleccione el numero de ejercicio que desea revisar"))

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    LINE_SPACE = '\n\n'

match ejercicio:
    case 1:
        print(f"{bcolors.OKGREEN} Crear una clase la cual se llame `propiedad` e incluya los atributos de calle, numero, localidad, año de construccion y cantidad de ambientes{bcolors.ENDC}")
        class Propiedad:
            def __init__(self, calle = "", numero = 0, localidad = "", anio_construccion = 0, cantidad_ambientes = 0):
                self.calle = calle
                self.numero = numero
                self.localidad = localidad
                self.anio_construccion = anio_construccion
                self.cantidad_ambientes = cantidad_ambientes

                if anio_construccion < 1870:
                    raise ValueError("Solo puedes ingresar propiedades cuyo año de construccion sea mayor a 1870")
                
            def __str__(self):
                return self.calle + " " + str(self.numero) + "(" + str(self.localidad) + ")"
            def get_localidad(self):
                return self.localidad
            def get_calle(self):
                return self.calle
            def get_numero(self):
                return self.numero
            def get_anio_construccion(self):
                return self.anio_construccion
            def get_cantidad_ambientes(self):
                return self.cantidad_ambientes
            
            def misma_localidad(self, propiedadB):
                return self.localidad == propiedadB.get_localidad()
        
            def mayor_numeracion(self, propiedadB):
                if self.calle != propiedadB.get_calle():
                    raise ValueError("Las propiedades no son de la misma calle")
                if self.numero > propiedadB.get_numero():
                    return self
                return propiedadB
        
            def calcular_impuesto_arba(self):
                cantidadAmbientes = self.get_cantidad_ambientes()
                if self.anio_construccion <= 1949:
                    if cantidadAmbientes < 4 and cantidadAmbientes > 0:
                        return str(5) + "%"
                    if cantidadAmbientes > 3 and cantidadAmbientes < 7:
                        return str(10) + "%"
                    return str(25) + "%"
                if cantidadAmbientes < 6 and cantidadAmbientes > 0:
                    return str(5) + "%"
                if cantidadAmbientes > 5:
                    return str(35) + "%"
                raise ValueError("La propiedad no tiene ambientes")
        
        propiedadPrueba = Propiedad("Calle Falsa", 123, "Springfield", 1950, 5)
        propiedadPrueba2 = Propiedad("Calle Falsa", 124, "Springfield", 1950, 10)
        print(f"{bcolors.OKCYAN}Se crean dos propiedades de prueba, {propiedadPrueba} y {propiedadPrueba2}{bcolors.ENDC}")
        print(f"{bcolors.OKCYAN}Si usamos mismaLocalidad, deberia devolver True: {propiedadPrueba.misma_localidad(propiedadPrueba2)}{bcolors.ENDC}")
        print(f"{bcolors.OKCYAN}La propiedad con mayor numeracion es {propiedadPrueba.mayor_numeracion(propiedadPrueba2)}{bcolors.ENDC}")
        print(f"{bcolors.OKCYAN}El impuesto de ARBA para la propiedad {propiedadPrueba} es de {propiedadPrueba.calcular_impuesto_arba()}{bcolors.ENDC}")
        print(f"{bcolors.OKCYAN}El impuesto de ARBA para la propiedad {propiedadPrueba2} es de {propiedadPrueba2.calcular_impuesto_arba()}{bcolors.ENDC}")
    case 2:
        print(f"{bcolors.OKGREEN} Crear una clase la cual se llame `quiniela` que modele un juego de quiniela con dos numeros premiados y un multiplicador")
        class Quiniela:
            def __init__(self, numero1 = 0, numero2 = 0, multiplicador = 0):
                self.numero1 = numero1
                self.numero2 = numero2
                self.multiplicador = multiplicador
                if numero1 < 0 or numero1 > 999:
                    raise ValueError("El primer numero debe ser entre 0 y 999")
                if numero2 < 0 or numero2 > 999:
                    raise ValueError("El segundo numero debe ser entre 0 y 999")
            
            def __str__(self):
                return "El primer numero ganador es " + str(self.numero1) + " - " + "Segundo numero ganador es " + str(self.numero2) + " Paga: " + str(self.multiplicador) + "X"

            def importe_a_pagar(self, numero, monto):
                if monto > 1000:
                    raise ValueError("El monto no puede ser mayor a 1000")
                if numero == self.numero1:
                    return self.multiplicador * monto
                if numero == self.numero2:
                    return (self.multiplicador * monto) / 2
                return 0
            
            def es_numero_ganador(self, numero):
                return numero == self.numero1 or numero == self.numero2
                    
            
            def premiados_cercanos(self):
                return self.numero1 - self.numero2 >= self.numero1 - 10
            
        quinielaPrueba = Quiniela(123, 456, 5)
        print(f"{bcolors.OKCYAN}Se crea una quiniela de prueba, {quinielaPrueba}{bcolors.ENDC}")
        print(f"{bcolors.OKCYAN}Si usamos esNumeroGanador con el numero 123, deberia devolver True: {quinielaPrueba.es_numero_ganador(123)}{bcolors.ENDC}")
        print(f"{bcolors.OKCYAN}Si usamos importeAPagar con el numero 123 y un monto de 100, deberia devolver 500: {quinielaPrueba.importe_a_pagar(123, 100)}{bcolors.ENDC}")
        print(f"{bcolors.OKCYAN}Si usamos premiosCercanos, deberia devolver False: {quinielaPrueba.premiados_cercanos()}{bcolors.ENDC}")
    case 3:
        print(f"{bcolors.OKGREEN} Crear una clase llamada `Cuenta` que modele una cuenta bancaria con su numero de cuenta, DNI, saldo e interes anual")
        class Cuenta:
            def __init__(self, numero_cuenta = 0, dni = 0, saldo = 0, interes_anual = 0):
                self.numero_cuenta = numero_cuenta
                self.dni = dni
                self.saldo = saldo
                self.interes_anual = interes_anual
                if dni < 10000000 or dni > 99999999:
                    raise ValueError("El DNI debe ser de 8 digitos")
                if numero_cuenta < 10000000 or numero_cuenta > 99999999:
                    raise ValueError("El numero de cuenta debe ser de 8 digitos")
                
            def __str__(self):
                return "Cuenta Nro: " + str(self.numero_cuenta) + " Titular: " + str(self.dni) + "(" + str(self.saldo) + ")"
            
            def actualizar_saldo(self, saldo):
                self.saldo = saldo - (self.interes_anual / 365)
            
            def ingresar_dinero(self, monto):
                if monto < 0:
                    raise ValueError("El monto no puede ser negativo")
                self.saldo += monto
            
            def retirar_dinero(self, monto):
                if monto < 0:
                    raise ValueError("El monto no puede ser negativo")
                if self.saldo - monto < 0:
                    raise ValueError("No hay suficiente saldo")
                self.saldo -= monto
        
        cuentaPrueba = Cuenta(12345678, 12345678, 1000, 1.5)
        print(f"{bcolors.OKCYAN}Se crea una cuenta de prueba, {cuentaPrueba}{bcolors.ENDC}")
        cuentaPrueba.ingresar_dinero(100)
        print(f"{bcolors.OKCYAN}Si usamos ingresarDinero con un monto de 100, el saldo deberia ser 1100:{cuentaPrueba}{bcolors.ENDC}")
        cuentaPrueba.retirar_dinero(100)
        print(f"{bcolors.OKCYAN}Si usamos retirarDinero con un monto de 100, el saldo deberia ser 1000:{cuentaPrueba}{bcolors.ENDC}")
        cuentaPrueba.actualizar_saldo(1000)
        print(f"{bcolors.OKCYAN}Si usamos actualizarSaldo con un monto de 1000, el saldo deberia ser 1000 - 1.5 / 365:{cuentaPrueba}{bcolors.ENDC}")
    case 4:
        print(f"{bcolors.OKGREEN} Crear una clase llamada 'tiempo que modele un tiempo con horas, minutos y segundos {bcolors.ENDC}")
        class Tiempo:
            def __init__(self, horas = 0, minutos = 0, segundos = 0):
                self.horas = horas
                self.minutos = minutos
                self.segundos = segundos
                if horas < 0 or horas > 23:
                    raise ValueError("Las horas deben ser entre 0 y 23")
                if minutos < 0 or minutos > 59:
                    raise ValueError("Los minutos deben ser entre 0 y 59")
                if segundos < 0 or segundos > 59:
                    raise ValueError("Los segundos deben ser entre 0 y 59")
            
            def __str__(self):
                return str(self.horas) + ":" + str(self.minutos) + ":" + str(self.segundos)
            
            def tiempo_a_segundos(self):
                return self.horas * 3600 + self.minutos * 60 + self.segundos
            
            def tiempo_desde_segundos(self, segundos):
                return Tiempo(segundos // 3600, (segundos % 3600) // 60, segundos % 60)
            
            def mayor_duracion(self, tiempoB):
                return self.tiempo_a_segundos() > tiempoB.tiempo_a_segundos()
            
        tiempoA = Tiempo(1, 30, 0)
        tiempoB = Tiempo(2, 0, 0)
        print(f"{bcolors.OKCYAN}Se crean dos tiempos de prueba, {tiempoA} y {tiempoB}{bcolors.ENDC}")
        print(f"{bcolors.OKCYAN}Si usamos tiempoADesdeSegundos con 3600, deberia devolver 1:0:0: {tiempoA.tiempo_desde_segundos(3600)}{bcolors.ENDC}")
        print(f"{bcolors.OKCYAN}Si usamos tiempoAtiempoASegundos, deberia devolver 5400: {tiempoA.tiempo_a_segundos()}{bcolors.ENDC}")
        print(f"{bcolors.OKCYAN}Si usamos mayorDuracion, deberia devolver False: {tiempoA.mayor_duracion(tiempoB)}{bcolors.ENDC}")
    case 5:
        print(f"{bcolors.OKGREEN} Crear una clase llamada `cancion' que modele una cancion con su nombre, autor, duracion, genero (rock, jazz, blues, funk, raggae o rap), año de edicion, numeroLikes {bcolors.ENDC}")
        
        class invalid_song_error(Exception):
            "Exception raised for invalid song."
            pass

        
        class Cancion:
            def __init__(self, nombre = "", autor = "", duracion = 0, genero = "", anio_edicion = 0, numero_likes = 0):
                self.nombre = nombre
                self.autor = autor
                self.duracion = duracion
                self.genero = genero
                self.anio_edicion = anio_edicion
                self.numero_likes = numero_likes
                for i in np.array(["rock", "jazz", "blues", "funk", "raggae", "rap"]):
                    if i == genero:
                        break
                    raise ValueError("El genero debe ser rock, jazz, blues, funk, raggae o rap")
            
            def __str__(self):
                return 'Nombre: ' + str(self.nombre) + " - Autor: " + str(self.autor) + '(' + str(self.duracion) + ')'
            
            def get_duracion(self):
                return self.duracion
            
            def get_cantidad_likes(self):
                return self.numero_likes
            
            def get_anio_edicion(self):
                return self.anio_edicion
            
            def get_genero(self):
                return self.genero
            
            def get_autor(self):
                return self.autor

            def mayor_duracion(self, cancionB):
                return self.duracion > cancionB.get_duracion()
            
            def agregar_likes(self, cantidadLikes):
                self.numero_likes += cantidadLikes

            def mas_votada(self, cancionB):
                if self.autor == cancionB.get_autor() and self.genero == cancionB.get_genero():
                    return self.numero_likes > cancionB.get_cantidad_likes()
                raise invalid_song_error("Las canciones no son del mismo autor o genero")
        
        cancionA = Cancion("Cancion A", "Autor A", 3, "rock", 2020, 10)
        cancionB = Cancion("Cancion B", "Autor A", 4, "rock", 2020, 20)
        print(f"{bcolors.OKCYAN}Se crean dos canciones de prueba, {cancionA} y {cancionB}{bcolors.ENDC}")
        print(f"{bcolors.OKCYAN}Si usamos mayorDuracion con CancionA y CancionB, deberia devolver False: {cancionA.mayor_duracion(cancionB)}{bcolors.ENDC}")
        cancionA.agregar_likes(1)
        print(f"{bcolors.OKCYAN}Si usamos agregarLikes con CancionA y un like, el numero de likes deberia ser 11: {cancionA.get_cantidad_likes()}{bcolors.ENDC}")
        print(f"{bcolors.OKCYAN}Si usamos masVotada con CancionA y CancionB, deberia devolver False: {cancionA.mas_votada(cancionB)}{bcolors.ENDC}")


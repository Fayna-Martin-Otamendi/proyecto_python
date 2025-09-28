from functools import reduce


#Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias de cada letra en la cadena. Los espacios no deben ser considerados.
def frecuencia_letras(cadena):
    cadena = cadena.replace(" ", "") #Quita los espacios
    frecuencia = {} #Diccionario vacio para añair las letras

    #Con el bucle for recorremos las letras de la cadena y si ya la habíamos contado, sumamos uno, si no, la añadimos
    for letra in cadena: 
        if letra in frecuencia:
            frecuencia[letra] += 1
        else:
            frecuencia[letra] = 1
    return frecuencia            

print(frecuencia_letras("Proyecto Python"))

#Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map()
numeros = [2, 5, 10, 3, 1]
doble_numeros = list(map(lambda numero: numero * 2, numeros))
print(f"El doble de cada número de nuestra lista es: {doble_numeros}")

#Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.
def buscar_palabra(lista_palabras, palabra_objetivo):
    resultado = []

    for palabra in lista_palabras:
        if palabra_objetivo in palabra:
            resultado.append(palabra)
    return resultado        

lista_palabras = ["perro", "gato", "jirafa", "ganso", "elfante"]
palabra_objetivo = "ga"

print(f"Las palabras que contienen '{palabra_objetivo}' son: {buscar_palabra(lista_palabras, palabra_objetivo)}")


#Ecribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por defecto es 5. La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual que nota aprobado. Si es así, el estado será "aprobado", de lo contrario, será "suspenso". La función debe devolver una tupla que contenga la media y el estado.
def notas(lista_numeros, nota_aprobado = 5):
    media = sum(lista_numeros) / len(lista_numeros)
    
    if media >= nota_aprobado:
        estado = "Aprobado"
    else:
        estado = "Suspenso"
    return (media, estado) 

    
print(notas([2, 9, 5, 7, 3]))


#Escribe una función que calcule el factorial de un número de manera recursiva.
def calculo_factorial(n):
    if n == 0 or n == 1:
      return 1
    else:
      return n * calculo_factorial(n-1)
print(calculo_factorial(5))

#Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map()
def convertir_tuplas (lista_tuplas):
    return list(map(lambda t: str(t), lista_tuplas))

lista_tuplas = [1, 2, 3, 4]
print(convertir_tuplas(lista_tuplas))


#Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico o intenta dividir por cero, maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje indicando si la división fue exitosa o no.
try:
 numero1 = int(input("Ingrese el primer número"))
 print("El primer número ingresado por el usuario es:", numero1)

 numero2 = int(input("Ingrese el segundo número"))
 print("El segundo número ingresado por el usuario es:", numero2)

 resultado = numero1 / numero2
 print("El resultado de la división es:", round(resultado, 2))

except ValueError:
   print("Por favor, ingrese un número")

except ZeroDivisionError:
    print("No se puede dividir entre 0") 


#Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"].Usa la función filter()
def mascotas_permitidas(nombres):
    prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
    return list(filter(lambda m: m not in prohibidas, nombres))

mascotas = mascotas = ["Perro", "Gato", "Tigre", "Canario", "Oso", "Conejo"]
print("Mis mascotas permitidas son:", mascotas_permitidas(mascotas))


#Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una excepción personalizada y maneja el error adecuadamente.
def calcular_promedio(numeros):
    try:
        promedio = sum(numeros) / len(numeros)
        return promedio
    except ZeroDivisionError:
        return "La lista está vacía"
    
print(calcular_promedio([5, 10, 2, 6, 4])) 
print(calcular_promedio([]))  


#Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120, maneja las excepciones adecuadamente.
try:
 edad = int(input("Introduce tu edad"))
 if edad >= 0 and edad <= 120:
  print("La edad del usuario es:", edad)
 else:
   print("Rango de edad no válido") 
except ValueError:
   print("Por favor, ingrese un número")


#Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función map()
def longitud_palabras(frase):
    palabras = frase.split()
    return list(map(len, palabras))

print(longitud_palabras("Empezamos el segundo curso del Master"))   

#Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en mayúsculas y minúsculas. Las letras no pueden estar repetidas .Usa la función map()
def mayus_minus(caracteres):
    caracteres_tuplas = set(caracteres)
    return list(map(lambda c: (c.upper(), c.lower()), caracteres_tuplas))
print(mayus_minus("Verano"))


#Crea una función que retorne las palabras de una lista de palabras que comience con una letra en especifico. Usa la función filter()
def palabras_por_letra(lista_palabras, letra):
    return list(filter(lambda p: p.startswith(letra), lista_palabras))

print(palabras_por_letra(["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"], "J"))


#Crea una función lambda que sume 3 a cada número de una lista dada.
numeros = [1, 4, 7, 10]

resultado = list(map(lambda n: n + 3, numeros))
print(resultado)

# Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de todas las palabras que sean más largas que n. Usa la función filter()
def palabras_largas(cadena, n):
    palabras = cadena.split()  
    return list(filter(lambda p: len(p) > n, palabras))

texto = "Ayer fui a la playa de Las Canteras pero se puso a llover"
print(palabras_largas(texto, 5))

#Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, 5,7,2 corresponde al número quinientos setenta y dos 572. Usa la función reduce()
def lista_a_numero(digitos):
    return reduce(lambda x, y: x * 10 + y, digitos)

print(lista_a_numero([5, 7, 2]))
print(lista_a_numero([1, 2, 3, 4]))

#Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes (nombre, edad, calificación) y use la función filter para extraer a los estudiantes con una calificación mayor o igual a 90. Usa la función filter()
estudiantes = [
    {"nombre": "Ana", "edad": 20, "calificacion": 95},
    {"nombre": "Luis", "edad": 22, "calificacion": 85},
    {"nombre": "Marta", "edad": 21, "calificacion": 90},
    {"nombre": "Pedro", "edad": 23, "calificacion": 70},
]
aprobados = list(filter(lambda e: e["calificacion"] >= 90, estudiantes))
print("Estudiantes con calificación mayor o igual a 90:", aprobados)

#Crea una función lambda que filtre los números impares de una lista dada.
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

impares = list(filter(lambda n: n % 2 != 0, numeros))
print("Números impares:", impares)


#Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. Usa la función filter()
elementos = [10, "hola", 25, "como", 42, "estás", 7]
solo_numeros = list(filter(lambda e: isinstance(e, int), elementos))

print("Lista solo con enteros:", solo_numeros)


#Crea una función que calcule el cubo de un número dado mediante una función lambda
cubo = lambda n: n ** 3

print(cubo(3))
print(cubo(10))

#Dada una lista numérica, obtén el producto total de los valores de dicha lista.Usa la función reduce() .
numeros = [2, 3, 4, 5]
producto_total = reduce(lambda x, y: x * y, numeros)

print("El producto total es:", producto_total)

#Concatena una lista de palabras.Usa la función reduce() .
palabras = ["Que", "calor", "hace"]
frase = reduce(lambda x, y: x + " " + y, palabras)

print("Frase concatenada:", frase)

#Calcula la diferencia total en los valores de una lista. Usa la función reduce()
numeros = [100, 20, 5]
diferencia_total = reduce(lambda x, y: x - y, numeros)

print("La diferencia total es:", diferencia_total)

#Crea una función que cuente el número de caracteres en una cadena de texto dada.
def contar_caracteres(cadena):
    return len(cadena)

print("Número de caracteres:", contar_caracteres("Estoy practicando Python"))


#Crea una función lambda que calcule el resto de la división entre dos números dados.
resto = lambda a, b: a % b

print(resto(10, 3))
print(resto(47, 4))
print(resto(22, 2))

#Crea una función que calcule el promedio de una lista de números.
def promedio(lista_numeros):
    return sum(lista_numeros) / len(lista_numeros)

numeros = [4, 7, 9, 2]
print("El promedio es:", promedio(numeros))

#Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.
def primer_duplicado(lista):
    vistos = set()
    for elemento in lista:
        if elemento in vistos:
            return elemento
        vistos.add(elemento)
    return None 

numeros = [3, 1, 4, 2, 5, 3, 6, 4]
print("El primer duplicado es:", primer_duplicado(numeros))

#Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres  con el carácter '#', excepto los últimos cuatro.
def enmascarar(variable):
    texto = str(variable)  # convertir a string
    if len(texto) <= 4:
        return texto
    else:
        return "#" * (len(texto) - 4) + texto[-4:]

print(enmascarar(123456789))
print(enmascarar("LLegoElOtoño"))
print(enmascarar(1234))

#Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras pero en diferente orden.
def son_anagramas(palabra1, palabra2):
    palabra1 = palabra1.replace(" ", "").lower()
    palabra2 = palabra2.replace(" ", "").lower()

    return sorted(palabra1) == sorted(palabra2)

print(son_anagramas("roma", "amor"))
print(son_anagramas("pared", "dapre"))
print(son_anagramas("python", "typhon"))
print(son_anagramas("elefante", "gallina"))

#Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en esa lista. Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se lanza una excepción.
def buscar_nombre():
    try:
        nombres = input("Ingrese una lista de nombres separados por comas: ")
        lista_nombres = [n.strip() for n in nombres.split(",")]

        nombre_buscar = input("Ingrese el nombre que desea buscar: ").strip()

        if nombre_buscar in lista_nombres:
            print(f"El nombre '{nombre_buscar}' fue encontrado en la lista.")
        else:
            raise ValueError(f"El nombre '{nombre_buscar}' no está en la lista.")

    except ValueError as e:
        print("Error:", e)

buscar_nombre()

#Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y devuelve el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona no trabaja aquí.
def buscar_empleado(nombre, empleados):
    for empleado in empleados:
        if empleado["nombre"] == nombre:
            return empleado["puesto"]
    return "La persona no trabaja aquí."

empleados = [
    {"nombre": "Ana Torres", "puesto": "Analista de datos"},
    {"nombre": "Luis García", "puesto": "Administrativo"},
    {"nombre": "Marta Santana", "puesto": "Programadora"}
]

print(buscar_empleado("Ana Torres", empleados))
print(buscar_empleado("Pedro Pérez", empleados))

#Crea una función lambda que sume elementos correspondientes de dos listas dadas.
lista1 = [1, 2, 3, 4]
lista2 = [10, 20, 30, 40]

suma_listas = list(map(lambda x, y: x + y, lista1, lista2))

print(suma_listas)

#Crea la clase Arbol , define un árbol genérico con un tronco y ramas como atributos. Los métodos disponibles son: crecer_tronco , nueva_rama , crecer_ramas , quitar_rama e info_arbol . El objetivo es implementar estos métodos para manipular la estructura del árbol.
class Arbol:
    def __init__(self):
        # Tronco de longitud 1 y lista vacía de ramas
        self.tronco = 1
        self.ramas = []

    def crecer_tronco(self):
        # Aumentar longitud del tronco en 1
        self.tronco += 1

    def nueva_rama(self):
        # Agregar nueva rama de longitud 1
        self.ramas.append(1)

    def crecer_ramas(self):
        # Aumentar en 1 todas las ramas existentes
        self.ramas = [r + 1 for r in self.ramas]

    def quitar_rama(self, posicion):
        #Eliminar una rama en una posición específica.
        idx = posicion - 1
        if 0 <= idx < len(self.ramas):
            self.ramas.pop(idx)
        else:
            print("Posición inválida: no existe esa rama.")

    def info_arbol(self):
        # Devolver información del árbol
        return {
            "longitud_tronco": self.tronco,
            "numero_ramas": len(self.ramas),
            "longitudes_ramas": list(self.ramas)
        }


#Crear un árbol.
arbol = Arbol()

#Hacer crecer el tronco del árbol una unidad.
arbol.crecer_tronco()

#Añadir una nueva rama al árbol.
arbol.nueva_rama()

#Hacer crecer todas las ramas del árbol una unidad.
arbol.crecer_ramas()

#Añadir dos nuevas ramas al árbol.
arbol.nueva_rama()
arbol.nueva_rama()

#Retirar la rama situada en la posición 2 (1-based).
arbol.quitar_rama(2)

#Obtener información sobre el árbol.
info = arbol.info_arbol()
print(info)

#Crea la clase UsuarioBanco ,representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta corriente. Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario y agregar dinero al saldo.
class UsuarioBanco:
    def __init__(self, nombre, saldo, cuenta_corriente=True):
        # Inicializar atributos
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente

    def retirar_dinero(self, cantidad):
        # Retira dinero si hay saldo suficiente
        if not self.cuenta_corriente:
            raise ValueError(f"{self.nombre} no tiene cuenta corriente.")
        if cantidad > self.saldo:
            raise ValueError(f"{self.nombre} no tiene saldo suficiente.")
        self.saldo -= cantidad
        return f"Retiro exitoso. Saldo actual de {self.nombre}: {self.saldo}"

    def transferir_dinero(self, otro_usuario, cantidad):
        if not otro_usuario.cuenta_corriente or not self.cuenta_corriente:
            raise ValueError("Ambos usuarios deben tener cuenta corriente.")
        if cantidad > otro_usuario.saldo:
            raise ValueError(f"{otro_usuario.nombre} no tiene saldo suficiente para transferir.")
        otro_usuario.saldo -= cantidad
        self.saldo += cantidad
        return f"Transferencia de {cantidad} desde {otro_usuario.nombre} a {self.nombre} realizada."

    def agregar_dinero(self, cantidad):
        if not self.cuenta_corriente:
            raise ValueError(f"{self.nombre} no tiene cuenta corriente.")
        self.saldo += cantidad
        return f"Se agregaron {cantidad} unidades. Saldo actual de {self.nombre}: {self.saldo}"

    def __str__(self):
        return f"Usuario: {self.nombre}, Saldo: {self.saldo}, Cuenta corriente: {self.cuenta_corriente}"

#Crear dos usuarios: "Alicia" con 100 y "Bob" con 50
alicia = UsuarioBanco("Alicia", 100, True)
bob = UsuarioBanco("Bob", 50, True)

#Agregar 20 unidades al saldo de Bob
print(bob.agregar_dinero(20))

#Transferir 80 desde Bob a Alicia
print(alicia.transferir_dinero(bob, 80))

#Retirar 50 del saldo de Alicia
print(alicia.retirar_dinero(50))

#Comprobar estados finales
print(alicia)
print(bob)

# Crea una función llamada procesar_texto que procesa un texto según la opción especificada: reemplazar_palabras , procesar_texto .
def contar_palabras(texto):
    palabras = texto.split()
    contador = {}
    for palabra in palabras:
        contador[palabra] = contador.get(palabra, 0) + 1
    return contador


#Función para reemplazar una palabra por otra
def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    return texto.replace(palabra_original, palabra_nueva)


#Función para eliminar una palabra
def eliminar_palabra(texto, palabra_a_eliminar):
    palabras = texto.split()
    palabras = [p for p in palabras if p != palabra_a_eliminar]
    return " ".join(palabras)


# Función procesar_texto
def procesar_texto(texto, opcion, *args):
    if opcion == "contar":
        return contar_palabras(texto)
    elif opcion == "reemplazar":
        if len(args) != 2:
            return "Error: se necesitan palabra_original y palabra_nueva."
        return reemplazar_palabras(texto, args[0], args[1])
    elif opcion == "eliminar":
        if len(args) != 1:
            return "Error: se necesita palabra_a_eliminar."
        return eliminar_palabra(texto, args[0])
    else:
        return "Opción no válida."

texto = "Estoy agobiada con las entregas"

print("Contar palabras:")
print(procesar_texto(texto, "contar"))

print("\nReemplazar palabra:")
print(procesar_texto(texto, "reemplazar", "agobiada", "encantada"))

print("\nEliminar palabra:")
print(procesar_texto(texto, "eliminar", "Estoy"))

#Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario.
def momento_dia():
    hora = int(input("Ingrese la hora en formato 24h (0-23): "))

    if hora < 0 or hora > 23:
        print("Hora no válida.")
    elif 6 <= hora < 12:
        print("Es de día (mañana).")
    elif 12 <= hora < 18:
        print("Es la tarde.")
    else:
        print("Es de noche.")

momento_dia()

#Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica. 
def calificacion():
    nota = int(input("Ingrese la calificación numérica (0-100): "))

    if nota < 0 or nota > 100:
        print("Calificación no válida.")
    elif 0 <= nota <= 69:
        print("Insuficiente")
    elif 70 <= nota <= 79:
        print("Bien")
    elif 80 <= nota <= 89:
        print("Muy bien")
    elif 90 <= nota <= 100:
        print("Excelente")

calificacion()

#Escribe una función que tome dos parámetros: "triangulo" ) y figura (una cadena que puede ser "rectangulo" , "circulo" o datos (una tupla con los datos necesarios para calcular el área de la figura).
import math

# Escribe una función que calcule el área según la figura indicada.
def calcular_area(figura, datos):
    if figura == "rectangulo":
        base, altura = datos
        return base * altura
    elif figura == "circulo":
        (radio,) = datos 
        return math.pi * radio ** 2
    elif figura == "triangulo":
        base, altura = datos
        return (base * altura) / 2
    else:
        return "Figura no válida"

print("Área rectángulo:", calcular_area("rectangulo", (4, 5)))
print("Área círculo:", calcular_area("circulo", (3,)))
print("Área triángulo:", calcular_area("triangulo", (6, 4)))

#En este ejercicio, se te pedirá que escribas un programa en Python que utilice condicionales para determinar el monto final de una compra en una tienda en línea, después de aplicar un descuento.
def compra_con_descuento():
    precio = float(input("Ingrese el precio original del artículo (€): "))

    tiene_cupon = input("¿Tiene un cupón de descuento? (sí/no): ").strip().lower()

    if tiene_cupon == "sí" or tiene_cupon == "si":
        descuento = float(input("Ingrese el valor del cupón de descuento (€): "))
        if descuento > 0:
            precio_final = precio - descuento
            if precio_final < 0:
                precio_final = 0
            print(f"El precio final con descuento es: {precio_final} €")
        else:
            print("El cupón no es válido. Precio sin descuento:", precio, "€")
    else:
        print("No se aplicó ningún descuento. Precio final:", precio, "€")


compra_con_descuento()
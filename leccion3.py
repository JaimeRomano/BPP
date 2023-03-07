# Una herramienta alternativa a Sphinx para generar documentación de código en Python
# es Pdoc.
# Su código es una fracción de la complejidad de Sphinx y la salida no está tan 
# pulida, pero funciona sin configuración en un solo paso. También admite cadenas 
# de documentación para variables a través del análisis del código fuente. 
# De lo contrario, utiliza la introspección. 

# Ejemplo de funcionamiento con la herramienta Sphinx: 
# 1. Instalar Sphinx: 'pip install sphinx'
# 2. Crear un proyecto Sphinx: Ejecuta el comando 'sphinx-quickstart' para crear
# un nuevo proyecto Sphinx en una carpeta de tu elección.
# 3. Escribir documentación: Abre el archivo 'index.rst' en tu editor de texto
# y comienza a escribir la documentación para tu proyecto.

#Mi Módulo de Funciones
#======================

#Este es un ejemplo de documentación para mi módulo de funciones.

#.. automodule:: my_module
#   :members:

# En este ejemplo, 'my_module' es el nombre del archivo Python que contiene las 
# funciones que deseamos documentar.
# 4. Escribir funciones: Crea un archivo Python llamado 'my_module.py' en la misma
# carpeta que 'index.rst'. 
# Aquí hay un ejemplo de algunas funciones simples que podemos documentar:

def sumar(a, b):
    """
    Suma dos números enteros y devuelve el resultado.

    :param a: El primer número entero.
    :type a: int
    :param b: El segundo número entero.
    :type b: int
    :return: La suma de los dos números.
    :rtype: int
    """
    return a + b

def restar(a, b):
    """
    Resta dos números enteros y devuelve el resultado.

    :param a: El primer número entero.
    :type a: int
    :param b: El segundo número entero.
    :type b: int
    :return: La diferencia entre los dos números.
    :rtype: int
    """
    return a - b

# La documentación está escrita utilizando la sintaxis de reStructuredText, 
# y describe los parámetros y valores de retorno de cada función.
# 5. Generar la documentación: Ejecuta el comando 'make html' para generar 
# la documentación en formato HTML.
# 6. Ver la documentación: Abre el archivo '_build/html/index.html' en un 
# navegador web para ver la documentación generada. Deberías ver una lista
# de las funciones en 'my_module.py', junto con su documentación.
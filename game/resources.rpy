## Personajes
# Presente
define adam    = Character("Adam Carter", color = "#f07b32")
define brayan  = Character("Brayan Orellana", color = "#3bc137")
define gavya   = Character("Gavya Meraki", color = "#8f9fff")
define melissa = Character("Melissa Torres", color = "#690591")
define erin    = Character("Teniente Erin Miller")

# Pasado
define adamP   = Character("Adam Miller", color = "#f38508") # tiene 9 años
define brayanP = Character("Brayan Orellana", color = "#218a17") # tiene 14 años
define gavyaP  = Character("Gavya Meraki", color = "#2fafcf") # tiene 12 años

## Imágenes
# Fondos
image intro = 'images/BG/Introducción.png'
image pasillo = 'images/BG/Pasillo.png'
image reunion = 'images/BG/Sala de reuniones.png'

# Personajes/sprites

image idleAdam = 'images/Sprites'

# Variables
define puntos          = 0 # Parámetros para avanzar al siguiente capítulo, van de 0 a 100 y definen las monedas de cada capítulo.
define monedas         = 0     # Dinero del juego
define rechazoDes      = 0 # Parámetros que define las veces en que el usuario se negó a estar en la misión, van de 0 a 5 y definen las probabilidades de tener el final malo.
define adamFeli        = 64    # Parámetros de felicidad de Adam Carter, van de 0 a 100 y estos definen el final.
define reputacionTra   = 0     # Parámetro de reputación en el equipo policial, va de -100 a +100 y define las monedas de cada día.
define enPasado        = False # Parámetro de si el jugador está en el pasado
define progresoRescate = 0     # Proceso de rescate desde el presente, de 0 a 100%, y esto define el final.
define diasPasado      = 0     # Días en el pasado, afecta al progreso de rescate
define adamCFeli       = 32    # Parámetros de felicidad de Adam Carter (niño), van de 0 a 100 y estos definen el final.
define reputacionP     = 0     # Parámetro de reputación en la academia de criminalística, va de -100 a +100 y define las monedas de cada día.

# Precios

# init python:
#     class producto:
#         def __init__(self, nombre, archivo, precio, descipcion, posee):
#         self.nombre = nombre
#         self.archivo = archivo
#         self.precio = precio
#         self.descripcion = descripcion
#         self.posee = posee

# define chocolate = producto("Chocolate", "chocolate", 200, "Una barra de chocolate dulce y deliciosa", 0)

# Inventario
define panConJamon = 0
define pelucheOso  = 0
define globo       = 0
define peluchePato = 0
define pelucheFoca = 0
define guitarra    = 0
define escoba      = 0


# Variables especiales (solo para ciertas personas/personajes)

# Posibles variables

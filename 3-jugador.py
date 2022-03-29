import pygame								# Importa el módulo pygame
import os								    # Importa el módulo os

pygame.init()                               # Inicializa pygame

# Función para cargar imágenes
def cargarImagen(imagen):                   
    ruta = os.path.join("assets", imagen)   # Construye la ruta completa
    return pygame.image.load(ruta)          # Carga la imagen y la devuelve

WIDTH = 800  								   # Anchura de la ventana
HEIGHT = 600 								   # Altura de la ventana
SHIP_WIDTH = 80
SHIP_HEIGHT = 54

# Crea una imagen de fondo con un mosaico de estrellas
def crearFondo():                      
    img = pygame.surface.Surface((WIDTH, HEIGHT)) # Crea una imagen del tamaño de la pantalla
    pieza = cargarImagen("stars.png")             # Carga la imagen de mosaico
    y = 0                               # Inicia recorrido vertical
    while (y < HEIGHT):                 # Recorre en vertical
        x = 0                           # Inicia recorrido horizontal
        while (x < WIDTH):              # Recorre en horizontal
            img.blit(pieza, (x,y))      # Pinta la pieza en la posición (x,y)
            x += pieza.get_width()      # Avanza el ancho de la pieza en horizontal
        y += pieza.get_height()         # Avanza el alto de la pieza en vertical
    return img

# Inicializa la ventana principal
WIN = pygame.display.set_mode((WIDTH, HEIGHT)) # Crea la ventana
pygame.display.set_caption("Space Shooter")    # Establece el título de la ventana
ICONO = cargarImagen("icon.png")               # Carga la imagen de icono 
pygame.display.set_icon(ICONO)                 # Establece el icono de la ventana

FONDO = crearFondo()   # Crea la imagen de fondo

# Sprite Jugador
class Jugador(pygame.sprite.Sprite): # Clase que deriva de Sprite
    # CONSTRUCTOR
    def __init__(self):
        super().__init__()                                                   # Llama al constructor de Sprite
        ship = cargarImagen("playerShip.png")                                # Carga la imagen
        self.image = pygame.transform.scale(ship, (SHIP_WIDTH,SHIP_HEIGHT))  # Reduce el tamaño
        self.rect = self.image.get_bounding_rect()                           # Crea el Rect con el tamaño de la imagen
        self.rect.midbottom = (WIDTH // 2, HEIGHT - 20)                      # Ajusta la posición
    
    # Dibuja el sprite en pantalla
    def draw(self):                 
        WIN.blit(self.image, self.rect)     # Dibuja la imagen en la ventana

nave = Jugador()   # Crea el sprite jugador

# Función que dibuja la pantalla completa en cada iteración del juego
def dibuja():
    WIN.blit(FONDO, (0,0))      # Dibuja el fondo
    nave.draw()                 # Dibuja la nave
    pygame.display.update()     # Actualiza la pantalla


def main(): 							# Función principal
    jugando = True 						# Condición del bucle
    while jugando: 					    # Bucle del juego
        
        for event in pygame.event.get(): 	# Obtiene los eventos y los recorre
            if event.type == pygame.QUIT:   # Evento QUIT
                jugando = False 		    # Salimos del bucle

        dibuja()                        # dibuja la pantalla

    pygame.quit() 						# Cerramos pygame

# Si han ejecutado directamente este archivo, lanzamos main()
if __name__ == "__main__":
    main()
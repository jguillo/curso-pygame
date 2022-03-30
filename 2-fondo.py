import pygame       # Importa el módulo pygame
import os           # Importa el módulo os

pygame.init()       # Inicializa pygame

# Función para cargar imágenes
def cargarImagen(imagen):                   
    ruta = os.path.join("assets", imagen)   # Construye la ruta completa
    return pygame.image.load(ruta)          # Carga la imagen y la devuelve

WIDTH = 800                                     # Anchura de la ventana
HEIGHT = 600                                    # Altura de la ventana

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

# Función que dibuja la pantalla completa en cada iteración del juego
def dibuja():
    WIN.blit(FONDO, (0,0))      # Dibuja el fondo
    pygame.display.update()     # Actualiza la pantalla


def main():                             # Función principal
    jugando = True                      # Condición del bucle
    while jugando:                      # Bucle del juego
        
        for event in pygame.event.get():     # Obtiene los eventos y los recorre
            if event.type == pygame.QUIT:   # Evento QUIT
                jugando = False             # Salimos del bucle

        dibuja()                        # dibuja la pantalla

    pygame.quit()                         # Cerramos pygame

# Si han ejecutado directamente este archivo, lanzamos main()
if __name__ == "__main__":
    main()
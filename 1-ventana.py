import pygame                                   # Importa el módulo pygame

pygame.init()                                   # Inicializa pygame

WIDTH = 800                                     # Anchura de la ventana
HEIGHT = 600                                    # Altura de la ventana
WIN = pygame.display.set_mode((WIDTH, HEIGHT))  # Crea la ventana
pygame.display.set_caption("Space Shooter")     # Establece el título

def main():                                 # Función principal
    jugando = True                          # Condición del bucle
    while jugando:                          # Bucle del juego
        
        for event in pygame.event.get():    # Obtiene los eventos y los recorre
            if event.type == pygame.QUIT:   # Evento QUIT
                jugando = False             # Salimos del bucle

    pygame.quit()                           # Cerramos pygame

# Si han ejecutado directamente este archivo, lanzamos main()
if __name__ == "__main__":
    main()
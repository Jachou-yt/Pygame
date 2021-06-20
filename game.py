import pygame
import pytmx
import pyscroll

class Game:

    def __init__(self):

        # Fenêtre du jeu
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Pygame - Mode Aventure")

        # Charger la carte
        tmx_data = pytmx.util_pygame.load_pygame('pygamemap.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())

        # Dessiner le groupe de calque
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=1)

    def run(self):

        # Boucle du jeu
        running = True

        while running:

            self.group.draw(self.screen)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
        pygame.quit()
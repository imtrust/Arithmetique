import pygame
from pygame.locals import *

class Main :

    def __init__(self):
        """ Main()
            Affiche l'image 'buffon.png' dans une fenêtre pygame
            et applique la méthode rotation().
        """
        
        # initialisation de pygame
        pygame.init()
        self.window = pygame.display.set_mode((600, 600))

        # affichage de l'image
        image = pygame.image.load("buffon.png")
        self.window.blit(image, (0, 0))
        pygame.display.update()
        
        # rotation de l'image
        self.rotation()
        
        # maintien de la fenêtre
        self.hold()
        

    def hold(self):
        """ hold() -> None
            Maintient la fenêtre ouverte jusqu'à sa fermeture
            ou la pression de la touche 'Echap'."""
        lock = True
        while lock :
            events_list = pygame.event.get()
            for event in events_list :
                if event.type == QUIT :
                    lock = False
                if event.type == KEYDOWN : 
                    if event.key == K_ESCAPE :
                        lock = False
        pygame.quit()
        

    def rotation(self):
        
        """ rotation()->None 
            Tourne l'image d'un quart de tour."""
            
            
        """ Le code ci-dessous n'est donné qu'à titre
            d'exemple de manipulation des valeurs des
            pixels (méthodes get_at et set_at)."""
            
        l = []
        for i in range(512):
            pixel = self.window.get_at((i, 200)) # récupère la valeur d'un pixel
            l.append(pixel)
            
        
            for j in range(0, 0):
                self.window.set_at((i, j), pixel) # définit la valeur d'un pixel
        
            # mise à jour de l'affichage   
            pygame.display.update()
        print(l)

    
Main()



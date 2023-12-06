import pygame
import sys
from player.player import Player
from assets.platform import Platform, Cube
from threading import Thread
ONLINE = True

if ONLINE:
    from server.server import Server
    server = Server("localhost", 5000)
    thread = Thread(target=server.start)
    thread.start()


# Initialisation de Pygame
pygame.init()

# Définition de la taille de la fenêtre
largeur, hauteur = 800, 600
taille_fenetre = (largeur, hauteur)

# Création de la fenêtre
fenetre = pygame.display.set_mode(taille_fenetre)
pygame.display.set_caption("Ma Fenêtre Pygame")

player = Player()
# Définition des propriétés du cube
cube_taille = player.size
cube_couleur = player.color  # Couleur du cube en RVB

# Position initiale du cube
cube_x, cube_y = player.posx, player.posy

# Vitesse de déplacement du cube
vitesse = player.speed

# Variables pour la gravité et le saut
gravite = 0.5
vitesse_verticale = 0
est_en_l_air = False

painter_size = 10

plateformes = [
    Platform(0, 500, 700, 10),
    Platform(0, 400, 200, 10),
]

blocs = []

police = pygame.font.Font(None, 24)

# Fonction pour afficher du texte
def afficher_texte(texte, x, y, couleur=(0, 0, 0)):
    l = len(texte)
    surface_texte = police.render(texte, True, couleur)
    fenetre.blit(surface_texte, (x-(l*3), y-4))

# Boucle principale
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Gestion des touches pressées
    touches = pygame.key.get_pressed()
    if touches[pygame.K_r]:
        blocs = []
    if touches[pygame.K_LEFT]:
        cube_x -= vitesse
    if touches[pygame.K_RIGHT]:
        cube_x += vitesse
    if not est_en_l_air and touches[pygame.K_UP]:
        vitesse_verticale = -player.jump_power
        est_en_l_air = True
    
    if pygame.mouse.get_pressed()[0]:  # Bouton gauche de la souris enfoncé
        pos_souris = pygame.mouse.get_pos()
        blocs.append(Cube(pos_souris[0] - painter_size // 2, pos_souris[1] - painter_size // 2, painter_size, color=player.color))
    # Appliquer la gravité
    vitesse_verticale += gravite
    cube_y += vitesse_verticale

    cube_rect = pygame.Rect(cube_x, cube_y + vitesse_verticale, cube_taille, cube_taille)
    for plateforme in plateformes + blocs:
        plateforme = plateforme.rect
        if cube_rect.colliderect(plateforme):
            # Si le cube entre en collision avec une plateforme, ajuster la position et la vitesse verticale
            if vitesse_verticale > 0:
                cube_y = plateforme.y - cube_taille
                vitesse_verticale = 0
                est_en_l_air = False
            elif vitesse_verticale < 0:
                cube_y = plateforme.y + plateforme.height
                vitesse_verticale = 0

    # Limiter la position du cube pour qu'il reste dans la fenêtre
    cube_x = max(0, min(largeur - cube_taille, cube_x))
    cube_y = max(0, min(hauteur - cube_taille, cube_y))

    # Si le cube atteint le sol, inverser la vitesse verticale et indiquer qu'il n'est plus en l'air
    if cube_y >= hauteur - cube_taille:
        cube_y = hauteur - cube_taille
        est_en_l_air = False


    # Effacer l'écran
    fenetre.fill((125, 255, 200))  # Remplir l'écran avec du blanc (RVB)

    # Dessiner le cube
    pygame.draw.rect(fenetre, cube_couleur, (cube_x, cube_y, cube_taille, cube_taille))

    if ONLINE:
        blocs.extend(server.blocs)

    for plateforme in plateformes:
        pygame.draw.rect(fenetre, (0, 0, 0), plateforme)

    # Dessiner les blocs posés
    for bloc in blocs:
        pygame.draw.rect(fenetre, bloc.color, bloc)
    
    #  Afficher le texte au-dessus du cube
    texte_position = f"{player.name}"
    afficher_texte(texte_position, cube_x, cube_y - 20, couleur=(0, 0, 0))
    afficher_texte(f"blocks: {len(blocs)}", 30,0)
    afficher_texte(f"player_pos: {cube_x}, {cube_y}", 30, 20)
    # Mettre à jour l'affichage
    pygame.display.flip()

    # Réguler la vitesse de la boucle
    pygame.time.Clock().tick(60) # max 60 fps

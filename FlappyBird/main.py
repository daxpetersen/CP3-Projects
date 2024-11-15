import pygame
import sys
from game import Game
 
pygame.init()
screen = pygame.display.set_mode((400,720))
clock = pygame.time.Clock()
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE,2200)
game = Game('img/bird.png','img/pipe.png','img/background.png','img/ground.png')
game.resize_images()
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game.bird_movement = -3.5
            if event.key == pygame.K_SPACE and game.active == False:
                game.restart()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit() 

        if event.type == SPAWNPIPE:
            game.add_pipe()


    game.show_background(screen)


    if game.active:
        game.show_bird(screen)
        game.update_bird()
        game.move_pipes()
        game.show_pipe(screen)
        game.check_collision()
        game.count_score()
        game.show_score("playing",screen,(255,255,255))
        game.move_ground()
    else:
        game.game_over(screen,(255,255,255))
    game.show_ground(screen)



    pygame.display.update()

    clock.tick(120)
  
    
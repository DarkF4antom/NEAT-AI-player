import pygame
import os
import random
import sys
import math
import neat

pygame.init()

## Global Constants
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

dname= os.path.dirname(__file__)

RUNNING = [ pygame.image.load(os.path.join(dname, "Assets\Dino\DinoRun1.png")),
            pygame.image.load(os.path.join(dname, "Assets\Dino\DinoRun2.png"))]
JUMPING =  pygame.image.load(os.path.join(dname, "Assets\Dino\DinoJump.png"))
DUCKING = [pygame.image.load(os.path.join(dname, "Assets\Dino\DinoDuck1.png")),
           pygame.image.load(os.path.join(dname, "Assets\Dino\DinoDuck2.png"))]

SMALL_CACTUS = [ pygame.image.load(os.path.join(dname, "Assets\Cactus\sc1.png")),
             pygame.image.load(os.path.join(dname, "Assets\Cactus\sc2.png")),
            pygame.image.load(os.path.join(dname, "Assets\Cactus\sc3.png"))]
LARGE_CACTUS = [ pygame.image.load(os.path.join(dname, "Assets\Cactus\lc1.png")),
             pygame.image.load(os.path.join(dname, "Assets\Cactus\lc2.png")),
            pygame.image.load(os.path.join(dname, "Assets\Cactus\lc3.png"))]


BIRD =  [pygame.image.load(os.path.join(dname, "Assets\Bird\Bird1.png")),
         pygame.image.load(os.path.join(dname, "Assets\Bird\Bird2.png"))]
CLOUD =  pygame.image.load(os.path.join(dname, "Assets\Other\Cloud.png"))

BG =  pygame.image.load(os.path.join(dname, "Assets\Other\Track.png"))





class Dinosaur:
    X_POS = 80
    Y_POS = 310
    Y_POS_DUCK = 340
    JUMP_VEL = 8.5

    def __init__(self):
        self.duck_img = DUCKING
        self.run_img = RUNNING
        self.jump_img = JUMPING

        self.dino_duck = False
        self.dino_run = True
        self.dino_jump = False

        self.step_index = 0
        self.jump_vel = self.JUMP_VEL
        self.image = self.run_img[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS

        self.color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
import pygame
import os
import random
import sys
import math
import neat

pygame.init()

## Global Constants
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

dname= os.path.dirname(__file__)

RUNNING = [ pygame.image.load(os.path.join(dname, "Assets\Dino\DinoRun1.png")),
            pygame.image.load(os.path.join(dname, "Assets\Dino\DinoRun2.png"))]
JUMPING =  pygame.image.load(os.path.join(dname, "Assets\Dino\DinoJump.png"))
DUCKING = [pygame.image.load(os.path.join(dname, "Assets\Dino\DinoDuck1.png")),
           pygame.image.load(os.path.join(dname, "Assets\Dino\DinoDuck2.png"))]

SMALL_CACTUS = [ pygame.image.load(os.path.join(dname, "Assets\Cactus\sc1.png")),
             pygame.image.load(os.path.join(dname, "Assets\Cactus\sc2.png")),
            pygame.image.load(os.path.join(dname, "Assets\Cactus\sc3.png"))]
LARGE_CACTUS = [ pygame.image.load(os.path.join(dname, "Assets\Cactus\lc1.png")),
             pygame.image.load(os.path.join(dname, "Assets\Cactus\lc2.png")),
            pygame.image.load(os.path.join(dname, "Assets\Cactus\lc3.png"))]


BIRD =  [pygame.image.load(os.path.join(dname, "Assets\Bird\Bird1.png")),
         pygame.image.load(os.path.join(dname, "Assets\Bird\Bird2.png"))]
CLOUD =  pygame.image.load(os.path.join(dname, "Assets\Other\Cloud.png"))

BG =  pygame.image.load(os.path.join(dname, "Assets\Other\Track.png"))




class Dinosaur:
    X_POS = 80
    Y_POS = 330
    Y_POS_DUCK = 350
    JUMP_VEL = 9.5

    def __init__(self):
        self.duck_img = DUCKING
        self.run_img = RUNNING
        self.jump_img = JUMPING

        self.dino_duck = False
        self.dino_run = True
        self.dino_jump = False

        self.step_index = 0
        self.jump_vel = self.JUMP_VEL
        self.image = self.run_img[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS

        self.color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))

    def update(self):
        if self.dino_duck:
            self.duck()
        if self.dino_run:
            self.run()
        if self.dino_jump:
            self.jump()

        if self.step_index >= 10:
            self.step_index = 0


    def duck(self):
        self.image = self.duck_img[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS_DUCK
        self.step_index += 1

    def run(self):
        self.image = self.run_img[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index += 1

    def jump(self):
        self.image = self.jump_img
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel < -self.JUMP_VEL:
            self.dino_jump = False
            self.dino_rect.y = self.Y_POS
            self.dino_run = True
            self.jump_vel = self.JUMP_VEL

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.dino_rect.x, self.dino_rect.y))
        pygame.draw.rect(SCREEN, self.color, self.dino_rect, 2)
        for obstacle in obstacles:
           pygame.draw.line(SCREEN, self.color, (self.dino_rect.x + 54, self.dino_rect.y + 12), obstacle.rect.center, 2)


class Cloud:
    def __init__(self):
        self.x = SCREEN_WIDTH + random.randint(800, 1000)
        self.y = random.randint(50, 100)
        self.image = CLOUD
        self.width = self.image.get_width()

   
    def update(self):
        self.x -= game_speed
        if self.x < -self.width:
            self.x = SCREEN_WIDTH + random.randint(2500, 3000)
            self.y = random.randint (50,100)
           
   
    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))



class Obstacle:
    def __init__(self,image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH
       

   
    def update(self):
        self.rect.x -= game_speed
        if self.rect.x < - self.rect.width:
            obstacles.pop()



    def draw(self, SCREEN):
        SCREEN.blit(self.image [self.type], self.rect)

class SmallCactus (Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 325

class LargeCactus (Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 300


class Bird(Obstacle):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = random.choice([270, 50])
        self.index = 0
   
    def draw(self, SCREEN):
        if self.index >= 9:
            self.index = 0
        SCREEN.blit(self.image[self.index//5], self.rect)
        self.index += 1


def remove(index):
    dinosaurs.pop(index)
    ge.pop(index)
    nets.pop(index)


def distance(pos_a, pos_b):
    dx = pos_a[0]-pos_b[0]
    dy = pos_a[1]-pos_b[1]
    return math.sqrt(dx**2+dy**2)

def eval_genomes(genomes, config) :
    global game_speed , x_pos_bg, y_pos_bg , points, obstacles, dinosaurs, ge, nets, gspeed
    run = True
    clock = pygame.time.Clock()
   
    cloud = Cloud()
    game_speed = 14
    gspeed = 14
    x_pos_bg = 0
    y_pos_bg = 380
    points = 0
    font = pygame.font.Font('freesansbold.ttf', 20)
   
   
    obstacles=[]
    dinosaurs = []
    ge = []
    nets = []


    for genome_id, genome in genomes:
        dinosaurs.append(Dinosaur())
        ge.append(genome)
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        nets.append(net)
        genome.fitness = 0





    def score():
        global points, game_speed, gspeed
        points += 1
        if points % 100 == 0 :
            gspeed += 1
            if not game_speed > 49:
                game_speed += 1
       
        text = font.render("points: "+ str(points), True , (0, 0, 0))
        textRect =  text.get_rect()
        textRect.center = (1000, 40)
        SCREEN.blit(text, textRect)
       
   

    def background ():
        global x_pos_bg, y_pos_bg
        image_width = BG.get_width()
        SCREEN.blit(BG, (x_pos_bg, y_pos_bg))
        SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
        if x_pos_bg <= -image_width:
            SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
            x_pos_bg = 0
        x_pos_bg -= game_speed


    def statistics():
        global dinosaurs, game_speed, ge, gspeed
        text_1 = font.render(f'Dinosaurs left:  {str(len(dinosaurs))}', True, (0,0,0))
        text_2 = font.render(f'Gen: {pop.generation+1} ', True, (0, 0, 0))
        text_3 = font.render(f'Game Speed: {str(gspeed)}', True, (0, 0, 0))

        SCREEN.blit(text_1, (50, 450))
        SCREEN.blit(text_2, (50,480))
        SCREEN.blit(text_3, (50, 510))
       

    while run : #while loop that runs the game (basic pygame shit)
        for event in pygame.event.get() :
            if event.type == pygame.QUIT: #safely exit with the X button
                run = False
                break
   
        SCREEN.fill((255,255,255)) #white bg


        for dinosaur in dinosaurs:

            dinosaur.update()
            dinosaur.draw(SCREEN)

        if len(dinosaurs) == 0:
            break
       

       

        if len(obstacles) == 0:
            if random.randint(0,2) == 0:
                obstacles.append(SmallCactus (SMALL_CACTUS))
            elif random.randint(0,2) ==1:
                obstacles.append(LargeCactus (LARGE_CACTUS))
            elif random.randint(0,2) == 2:
                obstacles.append(Bird(BIRD))

        for obstacle in obstacles:
            obstacle.draw(SCREEN)
            obstacle.update()
            for i, dinosaur in enumerate(dinosaurs):
                if dinosaur.dino_rect.colliderect(obstacle.rect):
                    ge[i].fitness -= 5
                    remove(i)
                else:
                    ge[i].fitness += 1
            for i, dinosaur in enumerate(dinosaurs):

                output = nets[i].activate((dinosaur.dino_rect.y,
                                        distance((dinosaur.dino_rect.x, dinosaur.dino_rect.y),
                                        obstacle.rect.midtop)))

                if output[0] > 0.5 and dinosaur.dino_rect.y == dinosaur.Y_POS and not dinosaur.dino_duck:
                    dinosaur.dino_jump = True
                    dinosaur.dino_duck = False
                    dinosaur.dino_run = False
               
                elif obstacle.rect.y < 300 and output[1] > 0.5 and not dinosaur.dino_jump:
                    dinosaur.dino_jump = False
                    dinosaur.dino_duck = True
                    dinosaur.dino_run = False
                    if len(obstacles)==0:
                        dinosaur.dino_jump = False
                        dinosaur.dino_duck = False
                        dinosaur.dino_run = True


           


        background()
        statistics()
        cloud.draw(SCREEN)
        cloud.update()

        score()

        clock.tick(60) #refresh rate of the game
        pygame.display.update()


#setup for neat

def run(config_path):
    global pop
    config = neat.config.Config(
        neat.DefaultGenome,
        neat.DefaultReproduction,
        neat.DefaultSpeciesSet,
        neat.DefaultStagnation,
        config_path
    )


    pop = neat.Population(config)
    pop.run(eval_genomes, 500)


if __name__ == '__main__':
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config.txt')
    run(config_path)
    def update(self):
        if self.dino_duck:
            self.duck()
        if self.dino_run:
            self.run()
        if self.dino_jump:
            self.jump()

        if self.step_index >= 10:
            self.step_index = 0


    def duck(self):
        self.image = self.duck_img[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS_DUCK
        self.step_index += 1

    def run(self):
        self.image = self.run_img[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index += 1

    def jump(self):
        self.image = self.jump_img
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel < -self.JUMP_VEL:
            self.dino_jump = False
            self.dino_rect.y = self.Y_POS
            self.dino_run = True
            self.jump_vel = self.JUMP_VEL

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.dino_rect.x, self.dino_rect.y))
        pygame.draw.rect(SCREEN, self.color, self.dino_rect, 2)
        for obstacle in obstacles:
           pygame.draw.line(SCREEN, self.color, (self.dino_rect.x + 54, self.dino_rect.y + 12), obstacle.rect.center, 2)


class Cloud:
    def __init__(self):
        self.x = SCREEN_WIDTH + random.randint(800, 1000)
        self.y = random.randint(50, 100)
        self.image = CLOUD
        self.width = self.image.get_width()

    
    def update(self):
        self.x -= game_speed
        if self.x < -self.width:
            self.x = SCREEN_WIDTH + random.randint(2500, 3000)
            self.y = random.randint (50,100)
            
    
    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))



class Obstacle:
    def __init__(self,image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH
        

    
    def update(self):
        self.rect.x -= game_speed
        if self.rect.x < - self.rect.width:
            obstacles.pop()



    def draw(self, SCREEN):
        SCREEN.blit(self.image [self.type], self.rect)

class SmallCactus (Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 325

class LargeCactus (Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 300


class Bird(Obstacle):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = random.choice([270, 50])
        self.index = 0
    
    def draw(self, SCREEN):
        if self.index >= 9:
            self.index = 0
        SCREEN.blit(self.image[self.index//5], self.rect)
        self.index += 1


def remove(index):
    dinosaurs.pop(index)
    ge.pop(index)
    nets.pop(index)


def distance(pos_a, pos_b):
    dx = pos_a[0]-pos_b[0]
    dy = pos_a[1]-pos_b[1]
    return math.sqrt(dx**2+dy**2)

def eval_genomes(genomes, config) :
    global game_speed , x_pos_bg, y_pos_bg , points, obstacles, dinosaurs, ge, nets
    run = True
    clock = pygame.time.Clock()
    
    cloud = Cloud()
    game_speed = 14
    x_pos_bg = 0
    y_pos_bg = 380
    points = 0
    font = pygame.font.Font('freesansbold.ttf', 20)
    
    
    obstacles=[]
    dinosaurs = []
    ge = []
    nets = []


    for genome_id, genome in genomes:
        dinosaurs.append(Dinosaur())
        ge.append(genome)
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        nets.append(net)
        genome.fitness = 0





    def score():
        global points, game_speed
        points += 1
        if points % 100 == 0:
            game_speed += 1
        
        text = font.render("points: "+ str(points), True , (0, 0, 0))
        textRect =  text.get_rect()
        textRect.center = (1000, 40)
        SCREEN.blit(text, textRect)
        
    

    def background ():
        global x_pos_bg, y_pos_bg
        image_width = BG.get_width()
        SCREEN.blit(BG, (x_pos_bg, y_pos_bg))
        SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
        if x_pos_bg <= -image_width:
            SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
            x_pos_bg = 0
        x_pos_bg -= game_speed


    def statistics():
        global dinosaurs, game_speed, ge
        text_1 = font.render(f'Dinosaurs left:  {str(len(dinosaurs))}', True, (0,0,0))
        text_2 = font.render(f'Gen: {pop.generation+1} ', True, (0, 0, 0))
        text_3 = font.render(f'Game Speed: {str(game_speed)}', True, (0, 0, 0))

        SCREEN.blit(text_1, (50, 450))
        SCREEN.blit(text_2, (50,480))
        SCREEN.blit(text_3, (50, 510))
        

    while run : #while loop that runs the game (basic pygame shit)
        for event in pygame.event.get() :
            if event.type == pygame.QUIT: #safely exit with the X button
                run = False
                break
    
        SCREEN.fill((255,255,255)) #white bg


        for dinosaur in dinosaurs:

            dinosaur.update()
            dinosaur.draw(SCREEN)

        if len(dinosaurs) == 0:
            break
        

        

        if len(obstacles) == 0:
            if random.randint(0,2) == 0:
                obstacles.append(SmallCactus (SMALL_CACTUS))
            elif random.randint(0,2) ==1:
                obstacles.append(LargeCactus (LARGE_CACTUS))
            elif random.randint(0,2) == 2:
                obstacles.append(Bird(BIRD))

        for obstacle in obstacles:
            obstacle.draw(SCREEN)
            obstacle.update()
            for i, dinosaur in enumerate(dinosaurs):
                if dinosaur.dino_rect.colliderect(obstacle.rect):
                    ge[i].fitness -= 5
                    remove(i)
                else:
                    ge[i].fitness += 1
            for i, dinosaur in enumerate(dinosaurs):

                output = nets[i].activate((dinosaur.dino_rect.y,
                                        distance((dinosaur.dino_rect.x, dinosaur.dino_rect.y),
                                        obstacle.rect.midtop)))

                if output[0] > 0.5 and dinosaur.dino_rect.y == dinosaur.Y_POS and not dinosaur.dino_duck:
                    dinosaur.dino_jump = True
                    dinosaur.dino_duck = False
                    dinosaur.dino_run = False
                
                elif obstacle.rect.y < 300 and output[1] > 0.5 and not dinosaur.dino_jump:
                    dinosaur.dino_jump = False
                    dinosaur.dino_duck = True
                    dinosaur.dino_run = False
                    if len(obstacles)==0:
                        dinosaur.dino_jump = False
                        dinosaur.dino_duck = False
                        dinosaur.dino_run = True


            


        background()
        statistics()
        cloud.draw(SCREEN)
        cloud.update()

        score()

        clock.tick(30) #refresh rate of the game
        pygame.display.update()


#setup for neat

def run(config_path):
    global pop
    config = neat.config.Config(
        neat.DefaultGenome,
        neat.DefaultReproduction,
        neat.DefaultSpeciesSet,
        neat.DefaultStagnation,
        config_path
    )


    pop = neat.Population(config)
    pop.run(eval_genomes, 15)


if __name__ == '__main__':
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config.txt')
    run(config_path)



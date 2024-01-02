import pygame
import os
import random
pygame.init()

# Global Constants
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

RUNNING = [ pygame.image.load(os.path.join(r"C:\Users\Hrishikesh\Soruce Codes\Project\Assets\Dino", "DinoRun1.png")),
            pygame.image.load(os.path.join(r"C:\Users\Hrishikesh\Soruce Codes\Project\Assets\Dino", "DinoRun2.png"))]
JUMPING =  pygame.image.load(os.path.join(r"C:\Users\Hrishikesh\Soruce Codes\Project\Assets\Dino", "DinoJump.png"))
DUCKING = [pygame.image.load(os.path.join(r"C:\Users\Hrishikesh\Soruce Codes\Project\Assets\Dino", "DinoDuck1.png")),
           pygame.image.load(os.path.join(r"C:\Users\Hrishikesh\Soruce Codes\Project\Assets\Dino", "DinoDuck2.png"))]

SMALL_CACTUS = [ pygame.image.load(os.path.join(r"C:\Users\Hrishikesh\Soruce Codes\Project\Assets\Cactus", "sc1.png")),
             pygame.image.load(os.path.join(r"C:\Users\Hrishikesh\Soruce Codes\Project\Assets\Cactus", "sc2.png")),
            pygame.image.load(os.path.join(r"C:\Users\Hrishikesh\Soruce Codes\Project\Assets\Cactus", "sc3.png"))]
LARGE_CACTUS = [ pygame.image.load(os.path.join(r"C:\Users\Hrishikesh\Soruce Codes\Project\Assets\Cactus", "lc1.png")),
             pygame.image.load(os.path.join(r"C:\Users\Hrishikesh\Soruce Codes\Project\Assets\Cactus", "lc2.png")),
            pygame.image.load(os.path.join(r"C:\Users\Hrishikesh\Soruce Codes\Project\Assets\Cactus", "lc3.png"))]


BIRD =  [pygame.image.load(os.path.join(r"C:\Users\Hrishikesh\Soruce Codes\Project\Assets\Bird", "Bird1.png")),
         pygame.image.load(os.path.join(r"C:\Users\Hrishikesh\Soruce Codes\Project\Assets\Bird", "Bird2.png"))]
CLOUD =  pygame.image.load(os.path.join(r"C:\Users\Hrishikesh\Soruce Codes\Project\Assets\Other", "Cloud.png"))

BG =  pygame.image.load(os.path.join(r"C:\Users\Hrishikesh\Soruce Codes\Project\Assets\Other", "Track.png"))



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

    def update(self, userInput):
        if self.dino_duck:
            self.duck()
        if self.dino_run:
            self.run()
        if self.dino_jump:
            self.jump()

        if self.step_index >= 10:
            self.step_index = 0

        if (userInput[pygame.K_UP] or userInput[pygame.K_SPACE]) and not self.dino_jump:
            self.dino_duck = False
            self.dino_run = False
            self.dino_jump = True
        elif userInput[pygame.K_DOWN] and not self.dino_jump:
            self.dino_duck = True
            self.dino_run = False
            self.dino_jump = False
        elif not (self.dino_jump or userInput[pygame.K_DOWN]):
            self.dino_duck = False
            self.dino_run = True
            self.dino_jump = False

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
        if self.jump_vel < - self.JUMP_VEL:
            self.dino_jump = False
            self.jump_vel = self.JUMP_VEL

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.dino_rect.x, self.dino_rect.y))


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
        self.rect.y = 250
        self.index = 0
    
    def draw(self, SCREEN):
        if self.index >= 9:
            self.index = 0
        SCREEN.blit(self.image[self.index//5], self.rect)
        self.index += 1





def main() :
    global game_speed , x_pos_bg, y_pos_bg , points, obstacles
    run = True
    clock = pygame.time.Clock()
    player = Dinosaur() #instance of dinosaur class
    cloud = Cloud()
    game_speed = 14
    x_pos_bg = 0
    y_pos_bg = 380
    points = 0
    font = pygame.font.Font('freesansbold.ttf', 20)
    obstacles=[]

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



    while run : #while loop that runs the game (basic pygame shit)
        for event in pygame.event.get() :
            if event.type == pygame.QUIT: #safely exit with the X button
                run = False
    
        SCREEN.fill((255,255,255)) #white bg
        userInput = pygame.key.get_pressed() 

        player.draw(SCREEN)
        player.update(userInput)

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
            if player.dino_rect.colliderect(obstacle.rect):
                pygame.draw.rect(SCREEN, (255, 0, 0), player.dino_rect, 2)

        background()

        cloud.draw(SCREEN)
        cloud.update()

        score()

        clock.tick(30) #refresh rate of the game
        pygame.display.update()




main()
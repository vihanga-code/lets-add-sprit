import pygame
import random
pygame.init()
sprit_change_event=pygame.USEREVENT+1
background_change_event=pygame.USEREVENT+2
blue=pygame.Color("blue")
orange=pygame.Color("orange")
green=pygame.Color("green")
red=pygame.Color("red")
black=pygame.Color("black")
limegreen=pygame.Color("limegreen")
lavender=pygame.Color("lavender")
class Sprite(pygame.sprite.Sprite):
    def __init__(self,color,width,height):
        super().__init__()
        self.image=pygame.Surface([width,height])
        self.image.fill(color)
        self.rect=self.image.get_rect()
        self.velocity=[random.choice([-1,1]),random.choice([-1,1])]
    def update(self):
        self.rect.move_ip(self.velocity)
        boundry=False
        if self.rect.left<=0 or self.rect.right>=500:
            self.velocity[0]=-self.velocity[0]
            boundry=True
        if self.rect.top<=0 or self.rect.bottom>=400:
             self.velocity[1]=-self.velocity[1]
             boundry=True
        if boundry:

            pygame.event.post(pygame.event.Event(sprit_change_event))
            pygame.event.post(pygame.event.Event(background_change_event))
    def change_color(self):
        self.image.fill(random.choice([blue,orange,green,red]))        
    def background(self):
        global bgcolor
        bgcolor=random.choice([black,limegreen,lavender])
all_sprite=pygame.sprite.Group()
Sp1=Sprite(lavender,20,30)
Sp1.rect.x=random.randint(0,480) 
Sp1.rect.y=random.randint(0,370)           
all_sprite.add(Sp1)
screen=pygame.display.set_mode((500,400))
bgcolor=blue
screen.fill(bgcolor)
exit=False
clock=pygame.time.Clock()
while not exit:
      # Event handling loop
    for event in pygame.event.get():
    # If the window's close button is clicked, exit the game
        if event.type == pygame.QUIT:
           exit = True
    # If the sprite color change event is triggered, change the sprite's color
        elif event.type == sprit_change_event:
             Sp1.change_color()
    # If the background color change event is triggered, change the background color
        elif event.type == background_change_event:
            Sp1.background()

  # Update all sprites
    all_sprite.update()
  # Fill the screen with the current background color
    screen.fill(bgcolor)
  # Draw all sprites to the screen
    all_sprite.draw(screen)

  # Refresh the display
    pygame.display.flip()
  # Limit the frame rate to 240 fps
    clock.tick(240)

# Uninitialize all pygame modules and close the window
pygame.quit()
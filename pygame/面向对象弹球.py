import sys,pygame

class Ball:
    def __init__(self,x,y):
        self.ball_x = x
        self.ball_y = y
        self.ball_x_speed = 7
        self.ball_y_speed = 7
        self.ball_pic = pygame.image.load("ball.png")

    #更新位置和速度
    def update(self):
        self.ball_x +=self.ball_x_speed
        self.ball_y +=self.ball_y_speed

        if self.ball_x> 320:self.ball_x_speed = -7
        if self.ball_y> 180:self.ball_y_speed = -7
        if self.ball_x<-150: self.ball_x_speed = 7
        if self.ball_y<-120: self.ball_y_speed = 7

    def render(self):
        screen.blit(self.ball_pic,(self.ball_x,self.ball_y))

pygame.init()

screen = pygame.display.set_mode((640,480))

ball1 = Ball(240,87)
ball2 = Ball(200,25)
ball3 = Ball(180,254)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill((90,230,90))

    ball1.update()
    ball1.render()
    ball2.update()
    ball2.render()
    ball3.update()
    ball3.render()

    pygame.display.flip()
    pygame.time.wait(10)
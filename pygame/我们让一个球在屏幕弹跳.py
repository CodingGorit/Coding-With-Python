import  sys,pygame

pygame.init()

screen = pygame.display.set_mode((640,480))

ball = pygame.image.load("ball.png")

#球的初始位置，屏幕的左上角为（0,0）然后往右是x轴，往下是y轴
ball_x = 10
ball_y = 10

#每次循环球位置的增加量
ball_x_speed =7
ball_y_speed =7

while 1:

    #检查操作系统事件中，如果窗口关闭则退出
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

#更新球的x，y坐标
    ball_x += ball_x_speed
    ball_y += ball_y_speed

#如果弹球碰到右侧，将速度设置为负值
    if ball_x>320: ball_x_speed =-7
    if ball_y>180: ball_y_speed =-7
#同理撞到左侧会反向
    if ball_x<-180: ball_x_speed = 7
    if ball_y<-160: ball_y_speed = 7

#RGB填充颜色
    screen.fill((90,230,90))

#指定x，y的坐标绘制球
    screen.blit(ball,(ball_x,ball_y))

#将球的碰撞状态展现到屏幕
    pygame.display.flip()
    pygame.time.wait(10)
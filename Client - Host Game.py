import socket
import pygame
import random
import threading

pygame.init()

HOST = ''
PORT = ''

WIDTH = 1200
HEIGHT = 800

screen = pygame.display.set_mode([WIDTH,HEIGHT])
clock = pygame.time.Clock()

fps = 165

class Player():
    
    def __init__(self, x, y, size, speed, name, color):
        self.x = x
        self.y = y
        self.size = size
        self.speed = speed / fps

        txt = pygame.font.SysFont("Arial", 20)
        self.name = txt.render(name, True, (255,255,255))

        self.color = color


    def detect(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.y -= self.speed
        if keys[pygame.K_s]:
            self.y += self.speed
        if keys[pygame.K_a]:
            self.x -= self.speed
        if keys[pygame.K_d]:
            self.x += self.speed

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x,self.y,self.size,self.size))
        screen.blit(self.name, (self.x, self.y-26, 20, 20))

def refresh_screen():
    screen.fill((0,0,0))

def foreign_player_draw(data):
    for client in data[0]:
        if client != data[1]:
            txt = pygame.font.SysFont("Arial", 20)
            player_name = txt.render(data[0][client][3], True, (255,255,255))
            screen.blit(player_name, (data[0][client][0], data[0][client][1]-28, data[0][client][4], data[0][client][4]))
            pygame.draw.rect(screen, data[0][client][2], (data[0][client][0], data[0][client][1], data[0][client][4], data[0][client][4]))

def menu_screen():
    global HOST, PORT
    run = True

    txt = pygame.font.SysFont("Arial", 30)
    host_txt  = txt.render("Host a game", True, (255,255,255))
    join_txt  = txt.render("Join a game", True, (255,255,255))
    back_txt = txt.render("Back", True, (255,255,255))

    host_button = pygame.Rect(40,20,200,50)
    join_button = pygame.Rect(40,70,200,50)
    back_button = pygame.Rect(WIDTH - 200,20,100,50)

    # host_game


    while run:
        clock.tick(10)
        refresh_screen()
        screen.blit(host_txt, host_button)
        screen.blit(join_txt, join_button)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if host_button.collidepoint(event.pos):
                    host_game()
                    user_input = create_name()
                    main(user_input, True)

            try:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if join_button.collidepoint(event.pos):
                        HOST = join_game("ip address of the host")
                        PORT = int(join_game("host's port number"))

                        user_input = create_name()
                        main(user_input, False)
            except Exception as e:
                error_screen(e)


        pygame.display.update()

def host_game():
    global HOST, PORT

    refresh_screen()

    hostname=socket.gethostname()
    IPAddr=socket.gethostbyname(hostname)

    HOST = IPAddr  # Standard loopback interface address (localhost)
    PORT = int(join_game("a port number you would like to open (ex. 65432)"))  # Port to listen on (non-privileged ports are > 1023)

def join_game(ip_or_port):
    run = True
    user_input = ''
    txt = pygame.font.SysFont("Arial", 30)
    host_txt = txt.render(f"Please enter the {ip_or_port} (press Esc to enter):", True, (255,255,255))
    
    while run:
        clock.tick(10)
        keys = pygame.key.get_pressed()
        refresh_screen()

        for event in pygame.event.get():

            if keys[pygame.K_0]:
                user_input += '0'
            if keys[pygame.K_1]:
                user_input += '1'
            if keys[pygame.K_2]:
                user_input += '2'
            if keys[pygame.K_3]:
                user_input += '3'
            if keys[pygame.K_4]:
                user_input += '4'
            if keys[pygame.K_5]:
                user_input += '5'
            if keys[pygame.K_6]:
                user_input += '6'
            if keys[pygame.K_7]:
                user_input += '7'
            if keys[pygame.K_8]:
                user_input += '8'
            if keys[pygame.K_9]:
                user_input += '9'
            if keys[pygame.K_PERIOD]:
                user_input += '.'
            if len(user_input) > 0:
                if keys[pygame.K_BACKSPACE]:
                    user_input = user_input.strip(user_input[-1])
            if keys[pygame.K_ESCAPE]:
                run = False

        ip_txt = txt.render(user_input, True, (255,255,255))
        screen.blit(ip_txt, (40,80,200,50))
        screen.blit(host_txt, (40,20,200,50))

        pygame.display.update()

    return user_input

def character_customization():
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()

def create_name():
    run = True
    user_input = ''
    txt = pygame.font.SysFont("Arial", 30)
    create_name = txt.render("Please Write Your Player Name (press Esc to enter):", True, (255,255,255))
    while run:
        clock.tick(10)
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():

            if keys[pygame.K_b]:
                user_input += 'b'
            if keys[pygame.K_c]:
                user_input += 'c'
            if keys[pygame.K_e]:
                user_input += 'e'
            if keys[pygame.K_f]:
                user_input += 'f'
            if keys[pygame.K_g]:
                user_input += 'g'
            if keys[pygame.K_h]:
                user_input += 'h'
            if keys[pygame.K_i]:
                user_input += 'i'
            if keys[pygame.K_j]:
                user_input += 'j'
            if keys[pygame.K_k]:
                user_input += 'k'
            if keys[pygame.K_l]:
                user_input += 'l'
            if keys[pygame.K_m]:
                user_input += 'm'
            if keys[pygame.K_n]:
                user_input += 'n'
            if keys[pygame.K_o]:
                user_input += 'o'
            if keys[pygame.K_p]:
                user_input += 'p'
            if keys[pygame.K_q]:
                user_input += 'q'
            if keys[pygame.K_r]:
                user_input += 'r'
            if keys[pygame.K_t]:
                user_input += 't'
            if keys[pygame.K_u]:
                user_input += 'u'
            if keys[pygame.K_v]:
                user_input += 'v'
            if keys[pygame.K_x]:
                user_input += 'x'
            if keys[pygame.K_y]:
                user_input += 'y'
            if keys[pygame.K_z]:
                user_input += 'z'
            if keys[pygame.K_w]:
                user_input += 'w'
            if keys[pygame.K_s]:
                user_input += 's'
            if keys[pygame.K_a]:
                user_input += 'a'
            if keys[pygame.K_d]:
                user_input += 'd'
            if len(user_input) > 0:
                if keys[pygame.K_BACKSPACE]:
                    user_input = user_input.strip(user_input[-1])
            if keys[pygame.K_ESCAPE]:
                run = False

        refresh_screen()
        screen.blit(create_name, (40,20,200,50))
        name_txt  = txt.render(user_input, True, (255,255,255))
        screen.blit(name_txt, (40,80,200,50))

        pygame.display.update()

    return user_input

def error_screen(e):
    txt = pygame.font.SysFont("Arial", 30)
    if "11001" in f"{e}":
        error_txt = txt.render("Looks like there was an error finding the host :(", True, (255,255,255))
    elif "''" in f"{e}":
        error_txt = txt.render("You can't just type in nothing when entering IP or Port number!", True, (255,255,255))
    else:
        error_txt = txt.render("Looks like there was an error...", True, (255,255,255))
    error_msg = txt.render(f"{e}", True, (255,255,255))
    continue_txt = txt.render("Click to continue...", True, (255,255,255))

    continue_button = pygame.Rect((40,140,300,50))

    run = True

    while run:

        refresh_screen()
        screen.blit(error_txt,(40,20,300,50))
        screen.blit(error_msg,(40,80,300,50))
        screen.blit(continue_txt,continue_button)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if continue_button.collidepoint(event.pos):
                    run = False
                    break

        pygame.display.update()

def main(user_input, open_port):

    if open_port:
        x = threading.Thread(target=server, daemon=True)
        x.start()

    run = True
    ran_int = []
    ran_int.append(random.randint(80,255))
    ran_int.append(random.randint(80,255))
    ran_int.append(random.randint(80,255))
    player = Player(10,10,40,300,user_input, (ran_int))
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            while run:
                clock.tick(fps)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        s.sendall(bytes(str(["close"]), "utf-8"))
                        run = False

                refresh_screen()

                player.detect()
                #                       0      1           2           3            4
                s.sendall(bytes(str([player.x,player.y, player.color, user_input, player.size]), "utf-8"))

                try:
                    data = eval(s.recv(2024))
                except Exception as e:
                    if "10054" in f"{e}":
                        print("The server closed succesfully...")
                    else:
                        error_screen(e)

                foreign_player_draw(data)
                player.draw()

                pygame.display.update()
    except Exception as e:
        error_screen(e)

def server():
    run = True

    def player_data(conn, addr):
        print(f"Threaded connection with {addr[0]} on port {addr[1]} started...")
        with conn:
            while True:
                client_data[addr[0]] = eval(conn.recv(2024))
                if client_data[addr[0]] == ["close"]:
                    client_data.pop(addr[0])
                    print(f"Threaded connection with {addr[0]} on port {addr[1]} finished...")
                    return
                conn.sendall(bytes(str([client_data, addr[0]]), "utf-8"))

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

        client_data = {}
        s.bind((HOST, PORT))
        s.listen()
        
        while run:
        
            conn, addr = s.accept()

            x = threading.Thread(target=player_data, args=(conn, addr))
        
            x.start()

            # print(threading.active_count())

menu_screen()
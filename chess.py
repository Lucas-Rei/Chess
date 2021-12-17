from pygame import *
import pygame

def turn_flip():
    global turn
    if turn:
        turn = False
    
    elif not turn:
        turn = True

# GameSprite class
class GameSprite(sprite.Sprite): 
    def __init__(self, sprite_image, size1, size2, coord, color = "white", select = False):
        super().__init__()
        self.size1 = size1
        self.size2 = size2
        self.image = transform.scale(pygame.image.load(sprite_image), (self.size1, self.size2))
        self.rect = self.image.get_rect()
        self.coord = coord
        self.color = color
        self.select = select
        self.stop = 1


    def reset(self):
        if self.coord[0] == 0:
            self.rect.x = x_positions[0]
        if self.coord[0] == 1:
            self.rect.x = x_positions[1]
        if self.coord[0] == 2:
            self.rect.x = x_positions[2]
        if self.coord[0] == 3:
            self.rect.x = x_positions[3]
        if self.coord[0] == 4:
            self.rect.x = x_positions[4]
        if self.coord[0] == 5:
            self.rect.x = x_positions[5]
        if self.coord[0] == 6:
            self.rect.x = x_positions[6]
        if self.coord[0] == 7:
            self.rect.x = x_positions[7]

        if self.coord[0] == -1:
            self.rect.x = 99999

        if self.coord[1] == 0:
            self.rect.y = y_positions[0]
        if self.coord[1] == 1:
            self.rect.y = y_positions[1]
        if self.coord[1] == 2:
            self.rect.y = y_positions[2]
        if self.coord[1] == 3:
            self.rect.y = y_positions[3]
        if self.coord[1] == 4:
            self.rect.y = y_positions[4]
        if self.coord[1] == 5:
            self.rect.y = y_positions[5]
        if self.coord[1] == 6:
            self.rect.y = y_positions[6]
        if self.coord[1] == 7:
            self.rect.y = y_positions[7]

        window.blit(self.image, (self.rect.x, self.rect.y))


class MoveSpace(GameSprite):
    def update(self):
        if pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos()):
            for piece in piece_group:
                if piece.select == True:
                    for piece2 in piece_group:
                        if piece2.coord == self.coord:
                            piece2.kill()
                            # probably add capturing noises and other shenanegins
                    piece.coord = self.coord
                    piece.select = False
                    sprite.Group.empty(moveSpace_group)
                    turn_flip()


class King(GameSprite):
    pass

class Queen(GameSprite):
    pass

class Bishop(GameSprite):
    pass

class Knight(GameSprite):
    pass

class Rook(GameSprite):
    def update(self):
        # generating movespaces
        if pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos()) and not self.select:
            self.select = True

            # generate left
            x_var = self.coord[0] - 1
            self.stop = 1
            for i in range(7):
                if self.stop == 3:
                    break

                # check for collisions with own pieces
                for piece in piece_group:
                    if piece.coord == [x_var, self.coord[1]]:
                        if piece.color == self.color:
                            self.stop = 2

                        elif piece.color != self.color:
                            self.stop = 3
                        

                if x_var < 0 or self.stop == 2:
                    break   


                new = MoveSpace("circle.png", 60, 60, [x_var, self.coord[1]])
                moveSpace_group.add(new)
                x_var -= 1

            # generate up
            y_var = self.coord[1] + 1
            self.stop = 1
            for i in range(7):
                if self.stop == 3:
                    break

                # check for collisions with own pieces
                for piece in piece_group:
                    if piece.coord == [self.coord[0], y_var]:
                        if piece.color == self.color:
                            self.stop = 2

                        elif piece.color != self.color:
                            self.stop = 3
                        

                if y_var > 7 or self.stop == 2:
                    break   


                new = MoveSpace("circle.png", 60, 60, [self.coord[0], y_var])
                moveSpace_group.add(new)
                y_var += 1

            # generate right
            x_var = self.coord[0] + 1
            self.stop = 1
            for i in range(7):  

                if self.stop == 3:
                    break

                # check for collisions with own pieces
                for piece in piece_group:
                    if piece.coord == [x_var, self.coord[1]]:
                        if piece.color == self.color:
                            self.stop = 2

                        elif piece.color != self.color:
                            self.stop = 3
                        

                if x_var > 7 or self.stop == 2:
                    break             
                        

                new = MoveSpace("circle.png", 60, 60, [x_var, self.coord[1]])
                moveSpace_group.add(new)
                x_var += 1

            # generate down
            y_var = self.coord[1] - 1
            self.stop = 1
            for i in range(7):
                if self.stop == 3:
                    break

                # check for collisions with own pieces
                for piece in piece_group:
                    if piece.coord == [self.coord[0], y_var]:
                        if piece.color == self.color:
                            self.stop = 2

                        elif piece.color != self.color:
                            self.stop = 3
                        

                if y_var < 0 or self.stop == 2:
                    break   


                new = MoveSpace("circle.png", 60, 60, [self.coord[0], y_var])
                moveSpace_group.add(new)
                y_var -= 1

class Pawn(GameSprite):
    pass


# creation

piece_group = sprite.Group()
white_sub = sprite.Group()
black_sub = sprite.Group()
moveSpace_group = sprite.Group()

window = display.set_mode((640, 640))
display.set_caption("Chess!")

board = transform.scale(image.load("chess board sample.png"), (640, 640))

blackRook1 = Rook("black rook.png", 60, 60, [4, 4], "black")
piece_group.add(blackRook1)
black_sub.add(blackRook1)

blackRook2 = Rook("black rook.png", 60, 60, [1, 4], "black")
piece_group.add(blackRook2)
black_sub.add(blackRook2)

whiteRook1 = Rook("white rook.jfif", 60, 60, [6, 4], "white")
piece_group.add(whiteRook1)
white_sub.add(whiteRook1)


# positions and other stuff

run = True
turn = False
FPS = 60
clock = time.Clock()

x_positions = [10, 90, 170, 250, 330, 410, 490, 570]
y_positions = [570, 490, 410, 330, 250, 170, 90, 10]



while run:
    key_list = key.get_pressed()
    for e in event.get():
        if e.type == QUIT:
            run = False

    #blit shite
    window.blit(board, (0, 0))
    for piece in piece_group:
        piece.reset()

    for space in moveSpace_group:
        space.reset()

    #updating
    if turn:
        white_sub.update()

    if not turn:
        black_sub.update()

    moveSpace_group.update()

    pygame.display.update()
    clock.tick(FPS)

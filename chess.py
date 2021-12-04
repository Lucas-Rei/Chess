from pygame import *
import pygame

# GameSprite class
class GameSprite(sprite.Sprite): 
    def __init__(self, sprite_image, size1, size2, coord, select = False):
        super().__init__()
        self.size1 = size1
        self.size2 = size2
        self.image = transform.scale(pygame.image.load(sprite_image), (self.size1, self.size2))
        self.rect = self.image.get_rect()
        self.coord = coord
        self.select = select


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
                    piece.coord = self.coord
                    piece.select = False
                    self.coord[0] = -1


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
        # test shit
        key_list = key.get_pressed()
        if key_list[K_RIGHT]: 
            self.coord[0] += 1
        if key_list[K_LEFT]: 
            self.coord[0] -= 1
        if key_list[K_UP]:
            self.coord[1] -= 1
        if key_list[K_DOWN]:
            self.coord[1] += 1

        if pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos()):
            self.select = True

            print("ready to move")

            for i in range(8):
                pass

class Pawn(GameSprite):
    pass


# creation

piece_group = sprite.Group()
MoveSpace_list = sprite.Group()

window = display.set_mode((600, 600))
display.set_caption("Chess!")

board = transform.scale(image.load("chess board sample.png"), (600, 600))

blackRook1 = Rook("black rook.png", 60, 60, [0, 0])
piece_group.add(blackRook1)

test = MoveSpace("circle.png", 60, 60, [3,2])




# positions and other stuff

run = True
FPS = 60
clock = time.Clock()

x_positions = [10, 85, 160, 235, 310, 385, 460, 535]
y_positions = [10, 85, 160, 235, 310, 385, 460, 535]



while run:
    key_list = key.get_pressed()
    for e in event.get():
        if e.type == QUIT:
            run = False

    #blit shite
    window.blit(board, (0, 0))
    blackRook1.reset()
    test.reset()

    #updating
    blackRook1.update()
    test.update()

    pygame.display.update()
    clock.tick(FPS)
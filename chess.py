from pygame import *
import pygame


def turn_flip():
    global turn
    if turn:
        turn = False
    
    elif not turn:
        turn = True


def generate_spaces(click_piece):
    sprite.Group.empty(moveSpace_group)
    for piece in piece_group:
        piece.select = False

    click_piece.select = True

    for ray in click_piece.move_set:
        for coord in ray:
            moveSpace_group.add(MoveSpace("circle.png", 60, 60, coord))

def check_bounds(coord):
    if coord[0] < 0 or coord[0] > 7 or coord[1] < 0 or coord[1] > 7:
        return False
    else:
        return True

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
        self.move_set = []
        self.check = False
        self.attacking = False


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
                    piece.update()
                    if piece.stop == 0:
                        piece.firstMove = False
               



# this is "spot" generating
# this is fookin bugged mate
class King(GameSprite):
    def update(self):
        self.move_set.clear()
        # generate bottom-left
        self.stop = 1
        ray = []
        # make sure it isn't out of bounds
        if not self.coord[0] - 1 < 0 and not self.coord[1] - 1 < 0: 
            for piece in piece_group:
                # check for collision with allies
                if piece.coord == [self.coord[0] - 1, self.coord[1] - 1] and piece.color == self.color:
                    self.stop = 2
                    break
                # check for enemies within view
                for ray in piece.move_set:
                    for coord in ray:
                        if coord == [self.coord[0] - 1, self.coord[1] - 1] and piece.color != self.color:
                            self.stop = 2
                            break
            
            if self.stop != 2:
                ray.append([self.coord[0] - 1, self.coord[1] - 1])
        
        self.move_set.append(ray)
        
        # generate left
        self.stop = 1
        ray = []
        if not self.coord[0] - 1 < 0: 
            for piece in piece_group:
                if piece.coord == [self.coord[0] - 1, self.coord[1]] and piece.color == self.color:
                    self.stop = 2
                    break
                for ray in piece.move_set:
                    for coord in ray:
                        if coord == [self.coord[0] - 1, self.coord[1]] and piece.color != self.color:
                            self.stop = 2
                            break
            
            if self.stop != 2:
                ray.append([self.coord[0] - 1, self.coord[1]])
        
        self.move_set.append(ray)

        # generate top-left
        self.stop = 1
        ray = []
        if not self.coord[0] - 1 < 0 and not self.coord[1] + 1 < 0: 
            for piece in piece_group:
                if piece.coord == [self.coord[0] - 1, self.coord[1] + 1] and piece.color == self.color:
                    self.stop = 2
                    break
                for ray in piece.move_set:
                    for coord in ray:
                        if coord == [self.coord[0] - 1, self.coord[1] + 1] and piece.color != self.color:
                            self.stop = 2
                            break
            
            if self.stop != 2:
                ray.append([self.coord[0] - 1, self.coord[1] + 1])
        
        self.move_set.append(ray)

        # generate up
        self.stop = 1
        ray = []
        if not self.coord[1] + 1 > 7: 
            for piece in piece_group:
                if piece.coord == [self.coord[0], self.coord[1] + 1] and piece.color == self.color:
                    self.stop = 2
                    break
                for ray in piece.move_set:
                    for coord in ray:
                        if coord == [self.coord[0], self.coord[1] + 1] and piece.color != self.color:
                            self.stop = 2
                            break
            
            if self.stop != 2:
                ray.append([self.coord[0], self.coord[1] + 1])
        
        self.move_set.append(ray)

        # generate top-right
        self.stop = 1
        ray = []
        if not self.coord[0] + 1 > 7 and not self.coord[1] + 1 > 7: 
            for piece in piece_group:
                if piece.coord == [self.coord[0] + 1, self.coord[1] + 1] and piece.color == self.color:
                    self.stop = 2
                    break
                for ray in piece.move_set:
                    for coord in ray:
                        if coord == [self.coord[0] + 1, self.coord[1] + 1] and piece.color != self.color:
                            self.stop = 2
                            break
            
            if self.stop != 2:
                ray.append([self.coord[0] + 1, self.coord[1] + 1])
        
        self.move_set.append(ray)

        # generate right
        self.stop = 1
        ray = []
        if not self.coord[0] + 1 > 7: 
            for piece in piece_group:
                if piece.coord == [self.coord[0] + 1, self.coord[1]] and piece.color == self.color:
                    self.stop = 2
                    break
                for ray in piece.move_set:
                    for coord in ray:
                        if coord == [self.coord[0] + 1, self.coord[1]] and piece.color != self.color:
                            self.stop = 2
                            break
            
            if self.stop != 2:
                ray.append([self.coord[0] + 1, self.coord[1]])
        
        self.move_set.append(ray)

        # generate bottom-right
        self.stop = 1
        ray = []
        if not self.coord[0] + 1 > 7 and not self.coord[1] - 1 < 0: 
            for piece in piece_group:
                if piece.coord == [self.coord[0] + 1, self.coord[1] - 1] and piece.color == self.color:
                    self.stop = 2
                    break
                for ray in piece.move_set:
                    for coord in ray:
                        if coord == [self.coord[0] + 1, self.coord[1] - 1] and piece.color != self.color:
                            self.stop = 2
                            break
            
            if self.stop != 2:
                ray.append([self.coord[0] + 1, self.coord[1] - 1])
        
        self.move_set.append(ray)

        # generate down
        self.stop = 1
        ray = []
        if not self.coord[1] - 1 < 0: 
            for piece in piece_group:
                if piece.coord == [self.coord[0], self.coord[1] - 1] and piece.color == self.color:
                    self.stop = 2
                    break
                for ray in piece.move_set:
                    for coord in ray:
                        if coord == [self.coord[0], self.coord[1] - 1] and piece.color != self.color:
                            self.stop = 2
                            break
            
            if self.stop != 2:
                ray.append([self.coord[0], self.coord[1] - 1])
        
        self.move_set.append(ray)

        if pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos()) and not self.select:
            generate_spaces(self)

    def check_check(self):
        # checking for enemy check
        if self.color == "white":
            for enemy in black_sub:
                for coord in enemy.move_set:
                    if coord == self.coord:
                        enemy.attacking = True
                        for piece in white_sub:
                            piece.check = True
                        print("check on white")

        elif self.color == "black":
            for enemy in white_sub:
                for coord in enemy.move_set:
                    if coord == self.coord:
                        for piece in black_sub:
                            piece.check = True
                        print("check on white")
            
            
class Queen(GameSprite):
    def update(self):
        self.move_set.clear()
        # generate top-left
        x_var = self.coord[0] - 1
        y_var = self.coord[1] + 1
        self.stop = 1 
        ray = []
        for i in range(7):
            if self.stop == 3:
                break
            for piece in piece_group:
                if piece.coord == [x_var, y_var]:
                    if piece.color == self.color:
                        self.stop = 2
                    elif piece.color != self.color:
                        self.stop = 3
                    
            if x_var < 0 or y_var > 7 or self.stop == 2:
                break   
            ray.append([x_var, y_var])
            x_var -= 1
            y_var += 1
        
        self.move_set.append(ray)


        # generate top-right
        x_var = self.coord[0] + 1
        y_var = self.coord[1] + 1
        self.stop = 1
        ray = []
        for i in range(7):
            if self.stop == 3:
                break
            for piece in piece_group:
                if piece.coord == [x_var, y_var]:
                    if piece.color == self.color:
                        self.stop = 2
                    elif piece.color != self.color:
                        self.stop = 3
                    
            if x_var > 7 or y_var > 7 or self.stop == 2:
                break   
            ray.append([x_var, y_var])
            x_var += 1
            y_var += 1

        self.move_set.append(ray)


        # generate bottom-right
        x_var = self.coord[0] + 1
        y_var = self.coord[1] - 1
        self.stop = 1
        ray = []
        for i in range(7):
            if self.stop == 3:
                break
            for piece in piece_group:
                if piece.coord == [x_var, y_var]:
                    if piece.color == self.color:
                        self.stop = 2
                    elif piece.color != self.color:
                        self.stop = 3
                    
            if x_var > 7 or y_var < 0 or self.stop == 2:
                break   
            ray.append([x_var, y_var])
            x_var += 1
            y_var -= 1

        self.move_set.append(ray)


        # generate bottom-left
        x_var = self.coord[0] - 1
        y_var = self.coord[1] - 1
        self.stop = 1
        ray = []
        for i in range(7):
            if self.stop == 3:
                break
            for piece in piece_group:
                if piece.coord == [x_var, y_var]:
                    if piece.color == self.color:
                        self.stop = 2
                    elif piece.color != self.color:
                        self.stop = 3
                    
            if x_var < 0 or y_var < 0 or self.stop == 2:
                break   
            ray.append([x_var, y_var])
            x_var -= 1
            y_var -= 1

        self.move_set.append(ray)

        ###############################

        # generate left
        x_var = self.coord[0] - 1
        self.stop = 1
        ray = []
        for i in range(7):
            if self.stop == 3:
                break

            for piece in piece_group:
                if piece.coord == [x_var, self.coord[1]]:
                    if piece.color == self.color:
                        self.stop = 2
                    elif piece.color != self.color:
                        self.stop = 3
                    
            if x_var < 0 or self.stop == 2:
                break   

            ray.append([x_var, self.coord[1]])
            x_var -= 1

        self.move_set.append(ray)

        # generate up
        y_var = self.coord[1] + 1
        self.stop = 1
        ray = []
        for i in range(7):
            if self.stop == 3:
                break
            for piece in piece_group:
                if piece.coord == [self.coord[0], y_var]:
                    if piece.color == self.color:
                        self.stop = 2
                    elif piece.color != self.color:
                        self.stop = 3
                    
            if y_var > 7 or self.stop == 2:
                break   
            ray.append([self.coord[0], y_var])
            y_var += 1

        self.move_set.append(ray)

        # generate right
        x_var = self.coord[0] + 1
        self.stop = 1
        ray = []
        for i in range(7):  
            if self.stop == 3:
                break
            for piece in piece_group:
                if piece.coord == [x_var, self.coord[1]]:
                    if piece.color == self.color:
                        self.stop = 2
                    elif piece.color != self.color:
                        self.stop = 3
                    
            if x_var > 7 or self.stop == 2:
                break             
                    
            ray.append([x_var, self.coord[1]])
            x_var += 1

        self.move_set.append(ray)

        # generate down
        y_var = self.coord[1] - 1
        self.stop = 1
        ray = []
        for i in range(7):
            if self.stop == 3:
                break
            for piece in piece_group:
                if piece.coord == [self.coord[0], y_var]:
                    if piece.color == self.color:
                        self.stop = 2
                    elif piece.color != self.color:
                        self.stop = 3
                    
            if y_var < 0 or self.stop == 2:
                break   

            ray.append([self.coord[0], y_var])
            y_var -= 1

        self.move_set.append(ray)


        # generating movespaces
        if pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos()) and not self.select and not self.check:
            generate_spaces(self)



# time to explain this stuff
# this is "continous" generating
class Bishop(GameSprite): 
    def update(self):
        self.move_set.clear()
        # generate top-left
        x_var = self.coord[0] - 1
        y_var = self.coord[1] + 1
        self.stop = 1 
        ray = []
        for i in range(7):
            # this means the piece has generated a space, and will be able to move onto the enemy piece
            if self.stop == 3:
                break
            # check for collisions with pieces
            for piece in piece_group:
                if piece.coord == [x_var, y_var]:
                    # change stop property based on piece properties
                    if piece.color == self.color:
                        self.stop = 2
                    elif piece.color != self.color:
                        self.stop = 3
                    
            # this means the piece is going out of bounds or is targeting an ally, it will not generate a space
            if x_var < 0 or y_var > 7 or self.stop == 2:
                break  

            ray.append([x_var, y_var])
            x_var -= 1
            y_var += 1
        
        self.move_set.append(ray)


        # generate top-right
        x_var = self.coord[0] + 1
        y_var = self.coord[1] + 1
        self.stop = 1
        ray = []
        for i in range(7):
            if self.stop == 3:
                break
            for piece in piece_group:
                if piece.coord == [x_var, y_var]:
                    if piece.color == self.color:
                        self.stop = 2
                    elif piece.color != self.color:
                        self.stop = 3
                    
            if x_var > 7 or y_var > 7 or self.stop == 2:
                break   

            ray.append([x_var, y_var])
            x_var += 1
            y_var += 1

        self.move_set.append(ray)


        # generate bottom-right
        x_var = self.coord[0] + 1
        y_var = self.coord[1] - 1
        self.stop = 1
        ray = []
        for i in range(7):
            if self.stop == 3:
                break
            for piece in piece_group:
                if piece.coord == [x_var, y_var]:
                    if piece.color == self.color:
                        self.stop = 2
                    elif piece.color != self.color:
                        self.stop = 3
                    
            if x_var > 7 or y_var < 0 or self.stop == 2:
                break 

            ray.append([x_var, y_var])
            x_var += 1
            y_var -= 1

        self.move_set.append(ray)


        # generate bottom-left
        x_var = self.coord[0] - 1
        y_var = self.coord[1] - 1
        self.stop = 1
        ray = []
        for i in range(7):
            if self.stop == 3:
                break
            for piece in piece_group:
                if piece.coord == [x_var, y_var]:
                    if piece.color == self.color:
                        self.stop = 2
                    elif piece.color != self.color:
                        self.stop = 3
                    
            if x_var < 0 or y_var < 0 or self.stop == 2:
                break   

            ray.append([x_var, y_var])
            x_var -= 1
            y_var -= 1

        self.move_set.append(ray)


        # generating movespaces
        if pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos()) and not self.select and not self.check:
            generate_spaces(self)



class Knight(GameSprite):
    def update(self):
        # strong is y movement of 2, strong is y movement of 1
        # weak top-left
        self.move_set.clear()
        self.stop = 1
        ray = []
        if check_bounds([self.coord[0] - 2, self.coord[1] + 1]): 
            for piece in piece_group:
                if piece.coord == [self.coord[0] - 2, self.coord[1] + 1]:
                    if piece.color == self.color:
                        self.stop = 2
            
            if self.stop != 2:
                ray.append([self.coord[0] - 2, self.coord[1] + 1])

        self.move_set.append(ray)
        
        # strong top-left
        self.stop = 1
        ray = []
        if check_bounds([self.coord[0] - 1, self.coord[1] + 2]): 
            for piece in piece_group:
                if piece.coord == [self.coord[0] - 1, self.coord[1] + 2]:
                    if piece.color == self.color:
                        self.stop = 2
            
            if self.stop != 2:
                ray.append([self.coord[0] - 1, self.coord[1] + 2])

        self.move_set.append(ray)

        # strong top-right
        self.stop = 1
        ray = []
        if check_bounds([self.coord[0] + 1, self.coord[1] + 2]): 
            for piece in piece_group:
                if piece.coord == [self.coord[0] + 1, self.coord[1] + 2]:
                    if piece.color == self.color:
                        self.stop = 2
            
            if self.stop != 2:
                ray.append([self.coord[0] + 1, self.coord[1] + 2])

        self.move_set.append(ray)

        # weak top-right
        self.stop = 1
        ray = []
        if check_bounds([self.coord[0] + 2, self.coord[1] + 1]): 
            for piece in piece_group:
                if piece.coord == [self.coord[0] + 2, self.coord[1] + 1]:
                    if piece.color == self.color:
                        self.stop = 2
            
            if self.stop != 2:
                ray.append([self.coord[0] + 2, self.coord[1] + 1])

        self.move_set.append(ray)

        # weak bottom-right
        self.stop = 1
        ray = []
        if check_bounds([self.coord[0] + 2, self.coord[1] - 1]): 
            for piece in piece_group:
                if piece.coord == [self.coord[0] + 2, self.coord[1] - 1]:
                    if piece.color == self.color:
                        self.stop = 2
            
            if self.stop != 2:
                ray.append([self.coord[0] + 2, self.coord[1] - 1])

        self.move_set.append(ray)

        # strong bottom-right
        self.stop = 1
        ray = []
        if check_bounds([self.coord[0] + 1, self.coord[1] - 2]): 
            for piece in piece_group:
                if piece.coord == [self.coord[0] + 1, self.coord[1] - 2]:
                    if piece.color == self.color:
                        self.stop = 2
            
            if self.stop != 2:
                ray.append([self.coord[0] + 1, self.coord[1] - 2])

        self.move_set.append(ray)

        # strong bottom-left
        self.stop = 1
        ray = []
        if check_bounds([self.coord[0] - 1, self.coord[1] - 2]): 
            for piece in piece_group:
                if piece.coord == [self.coord[0] - 1, self.coord[1] - 2]:
                    if piece.color == self.color:
                        self.stop = 2
            
            if self.stop != 2:
                ray.append([self.coord[0] - 1, self.coord[1] - 2])

        self.move_set.append(ray)

        # weak bottom-left
        self.stop = 1
        ray = []
        if check_bounds([self.coord[0] - 2, self.coord[1] - 1]):   
            for piece in piece_group:
                if piece.coord == [self.coord[0] - 2, self.coord[1] - 1]:
                    if piece.color == self.color:
                        self.stop = 2
            
            if self.stop != 2:              
                ray.append([self.coord[0] - 2, self.coord[1] - 1])

        self.move_set.append(ray)

        # generate spaces
        if pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos()) and not self.select and not self.check:
            generate_spaces(self)



class Rook(GameSprite):
    def update(self):
        self.move_set.clear()
        # generate left
        x_var = self.coord[0] - 1
        self.stop = 1
        ray = []
        for i in range(7):
            if self.stop == 3:
                break

            for piece in piece_group:
                if piece.coord == [x_var, self.coord[1]]:
                    if piece.color == self.color:
                        self.stop = 2
                    elif piece.color != self.color:
                        self.stop = 3
                    
            if x_var < 0 or self.stop == 2:
                break   

            ray.append([x_var, self.coord[1]])
            x_var -= 1

        self.move_set.append(ray)

        # generate up
        y_var = self.coord[1] + 1
        self.stop = 1
        ray = []
        for i in range(7):
            if self.stop == 3:
                break
            for piece in piece_group:
                if piece.coord == [self.coord[0], y_var]:
                    if piece.color == self.color:
                        self.stop = 2
                    elif piece.color != self.color:
                        self.stop = 3
                    
            if y_var > 7 or self.stop == 2:
                break   
            ray.append([self.coord[0], y_var])
            y_var += 1

        self.move_set.append(ray)

        # generate right
        x_var = self.coord[0] + 1
        self.stop = 1
        ray = []
        for i in range(7):  
            if self.stop == 3:
                break
            for piece in piece_group:
                if piece.coord == [x_var, self.coord[1]]:
                    if piece.color == self.color:
                        self.stop = 2
                    elif piece.color != self.color:
                        self.stop = 3
                    
            if x_var > 7 or self.stop == 2:
                break             
                    
            ray.append([x_var, self.coord[1]])
            x_var += 1

        self.move_set.append(ray)

        # generate down
        y_var = self.coord[1] - 1
        self.stop = 1
        ray = []
        for i in range(7):
            if self.stop == 3:
                break
            for piece in piece_group:
                if piece.coord == [self.coord[0], y_var]:
                    if piece.color == self.color:
                        self.stop = 2
                    elif piece.color != self.color:
                        self.stop = 3
                    
            if y_var < 0 or self.stop == 2:
                break   

            ray.append([self.coord[0], y_var])
            y_var -= 1

        self.move_set.append(ray)


        # generating movespaces
        if pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos()) and not self.select and not self.check:
            generate_spaces(self)




class Pawn(GameSprite):
    def __init__(self, sprite_image, size1, size2, coord, color):
        super().__init__(sprite_image, size1, size2, coord, color)
        self.firstMove = True

    def update(self):
        # for white pawns
        if self.color == "white":
            self.move_set.clear()
            ray = []
            if self.firstMove:
                for piece in piece_group:
                    if piece.coord == [self.coord[0], self.coord[1] + 1]:
                        self.stop = 8
                    elif piece.coord == [self.coord[0], self.coord[1] + 2]:
                        self.stop = 9

                if not self.stop >= 8:
                    ray.append([self.coord[0], self.coord[1] + 2])
                    ray.append([self.coord[0], self.coord[1] + 1])
                    self.move_set.append(ray)

                if self.stop == 9:
                    ray.append([self.coord[0], self.coord[1] + 1])
                    self.move_set.append(ray)

                self.stop = 0
                


            else:
                for piece in piece_group:
                    if piece.coord == [self.coord[0], self.coord[1] + 1]:
                        self.stop = 8

                if self.stop != 8:
                    ray.append([self.coord[0], self.coord[1] + 1])
                    self.move_set.append(ray)


            ray = []
            for piece in piece_group:
                if piece.coord == [self.coord[0] - 1, self.coord[1] + 1] and piece.color != self.color:
                    ray.append([self.coord[0] - 1, self.coord[1] + 1])
                if piece.coord == [self.coord[0] + 1, self.coord[1] + 1] and piece.color != self.color:
                    ray.append([self.coord[0] + 1, self.coord[1] + 1])

            self.move_set.append(ray)


        # for black pawns
        if self.color == "black":
            self.move_set.clear()
            ray = []
            if self.firstMove:
                for piece in piece_group:
                    if piece.coord == [self.coord[0], self.coord[1] - 1]:
                        self.stop = 8
                    elif piece.coord == [self.coord[0], self.coord[1] - 2]:
                        self.stop = 9

                if not self.stop >= 8:
                    ray.append([self.coord[0], self.coord[1] - 2])
                    ray.append([self.coord[0], self.coord[1] - 1])
                    self.move_set.append(ray)

                if self.stop == 9:
                    ray.append([self.coord[0], self.coord[1] - 1])
                    self.move_set.append(ray)

                self.stop = 0
                


            else:
                for piece in piece_group:
                    if piece.coord == [self.coord[0], self.coord[1] - 1]:
                        self.stop = 8

                if self.stop != 8:
                    ray.append([self.coord[0], self.coord[1] - 1])
                    self.move_set.append(ray)


            ray = []
            for piece in piece_group:
                if piece.coord == [self.coord[0] - 1, self.coord[1] - 1] and piece.color != self.color:
                    ray.append([self.coord[0] - 1, self.coord[1] - 1])
                if piece.coord == [self.coord[0] + 1, self.coord[1] - 1] and piece.color != self.color:
                    ray.append([self.coord[0] + 1, self.coord[1] - 1])
                    
            self.move_set.append(ray)


        if pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos()) and not self.select and not self.check:
            generate_spaces(self)

        # elif pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos()) and not self.select and self.check:
        #     save = self.coord
        #     for coord in self.move_set:
        #         for piece in piece_group:
        #             if piece.attacking and piece.color != self.color:
        #                 for enemy_coord in piece.move_set:
        #                     if enemy_coord == coord:
        #                         self.coord = enemy_coord
        #                         if self.color == "white":
        #                             whiteKing.check_check()
        #                             # successful block
        #                             if not whiteKing.check:
        #                                 sprite.Group.empty(moveSpace_group)
        #                                 for piece in piece_group:
        #                                     piece.select = False

        #                                 self.select = True
        #                                 moveSpace_group.add(MoveSpace("circle.png", 60, 60, coord))
        #                                 self.coord = save

        #                             # unsuccessful block
        #                             else:
        #                                 continue

        #                         elif self.color == "black":
        #                             blackKing.check_check()
        #                             # successful block
        #                             if not blackKing.check:
        #                                 sprite.Group.empty(moveSpace_group)
        #                                 for piece in piece_group:
        #                                     piece.select = False

        #                                 self.select = True
        #                                 moveSpace_group.add(MoveSpace("circle.png", 60, 60, coord))
        #                                 self.coord = save

        #                             # unsuccessful block
        #                             else:
        #                                 continue


# creation

piece_group = sprite.Group()
white_sub = sprite.Group()
black_sub = sprite.Group()
moveSpace_group = sprite.Group()

window = display.set_mode((640, 640))
display.set_caption("Chess!")

board = transform.scale(image.load("chess board sample.png"), (640, 640))


whiteKing = King("white king.png", 60, 60, [4, 0], "white")
piece_group.add(whiteKing)
white_sub.add(whiteKing)

whiteQueen = Queen("white queen.jpg", 60, 60, [3, 0], "white")
piece_group.add(whiteQueen)
white_sub.add(whiteQueen)

whiteBishop1 = Bishop("white bishop.jpg", 60, 60, [2, 0], "white")
piece_group.add(whiteBishop1)
white_sub.add(whiteBishop1)

whiteBishop2 = Bishop("white bishop.jpg", 60, 60, [5, 0], "white")
piece_group.add(whiteBishop2)
white_sub.add(whiteBishop2)

whiteKnight1 = Knight("white horse.jfif", 60, 60, [1, 0], "white")
piece_group.add(whiteKnight1)
white_sub.add(whiteKnight1)

whiteKnight2 = Knight("white horse.jfif", 60, 60, [6, 0], "white")
piece_group.add(whiteKnight2)
white_sub.add(whiteKnight2)

whiteRook1 = Rook("white rook.jfif", 60, 60, [7, 0], "white")
piece_group.add(whiteRook1)
white_sub.add(whiteRook1)

whiteRook2 = Rook("white rook.jfif", 60, 60, [0, 0], "white")
piece_group.add(whiteRook2)
white_sub.add(whiteRook2)

whitePawn1 = Pawn("white pawn.jfif", 60, 60, [0, 1], "white")
piece_group.add(whitePawn1)
white_sub.add(whitePawn1)

whitePawn2 = Pawn("white pawn.jfif", 60, 60, [1, 1], "white")
piece_group.add(whitePawn2)
white_sub.add(whitePawn2)

whitePawn3 = Pawn("white pawn.jfif", 60, 60, [2, 1], "white")
piece_group.add(whitePawn3)
white_sub.add(whitePawn3)

whitePawn4 = Pawn("white pawn.jfif", 60, 60, [3, 1], "white")
piece_group.add(whitePawn4)
white_sub.add(whitePawn4)

whitePawn5 = Pawn("white pawn.jfif", 60, 60, [4, 1], "white")
piece_group.add(whitePawn5)
white_sub.add(whitePawn5)

whitePawn6 = Pawn("white pawn.jfif", 60, 60, [5, 1], "white")
piece_group.add(whitePawn6)
white_sub.add(whitePawn6)

whitePawn7 = Pawn("white pawn.jfif", 60, 60, [6, 1], "white")
piece_group.add(whitePawn7)
white_sub.add(whitePawn7)

whitePawn8 = Pawn("white pawn.jfif", 60, 60, [7, 1], "white")
piece_group.add(whitePawn8)
white_sub.add(whitePawn8)

# # # # # # # # # #

blackKing = King("black king.png", 60, 60, [4, 7], "black")
piece_group.add(blackKing)
black_sub.add(blackKing)

blackQueen = Queen("black queen.jpg", 60, 60, [3, 7], "black")
piece_group.add(blackQueen)
black_sub.add(blackQueen)

blackBishop1 = Bishop("black bishop.jfif", 60, 60, [2, 7], "black")
piece_group.add(blackBishop1)
black_sub.add(blackBishop1)

blackBishop2 = Bishop("black bishop.jfif", 60, 60, [5, 7], "black")
piece_group.add(blackBishop2)
black_sub.add(blackBishop2)

blackKnight1 = Knight("black horse.png", 60, 60, [1, 7], "black") #remember to size fix this
piece_group.add(blackKnight1)
black_sub.add(blackKnight1)

blackKnight2 = Knight("black horse.png", 60, 60, [6, 7], "black")
piece_group.add(blackKnight2)
black_sub.add(blackKnight2)

blackRook1 = Rook("black rook.png", 60, 60, [0, 7], "black")
piece_group.add(blackRook1)
black_sub.add(blackRook1)

blackRook2 = Rook("black rook.png", 60, 60, [7, 7], "black")
piece_group.add(blackRook2)
black_sub.add(blackRook2)

blackPawn1 = Pawn("black pawn.jpg", 60, 60, [0, 6], "black")
piece_group.add(blackPawn1)
black_sub.add(blackPawn1)

blackPawn2 = Pawn("black pawn.jpg", 60, 60, [1, 6], "black")
piece_group.add(blackPawn2)
black_sub.add(blackPawn2)

blackPawn3 = Pawn("black pawn.jpg", 60, 60, [2, 6], "black")
piece_group.add(blackPawn3)
black_sub.add(blackPawn3)

blackPawn4 = Pawn("black pawn.jpg", 60, 60, [3, 6], "black")
piece_group.add(blackPawn4)
black_sub.add(blackPawn4)

blackPawn5 = Pawn("black pawn.jpg", 60, 60, [4, 6], "black")
piece_group.add(blackPawn5)
black_sub.add(blackPawn5)

blackPawn6 = Pawn("black pawn.jpg", 60, 60, [5, 6], "black")
piece_group.add(blackPawn6)
black_sub.add(blackPawn6)

blackPawn7 = Pawn("black pawn.jpg", 60, 60, [6, 6], "black")
piece_group.add(blackPawn7)
black_sub.add(blackPawn7)

blackPawn8 = Pawn("black pawn.jpg", 60, 60, [7, 6], "black")
piece_group.add(blackPawn8)
black_sub.add(blackPawn8)

# positions and other stuff

run = True
turn = True
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

    whiteKing.check_check()
    blackKing.check_check()
    clock.tick(FPS)

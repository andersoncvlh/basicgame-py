class Robo():
        def __init__(self, x, y):
            self.x = x
            self.y = y

        
        def move_up(self):
            if self.y < 10:
                self.y =  self.y + 1
            else:
                print('Movimento Proibido')
                
        
        def move_down(self):
            if self.y > 0:
                self.y = self.y - 1
            else:
                print('Movimento Proibido')

        def move_right(self):
            if self.x < 10:
                self.x = self.x + 1
            else:
                print('Movimento Proibido')

        def move_left(self):
            if self.x > 0:
                self.x = self.x - 1
            else:
                print('Movimento Proibido')
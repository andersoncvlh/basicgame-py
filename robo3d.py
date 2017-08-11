import robo

class Robo3D(robo.Robo):
    def __init__(self, x, y, z):
        super(Robo3D, self).__init__(x, y)
        self.z = z
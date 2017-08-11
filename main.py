import robo
import robo3d


robo1 = robo.Robo(2,2)
print(type(robo1))
print(robo1.x)
print(robo1.y)

robo3d = robo3d.Robo3D(5, 5, 10)
print(type(robo3d))
print(robo3d.x)
print(robo3d.y)
print(robo3d.z)
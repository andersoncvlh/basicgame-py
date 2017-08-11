import robo
import robo3d
import reward


robo1 = robo.Robo(2,2)
print(type(robo1))
print('X igual a %s' % robo1.x)
print('Y igual a %s' % robo1.y)

robo3d = robo3d.Robo3D(5, 5, 10)
print(type(robo3d))
print('X igual a %s' % robo3d.x)
print('Y igual a %s' % robo3d.y)
print('Z igual a %s' % robo3d.z)

robo3d.move_down()
print('Y igual a %s' % robo3d.y)

reward = reward.Reward(5, 5, 'Recompensa')
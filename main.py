import robo
import robo3d
import reward

def check_reward(robot, rewards):
    ok = False
    for reward in rewards:
        if reward.x == robot.x and reward.y == robot.y:
            print('O robo achou a recompensa %s' % reward.name)
            ok = True
    return ok

rew1 = reward.Reward(5, 5, 'Moeda')
rew2 = reward.Reward(2, 2, 'Gasolina')
rewardList = [rew1, rew2]

robo1 = robo.Robo(5,7)
print(type(robo1))
print('X igual a %s' % robo1.x)
print('Y igual a %s' % robo1.y)

robo2 = robo3d.Robo3D(5, 5, 10)
print(type(robo2))
print('X igual a %s' % robo2.x)
print('Y igual a %s' % robo2.y)
print('Z igual a %s' % robo2.z)

robo1.move_down()
robo1.move_down()
check_reward(robo1, rewardList)

robo1.move_down()
robo1.move_down()
robo1.move_down()
robo1.move_left()
robo1.move_left()
robo1.move_left()
check_reward(robo1, rewardList)

check_reward(robo2, rewardList)




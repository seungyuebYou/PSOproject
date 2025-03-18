from MyPSO import *
import time
import matplotlib.pyplot as plt
import numpy

num_particles = 10

part = MyPSO(num_particles)

# print(part.particle_pos)

for i in range(200):
    part.fitness_finc(part.particle_pos,part.particle_vel)

    part.update_pos(part.particle_pos,part.particle_vel)
    part.update_velocity(part.particle_pos, part.particle_vel, part.p_best, part.g_best, c1= 0.5, c2 = 1.5, w = 0.75)

    part.check_best(num_particles)



    plt.plot(part.particle_pos[0,:],part.particle_pos[1,:])
    plt.show()
    time.sleep(5)

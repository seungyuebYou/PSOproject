import numpy as np

class MyPSO:
    def __init__(self,n_particles):
        self.n_particles = n_particles,
        self.particle_pos = np.random.uniform(size=(2,self.n_particles)),
        self.particle_vel = np.random.uniform(0, 10, size=(2,self.n_particles)),
        self.p_best = self.particle_pos,
        self.g_best = self.particle_pos
        


    def fitness_finc(self,pos,vel):
        for _ in range(pos):
            fitness += np.sqrt((3-pos[0])**2+(4-pos[1])**2)
            return fitness
        
    
        
    def update_velocity(self,pos,vel,p_best,g_best, c1= 0.5, c2 = 1.5, w = 0.75):
        pos = np.array(pos)
        vel = np.array(vel)
        r = np.random.uniform()
        p_best = np.array(p_best)
        g_best = np.array(g_best)
        assert pos.shape == vel.shape 
        
        new_vel = w * vel + c1 * (p_best - pos) + c2 * r * (g_best - pos)
        return new_vel
    
    def update_pos(self,pos,vel):
        pos = np.array(pos)
        vel = np.array(vel)

        new_pos = pos + vel
        return new_pos
        



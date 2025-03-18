import numpy as np

class MyPSO:
    def __init__(self, n_particles):
        self.n_particles = n_particles,
        self.particle_pos = np.random.rand(2,n_particles),
        self.particle_vel = np.random.rand (2,n_particles),
        self.p_best = self.particle_pos,
        self.g_best = self.particle_pos,
        self.fitness = 0


    def fitness_finc(self,particle_pos,particle_vel):
        pos = np.array(particle_pos)
        fit = self.fitness
        print(pos.shape)
        # fit += np.sqrt((3-pos[0,:])**2+(4- pos[1,:])**2)
        self.fitness = fit
        return self.fitness
        
    
        
    def update_velocity(self,particle_pos, particle_vel, p_best, g_best, c1= 0.5, c2 = 1.5, w = 0.75):
        pos = np.array(particle_pos)
        vel = np.array(particle_vel)
        # print(pos)
        # print(vel)
        r = np.random.uniform()
        p_best = np.array(p_best)
        g_best = np.array(g_best)
        # assert pos.shape == vel.shape 
        
        new_vel = w * vel + c1 * (p_best - pos) + c2 * r * (g_best - pos)
        self.particle_vel = new_vel
        return particle_vel
    
    def update_pos(self,particle_pos,particle_vel):
        pos = np.array(particle_pos)
        vel = np.array(particle_vel)

        new_pos = pos + vel
        particle_pos = new_pos
        return particle_pos
        

    def check_best(self,n_particles):
        for i in range(n_particles):
            x = self.particle_pos[i]
            v = self.particle_vel[i]
            p_best = self.p_best[i]
            self.particle_vel[i] = self.update_velocity(x,v,p_best,self.g_best)
            self.particle_pos[i] = self.update_pos(x,v)

            if self.particle_pos[i] < p_best[i]:
                self.p_best[i] = self.particle_pos[i]


            if self.particle_pos[i] < self.g_best:
                self.g_best = self.particle_pos[i]
        print(self.g_best)
        return self.g_best



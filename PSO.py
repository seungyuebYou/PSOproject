import numpy as np


class PSO(object):
    """
    Class implementing PSO algorithm
    """
    def __init__(self, func, init_pos, n_particles):
        """
        Initialize the key variables.
        
        Args:
            fun (function): the fitness function to optimize
            init_pos(array_like):
            n_particles(int): the number of particles of the swarm.
        """
        self.func = func
        self.n_particles = n_particles
        self.init_pos = init_pos
        self.particle_dim = len(init_pos)
        self.particles_pos = np.random.uniform(size=(n_particles, self.particle_dim)) \
                            * self.init_pos
        self.velocities = np.random.uniform(size=(n_particles, self.particle_dim))
        #Initilize the best positions
        self.g_best = init_pos
        self.p_best = self.particles_pos
        
    
    def update_position(self, x, v):
        """
        Update particle position
        
        Args:
            x (array-like): particle current position
            v (array-like): particle current velocity
        
        Returns:
            The updated position(array-like)
        """
        x = np.array(x)
        v = np.array(v)
        new_x = x + v
        return new_x
    
    
    def update_velocity(self, x, v, p_best, g_best, c0=0.5, c1=1.5, w=0.75):
        """
            Update particle velocity
            
            Args:
                x(array-like): particle current position
                v (array-like): particle current velocity
                p_best(array-like): the best position found so far for a particle
                g_best(array-like): the best position regarding all the particles found so far
                c0 (float): the congnitive scaling constant, ���� �����ϸ� ���
                c1 (float): the social scaling constant
                w (float): the inertia weight, ���� �߷�
                
            Returns:
                The updated velocity (array-like).
        """
        x = np.array(x)
        v = np.array(v)
        assert x.shape == v.shape, "Position and velocity must have same shape."
        # a random number between 0 and 1
        r = np.random.uniform()
        p_best = np.array(p_best)
        g_best = np.array(g_best)
        
        new_v = w*v + c0*r*(p_best - x) + c1*r*(g_best-x)
        return new_v
    
    
    def optimize(self, maxiter=200):
        """
        Run the PSO optimization process utill the stoping critera is met.
        Cas for minization. The aim is to minimize the cost function
        
        Args:
            maxiter (int): the maximum number of iterations before stopping the optimization
            
        Returns:
            The best solution found (array-like)
        """
        for _ in range(maxiter):
            for i in range(self.n_particles):
                x = self.particles_pos[i]
                v = self.velocities[i]
                p_best = self.p_best[i]
                self.velocities[i] = self.update_velocity(x, v, p_best, self.g_best)
                self.particles_pos[i] = self.update_position(x,v)
                # Update the besst position for particle i
                if self.func(self.particles_pos[i]) < self.func(p_best):
                    self.p_best[i] = self.particles_pos[i]
                # Update the best position overall
                if self.func(self.particles_pos[i]) < self.func(self.g_best):
                    self.g_best = self.particles_pos[i]
                    
        return self.g_best, self.func(self.g_best)
    
    
def sphere(x):
    """
        In 3D : f(x,y,z) = x�� + y�� + z��
    """
    return np.sum(np.square(x))
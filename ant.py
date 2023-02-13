import time
import numpy as np
import threading 

class ACOQAP:
    def __init__(self,
                 matirx_d: np.array,
                 flow_matrix: np.array,
                 ants_total: int,
                 num_iterations: int,
                 e_rate: float 
        ):
        
        self.ants_total = ants_total
        self.e_rate = e_rate
        self.ants = []
        self.matirx_d = matirx_d
        self.flow_matrix = flow_matrix
        
    def run(self):
        start_ant = 0 
        num_iteration = 10000
        Best_solution = None

        
        for iteration in range(num_iteration):  
            
            num_ofAnts = len(self.ants)

            if num_ofAnts > start_ant:
                solution_current = min(self.ants, key=self.evaluate_fitness)
                if self.evaluate_fitness(solution_current) < self.evaluate_fitness(Best_solution):
                     Best_solution = solution_current
                 
            self.generate_solutions()
            self.update_pheronames()
            
        return Best_solution, self.evaluate_fitness(Best_solution)
            
    def generate_solutions(self):
        self.ants.clear()
        for ant in range(self.ants_total):
            nodes_before = []
            path = []

            prev_node = start_node
            start_node = 0
            
            distance = len(self.matirx_d)

            for i in range(distance):
                p_matrix = np.random(matirx_d.shape)
                
                pheromones = np.copy(p_matrix[start_node])
                
                pheromones[nodes_before] = 0
                
                pheromones = pheromones / pheromones.sum()
                
                next_node = np.random.choice(range(distance), 1, p=pheromones)[0]
                
                path.append(next_node)
                nodes_before.append(next_node)
                prev_node = next_node

            self.ants.append(path)
            
    def evaluate_fitness(self, path):
        if path == None:
            return float('inf')
        return np.sum(self.matirx_d[np.ix_(path, path)]*self.flow_matrix)
    
    def update_pheronames(self):
        for direction in self.ants:
            for path in direction:
                fitness = self.evaluate_fitness(direction)

                p_matrix = np.random.random_sample(matirx_d.shape)
                matrix =  p_matrix[path]
                matrix = matrix] + 1 / fitness
                
                
def ACO(matirx_d, flow_matrix, ants_total, e_rate, iterations):
    
    argument = ACOQAP(matirx_d, flow_matrix, ants_total, iterations, e_rate)
    
    solution = argument.run()  
    fitness = argument.run()
    
    with open("experiment4-1solution.txt", "a") as txt:
        txt.write(f"m= {ants_total}, e= {e_rate}, fitness evaluation= {iterations} , \nbest solution= {solution}, fitness: {fitness}")

if __name__ == "__main__":
    with open("Uni50a.dat.txt", "r") as r:
        data = r.readlines()

        
    matirx_d = np.array(
        list(map(
            lambda x: list(map(
                lambda y: int(y),
                x.strip().split()
            )),
        data[2:52]))
    )
    
    flow_matrix = np.array(
        list(map(
            lambda x: list(map(
                lambda y: int(y),
                x.strip().split()
            )),
        data[53:]))
    )
    # change values according the parameters for each experiment
    experiment = threading.Thread(target=ACO, args=(matirx_d, flow_matrix, 10, 0.5, 10000))
    t1.start()



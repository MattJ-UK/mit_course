import random
import pylab

# Global Variables
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 500
CURRENTFOXPOP = 30

def rabbitGrowth():
    """ 
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up, 
      a new rabbit may be born.
    Nothing is returned.
    """
    # you need this line for modifying global variables
    global CURRENTRABBITPOP

    # TO DO
    for i in range(CURRENTRABBITPOP):
        if random.random() < 1 - CURRENTRABBITPOP / MAXRABBITPOP:
            CURRENTRABBITPOP += 1


def foxGrowth():
    """ 
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat 
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    # you need these lines for modifying global variables
    global CURRENTRABBITPOP
    global CURRENTFOXPOP

    # TO DO
    for f in range(CURRENTFOXPOP):
        eats_rabbit = False
        if random.random() < CURRENTRABBITPOP / MAXRABBITPOP and CURRENTRABBITPOP > 10:
            eats_rabbit = True
            CURRENTRABBITPOP -= 1
        if eats_rabbit:
            if random.random() < 0.333:
                CURRENTFOXPOP += 1
        else:
            if random.random() < 0.1 and CURRENTFOXPOP > 10:
                CURRENTFOXPOP -= 1
    
            
def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the 
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """

    # TO DO
    rabbits_counts = []
    foxes_counts = []
    for i in range(numSteps):
        rabbitGrowth()
        foxGrowth()
        rabbits_counts.append(CURRENTRABBITPOP)
        foxes_counts.append(CURRENTFOXPOP)

    return (rabbits_counts, foxes_counts)

def plot_sim(numSteps):
    sim_results = runSimulation(numSteps)

    rabbits = sim_results[0]
    foxes = sim_results[1]

    pylab.plot(rabbits, label = 'rabbits')
    pylab.plot(foxes, label = 'foxes')
    rabbit_model = pylab.polyfit(range(numSteps),rabbits,1)
    pylab.plot(rabbit_model)
    pylab.ylabel('Population')
    pylab.xlabel('steps')
    pylab.legend()
    pylab.show()

plot_sim(200)
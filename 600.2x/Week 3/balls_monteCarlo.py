import random

def pickBall(options):
    """
    Picks a ball and removes it from options
    :param options: list of options to pick
    :return: picked ball
    """
    choice = random.choice(options)
    options.remove(choice)

    return choice

def runTrial(picks, options):
    """
    Returns True if all balls picked are the same colour
    :param picks: Number of balls to pick
    :param options: List containing options
    :return: Boolean
    """
    choices = []
    for i in range(picks):
        choice = pickBall(options)
        choices.append(choice)

    comparison = choices[0]
    result = True
    for i in range(1,len(choices)):
        if choices[i] != comparison:
            result = False
    return result



def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3
    balls of the same color were drawn.
    '''
    # Your code here

    count_matched = 0
    for t in range(numTrials):
        options = ['r', 'r', 'r', 'g', 'g', 'g']
        count_matched += int(runTrial(3,options.copy()))

    result = float(count_matched) / float(numTrials)

    return result



print(noReplacementSimulation(10000))


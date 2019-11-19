###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    def sortCows(cows):
        """
        Helper function - splits the dict into two lists and sorts them, ascending
        :param cows: A dict containing cows and their weights
        :return: keys, vals -> Sorted lists 
        """
        keys = list(cows.keys())
        vals = list(cows.values())
        swaps = 1
        while swaps > 0:
            swaps = 0
            for i in range(len(vals)-1):
                #print('Test ' + str(vals[i]) + ' > ' + str(vals[i+1]))
                if vals[i] > vals[i+1]:
                    #print('swap')
                    vals[i], vals[i+1] = vals[i+1], vals[i]
                    keys[i], keys[i+1] = keys[i+1], keys[i]
                    swaps +=1
                    #print('swaps: ' + str(swaps))
                    #print(keys)
                    #print(vals)
        return keys, vals

    keys, vals = sortCows(cows)

    all_trips = []


    while len(keys) > 0:
        #print('keys left: ' + str(len(keys)))
        remaining = limit
        unused_keys = []
        unused_vals = []
        current_trip = []
        for i in range(len(vals)):
            cow = keys.pop()
            cow_weight = vals.pop()
            if cow_weight > remaining:
                #print('Not loading ' + cow + ': weight is ' + str(cow_weight) + '. Remaining: ' + str(remaining))
                unused_keys = [cow] + unused_keys
                unused_vals = [cow_weight] + unused_vals
                #print('unused cows: ' + str(unused_keys))
            else:
                current_trip.append(cow)
                remaining -= cow_weight
                #print('Loading ' + cow + ': weight is ' + str(cow_weight) + '. Remaining: ' + str(remaining))
        #print('Appending trip ' + str(current_trip) +'. Remaining: ' + str(remaining))
        all_trips.append(current_trip)
        keys = keys + unused_keys
        vals = vals + unused_vals

    return all_trips






# Problem 2
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """


    def valid_trip(trip, cows, limit):
        """
        Determines whether a trip is valid
        :param trip: single trip as list
        :param limit: max weight allowed
        :param cows: dict of cows & weights
        :return: True / False
        """
        valid = True
        remaining = limit
        for cow in trip:
            remaining -= cows[cow]
            if remaining < 0:
                valid = False
                break
        return valid

    smallest_trips = 0
    current_best = []

    for elt in get_partitions(cows):
        #print('testing list:' + str(elt))
        trip_count = 0
        all_valid = True
        #if len(elt) > smallest_trips and smallest_trips != 0:
        for l in elt:
            #print('testing trip: ' + str(l))
            if valid_trip(l, cows, limit):
                trip_count += 1
                #print('Valid. Trip count: ' + str(trip_count) )
            else:
                all_valid = False
                #print('************INVALID************')
                break

        if all_valid and (trip_count < smallest_trips or smallest_trips == 0):
            smallest_trips = trip_count
            current_best = elt

        #print('Current best: ' + str(current_best) + '. Trip count: ' + str(smallest_trips))

    return current_best






        
# Problem 3
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    cows = load_cows("ps1_cow_data.txt")
    limit = 10
    print(cows)
    import time

    greedy_start = time.time()
    print(greedy_cow_transport(cows, limit))
    greedy_end = time.time()

    bruteforce_start = time.time()
    print(brute_force_cow_transport(cows, limit))
    bruteforce_end = time.time()

    print('greedy took: ' + str(greedy_end-greedy_start))
    print('bruteforce took: ' + str(bruteforce_end - bruteforce_start))



"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

compare_cow_transport_algorithms()



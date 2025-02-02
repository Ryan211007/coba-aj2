import itertools  

def brute_force_pattern(possible_points):  
    for length in range(4, len(possible_points) + 1):  
        for pattern in itertools.permutations(possible_points, length):  
            yield pattern  

points = ['1', '2', '3', '4', '5', '6', '7', '8', '9']  

for attempt in brute_force_pattern(points):  
    print("Trying pattern:", "".join(attempt))  

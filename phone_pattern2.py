import itertools  

def brute_force_pattern(possible_points, limit):  
    count = 0
    for length in range(4, len(possible_points) + 1):  
        for pattern in itertools.permutations(possible_points, length):  
            yield pattern  
            count += 1
            if count >= limit:
                return  

points = ['1', '2', '3', '4', '5', '6', '7', '8', '9']  
limit = 1000 # Set the desired limit

for attempt in brute_force_pattern(points, limit):  
    print("Trying pattern:", "".join(attempt))  

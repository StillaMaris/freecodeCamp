
def largest_number(list):
    largest_so_far = -1
    for i in list:
        if i > largest_so_far:
            largest_so_far = i
    return largest_so_far



list = [9,41, 12, 4, 75, 15]
num_max = largest_number(list)
print('Max number', num_max)

def min(list):
    smallest = None
    for value in list:
        if smallest is None or value < smallest:
            smallest = value
    return smallest
    
print('Min number', min(list))
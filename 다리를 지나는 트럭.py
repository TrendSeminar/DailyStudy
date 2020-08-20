'''
input
'''
bridge_length = 2
weight = 10
truck_weight = [7, 4, 5, 6]

bridge = [0]*bridge_length
count = 0

while bridge:
    count += 1
    bridge.pop(0)
    if truck_weight:
        next_truck = truck_weight.pop(0)
        if sum(bridge)+next_truck <= weight:
            bridge.append(next_truck)
        else:
            bridge.append(0)

print(count)

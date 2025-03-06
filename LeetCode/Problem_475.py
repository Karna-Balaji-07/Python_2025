# Heaters

def solution1(houses, heater):
    houses.sort()
    heater.sort()
    i = 0
    res = 0
    for house in houses:
        while i < len(heater) - 1 and abs(heater[i + 1] - house) <= abs(heater[i] - house):
            i += 1
        res = max(res, abs(heater[i] - house))
    return res      


houses = [1,2,3]    
heaters = [2]
print(solution1(houses, heaters)) # 1
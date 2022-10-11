def findTheRange(n, val):
    planet = [0 for x in range(n)]
    for x in val:
        i = x[0]
        while(i < x[1]):
            planet[i]+=x[2]
            i+=1
    print([planet.index(max(planet)), planet.index(max(planet))+1, max(planet)])

findTheRange(5, [[2, 4, 5], [1, 3, 6], [2, 4, 7]])
def findPlanet(solar_system_details, suitable_range):
    ans_list = []
    for solar_system in solar_system_details:
        total_energy = 0
        for star in solar_system:
            total_energy += star[0]*(1/star[1])
        ans_list.append(total_energy)
    for i in range(len(ans_list)):
        if(suitable_range[0] <= ans_list[i] <suitable_range[1]):
            print(i)

findPlanet([[[0.433, 200]], [[0.89, 400], [0.6, 300]]], [0.003, 0.005])
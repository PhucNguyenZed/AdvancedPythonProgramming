def least_likely(probabilitys):
    smallest = 1
    name = ""
    for particle in probabilitys:
        probability = probabilitys[particle] 
        if probability < smallest:
            smallest = probability
            name = particle 
    return particle
print(least_likely({'neutron':0.55,'proton':0.21,'meson':0.03,'muon':0.07,'neutrino':0.14}))
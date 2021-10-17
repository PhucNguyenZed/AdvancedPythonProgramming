class Country:
    def __init__(self, name, population, area):
        self.name = name
        self.population = population
        self.area = area
    def is_larger(self, other):
        return self.area > other.area 
    def population_density(self):
        return self.population / self.area
    def __str__(self):
        return '{} has a population of {} and is {} square km.'.format(self.name, self.population, self.area)
    def __repr__(self):
        return "Country('{0}', {1}, {2})".format(self.name,self.population, self.area)
canada = Country('Canada', 34482779, 9984670)
#print(canada.name)
#print(canada.population)
#print(canada.area)
usa = Country('United States of America', 313914040, 9826675)
#print(canada.is_larger(usa))
#print(canada.population_density())
#print(usa)
print(canada)

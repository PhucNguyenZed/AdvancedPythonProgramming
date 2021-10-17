class Continent:
        def is_larger(self, other):
            return self.area > other.area 
        def population_density(self):
            return self.population / self.area
        def __str__(self):
            return '{} has a population of {} and is {} square km.'.format(self.name, self.population, self.area)
        def __repr__(self):
            return "Country('{0}', {1}, {2})".format(self.name,self.population, self.area)
        class country:
            def Country(self,name, population, area):
                self.name = name
                self.population = population
                self.area = area
        canada =country.Country('Canada', 34482779, 9984670)
        usa = country.Country('United States of America', 313914040,9826675)
        mexico = country.Country('Mexico', 112336538, 1943950)
north_america =Continent('North America',)
for country in north_america.countries:
            north_america.total_population()
            print(north_america)



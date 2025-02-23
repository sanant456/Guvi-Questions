class City():
  def __init__(self,name,population):
    #....  YOUR CODES STARTS HER ....#
    self.name = name
    self.population = population
    #....  YOUR CODES ENDS HERE....#
 def print_details():
    #....  YOUR CODES STARTS HERE ....#
    print(f"City: {self.name}, Population: {self.population}")
    #....  YOUR CODES ENDS HERE....#
class District():
  def __init__(self,name,population,num_cities):
     #....  YOUR CODES STARTS HERE....#
    super().__init__(name, population)
        self.num_cities = num_cities
    #....  YOUR CODES ENDS HERE....#
class TamilNadu(District):
  def __init__(self,name,population,num_district):
     #....  YOUR CODES STARTS HERE....#
    super().__init__(name, population, num_districts)
     #....  YOUR CODES ENDS HERE ....#
    def printdetails(self):
      #....  YOUR CODES STARTS HERE....#
      print(f"State: {self.name}, Population: {self.population}, Number of Districts: {self.num_cities}")
        #....  YOUR CODES ENDS HERE ....#

 def clean_input(value):
   return str(value.strip())

def main():
  city_name, city_population = map(clean_input, input().strip().spilt(","))
  city = City(city_name, int(city_population))

district_name, district_population, num_cities = map
  (clean_input, input().strip().split(","))
district = District(district_name, int(district_population),
    int(num_cities))

state_name, state_population, num_districts = map(clean_input, input().strip().spilt(","))
state = TamilNadu(state_name, int(state_population), int(num_dustricts))

city.print_details()
dustrict.print_deatils()
state.print_details()

if __name__ = "__main__":
main()

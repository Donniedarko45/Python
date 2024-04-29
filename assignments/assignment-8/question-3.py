"""3. Assume a file city.txt with details of 5 cities in given format (cityname population(in
lakhs) area(in sq KM) ):
Example:
Dehradun 5.78 308.20
Delhi 190 1484
……………
Open file city.txt and read to:
a. Display details of all cities
b. Display city names with population more than 10Lakhs
c. Display sum of areas of all cities"""

"""3. Assume a file city.txt with details of 5 cities in given format (cityname population(in
lakhs) area(in sq KM) ):
Example:
Dehradun 5.78 308.20
Delhi 190 1484
……………
Open file city.txt and read to:
a. Display details of all cities
b. Display city names with population more than 10Lakhs
c. Display sum of areas of all cities"""

def adding_data(filename):
    cities = {}
    f=open(filename,"w")
    for _ in range(5):
        city_name = input("Enter the city name: ")
        city_population = float(input("Enter the population of that city (in lakhs): "))
        city_area = float(input("Enter the area of the city (in sq. km): "))
        cities[city_name] = {"population": city_population, "area": city_area}
        f.write(f"{city_name} {city_population} {city_area}\n")
    return cities

def display_all_cities(cities):
    for city, details in cities.items():
        print(f"{city}: population - {details['population']} lakhs, Area:- {details["area"]} sq. km")

def display_cities_population_more_than_10_lakhs(cities):
    for city, details in cities.items():
        if details['population'] > 10:
            print(city)

def sum_of_areas_of_all_cities(cities):
    total_area = sum(details['area'] for details in cities.values())
    return total_area

filename = "city.txt"
cities = adding_data(filename)

print(" Display details of all cities:")
display_all_cities(cities)

print("\n Display city names with population more than 10 Lakhs:")
display_cities_population_more_than_10_lakhs(cities)

print("\n Display sum of areas of all cities:")
total_area = sum_of_areas_of_all_cities(cities)
print("Total area of all cities:", total_area, "sq. km")

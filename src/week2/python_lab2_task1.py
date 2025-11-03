temperatures = [68, 70, 72, 75, 74, 71, 69]
city_population = {"New York": 8419600, "Los Angeles": 3980400, "Chicago": 2716000, "Houston": 2328000, "Phoenix": 1690000}

average_temperature = sum(temperatures) / len(temperatures)
largest_city = max(city_population, key=city_population.get)
largest_population = city_population[largest_city]
total_population = sum(city_population.values())

print("Average temperature:", round(average_temperature, 2))
print("Largest city:", largest_city, "-", largest_population)
print("Total population:", total_population)

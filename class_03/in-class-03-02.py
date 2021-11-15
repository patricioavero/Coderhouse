## Class 03
## In-class Excercise

## Given tuple
cities = ("San Jorge", "Quitilipi", "Granadero Baigorria", "Alderetes", "Gualeguay", "Chimbas", "Rada Tilly", "Cote-Lai", "Elena", "Yerba Buena", "Laboulaye", "La Rioja", "Castelli", "Aminga", "Isla Verde", "Pirane", "General Enrique Godoy", "Alumine", "Rio Pico", "Sampacho", "Villa de Soto", "Embarcacion", "Caseros", "Jesus Maria", "Salta", "Esquina", "Puerto Iguazu", "Mercedes", "Castelli", "Cinco Saltos", "El Bolson", "Tamberias", "Guernica", "Doblas", "Villa Santa Rita", "Mercedes", "Carlos Casares", "Vera", "Zapala", "Santa Ana", "Libertador General San Martin", "Villa Maria", "Basail", "Gualeguay", "Villa La Angostura", "Basail", "San Lorenzo", "Tostado", "Libertad", "General Conesa", "General Pico")

## Request a city to the user
city_to_search=str(input("What city do you want to search? "))

## Some calculations of the tuple
# Total elements in the tuple
tuple_total = len(cities)
# The index number for the middle of the tuple
tuple_middle = tuple_total / 2
# Check if the city inserted is an element in the given tuple
# Parse to lowercase just to avoid mistakes.
if (city_to_search in cities):
    city_index = cities.index(city_to_search)
    # To facilitate human reading
    city_position = city_index + 1
    if (int(city_index) > int(tuple_middle)):
        print(f'The city {city_to_search} is over the middle of the list [Position: {city_position}]')
    elif (int(city_index) < int(tuple_middle)):
        print(f'The city {city_to_search} is under the middle of the list [Position: {city_index}]')
    else:
        print(f'The city {city_to_search} is in the middle of the list [Position: {city_index}]')
else:
    print("The city you inserted is not present in the tuple")


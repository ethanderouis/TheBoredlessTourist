# SETTING UP YOU PROJECT

destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt"]
test_traveler = ["Erin Wilkes", "Shanghai, China", ['historical site', 'art']]

# TRAVELLING TO FARAWAY LANDS

def get_destination_index(destination):
    destination_index = destinations.index(destination)
    return destination_index

# print(get_destination_index("Los Angeles, USA")) # prints 2 in terminal
# print(get_destination_index("Paris, France")) # prints 0 in terminal
# print(get_destination_index("Hyderabad, India")) # error since it is not in the list

def get_traveler_location(traveler):
    traveler_destination = traveler[1]
    return traveler_destination

test_destination_index = get_destination_index(get_traveler_location(test_traveler))
print(test_destination_index) # returns 1

# VISITING INTERESTING PLACES

attractions = []
for i in range(len(destinations)):
    attractions.append([])

print(attractions) # should print 5 empty lists in a list

def add_attraction(destination, attraction):
    destination_index=get_destination_index(destination)
    attractions[destination_index].append(attraction)
    
    

add_attraction("Los Angeles, USA", ["Venice Beach", ["beach"]])


add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

print(attractions)

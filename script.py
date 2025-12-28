# SETTING UP YOU PROJECT

destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "Sao Paulo, Brazil", "Cairo, Egypt"]
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


import googlemaps

gmaps = googlemaps.Client(key='AIzaSyD872uTbM8dkSusVD9HvbG_W2Ggkb1K6cE')
geocode_result = gmaps.geocode('20 Ropemaker Street, London, EC2Y 9AR')

location_ = geocode_result[0]['geometry']['location'] # creates a placeholder to abbreviate the print lookups below
# in JSON the full location is [0]['geometry']['location']['lat'] location_ allows us to abbreviate the bulk of the
# JSON file so you can do this:

print(location_['lat'])
print(location_['lng'])

direction_result = gmaps.directions('London, EC2Y 9AR','London, N8 8PT', units='imperial')
direction_ = direction_result[0]['legs'][0]['distance']['text']
print(direction_)

direction_result = gmaps.directions('London, EC2Y 9AR','London, N8 8PT', mode='walking') # we have added mode='walking'
print(direction_result)

# create a function called my_get_direction which takes two addresses and returns

#def my_get_direction('add1', 'add2'):
 #   direction_result = gmaps.directions('London, EC2Y 9AR', 'London, N8 8PT', units='imperial')
    # returns step-by-step directions
    # provides total time, total distance


def my_add(num1, num2):
    my_sum = num1 + num2
    return my_sum


geocode_result = gmaps.geocode('WD23 3EW')
print(geocode_result)
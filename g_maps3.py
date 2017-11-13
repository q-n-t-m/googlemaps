import googlemaps
import datetime
import time

gmaps = googlemaps.Client(key='AIzaSyD872uTbM8dkSusVD9HvbG_W2Ggkb1K6cE')

#geocode_result = gmaps.geocode('20 Ropemaker Street, London, EC2Y')

#start_address = input("where are you traveling from?")
#end_address = input("where are you going to?")

#my_directions_input = gmaps.directions(start_address), gmaps.directions(end_address)



def my_directions(add1, add2):
    result = gmaps.directions(add1, add2)
    list_of_directions = []
    list_of_steps = result[0]['legs'][0]['steps']

    for s in list_of_steps:
        list_of_directions.append(s['html_instructions'])

    #for j in list_of_directions

